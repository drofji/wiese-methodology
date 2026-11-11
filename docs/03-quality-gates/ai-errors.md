# AI Failure Patterns & Hallucinations

Hand a friend a fat folder of two hundred pages and ask one question. The answer is on page ninety. They read the first pages carefully, skim the middle, read the last pages again, and give you an answer with a straight face. It's wrong. They didn't lie. They just missed the middle.

AI models make the very same mistake, and they make it in a voice that sounds every bit as sure as when they're right. An answer that sounds certain but isn't backed by the facts is called a **hallucination**. This chapter is about where those errors come from, and why most of them never have to reach your final result.

Every number here comes from published research you can read for free. Each study is named right where it's used, with a link, and the list at the end tells you which point each one backs up. Where an idea rests on reasoning rather than on measurement, the text says so.

---

## The middle of the pile

A model doesn't read its input the way you'd read a contract, line by line with the same attention all the way through. It uses what's at the **start** and at the **end** best, and what's in the **middle** worst.

And the effect is bigger than you'd think. In the study *Lost in the Middle* ([Liu et al., 2024](https://arxiv.org/abs/2307.03172)) [1], a model got the answer right 75.8% of the time when it sat in the first of twenty documents, and only 53.8% when it sat in the middle. With no documents at all, it scored 56.1%. Read that again: hiding the answer in the middle helped less than giving the model nothing.

