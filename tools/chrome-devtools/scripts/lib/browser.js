/**
 * Shared browser utilities for Chrome DevTools scripts
 */
import puppeteer from 'puppeteer';
import debug from 'debug';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ENDPOINT_FILE = path.join(__dirname, '..', '.browser-endpoint');

const log = debug('chrome-devtools:browser');

let browserInstance = null;
let pageInstance = null;
let _isConnected = false; // true if we connected to an existing browser (not launched)

/**
 * Default browser URL used when no explicit endpoint is given.
 * Priority: explicit --browser-url/--ws-endpoint > env vars > built-in default.
 */
function resolveBrowserUrl(options = {}) {
  if (options.browserUrl) return options.browserUrl;
  if (options.wsEndpoint) return null; // ws endpoint takes separate path
  return process.env.CHROME_DEVTOOLS_BROWSER_URL
    || process.env.BROWSER_URL
    || 'http://127.0.0.1:9222';
}

/**
 * Launch or connect to browser.
 *
 * Connection strategy:
 * 1. Reuse existing singleton.
 * 2. Try the persistent endpoint file written by launch-persistent.
 * 3. Try the default browser URL (env or http://127.0.0.1:9222).
 * 4. Fall back to launching a new headless browser.
 */
export async function getBrowser(options = {}) {
  if (browserInstance && browserInstance.isConnected()) {
    log('Reusing existing browser instance');
    return browserInstance;
  }

  // 2. Check for persistent browser endpoint file
  if (!options.browserUrl && !options.wsEndpoint && fs.existsSync(ENDPOINT_FILE)) {
    try {
      const wsEndpoint = fs.readFileSync(ENDPOINT_FILE, 'utf8').trim();
      log('Found persistent browser endpoint, connecting...');
      browserInstance = await puppeteer.connect({ browserWSEndpoint: wsEndpoint });
      _isConnected = true;
      return browserInstance;
    } catch (error) {
      log('Failed to connect to persistent browser, continuing:', error.message);
      if (fs.existsSync(ENDPOINT_FILE)) {
        fs.unlinkSync(ENDPOINT_FILE);
      }
    }
  }

  // 3. Try connecting to an existing Chrome via the default browser URL
  //    (only when neither browserUrl nor wsEndpoint was explicitly given)
  if (!options.browserUrl && !options.wsEndpoint) {
    const defaultUrl = resolveBrowserUrl(options);
    try {
      log('Attempting to connect to existing Chrome at', defaultUrl);
      browserInstance = await puppeteer.connect({ browserURL: defaultUrl });
      _isConnected = true;
      return browserInstance;
    } catch (error) {
      log('Could not connect to existing Chrome, will launch new one:', error.message);
    }
  }

  // 4. Explicit connection or launch fallback
  const launchOptions = {
    headless: options.headless !== false,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      ...(options.args || [])
    ],
    defaultViewport: options.viewport || {
      width: 1920,
      height: 1080
    },
    ...options
  };

  if (options.browserUrl || options.wsEndpoint) {
    log('Connecting to existing browser (explicit)');
    browserInstance = await puppeteer.connect({
      browserURL: options.browserUrl,
      browserWSEndpoint: options.wsEndpoint
    });
    _isConnected = true;
  } else {
    log('Launching new browser');
    browserInstance = await puppeteer.launch(launchOptions);
    _isConnected = false;
  }

  return browserInstance;
}

/**
 * Get current page or create new one
 */
export async function getPage(browser) {
  if (pageInstance && !pageInstance.isClosed()) {
    log('Reusing existing page');
    return pageInstance;
  }

  const pages = await browser.pages();
  if (pages.length > 0) {
    pageInstance = pages[0];
  } else {
    pageInstance = await browser.newPage();
  }

  return pageInstance;
}

/**
 * Close browser (or disconnect if connected to existing).
 *
 * When we connected to a user's already-running Chrome (remote debugging),
 * we disconnect instead of closing to avoid killing their main browser session.
 */
export async function closeBrowser() {
  if (!browserInstance) return;

  if (_isConnected) {
    try { await browserInstance.disconnect(); } catch (_) {}
  } else {
    try { await browserInstance.close(); } catch (_) {}
  }

  browserInstance = null;
  pageInstance = null;
  _isConnected = false;
}

/**
 * Parse command line arguments
 */
export function parseArgs(argv, options = {}) {
  const args = {};

  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];

    if (arg.startsWith('--')) {
      const key = arg.slice(2);
      const nextArg = argv[i + 1];

      if (nextArg && !nextArg.startsWith('--')) {
        args[key] = nextArg;
        i++;
      } else {
        args[key] = true;
      }
    }
  }

  return args;
}

/**
 * Output JSON result
 */
export function outputJSON(data) {
  console.log(JSON.stringify(data, null, 2));
}

/**
 * Output error
 */
export function outputError(error) {
  console.error(JSON.stringify({
    success: false,
    error: error.message,
    stack: error.stack
  }, null, 2));
  process.exit(1);
}
