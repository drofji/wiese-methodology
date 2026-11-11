# Flow Stages & Atomic Tasks

Nobody moves house in one go. You pack room by room, box by box, and you scribble "kitchen" or "bathroom" on every single one. Sounds boring? It's the reason that, when a box goes missing, you know right away which one it is and where it was supposed to go.

Now imagine telling an AI: "Build me the whole online shop." You'll get something back. It'll even look finished. And that's exactly the problem, because you have no idea which parts you can trust. So let's cut the work into pieces you can.

---

## Why a big task goes wrong

Ask a friend to "do the shopping for the whole month" and watch what happens: a full car, and half the stuff you actually needed is missing. Ask for tomorrow's dinner, with a short list, and you get exactly that.

A big task for AI fails the same way, just in five directions at once. Some of what you asked for quietly disappears, because in a long task a lot ends up in the middle, and the middle is where models pay the least attention (the details are in [The middle of the pile](../03-quality-gates/ai-errors.md#the-middle-of-the-pile)). The gaps get filled with guesses, so you get extra stuff or the wrong stuff, delivered with total confidence. Checking it all? Good luck reviewing a whole shop with real care. Fixing it? One mistake at the bottom and everything on top comes down with it. And afterwards, nobody can tell you what changed where, or why.

A small task dodges all five. Not because the AI got smarter, but because there's simply less room for things to go wrong.

---

## Few levels, each with a job

Planning a wedding works like this too. There's the big day. There are stages with dates, like invitations out by May and the venue booked by June. And there are the small jobs, like actually sending those fifty invitations.

AI work uses the same three levels. The **project** is the whole thing, the online shop. A **stage** is a chunk you can finish and use on its own, a first version or a release, with a clear "done", a deadline and its list of tasks. A **task** is one piece of work inside a stage. Big projects add one more level in between, a **feature** like "discounts in orders". Small projects skip it, and they're right to, because every extra level is one more crack for something to fall through.

You split the work down to tasks. Before a stage kicks off, the AI lays the stage description next to its task list and checks that nothing promised has gone missing.

Each level answers one question: what's the whole thing, what's done when, and what's next.

---

## How small is small

Forget hours. An AI and a person work at completely different speeds, and the clock tells you nothing about whether you can still check the result.

Ask two things instead. Does the task change **one area**? And is its **checklist short**? Think of a moving box that holds one room and nothing else: the discount task touches the order part of the shop and leaves the rest alone. If the checklist keeps getting longer, that's your cue. The task is too big, so cut it in two.

Both questions really ask the same thing: can you still see the whole task at a glance?

---

## A task that stands alone

A good note for the babysitter fits on one page. Phone numbers, bedtime, the allergy, where the plasters are. It never says "see the other folder".

Same with a task. It's one complete job that a person or an AI can do without hunting through other documents. It carries a short summary of what matters from the project and the stage, written by the AI when the task is created, and the full texts are there if anyone asks, but the task doesn't depend on them. Inside, every task takes the same short walk: it gets just the context it needs, the AI makes only what was asked for, checks outside the model test it, and then it joins the project. What to do and how you know it's done live in two separate lists, and [Quality Gates: Checklists at Every Step](../03-quality-gates/automated-gates.md) shows how.

A task that needs nothing else can go to anyone, and anyone can check it.

---

## One task, one trace

The label on a moving box tells you where it belongs. In software, the label is the commit, the saved record of one change.

So: **one task, one commit**, linked to that task in the task manager. Anyone can see which files changed, and the task tells them why. When something breaks a month later, the trail leads straight to the change behind it, and you can undo just that one change without touching anything else.

If you can trace a change, you can take it back.

---

## Statuses that grow with the project

A note on the fridge needs two columns: to do, done. A building site needs a few more.

Task statuses grow with the project the same way. A small project is fine with four: *to do*, *in progress*, *check*, *done*. A big one goes with seven, from *draft* through *preparation*, *approval*, *in progress*, *AI check* and *review* all the way to *done*, plus *blocked* and *needs edit* for when things get stuck. The extra steps show up exactly where more people and more risk come in, because now someone prepares the lists, someone signs them off and someone reviews the result.

All of it sits in one shared task list that every session can see, like in [Many hands, one memory](../03-quality-gates/ai-errors.md#many-hands-one-memory). And when several AI sessions run at once, the main session decides which tasks can go side by side and hands them out.

Use as many steps as your project needs. Not one more.

---

## When the plan changes

Fifty guests just became thirty. Whoever ordered the chairs and the cake needs to know, or you'll be eating cake for a week.

When the idea behind a project changes, its open tasks are in the same boat. Say the discount limit drops from 50 to 30 percent. The AI finds every unfinished task this touches, marks it *needs edit* and suggests the fix. Nothing changes until a person says yes.

Change the plan in one place, and it has to change everywhere it's used. Out loud, never quietly.
