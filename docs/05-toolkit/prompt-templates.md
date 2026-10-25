# Writing a Task for AI

You ask someone at home: "Can you buy milk?" They come back with a big bottle of full-fat milk. You wanted a small carton of lactose-free milk. They also bought bread, because the bread looked good, and they paid more than you expected.

Nobody did anything wrong. You asked for milk, and you got milk. Everything else, they had to guess.

An AI works the same way. It does exactly what the task says and guesses the rest. This chapter is about writing tasks that leave nothing important to guess.

---

## What a good task says

Compare two notes:

- "Buy milk."
- "Buy one small carton of lactose-free milk at the shop on the corner. Nothing else. Bring the receipt."

The second note answers every question before it is asked: which product, where, how much, what not to do, and what to bring back.

A good task for AI answers the same questions:

- **Where:** which project, and which part of it.
- **What:** what exactly should change.
- **What the result should look like:** ideally an example, otherwise a clear description.
- **How it will be checked:** which tests or checks must pass.
- **What happens at the end:** should the result be saved or published, or only shown to you first?

For example:

- **In software:** "In the shop app, add a discount field to orders, from 0 to 50 percent. Run the existing tests. Do not commit; show me the change first."
- **In everyday life:** the second milk note.

The last point is easy to forget. Saving or publishing is never assumed. The task says it, every time.

---

## Where the AI must stop and ask

Some things you would never want done without a quick call first. "If the milk costs more than two euros, call me before you buy it." "If they are out of it, do not buy something else, just tell me."

An AI needs the same kind of stop. It must stop and ask before three kinds of action:

1. **Anything public.** Releasing a change to a live system, or updating a page other people can see. Once others have seen it, it cannot be taken back.
2. **Deleting.** Instead of deleting, the AI comments the part out or keeps a copy, so that it can be restored.
3. **Anything that was not asked for.** If the task does not say what you want, the AI asks instead of guessing. An extra change you did not request is a guess, however helpful it looks.

The rule behind all three is simple: the AI may do on its own only what can easily be undone and what you asked for.

---

## Show, don't describe

"A nice birthday cake" can mean a hundred different cakes. A photo of the cake you want means one.

The same is true for AI. A description leaves room for interpretation; an example does not. If you want a report to look a certain way, show a row of the report. If you want a page in a certain style, point to a page that already has that style. When there is no example yet, describe the result in plain words, as precisely as you can.

---

## Write it once

Some things are true for every shopping trip: "We only drink lactose-free milk." You do not repeat that on every note. You stick it on the fridge once, and everyone in the house knows it.

Other things are true only for one job. The recipe for your grandmother's cake has its own notes in the margin: "use less sugar than written". You read them only when you bake that cake. And some things come with the object itself: the washing machine has its instructions printed on its lid.

Instructions for AI can be kept in the same three places:

- **The note on the fridge** is a central rule file for the whole project: the rules that are always true, such as "never publish without asking".
- **The notes in the recipe book** are reusable instructions for one kind of job, often called skills: how to write a page, how to prepare a release.
- **The instructions on the lid** belong to the tools themselves. Each tool the AI can use carries its own rules, and each action of that tool can carry its own short instructions.

Each instruction is then read only at the moment it is needed. The rules for publishing are read when something is published, not during every other task.

This is not only about saving time. As the chapter [AI Failure Patterns & Hallucinations](../03-quality-gates/ai-errors.md) shows, every extra piece of text in the AI's context makes it a little worse at using the rest. Instructions that arrive only when they are needed keep the context small, and they also keep the AI from doing extra work or extra thinking that nobody asked for.