Length makes it worse. The *RULER* benchmark ([Hsieh et al., 2024](https://arxiv.org/abs/2404.06654)) [2] tested seventeen models that claimed to handle at least 32,000 tokens, and only about half still did well at that length. When the answer uses different words from the question, so the model has to actually understand instead of just matching, the drop gets steeper: in the *NoLiMa* test ([Modarressi et al., 2025](https://arxiv.org/abs/2502.05167)) [3], one leading model fell from 99.3% to 69.7%. And the study *Same Task, More Tokens* ([Levy et al., 2024](https://arxiv.org/abs/2402.14848)) [4] shows that reasoning gets weaker long before a model hits its technical limit.

Your first instinct is probably to give the AI *more*, just to be safe. That's exactly the wrong move. The *Context Rot* study ([Hong et al., 2025](https://www.trychroma.com/research/context-rot)) [5] tested eighteen models and found that quality drops as the input grows, even when the task stays the same. On one memory test, a short, focused input of about 300 tokens beat the full input of about 113,000 tokens for every single model. Material that looked similar but didn't matter made things worse still.

So the methodology goes the other way. You split big work into small tasks, and each task gets only what it needs: its goal, the parts it touches and the rules that apply. When you ask someone to bake a cake, you hand them that one recipe, not the whole cookbook, and a developer likewise hands over one module and its interface, not the entire codebase. Whatever context size a model advertises, you treat it as a ceiling, never as the size you actually work with.

A short context is easier for the model to use, and it's also easier for you to check. That second part turns out to matter even more.

---

## Rules that fade

At the start of a long session you set the rules: no personal data in reports, no touching the tests, ask before deleting anything. Many steps later, the AI quietly stops following one of them.

Nothing spooky happened. The rules were given once, and as the conversation grew, they slid into the middle, the part the model uses least. Nothing pulled them back up.

A shopping list only helps if you look at it right before you leave the house, not once on Monday morning. The methodology works the same way: right before each piece of work, the task repeats three things, namely what the goal is, where the AI has to stop and hand back, and which checklist the result has to pass. It takes a few lines.

This idea hasn't been measured on its own; it follows from how models use their input. Whatever stands right before the work is what the model uses best, so that's where your rules belong.

---

## Who checks the checker

The AI says: "Done. Everything works." Part of it doesn't.

Telling the model to "check carefully" helps a bit, but it's just one more instruction that can fade, judged by the same attention that made the mistake in the first place. Still, a deliberate checking step makes a striking difference. In the *Chain-of-Verification* study ([Dhuliawala et al., 2023](https://arxiv.org/abs/2309.11495)) [6], having the model verify its own answers in a structured way more than doubled the precision of its lists (from 0.17 to 0.36) and raised a fact score for biographies from 55.9 to 71.4.

The methodology goes one step further and moves the check **outside the model**, where attention plays no part, and every result passes three checks in the same order. First comes **the checklist**: is everything the task asked for actually there? The AI ticks an item only with proof, like a test that passes or a link to the place that does the job, and an item without proof stays open, so the work isn't finished. Then come **the tests**: the work counts as done only when the automatic checks find nothing. A small finding can become a new task and get fixed later, but it's never ignored, and a test is **never** weakened to make it pass, because a weakened test doesn't remove the error, it just hides it. Last comes **a human look where it matters**. A person always checks the important items, meaning anything that touches money or personal data, changes how parts work together or how data is stored, or has been marked as risky, and gives the rest spot checks of their own choosing. Small, ordinary tasks get looked at together once their whole module is ready, while large and risky tasks get looked at one by one.

A clean test run doesn't replace the checklist, by the way. A test only finds what it was built to look for, so you still walk the checklist item by item.

A teacher with thirty notebooks works exactly like this. She doesn't redo every sum. She checks that every exercise is there, looks closely at the hardest one and picks a few others at random. And before any work starts, someone also reads the task itself, because a wrong task gets you a perfect answer to the wrong question.

This is what lets the work move fast. An AI soon produces more than anyone can read line by line, so the system has to find most errors on its own, with checklists that demand proof and tests that never get tired. Your attention then goes where a mistake would cost the most.

A test either passes or fails. It doesn't get tired, and you can't talk it round.

---

## Many hands, one memory

The checks above quietly do something else, too: they **remember**.

Picture a family getting ready for a big birthday party. Lots of jobs, lots of helpers, and nobody can keep it all in their head. It still works, because the jobs are on a list on the fridge and everyone writes their name next to the one they take. Nothing gets bought twice, and nothing gets forgotten.

AI work looks more and more like that party. You might run several AI sessions at once, and several people might work on the same project. Each session only remembers its own conversation and can't see what the session next to it has done or is about to do. Left alone, steps get lost and work gets done twice.

So the methodology keeps the memory outside the AI, where everyone can see it. A **shared task list** shows what's open, reserved, in progress and done; in a small project one file is enough, and a bigger one uses a task manager. A **visible reservation** marks a task as "in progress" before anyone starts on it, so no other session grabs it, and **automatic checks** make sure no session works on a task someone else has reserved. On top of that, the **stages are planned up front**: you split the work as well as you can, the AI may split it further into steps that suit it, and then talks its plan and any unclear points through with you before it starts. Each stage then passes the three checks.

The written stages and the shared status are your list on the fridge. They keep track of what has to be done and what was supposed to be done, however many hands are at work.

---

## What the methodology can and cannot promise

Let's be precise here, because overpromising is its own kind of hallucination.

The methodology doesn't make a model invent less. How often a model makes things up depends on the model itself. On the public *Hallucination Leaderboard* ([Vectara](https://github.com/vectara/hallucination-leaderboard)) [7], the rate for summarising a given text ranged from 1.8% to 24.2%, depending on the model (as of 22 October 2026).

What the methodology changes is how many of those errors **get through**. A short, focused context gives the model less to miss. A goal repeated right before the work keeps the rules alive. Checks outside the model catch what's left, and a shared memory makes sure nothing falls between sessions or people.

A free prompt bets on the model getting everything right. A simple task list helps everyone find their way, but it's only more text in the same context, and nothing enforces it. How big the difference between these ways of working really is hasn't been measured yet. That measurement is planned, and this chapter will be updated with the results.

---

## Sources

All sources are open and free to read. Each entry says which point in this chapter it supports.

1. **Liu et al., *Lost in the Middle: How Language Models Use Long Contexts*, TACL 2024** — https://arxiv.org/abs/2307.03172
   Supports: models use the start and end of their input best and the middle worst (75.8% / 53.8% / 56.1%). Section "The middle of the pile".
2. **Hsieh et al., *RULER: What's the Real Context Size of Your Long-Context Language Models?*, COLM 2024** — https://arxiv.org/abs/2404.06654
   Supports: only about half of seventeen models claiming 32,000 tokens still perform well at that length. Section "The middle of the pile".
3. **Modarressi et al., *NoLiMa: Long-Context Evaluation Beyond Literal Matching*, ICML 2025** — https://arxiv.org/abs/2502.05167
   Supports: the drop is larger when the answer uses different words from the question (99.3% → 69.7%). Section "The middle of the pile".
4. **Levy, Jacoby, Goldberg, *Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models*, ACL 2024** — https://arxiv.org/abs/2402.14848
   Supports: reasoning weakens long before the technical limit. Section "The middle of the pile".
5. **Hong, Troynikov, Huber, *Context Rot: How Increasing Input Tokens Impacts LLM Performance*, Chroma, 2025** — https://www.trychroma.com/research/context-rot
   Supports: more input lowers quality; a focused input of about 300 tokens beat about 113,000 tokens for every model. Section "The middle of the pile".
6. **Dhuliawala et al., *Chain-of-Verification Reduces Hallucination in Large Language Models*, 2023** — https://arxiv.org/abs/2309.11495
   Supports: a structured checking step reduces invented answers (precision 0.17 → 0.36; fact score 55.9 → 71.4). Section "Who checks the checker".
7. **Vectara, *Hallucination Leaderboard*** — https://github.com/vectara/hallucination-leaderboard
   Supports: how often a model invents facts depends on the model (1.8% to 24.2%, as of 22 October 2026). Section "What the methodology can and cannot promise".
