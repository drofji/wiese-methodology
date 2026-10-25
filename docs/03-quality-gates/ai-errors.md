# AI Failure Patterns & Hallucinations

Imagine handing a new colleague a folder of two hundred pages and asking one question. The answer is on page ninety. They read the first pages with care, skim the middle, read the last pages again, and answer with confidence. The answer is wrong. They did not lie. They simply missed the middle.

AI models make the same kind of mistake, and they make it in a voice that sounds just as sure as when they are right. An answer that sounds certain but is not backed by the facts is called a **hallucination**. This chapter is about where such errors come from and why most of them never need to reach the final result.

Every number here comes from published research that anyone can read for free. Each study is named where it is used, with a link, and the list at the end says which point each one supports. Where an idea rests on reasoning rather than on measurement, the text says so.

---

## The middle of the pile

A model does not read its input the way a careful person reads a contract, line by line with equal attention. It uses what stands at the **start** and at the **end** best, and what lies in the **middle** worst.

The effect is larger than most people expect. In the study *Lost in the Middle* ([Liu et al., 2024](https://arxiv.org/abs/2307.03172)) [1], a model answered correctly 75.8% of the time when the answer was in the first of twenty documents, and only 53.8% when it was in the middle. Given no documents at all, it scored 56.1%. In other words, burying the answer in the middle helped less than giving the model nothing.

Length makes it worse. The *RULER* benchmark ([Hsieh et al., 2024](https://arxiv.org/abs/2404.06654)) [2] tested seventeen models that claimed to handle at least 32,000 tokens; only about half still performed well at that length. When the answer uses different words from the question, so that the model has to understand rather than match, the drop is larger: in the *NoLiMa* test ([Modarressi et al., 2025](https://arxiv.org/abs/2502.05167)) [3], one leading model fell from 99.3% to 69.7%. And the study *Same Task, More Tokens* ([Levy et al., 2024](https://arxiv.org/abs/2402.14848)) [4] shows that reasoning weakens long before a model reaches its technical limit.

The natural reaction is to give the AI *more*, just to be safe. That is exactly the wrong move. The *Context Rot* study ([Hong et al., 2025](https://www.trychroma.com/research/context-rot)) [5] tested eighteen models and found that quality drops as the input grows, even when the task itself stays the same. On one memory test, a short, focused input of about 300 tokens beat the full input of about 113,000 tokens for every model tested. Similar-looking but irrelevant material made things worse still.

So the methodology works the other way round. Large work is split into small tasks, and each task receives only what it needs: its goal, the parts it touches, and the rules that apply. A developer hands over one module and its interface, not the whole codebase. A good kitchen hands the cook one recipe card, not the pantry inventory. The advertised size of a model's context is treated as a ceiling, never as a working size.

A short context is easier for the model to use, and it is also easier for a person to check. That second benefit turns out to matter even more.

---

## Rules that fade

At the start of a long session you set the rules: no personal data in reports, no changes to the tests, ask before deleting anything. Many steps later, the AI quietly stops following one of them.

Nothing mysterious has happened. The rules were given once, and as the conversation grew they drifted into the middle, the place the model uses least. Nothing brought them back.

Pilots have a simple answer to this problem: they read the same checklist before every take-off, even after thousands of flights. The methodology does the same. Right before each piece of work, the task restates three things: what the goal is, where the AI must stop and hand back, and which checklist the result must pass. It takes a few lines.

This idea has not been measured on its own; it follows from how models use their input. What stands just before the work is what the model uses best, so that is where the rules belong.

---

## Who checks the checker

The AI reports: "Done. Everything works." Part of it does not.

Asking the model to "check carefully" helps a little, but it is one more instruction that can fade, judged by the same attention that made the mistake. Even so, the effect of a deliberate checking step is striking. In the *Chain-of-Verification* study ([Dhuliawala et al., 2023](https://arxiv.org/abs/2309.11495)) [6], having the model verify its own answers in a structured way more than doubled the precision of its lists (from 0.17 to 0.36) and raised a fact score for biographies from 55.9 to 71.4.

The methodology goes one step further and moves the check **outside the model**, where attention plays no part. Every result passes three checks, always in the same order:

1. **The checklist.** Is everything the task asked for actually there? If something is missing, the work is not finished.
2. **The tests.** Do the automatic checks pass? If a test fails, the code is fixed, or the case that failed is handled. A test is **never** weakened to make it pass, because a weakened test does not remove the error. It only hides it.
3. **A human look.** Does it work the way it should? If not, it is fixed or redone.

A house is accepted the same way. The builder ticks off the work order, an inspector tests the wiring, and only then does the owner walk through the rooms. Before any work starts, a person also reads the task itself, because a wrong task produces a perfect answer to the wrong question.

A test either passes or fails. It does not get tired, and it does not get persuaded.

---

## Many hands, one memory

The checks above do something less obvious as well: they **remember**.

Picture a busy restaurant on a Friday night. Ten cooks, forty orders, and no one can hold all of it in their head. The kitchen still works, because every order is a ticket on a board. A cook takes a ticket and pins it to their station. No dish is cooked twice, and none is forgotten.

Work with AI looks more and more like that kitchen. One person may run several AI sessions at once; several people may work on the same project. Each session remembers only its own conversation. It cannot see what the session next to it has done or is about to do. Without help, steps get lost and work gets done twice.

The methodology keeps the memory where everyone can see it, outside the AI:

- **A shared task list** shows what is open, reserved, in progress and done. In a small project one file is enough; a larger project uses a task manager.
- **A visible reservation** marks a task as "in progress" before anyone starts on it, so no other session picks it up.
- **Automatic checks** confirm that no session is working on a task that another one has reserved.
- **Stages planned up front.** The person splits the work as well as possible. The AI may split it further into steps that suit it, and then talks its plan and any unclear points through with the person before it begins. Each stage then passes the three checks.

The written stages and the shared status are the restaurant's ticket board. They keep track of what has to be done and what was supposed to be done, however many hands are at work.

---

## What the methodology can and cannot promise

It is worth being precise here, because overpromising is its own kind of hallucination.

The methodology does not make a model invent less. How often a model invents facts depends on the model itself. On the public *Hallucination Leaderboard* ([Vectara](https://github.com/vectara/hallucination-leaderboard)) [7], the rate for summarising a given text ranged from 1.8% to 24.2%, depending on the model (as of 22 October 2026).

What the methodology changes is how many of those errors **get through**. A short, focused context gives the model less to miss. A goal restated before the work keeps the rules alive. Checks outside the model catch what is left, and a shared memory makes sure nothing falls between sessions or people.

A free prompt relies on the model to get everything right. A simple task list helps everyone find their way, but it is only more text in the same context, and nothing enforces it. How large the difference is between these ways of working has not yet been measured. That measurement is planned, and this chapter will be updated with its results.

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
