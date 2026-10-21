# The Manifesto & Challenges

## Why this methodology exists

Many people are afraid to work with AI.

Not only beginners. Very experienced developers often refuse to use it. And it is not only developers — people in many other fields feel the same.

Three fears come up again and again:

1. **Data leaks.** "What happens to the information I give the AI? Who else can see it?"
2. **Wrong work.** "I asked for one thing, and the AI did something else."
3. **Hallucinations.** "The AI made something up — and it sounded completely sure."

These fears are fair. Each of them can really happen.

But staying away from AI is not the answer. The answer is a way of working that makes these risks **visible** and **controllable**. That is what this methodology is about.

## What the Wiese Methodology is

The Wiese Methodology is a practical way to work with AI safely and with confidence.

It is built from my own path as a developer: what I tried, what failed, what worked, and how my way of thinking had to change. It brings together:

- **The concept** — the core ideas behind working with AI in a controlled way.
- **My path** — how I grew as a developer and how I came to these ideas.
- **What works** — the solutions and ways of working I found.
- **Mistakes** — my own, and common mistakes other people make (described in general terms, not about any specific person or company).
- **Better thinking** — how to improve the way you plan, work, and check results, especially when an AI is part of the work.

## Who it is for

Everyone who works with AI — or wants to, but is not sure they can trust it.

Most examples come from software development. That is my field, and it is also the field most closely tied to AI today. Developers meet AI's problems first and most often, so their lessons are a good map for everyone else.

If you are not a developer, read the examples as stories. The tools change from field to field. The thinking stays the same.

## How the methodology answers each fear

| Fear | Where it usually comes from | What the methodology does |
|---|---|---|
| **Data leaks** | The AI gets more information than the task needs. | Give the AI only what the task needs. Never share passwords, private data, or anything confidential. Work with general, public information wherever you can. |
| **Wrong work** | The task is too big or not clear enough. | Split work into small, clear steps. Say exactly what "done" looks like before you start. Check each step before moving on. |
| **Hallucinations** | The AI fills gaps by guessing. | Give clear facts instead of leaving gaps. Allow the AI to say "I don't know". Never use a result without checking it — first with automatic checks, then with your own eyes. |

The following chapters explain each answer in detail:

- [Flow Stages & Atomic Tasks](../02-pipeline/stages.md) — how to split work into small, safe steps.
- [Context Window Management](../02-pipeline/context-management.md) — what to give the AI, and what to keep away from it.
- [AI Failure Patterns & Hallucinations](../03-quality-gates/ai-errors.md) — how AI goes wrong, and how to notice it.
- [Automated Quality Gates](../03-quality-gates/automated-gates.md) and the [Pre-Merge Human Review Checklist](../03-quality-gates/human-checklist.md) — how to check results before you trust them.

## A key principle: say it simply

This methodology is written in plain English, on purpose.

Clear and simple words are not just easier to read. They are part of the method. When you describe a task simply and precisely, the AI has less to interpret and less room to guess. The same is true for people.

Unclear words lead to guesses. Guesses lead to mistakes. So the first and cheapest way to prevent mistakes is to say exactly what you mean, in words anyone can understand.

**Clear input → fewer wrong turns.**

## The core ideas in short

1. **Say it simply.** Clear words leave less room for guessing.
2. **Take small steps.** Small tasks are easier to explain, check, and fix.
3. **Share only what is needed.** What the AI never sees, it cannot leak.
4. **Check before you trust.** Every result passes a check before it is used.
5. **Learn from mistakes.** Your own, and the ones others have already made.

## What you will not find here

No company secrets, no client stories, no private code. Everything here is based on public, general knowledge and on my personal experience. Mistakes made by others are described in general terms, so the lesson stays and the people stay private.
