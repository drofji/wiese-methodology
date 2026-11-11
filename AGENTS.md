# AGENTS.md — Guide for AI Assistants

This file tells any AI assistant what the Wiese Methodology is and how to work on it correctly. Read it before you change anything in this repository.

## What this project is

- **The Wiese Methodology** is a practical way to work with AI safely and with confidence. It is the author's (Alexander Wiese) own method, built from his path as a developer: what he tried, what failed, what worked.
- **The repository is a book.** It is published on GitBook from the `main` branch. A push to `main` goes live at once.
- **The mission is to remove the fear of working with AI.** Three fears keep people away: data leaks, AI doing the wrong work, and hallucinations (the AI inventing facts). Every page answers these fears with concrete practices that anyone can check.
- **The audience is everyone who works with AI**, not only developers. Software is the example domain, because it is the author's field and the one most closely tied to AI today.

## The core ideas

1. **Say it simply.** Clear words leave less room for guessing.
2. **Take small steps.** Small tasks are easier to explain, check and fix.
3. **Share only what is needed.** What the AI never sees, it cannot leak.
4. **Check before you trust.** Every result passes a check before it is used.
5. **Learn from mistakes.** Your own, and the ones others have already made.

## How the methodology works with AI

These are the author's approved practices. Follow them in your own work on this repository too.

- **A task says five things:** where, what, what the result looks like, how it is checked, and what happens at the end. It gives the result and who it is for first; it gives the path only where the path matters. See *Writing a Task for AI*.
- **Show, don't describe.** Point to an existing example instead of describing one.
- **Read first.** Read what already exists before you add anything. Show your analysis only in risky tasks.
- **Ask, don't guess.** If something is unclear, ask. Make an assumption only when no answer comes, and then state it openly.
- **Stop and ask before** anything public, any deletion (keep a copy instead), and anything that was not asked for.
- **Side finds are never lost and never changed silently.** Mark each find as important (it belongs to the same part as the task) or secondary. If it is important, ask, and change it only after the author's yes. Otherwise leave it alone and add it as a new task to the plan.
- **Name the source and its version, always.**
- **Anything that leaves the working circle is a draft.** E-mails, shared data, files and public pages are never sent or opened without a check by a person. Another AI session may check internal work only.
- **Guide with words, check with fixed rules.** What must always hold is enforced by automatic checks, not only by words in a prompt. The check stays apart from the work. Say openly what you could not check.
- **Tests:** a bug fix starts with a test that fails without the fix; a new feature gets its tests after its interface is designed. Accessibility is always part of the checks.
- **Build on ready parts:** reuse what already works and what people have checked; once a procedure works, turn it into a script. See *Ready Parts*.

## How to write for the book

- **Plain English.** Short sentences, everyday words, one idea per sentence. If a technical term cannot be avoided, explain it in one plain sentence. This is part of the method itself: clear input leads to fewer wrong turns.
- **It reads like a book, not like a form.** Tell each idea as flowing text: the problem, why it happens, the solution, why this solution and not the obvious alternatives, and what the reader gains. Open a chapter with a short everyday scene. Write prose, not documentation: paragraphs instead of bullet points and numbered lists, unless the content truly is a list.
- **Tone: simple, lively, slightly youthful, abstract.** A light, friendly voice that talks to the reader directly as "you", with short sentences, a question or a bit of humour where it fits, and ideas framed as general principles. Light does not mean sloppy: correct grammar, consistent terms, no slang a reader might not know.
- **The simplest examples.** Use situations everyone knows (buying milk, a shopping list, a note on the fridge, a recipe) and weave the matching software example into the same sentences. Examples live inside the text, never in separate blocks.
- **No repetition.** Each fact, rule or example appears once; later sections refer back to it. No summary sections that only repeat a chapter.
- **Short section titles in plain words.** End each section on a line that makes its point.
- **Exact facts.** Numbers come only from cited, open and free sources. Say plainly when an idea is reasoning, not measurement.
- **Sources traceable both ways.** Name the source where it is used — title in italics, a link with authors and year, and its number: `the study *Lost in the Middle* ([Liu et al., 2024](url)) [1]`. In the list at the end, number sources in order of first use and add to each a line "Supports: <claim and numbers>. Section "<title>"."
- **Tool-neutral.** Never tie a title, file name or principle to one AI product or one rule-file format. Name specific tools only as one example among several.
- **Terms:** use *Pipeline Architecture*, *Quality Gates*, *Automated Validation* and *Failure Prevention* (or *mistake-proofing*). Do not use "Poka-Yoke".

## Content boundary

- **Public and personal only.** No client names, employer internals, proprietary code, contracts, figures, or anything traceable to a specific company or project.
- **Other people's mistakes are described in general terms**, never as identifiable people, companies or projects.
- **Never invent the author's experience or opinions.** If something is missing, mark it as an open question for the author.
- **No AI or co-author traces** in the content.

## How changes reach the book

- **The author approves every topic first.** Topics are discussed and drafts are kept in the git-ignored `.claude/` folder (`.claude/roadmap.md`, `.claude/drafts/`) until the author approves them. Only then do they move into `docs/`.
- **Every page sits in the `SUMMARY.md` hierarchy.** The "Docs check" CI validates `gitbook-docs.yaml` and the `SUMMARY.md` links; run it locally with `python .github/scripts/check_gitbook.py`.
- **Every visible change gets an entry in `CHANGELOG.md`** under `## [Unreleased]`, in the same change.
- **Never commit, push or publish without the author's explicit yes.** A push to `main` is a publication.
