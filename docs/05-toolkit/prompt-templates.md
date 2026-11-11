# Writing a Task for AI

You ask someone at home: "Can you grab some milk?" They come back with a big bottle of full-fat. You wanted a small carton of lactose-free. They also bought bread, because the bread looked good, and it all cost more than you expected.

Did anyone do anything wrong? Not really. You asked for milk, you got milk. Everything else, they had to guess.

An AI works exactly the same way. It does what the task says and guesses the rest. This chapter is about writing tasks that leave nothing important to guess.

---

## What a good task says

Put two notes side by side. One says "Buy milk." The other says "Buy one small carton of lactose-free milk at the shop on the corner. Nothing else. Bring the receipt." The second one answers every question before anyone has to ask it: which product, where, how much, what not to do, and what to bring back.

A good task for AI answers the same questions. It says **where** the work happens, so which project and which part of it, and **what** exactly should change. It shows **what the result should look like**, ideally with an example, otherwise with a clear description. It says **how the result will be checked**, meaning which tests or checks have to pass. And it says **what happens at the end**: should the result be saved or published, or only shown to you first? In a shop app, that could sound like "add a discount field to orders, from 0 to 50 percent, run the existing tests, and don't commit, show me the change first", and at home, it's the second milk note.

That last part is the one people forget. Saving or publishing is never assumed. The task says it, every single time.

---

## Where the AI must stop and ask

Some things you'd never want done without a quick call first. "If the milk costs more than two euros, call me before you buy it." "If they're out of it, don't buy something else, just tell me."

An AI needs the same kind of stop, and there are three kinds of action where it has to pause and ask. The first is **anything public**, like releasing a change to a live system or updating a page other people can see, because once others have seen it, you can't take it back. The second is **deleting**: instead of deleting, the AI comments the part out or keeps a copy, so it can be brought back. The third is **anything nobody asked for**. If the task doesn't say what you want, the AI asks instead of guessing, because an extra change you didn't request is a guess, however helpful it looks.

The rule behind all three is simple: on its own, the AI may only do what you asked for and what's easy to undo.

---

## Show, don't describe

"A nice birthday cake" can mean a hundred different cakes. A photo of the cake you want means one.

AI is no different. A description leaves room for interpretation, and an example doesn't. Want a report to look a certain way? Show one row of it. Want a page in a certain style? Point to a page that already has that style. And when there's no example yet, describe the result in plain words, as precisely as you can.

---

## Write it once

Some things are true for every shopping trip, like "we only drink lactose-free milk". You don't repeat that on every note. You stick it on the fridge once, and everyone in the house knows. Other things are true for one job only: your grandmother's cake recipe has its own note in the margin, "use less sugar than it says", and you only read it when you bake that cake. And some things come with the object itself, like the instructions printed on the lid of the washing machine.

You can keep instructions for AI in the same three places. The note on the fridge is a central rule file for the whole project, holding the rules that are always true, such as "never publish without asking". The notes in the recipe book are reusable instructions for one kind of job, often called skills, such as how to write a page or how to prepare a release. And the instructions on the lid belong to the tools themselves: each tool the AI can use carries its own rules, and each action of that tool can carry its own short instructions.

That way, each instruction gets read only at the moment it's needed. The rules for publishing get read when something is published, not during every other task.

And this isn't only about saving time. As [AI Failure Patterns & Hallucinations](../03-quality-gates/ai-errors.md) shows, every extra bit of text in the AI's context makes it a little worse at using the rest. Instructions that show up only when they're needed keep the context small, and they keep the AI from doing extra work or extra thinking that nobody asked for.
