# Ready Parts: Preparing the Ground for AI

Think of two ways to build a bookshelf. In the first, you get a pile of planks, a saw and a bag of loose screws. In the second, you get a flat box: the boards are cut to size, every hole is drilled, the screws are sorted into labelled bags, and a picture shows how it all fits together. Both shelves can turn out fine. But only one of them is likely to stand straight on the first try.

Working with AI is the same. Whoever does the next piece of work, you, a colleague or an AI, starts with only what you provide. So the most important work happens **before** anything is written: preparing the ground. This chapter describes eight ways to do it.

---

## Start from what already works

When there is nothing ready to reuse, the AI builds everything from scratch. Each result is a little different from the last, and each one has to be checked from the beginning.

The answer is to collect ready parts: pieces that have already been tested and are known to work. New work then becomes mostly a matter of putting these parts together, with as little new material as possible.

Parts that many people have already checked are the safest. A widely used open-source framework, reviewed by thousands of developers, is more reliable than code written once by one person or one AI. In my own work I build on Django, a framework maintained by a large community, and I collect my own ready parts in an open-source library, Django-Snapadmin. A new feature becomes mostly configuration rather than new code. At home it is the same idea as cooking from a recipe your family has made a hundred times, instead of guessing the amounts.

Checking is the slowest and most expensive part of working with AI. A part that many people have already checked does not need to be checked again from zero. And when proven parts are combined, an error can only be a gap in the final picture: a missing field, a missing detail. Gaps are easy to see.

---

## Let the part explain itself

If using a part correctly takes a long instruction, that instruction will sooner or later be lost, forgotten or misread. The knowledge sits in someone's head or in a separate document, not in the part itself.

A light switch needs no manual. You see it and you know what to do. The same goes for a plug that fits only one way into the socket. Good parts for AI work like that: they have a clear interface that shows how they are used. A well-described API or MCP server (a fixed, documented way for a program or an AI to use a tool) tells the AI what it can do and what data it needs, without any extra explanation.

An instruction kept somewhere else drifts away from the part and goes out of date. An interface cannot be skipped: it is used every time the part is used, so it stays current. And it works the same way for a person and for an AI.

---

## Guide with words, check with fixed rules

You write rules into your request, and the AI follows some of them and ignores others. That is not bad will. Rules written in a request are only advice, and nothing makes anyone follow advice.

So the methodology uses two kinds of rules:

- **Guiding rules** are the information you give in the context. They point the work in the right direction.
- **Fixed rules** are built into an interface: an API, a script, a test. They check the result at the end.

A parent can ask the children to fasten their seat belts. That is guidance. The car that keeps beeping until every belt is fastened is a fixed rule. In software, the request describes what to build, and automated tests decide whether the result is accepted.

Neither kind is enough on its own. Fixed rules always leave something to correct, and guidance alone is too weak because nothing enforces it. Together, the words give flexibility during the work and the fixed rules give certainty at the end.

---

## Let mistakes make noise

When information is missing, the AI fills the gap with a guess, and the guess looks just like a real answer. Nothing stops it.

The cure is to set things up so that a missing piece causes a **clear, visible error**. A cash machine gives no money until the right PIN is entered; it does not hand out a guess. In software, a required field without a value stops the process with a clear message. The AI then cannot carry on until it supplies the right data. It tries, adjusts and tries again, the way people work through an unfamiliar problem, and the way developers once searched forums until something finally worked.

A wrong result that looks right is the most expensive mistake of all, because it is found late, often by the person who uses it. A visible error costs one more attempt. Making gaps visible turns the AI's persistence from a risk into an advantage.

---

## Keep the check apart from the work

Sometimes the AI changes not only the work, but also the check that is supposed to test it.

When the same worker writes both the result and its check, with the same reasoning and the same context, the check has the same blind spots. You would not mark your own exam. And a check that can be edited during the task can be edited until it passes.

So the check is built as a separate part, as if one person were reviewing another. The reviewer gets its own instructions and its own reasoning, and starts from the beginning with its own knowledge and tools, without the first worker's context.

The check lives in a fixed interface, such as an API, an MCP server, a framework or a library. While a task is running, the check does not change: the AI must follow its rules and checklists, and often it cannot change them at all. Improving the checks is a separate task, done and reviewed on its own. Automatic checks are combined with human review, and the work is cut into small modules and small steps, so that a person can keep up with everything that needs checking.

A check that is independent and fixed for the length of a task holds the line. It still improves over time, but only as separate, reviewed work.

---

## Once it works, make it a script

The AI performs the same job again and again, and each result can be slightly different or slightly wrong. Every new attempt is a new chance to get it wrong, and nothing from the last attempt that worked is kept.

You would not set your alarm by hand every evening if your phone can repeat it. In the same way, as soon as a procedure is clear, it becomes a script: a defined action that runs with one command. The script is split into small modules, each with one job, so the modules can be reused, and each module is covered by tests. AI models already write small helper scripts in the background to process data. Those drafts are worth keeping and turning into tools.

A better prompt is still a new attempt every time. A script is checked once and then behaves the same way every time. Writing it is not lost time: the goal is not to save time, but to use your effort where it counts. What you build up is a growing library of actions you can trust.

---

## Keep related things together

The AI builds something that already exists, simply because it looked in the wrong place. Related parts were scattered, or the same thing appeared under different names.

A shopping list sorted by aisle makes sure you do not forget the item next to the one you came for. In a shop, signs and shelf labels lead you to the right place. But in a second-hand shop you will never find a "T-shirt" that hangs under "tank top".

Work for AI is organised the same way, as a **tree** in which related items sit side by side and each has a short description:

- **Search first, then the tree.** Search by keyword first. If that fails, walk the tree, which is the reliable path.
- **Signs along the way.** Every level of the tree has short hints and links to related branches.
- **One thing, one name.** Different names for the same thing break the search.
- **Maps for people.** Alongside the structure, short maps, diagrams or mockups help people find their way.

Search alone fails as soon as something has a different name. The tree alone is reliable but slow. Searching first saves time, and the tree adds certainty. A full list of every name and synonym does not solve it either: with a lot of data it grows too big to keep up to date.

---

## Build on what people have checked

More and more of what is written today is produced by machines, and it is easy to build on material that nobody has actually checked. Machine-made content is fast and plentiful. Material checked by people takes longer to make and is harder to find.

That checked material is the foundation: working solutions, templates, rules, formulas and scripts. It is collected, kept up to date and given to the AI as the basis for new work. Without it there is nothing to compare a result against, and errors pass from one piece of work into the next unnoticed.

The people who build AI models face the same problem. The study *AI models collapse when trained on recursively generated data* ([Shumailov et al., 2024](https://doi.org/10.1038/s41586-024-07566-y)) [1] showed that models trained again and again on text made by other models slowly lose the less common parts of the original data and get worse with each generation. The authors call this "model collapse" and conclude that data from real human activity becomes more valuable as machine-made content spreads.

Material that people have checked is the measuring stick. Everything else is measured against it.

---

## Sources

All sources are open and free to read. Each entry says which point in this chapter it supports.

1. **Shumailov et al., *AI models collapse when trained on recursively generated data*, Nature 631, 2024** — https://doi.org/10.1038/s41586-024-07566-y
   Supports: models trained repeatedly on machine-made content lose rare data and degrade; human-made data gains value. Section "Build on what people have checked".
