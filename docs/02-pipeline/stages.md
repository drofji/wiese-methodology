# Flow Stages & Atomic Tasks

Nobody moves house in one go. You pack room by room, box by box, and you write on every box which room it belongs to. When a box goes missing, you know at once which one it is and where it should have gone.

Now picture asking an AI: "Build the whole online shop." It will produce something, and it will look finished. This chapter is about why that result cannot be trusted, and how to split the work so that every piece of it can be.

---

## Why a big task goes wrong

Ask a friend to "do the shopping for the whole month", and you will get a full car and a missing half of what you needed. Ask for tomorrow's dinner, with a short list, and you get exactly that.

A big task for AI fails in five ways at once:

- **Requirements get lost.** The longer the task, the more of it lands in the middle, where models pay the least attention (see [The middle of the pile](../03-quality-gates/ai-errors.md#the-middle-of-the-pile)).
- **Extra or wrong work appears.** Gaps get filled with guesses, and a guess looks just like a real answer.
- **The result is hard to check.** Nobody can review a whole shop with care.
- **The result is hard to fix.** One mistake in the base pulls the rest down with it.
- **There is no trace.** It is impossible to say which parts changed, or why.

A small task avoids all five, not because the AI works better, but because there is less room for each of them.

---

## Few levels, each with a job

A wedding is planned the same way. There is the event itself. There are stages with a date: invitations sent by May, the venue booked by June. And there are tasks: send fifty invitations.

Work with AI uses the same three levels:

- **The project** is the whole thing: the online shop.
- **A stage** is a part that can be finished and used on its own, such as a first version or a release. It has a clear "done", a deadline and its list of tasks.
- **A task** is one piece of work inside a stage.

Large projects add one more level between stage and task, a **feature**, such as "discounts in orders". Small projects do without it. Every extra level is one more place where something can get lost, so there are as few as the work allows.

The person splits the work down to tasks. Before a stage starts, the AI compares the stage's description with its list of tasks, so that nothing promised in the stage is missing from the work.

Each level answers one question: what the whole is, what is finished when, and what is done next.

---

## How small is small

The size of a task is not measured in hours. An AI and a person work at very different speeds, and time says nothing about whether the result can still be checked.

Two signs say a task is the right size:

- **It changes one area.** Like a box that holds one room, a task touches one part of the program. The discount task changes orders, and nothing else.
- **Its checklist stays short.** If the list of checks keeps growing, the task is too big, and it is split in two.

Both signs measure the same thing: whether a person can still see the whole task at once.

---

## A task that stands alone

A good note for a babysitter fits on one page: phone numbers, bedtime, the allergy, where the plasters are. It never says "see the other folder".

A task works the same way. It is one complete assignment that a person or an AI can carry out without any other document. It holds a short list of the key points from the project and the stage, written by the AI when the task is created. The full texts are available on request, but the task does not depend on them.

Inside, every task follows the same short path:

1. **Context:** only what this task needs.
2. **Strict generation:** the AI produces only what the task asks for.
3. **Automated validation:** checks outside the model test the result.
4. **Integration:** the result joins the project.

What to do and how to know it is done are written as two lists, described in [Quality Gates: Checklists at Every Step](../03-quality-gates/automated-gates.md).

A task that needs nothing else can be handed to anyone, and checked by anyone.

---

## One task, one trace

The label on a moving box tells you where it belongs. In software, the label is the commit: the saved record of one change.

**One task is one commit**, linked to that task in the task manager. Anyone can see which files changed, and the task says why. When something breaks later, the trace leads straight to the change that caused it, and that change can be undone without touching the rest.

A change you can trace is a change you can take back.

---

## Statuses that grow with the project

A note on the fridge needs only two columns: to do and done. A building site needs many more.

The statuses of a task grow with the project in the same way. A small project needs four: *to do → in progress → check → done*. A large one uses seven: *draft → preparation → approval → in progress → AI check → review → done*, plus *blocked* and *needs edit*. The extra steps exist where more people and more risk are involved: someone prepares the lists, someone approves them, someone reviews the result.

All of this lives in one shared task list that every session can see, as described in [Many hands, one memory](../03-quality-gates/ai-errors.md#many-hands-one-memory). When several AI sessions work at once, the main session decides which tasks may run side by side and hands them out.

Use as many steps as the project needs, and not one more.

---

## When the plan changes

Fifty guests become thirty. Whoever ordered the chairs and the cake has to know, or the old order quietly stays in place.

When the idea behind a project changes, the same thing happens to its open tasks. Say the discount limit drops from 50 to 30 percent. The AI finds every unfinished task that this touches, marks it *needs edit*, and proposes the change. The tasks are changed only after a person says yes.

A plan that changes in one place must change everywhere it is used, and never silently.
