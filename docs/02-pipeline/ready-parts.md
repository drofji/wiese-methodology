# Ready Parts: Preparing the Ground for AI

There are two ways to build a bookshelf. In the first, you get a pile of planks, a saw and a bag of loose screws. In the second, you get a flat box with every board cut to size, every hole drilled, the screws sorted into little labelled bags and a picture of how it all goes together. Both shelves can end up fine. Only one of them has a real chance of standing straight on the first try.

AI work is exactly like that. Whoever does the next piece of work, you, a colleague or an AI, starts with nothing but what you hand over. So the most important part happens **before** anything gets written: you prepare the ground. Here are eight ways to do it.

---

## Start from what already works

When there's nothing ready to reuse, the AI builds everything from scratch. Every result comes out a little different from the last one, and you get to check each one from the very beginning. Fun? Not really.

So you collect ready parts, pieces that have already been tested and are known to work. New work then turns mostly into putting those parts together, with as little brand-new material as possible. The safest parts are the ones lots of people have already checked: a widely used open-source framework, reviewed by thousands of developers, beats code that one person or one AI wrote once. In my own work I build on Django, a framework kept alive by a big community, and I collect my own ready parts in an open-source library, Django-Snapadmin, so a new feature becomes mostly settings instead of new code. At home it's the same as cooking from the recipe your family has made a hundred times, instead of guessing the amounts.

Checking is the slowest and most expensive part of working with AI, and a part that many people have already checked doesn't need checking from zero again. Better still, when you combine proven parts, the only thing that can go wrong is a gap in the final picture, a missing field or a missing detail. And gaps are easy to spot.

---

## Let the part explain itself

If using a part the right way takes a long instruction, that instruction will get lost, forgotten or misread sooner or later. The knowledge lives in someone's head or in some other document, not in the part itself.

Nobody reads a manual for a light switch. You see it, you get it. Same with a plug that only fits into the socket one way. Good parts for AI work like that too: they have a clear interface that shows how to use them. A well-described API or MCP server, which is just a fixed, documented way for a program or an AI to use a tool, tells the AI what it can do and what data it needs, no extra explanation required.

An instruction kept somewhere else drifts away from the part and goes stale. An interface can't be skipped, because you use it every time you use the part, so it stays up to date by itself. And it works the same for a person as for an AI.

---

## Guide with words, check with fixed rules

You write rules into your request, and the AI follows some and ignores others. It isn't being difficult. Rules in a request are only advice, and nothing forces anyone to take advice.

So the methodology uses two kinds of rules. **Guiding rules** are the information you put into the context, and they point the work in the right direction. **Fixed rules** are built into an interface, like an API, a script or a test, and they check the result at the end. A parent can ask the kids to buckle up, and that's guidance. The car that keeps beeping until every belt clicks is a fixed rule. In software, your request describes what to build, and automated tests decide whether the result gets in.

You need both. Fixed rules always leave something to fix, and guidance on its own is too weak, because nothing backs it up. Together, the words keep the work flexible and the fixed rules give you certainty at the end.

---

## Let mistakes make noise

When information is missing, the AI fills the hole with a guess, and the guess looks just like a real answer. Nothing stops it.

The cure is to set things up so that a missing piece causes a **loud, visible error**. A cash machine gives you no money until you type the right PIN; it doesn't hand out a guess. In software, a required field without a value stops the process with a clear message, and the AI can't carry on until it supplies the right data. So it tries, adjusts and tries again, the way you'd work through an unfamiliar problem, or the way developers once trawled forums until something finally worked.

A wrong result that looks right is the most expensive mistake there is, because you find it late, often when someone is already using it. A visible error costs one more attempt. Make the gaps loud, and the AI's stubbornness turns from a risk into a strength.

---

## Keep the check apart from the work

Sometimes the AI changes not just the work, but also the check that's supposed to test it.

Think about it: when the same worker writes the result and its check, with the same reasoning and the same context, the check has the same blind spots. You wouldn't mark your own exam. And a check you can edit during the task can be edited until it passes.

So the check is built as a separate part, as if one person were reviewing another. The reviewer gets its own instructions and its own reasoning, and starts from the beginning with its own knowledge and tools, without the first worker's context. The check lives in a fixed interface, such as an API, an MCP server, a framework or a library, and while a task runs, it doesn't move: the AI has to follow its rules and checklists, and often can't change them at all. Improving the checks is its own task, done and reviewed separately. On top of that, automatic checks go together with a human look, and the work is cut into small modules and small steps, so a person can actually keep up with everything that needs checking.

A check that stands apart and stays put for the whole task holds the line. It still gets better over time, just never in the middle of the work it's checking.

---

## Once it works, make it a script

The AI does the same job again and again, and every result can come out slightly different or slightly wrong. Each new try is a new chance to mess up, and nothing from the last try that worked gets kept.

You wouldn't set your alarm by hand every evening when your phone can repeat it. In the same way, as soon as a procedure is clear, you turn it into a script, one defined action that runs with one command. You split the script into small modules with one job each, so you can reuse them, and you cover each module with tests. AI models already write little helper scripts in the background to crunch data, and those drafts are worth keeping and turning into real tools.

A better prompt is still a fresh attempt every single time. A script is checked once and then behaves the same way forever. Writing it isn't wasted time either: the point isn't to save time, it's to put your effort where it counts. What you build up is a growing library of actions you can trust.

---

## Keep related things together

The AI builds something that already exists, just because it looked in the wrong place. Related parts were scattered around, or the same thing went by different names.

A shopping list sorted by aisle makes sure you don't forget the thing next to the one you came for, and in a shop the signs and shelf labels lead you to the right spot. But in a second-hand shop you'll never find that "T-shirt" if it's hanging under "tank top".

So you organise work for AI as a **tree**, where related things sit side by side and each one has a short description. You search by keyword first, and if that fails, you walk the tree, which is the reliable way in. Every level of the tree carries short hints and links to related branches, like signs along a path. Each thing has one name only, because two names for the same thing break the search. And next to the structure, short maps, diagrams or mockups help people find their way too.

Why both search and the tree? Search alone falls over as soon as something has a different name. The tree alone is reliable but slow. Search first saves time, and the tree adds certainty. And a giant list of every name and synonym doesn't fix it either, because with a lot of data it grows too big to keep up to date.

---

## Build on what people have checked

More and more of what gets written today is made by machines, and it's easy to build on stuff nobody has actually checked. Machine-made content is fast and everywhere. Material checked by people takes longer to make and is harder to find.

That checked material is your foundation: working solutions, templates, rules, formulas and scripts. You collect it, keep it up to date and give it to the AI as the base for new work. Without it you have nothing to compare a result against, and errors slip from one piece of work into the next without anyone noticing.

The people who build AI models run into the same problem. The study *AI models collapse when trained on recursively generated data* ([Shumailov et al., 2024](https://doi.org/10.1038/s41586-024-07566-y)) [1] showed that models trained again and again on text made by other models slowly lose the rarer parts of the original data and get worse with every generation. The authors call it "model collapse" and conclude that data from real human activity gets more valuable as machine-made content spreads.

What people have checked is your measuring stick. Everything else gets measured against it.

---

## Sources

All sources are open and free to read. Each entry says which point in this chapter it supports.

1. **Shumailov et al., *AI models collapse when trained on recursively generated data*, Nature 631, 2024** — https://doi.org/10.1038/s41586-024-07566-y
   Supports: models trained repeatedly on machine-made content lose rare data and degrade; human-made data gains value. Section "Build on what people have checked".
