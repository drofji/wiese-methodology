# Quality Gates: Checklists at Every Step

You are leaving for a two-week holiday. The bags are in the car, and you stop at the door. Is the stove off? The iron? Are the windows closed? You do not remember anything being wrong, and you check anyway. "I don't remember a problem" is not the same as "I checked".

Work with AI needs the same stop at the door. When there are many topics, many steps and several AI sessions, it soon becomes unclear what actually works and what was really discussed. So every step ends with a **quality gate**: a short list that must be passed before the next step may start.

---

## Two lists for every task

A recipe has two parts. The steps tell you what to do: cut, fry, bake. The test at the end tells you when it is ready: the toothpick comes out of the cake clean.

A task for AI has the same two parts:

- **The task list** says what to do. These are the small steps of the work.
- **The check list** says how we know it is done. These are the checks.

Take a task from a shop app: "Orders get a discount from 0 to 50 percent." The task list is short: add the field, set its limits, show the new price. The check list asks: are 0 and 50 percent accepted? Is 51 percent refused? Do old orders still open? Is the discounted price visible on the order page?

The order never changes. The AI works through the task list, then through the check list, and only then does the next task in the plan begin.

This holds for work without any code, too. When a topic is discussed, the questions are the task list. The checks are "no open questions are left" and "the author has approved it".

What to do and how to know it is done are two different questions, so they get two different lists.

---

## Agree on the lists before you start

A packing list is written at home, not in the taxi to the airport.

Both lists are agreed in full when the task is set, and they are not patched while the work runs. A list that changes during the work tends to bend toward what was done, instead of what was needed.

Sometimes an item turns out not to fit. "Check it on a phone" makes no sense for an e-mail. The AI does not skip such an item on its own. It asks, and skips it only after a person says yes. An item skipped without anyone's approval is a silent change, and silent changes are exactly what the [stop-and-ask rule](../05-toolkit/prompt-templates.md) forbids.

The list is the agreement. Changing it is a decision, not a side effect.

---

## A new list, fixed rules

A shopping list is new every week. Yet one rule applies to every item on it: look at the expiry date.

The check list works the same way. It is written anew for each task, from that task's own acceptance criteria, so it fits the work in front of it. What must hold everywhere lives in the **project rules** for that area, and it joins every new list on its own. For web pages, one such rule is accessibility: anyone can use the page, with large text, without a mouse, or with a screen reader.

A fixed template alone grows stale and gets ticked without reading. A list built only from the task forgets the basics. Together, the task brings what is special, and the rules bring what always counts.

---

## A tick needs proof

In the discount task, the first three checks pass their tests. The AI then ticks the fourth one too, "the price is visible on the order page", although nobody opened the page. That is a checklist done on autopilot.

Two locks stop it, and they work together:

- **Each item has its own proof**: a test, a link, a screenshot. Proof for one item never counts for another.
- **A separate session runs the checks.** It does not take the worker's word for anything. It opens the page itself.

The AI always tries to run the checks itself, because people make mistakes too. A separate checker also saves time: while it checks, the main session goes on with the next piece of work. Where a person still has to look, and what they look at, is described in [Who checks the checker](ai-errors.md#who-checks-the-checker).

A tick without proof is only a promise.

---

## When a check fails

You fix a leaking tap under the sink. Then you check more than the tap: is the floor dry, and does the water still run in the kitchen?

When a check fails, the AI fixes the problem and then runs the **whole** check list again, from the start. A fix is a new change, and it can break something that passed before. Re-running only the failed check trusts old results that no longer describe the work.

After a fix, every tick has to be earned again.

---

## The list ends the task, not the conversation

A note on the fridge is useful because it is the only one there. Ten notes, and nobody reads any of them.

A list of "what to check, what comes next" belongs at the end of a planned task. It does not belong under every answer in a conversation. A list after every reply turns into noise, and noise gets skimmed: the same autopilot from another direction.

A gate works because you meet it only where it matters, and you cannot walk past it.
