---
name: treasury-and-liquidity
description: Build a short-horizon cash forecast, assess runway and working capital, review bank or currency concentration, or plan liquidity actions around timing and counterparty exposure.
disable-model-invocation: true
---

# Treasury and liquidity

Use this for financial decision support. Preserve source dates, currency, entity, reporting basis,
and jurisdiction assumptions. Qualified finance professionals must determine financing, tax, or
regulatory implications; show uncertainty instead of overstating runway.

## Inputs and context

Gather bank balances, restricted cash, expected receipts and disbursements, payment dates, payroll,
committed spend, debt, working-capital aging, currency exposures, counterparties, and decision dates.
Use an approved processing environment, minimize account and employee identifiers, redact credentials
and unrelated personal data, and mark the forecast for controlled need-to-know retention.

## Workflow

1. Build a direct weekly cash view for the operating horizon, separating committed, likely, and
   optional flows.
2. Reconcile opening cash to statements and compare the prior forecast with actual timing.
3. Model base, downside, delayed-receipt, and planned-action cases; identify decision deadlines.
4. Review receivables, payables, inventory, payment terms, and funding trapped in the cycle.
5. Test bank, currency, instrument-maturity, and customer concentration against limits.
6. Assign actions, approvals, owners, and monitoring cadence without confusing recommendations with
   executed transfers or financing.

## Output / decision record

Return the cash forecast, runway range, scenario assumptions, liquidity thresholds, concentration
findings, action options, cost and trade-offs, approvals required, and next review date.

## Uncertainty and failure handling

Isolate stale balances, uncertain receipt dates, restricted funds, and uncommitted expenses. If a
scenario crosses a decision threshold, escalate before the cash date; obtain qualified review for
financing, tax, regulatory, or investment questions.

## Routing boundaries

Use this skill only for its stated capability and required context. For adjacent work, select a more specific skill from `skill-index.tsv`; do not infer coverage from this department folder or use this skill to authorize actions outside its scope.

## Never

- Describe runway with one unsupported number.
- Treat accounting profit as available cash.
- Move or invest funds based only on this recommendation.
