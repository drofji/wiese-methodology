# Human Review: Where a Person Looks

Your guests arrive in an hour. You don't cook every dish a second time just to be sure. You taste the soup, glance over the table and check the one dish without nuts, because one of your guests is allergic. Everything else you trust to the recipe and to the care you took while cooking.

Reviewing AI work goes the same way. The checks in [Quality Gates: Checklists at Every Step](automated-gates.md) carry most of the load. This chapter is about the part that's left for you, and about the work that keeps your look short and actually useful.

---

## Know what a change touches

Before you carry a new sofa into the flat, you check every door it has to squeeze through on the way.

A change in a program has the same problem. The same piece of code often gets used in several places, so the discount is worked out for the order and then again for the invoice. Change it for one, and the other changes too.

That's why, in a risky task, every item on the task list says what else it touches, right at the step where the change actually happens rather than in one big block at the start. The AI writes this, and the AI signs it off. People read less and less code every day, so the system has to keep track of these links by itself, and your attention is saved for the result.

When every step names what it touches, nothing changes by surprise.

---

## Four things a person looks at

Machines are great at checking what can be measured. Some things still need a human eye, and a review covers four of them.

You start with **what the AI couldn't check**, the items it openly marked as unproven, because nothing else has looked at those yet. Then you look at **the logic of the work**: does the result do what people actually need? A discount can pass every single test and still follow the wrong rule of the shop. Next comes **how it looks**, on a real phone and a real computer, not just inside a test. And finally you check **the important items**, anything that touches money, personal data or the links between parts.

Everything else gets spot checks that you pick yourself, as described in [Who checks the checker](ai-errors.md#who-checks-the-checker).

A review is short when it knows where to look.

---

## When the review finds a problem

A plate comes back from the table. Was it cooked badly, or was the recipe wrong? The answer decides who has to fix it.

When a review finds a problem, the AI suggests the cause and the reviewer decides. If the error is in the work, it goes back to whoever did the task. If the error is in the task itself, it goes to the task's author first, and once the task is fixed, back to whoever does the work. After the author's fix, the AI changes only the checklist items the fix actually affects, and the rest stays as it was agreed.

Fix the cause where it lives, and the same mistake won't come back.
