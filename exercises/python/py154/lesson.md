# Mission: reconcile the snack ledger

Aggregate records while keeping money in integer cents.

## Reconcile each account independently

- **Use signed integer cents.** Positive and negative entries change the corresponding account's balance.

- **Initialize when an account first appears.** An entry of zero still establishes that account's presence.

- **Keep zero balances and the original ledger.** Reconciliation should be repeatable without changing the input records.

## Walk through an example

```python
balances = {}
for account, cents in [("tea", 500), ("tea", -125)]:
    balances[account] = balances.get(account, 0) + cents
```

<details class="lesson-deeper">
<summary>A little more explanation</summary>

A ledger is a sequence of changes, not merely a current balance. Processing it means applying each signed amount to the correct account. A deposit is positive and a charge is negative in this simplified contract.

Initialize an account the first time it appears, including when its first entry is zero. Do not drop an account just because its final balance is zero; its presence in the ledger is meaningful. Integer cents avoid binary decimal representation issues for these whole-cent calculations.

Keep records unchanged so the same ledger can be reconciled again. This repeatability is valuable when debugging and retrying data pipelines. The output dictionary needs no extra ordering promise because callers look up balances by account key. Pip spent the entire snack budget on a subscription to more snack budgets. Accounting would like a deterministic function.

</details>

## Before you run

Why should a zero balance not automatically remove an account from this report?

Read the explanation, predict what the example does, then try the mission. Ask the tutor about any unfamiliar word or line. Hints and a reference solution are available after you try. Your work stays saved on the laptop.
