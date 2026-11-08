# Human Review: Where a Person Looks

Guests arrive in an hour. You do not cook every dish a second time to make sure it is right. You taste the soup, look at the table, and check the one dish without nuts, because one guest is allergic. Everything else you trust to the recipe and to the care you took while cooking.

A person reviewing AI work does the same. The checks described in [Quality Gates: Checklists at Every Step](automated-gates.md) carry most of the load. This chapter is about the part that is left to a person, and about the work that makes their look short and useful.

---

## Know what a change touches

Before you carry a new sofa into the flat, you check every door it has to pass on the way.

A change in a program has the same problem. The same piece of code is often used in several places: the discount is worked out for the order, and again for the invoice. Change it for one, and the other changes too.

So in a risky task, every item on the task list says what else it touches. Not in one block at the start, but at each step, where the change is actually made. The AI writes this, and the AI approves it. People read less and less code every day, so the system has to keep track of these links itself. A person's attention is saved for the result.

When each step names what it touches, nothing is changed by surprise.

---

## Four things a person looks at

Machines are good at checking what can be measured. Some things still need a human eye. A review covers four of them:

1. **What the AI could not check.** The AI says openly which items it was unable to prove. These come first, because nothing else has looked at them.
2. **The logic of the work.** Does the result do what people actually need? A discount can pass every test and still follow the wrong rule of the shop.
3. **How it looks.** On a real phone and a real computer, not only in a test.
4. **The important items.** Anything that touches money, personal data, or the links between parts.

Everything else gets spot checks, chosen by the person, as described in [Who checks the checker](ai-errors.md#who-checks-the-checker).

A review is short when it knows where to look.

---

## When the review finds a problem

A dish comes back from the table. Was it cooked badly, or was the recipe wrong? The answer decides who has to fix it.

When a review finds a problem, the AI proposes the cause, and the reviewer decides:

- **An error in the work** goes back to whoever did the task.
- **An error in the task itself** goes to the author of the task first. Once the task is fixed, it goes back to the one who does the work.

After the author's fix, the AI changes only the checklist items that the fix affects. The rest stays as it was agreed.

Fix the cause where it lives, and the same mistake does not come back.
