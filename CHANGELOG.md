# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
History before this file was created lives in the git log.

## [Unreleased]

### Added
- "Who Decides, Who Works" page (was the empty "Role Separation: Architect vs. Operator"): roles instead of job titles, one main AI session that talks to you and runs the helpers, why a helper gets a complete task and why every plan comes back to the main session, how the model is picked by the kind of work, and the three things only a person ever does.
- "Human Review: Where a Person Looks" page (was the empty "Pre-Merge Human Review Checklist"): how a risky task names, at each step, what else it touches; the four things a person looks at in review; and where a failed review sends the work back to.
- "Flow Stages & Atomic Tasks" page (was empty): how work is split into project, stages and tasks, why a task is measured by one area of change and a short checklist rather than by time, why each task stands alone and leaves one trace, how statuses grow with the project, and what happens to open tasks when the plan changes.
- "Quality Gates: Checklists at Every Step" page (was the empty "Automated Quality Gates"): every task carries two lists — what to do and how we know it is done — agreed before work starts; each tick needs its own proof, a separate session runs the checks, and a failed check sends the whole list back to the start.
- "Writing a Task for AI" page (was the empty "Prompt Templates"): what a good task says, where the AI must stop and ask (anything public, deleting, anything not asked for), why an example beats a description, and how repeated instructions are written once in three layers — project rules, reusable skills, and the tools themselves.
- "AI Failure Patterns & Hallucinations" page: why models miss information in long context and invent facts, what open research has measured about it, and how short tasks, restated goals, checks outside the model and a shared task memory keep these errors from reaching the result. Seven open sources, each named where it is used and listed with the point it supports; no unmeasured numbers.
- "Ready Parts: Preparing the Ground for AI" page: eight principles for preparing work before AI touches it, each explained as problem, cause, solution, reasoning and result, with everyday examples.
- "The Manifesto & Challenges" page: why the methodology exists, the three common fears about AI (data leaks, wrong work, hallucinations) and how the methodology answers each, who it is for, and the plain-language principle.
- "Docs check" CI workflow on pushes and pull requests to `main`: validates `gitbook-docs.yaml` against GitBook's published schema and import rules, and fails when `SUMMARY.md` links a missing file or lists a file twice. Run it locally with `python .github/scripts/check_gitbook.py`.

### Changed
- "The Manifesto & Challenges" page rewritten in the new tone: light, flowing text that talks to the reader; the fears table and the lists are now told as prose.
- "Writing a Task for AI" page rewritten in the new tone: light, flowing text that talks to the reader, with the examples inside the sentences instead of lists.
- "Human Review: Where a Person Looks" page rewritten in the new tone: light, flowing text that talks to the reader, with the examples inside the sentences instead of lists.
- "Quality Gates: Checklists at Every Step" page rewritten in the new tone: light, flowing text that talks to the reader, with the examples inside the sentences instead of lists.
- "AI Failure Patterns & Hallucinations" page rewritten in the new tone: light, flowing text that talks to the reader, with the examples inside the sentences instead of lists; all numbers and sources unchanged.
- "Ready Parts" page rewritten in the new tone: light, flowing text that talks to the reader, with the examples inside the sentences instead of lists.
- "Flow Stages & Atomic Tasks" page rewritten in the new tone: the same content told as light, flowing text that talks to the reader, with the examples inside the sentences instead of lists.
- `AGENTS.md` writing rules now ask for written prose instead of lists, examples inside the sentences, and a simple, lively, slightly youthful tone.
- "AI Failure Patterns & Hallucinations" page: the human check now goes where it matters — a person always checks the important items and spot-checks the rest; checklist items are ticked only with proof; small findings may become new tasks. The Manifesto says the same.
- `AGENTS.md` now explains the methodology itself — its mission, core ideas, approved ways of working with AI, writing rules, content boundary and how changes reach the book — so any AI assistant can work on the project correctly.
- "AI Failure Patterns & Hallucinations" page: examples replaced with everyday ones (a recipe, a shopping list, checking homework, a party list on the fridge).
- "Ready Parts" page rewritten to read like a book chapter: the same eight principles told as one story with everyday examples, without repeated headings or the summary table, and with its source named in the text.
- The toolkit page on rule files is now tool-neutral: "System Rules for AI Assistants" replaces "System Rules (.cursorrules)", and the README no longer ties the methodology to a single AI tool.

### Fixed
- The author's GitHub link on the "Contributors & Attribution" page now points to the real account (@drofji).
- GitBook site sync: `gitbook-docs.yaml` now follows GitBook's site configuration schema, so the documentation site can publish from the repository instead of failing every sync with "Failed to parse site configuration".
- The "Prompt Templates" entry in the table of contents now points to an existing page (the file name had a typo).
- The table of contents no longer links the non-existent `CONTRIBUTORS.md`; contributors and attribution live on a single page.
