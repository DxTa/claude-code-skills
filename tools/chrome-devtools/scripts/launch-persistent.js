#!/usr/bin/env node
/**
 * Launch a persistent Chrome browser that can be reused across multiple commands
 * Saves the WebSocket endpoint to a file for other scripts to connect to
 */
import puppeteer from 'puppeteer';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ENDPOINT_FILE = path.join(__dirname, '.browser-endpoint');

/**
 * Resolve the remote-debugging port from env vars or CLI.
 * Priority: CLI --port=N > CHROME_DEVTOOLS_BROWSER_URL (parsed) > BROWSER_URL (parsed) > 9222.
 */
function resolveDebugPort(args) {
  const cliPort = args.find(arg => arg.startsWith('--port='))?.split('=')[1];
  if (cliPort) return cliPort;

  const url = process.env.CHROME_DEVTOOLS_BROWSER_URL || process.env.BROWSER_URL;
  if (url) {
    try { return new URL(url).port || '9222'; } catch (_) {}
  }
  return '9222';
}

async function main() {
  // Parse command line arguments
  const args = process.argv.slice(2);
  const headless = !args.includes('--headless=false') && !args.includes('--no-headless');
  const url = args.find(arg => arg.startsWith('--url='))?.split('=')[1] || 'about:blank';
  const debugPort = resolveDebugPort(args);

  console.log(`Launching persistent Chrome browser (remote-debugging port ${debugPort})...`);

  const browser = await puppeteer.launch({
    headless,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      `--remote-debugging-port=${debugPort}`
    ],
    defaultViewport: {
      width: 1920,
      height: 1080
    }
  });

  const wsEndpoint = browser.wsEndpoint();
  
  // Save endpoint to file
  fs.writeFileSync(ENDPOINT_FILE, wsEndpoint);
  console.log(`Browser launched. WebSocket endpoint saved to: ${ENDPOINT_FILE}`);
  console.log(`WebSocket: ${wsEndpoint}`);
  
  // Navigate to initial URL if provided
  if (url !== 'about:blank') {
    const page = (await browser.pages())[0];
    console.log(`Navigating to: ${url}`);
    await page.goto(url, { waitUntil: 'networkidle2' });
  }

  console.log('\n✓ Browser is ready for commands!');
  console.log('  Use other scripts normally - they will connect to this browser.');
  console.log('  Run "node close-persistent.js" or press Ctrl+C to close.\n');

  // Keep process alive
  process.on('SIGINT', async () => {
    console.log('\nClosing browser...');
    await browser.close();
    if (fs.existsSync(ENDPOINT_FILE)) {
      fs.unlinkSync(ENDPOINT_FILE);
    }
    process.exit(0);
  });

  // Keep alive indefinitely
  await new Promise(() => {});
}

main().catch(error => {
  console.error('Error launching browser:', error);
  process.exit(1);
});
