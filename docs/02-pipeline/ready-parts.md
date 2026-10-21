# Ready Parts: Preparing the Ground for AI

When you work with AI, you rarely know who will write the next part of the work: you, a colleague, or an AI model. Whoever it is starts with only what you provide.

The most important work therefore happens **before** anything is written: preparing the ground. This chapter describes eight principles for doing so.

Each principle follows the same structure: **the problem, why it happens, how to solve it, why this approach, and what you gain.**

---

## 1. Build from proven parts

**The problem**
The AI builds everything from scratch. Each result differs slightly from the last, and each one must be checked in full.

**Why it happens**
The AI has no proven building blocks to start from. When there is nothing to reuse, it invents.

**How to solve it**
Collect ready parts: components that have already been tested and are known to work. Build new solutions by combining these parts, and keep the amount of new work to a minimum.

Prefer parts that many people have already checked. A widely used open-source framework, reviewed by thousands of developers, is more reliable than code written once by a single person or a single AI.

- **In software:** I build on Django, a framework maintained and reviewed by a large community. On top of it, I collect my own ready parts in an open-source library, Django-Snapadmin. A new feature becomes mostly configuration rather than new code.
- **In everyday life:** a cook follows a tested recipe instead of guessing quantities. An accountant uses an invoice template whose formulas are already correct.

**Why this approach**
Checking is the slowest and most expensive part of working with AI. A part that many people have already checked does not need to be checked again from the beginning. Writing everything anew, even with careful review, means a full review every time. Composition also limits what can go wrong: when proven parts are combined, an error can only be a gap in the final picture, and gaps are easy to see.

**What you gain**
Less new work, fewer new errors, and faster results. When something is still wrong, it is usually something *missing*, such as a field or a detail, rather than something broken.

---

## 2. Let the interface explain itself

**The problem**
Using a component correctly requires long instructions. Those instructions get lost, forgotten, or misread.

**Why it happens**
The knowledge of how to use the component lives in someone's head or in a separate document, not in the component itself.

**How to solve it**
Give every component a clear interface that shows how it is used. The interface becomes the instruction.

- **In software:** a well-described API or MCP server tells the AI what it can do and which data it requires. No additional context is needed.
- **In everyday life:** a well-designed form has clear fields and labels. Nobody needs a manual to complete it.

**Why this approach**
Instructions kept in a separate document drift away from the component, become outdated, or are simply not read. An interface cannot be skipped: it is used every time the component is used, so it stays current. It also works the same way for a person and for an AI.

**What you gain**
Less context to supply, less to explain, and less room for misunderstanding, for people and AI alike.

---

## 3. Guide with context, verify with fixed rules

**The problem**
You include rules in your request. The AI follows some of them and ignores others.

**Why it happens**
Rules written in a request are guidance only. Nothing enforces them.

**How to solve it**
Use two kinds of rules:

- **Dynamic rules** are the information you provide in the context. They **guide** the work in the right direction.
- **Fixed rules** are built into an interface, such as an API, a script, or a test. They **verify** the result at the end.

Context guides; the interface verifies.

- **In software:** the request describes what to build; automated tests decide whether the result is accepted.
- **In everyday life:** a manager explains a task to a new employee (guidance), while the accounting system rejects any invoice without a tax number (a fixed rule).

**Why this approach**
Fixed rules alone are never enough: every set of fixed rules always has something left to correct. Guidance alone is too weak: nothing ensures it is followed. Combining the two gives each its proper role: flexibility during the work, certainty at the end.

**What you gain**
Flexibility where it is useful, and a firm stop where mistakes are not acceptable.

---

## 4. Let errors show the way

**The problem**
When information is missing, the AI fills the gap with a guess, and the guess looks like a real answer.

**Why it happens**
Nothing stops it. A silent gap is filled with something that merely *sounds* right.

**How to solve it**
Design your work so that missing information produces a **clear, visible error**. The AI then cannot proceed until it supplies the correct data. It tries, adjusts, and tries again, just as people approach an unfamiliar problem, and just as developers once searched forums and chats until a solution finally worked.

- **In software:** a required field without a value stops the process with a clear message.
- **In everyday life:** a cash machine releases no money until the correct PIN is entered.

**Why this approach**
A wrong result that looks correct is the most expensive kind of mistake, because it is discovered late, often by the end user. An error costs one more attempt. A hidden guess can cost far more, much later. Making gaps visible turns the AI's persistence into an advantage instead of a risk.

**What you gain**
No silent wrong results. Every gap surfaces early, while it is still cheap to fix.

---

## 5. Keep the check separate from the work

**The problem**
The AI changes not only the work, but also the check that is meant to test it.

**Why it happens**
When the same worker creates both the result and its check, with the same reasoning and the same context, the check inherits the same blind spots. And a check that can be edited during the task can be edited to pass.

**How to solve it**
Build the check as an independent part, as if one person were reviewing another. The reviewer has separate instructions and separate reasoning, and starts from the beginning with its own knowledge and tools, without the first worker's context.

Place the check in a fixed interface, such as an API, an MCP server, a framework, or a library. While a task is being processed, the check does not change: the AI must follow its rules and checklists, and in many cases it cannot change them at all. Improving the checks is a separate task, done and reviewed on its own.

Combine automated checks with human review, and work in small modules and small steps, so that a person can keep pace with everything that needs to be verified.

- **In software:** tests and validation rules live in their own interface, and any change to them is reviewed by a person.
- **In everyday life:** the person who drafts a contract is not the person who approves it.

**Why this approach**
Asking the same AI to review its own work repeats its reasoning and its blind spots. A check kept in the same place as the work can be bent to fit the work. A check that is independent and fixed for the duration of the task holds the line; it still evolves over time, but only as separate, reviewed work.

**What you gain**
Mistakes are found by someone who did not make them. Weak points appear early, while they are still small.

---

## 6. Turn every algorithm into a script

**The problem**
The AI performs the same task again and again, and each result may differ slightly or be slightly wrong.

**Why it happens**
Every new attempt is a new opportunity to hallucinate, and nothing is kept from the last attempt that worked.

**How to solve it**
As soon as a procedure is clear, turn it into a script: a defined action that runs with a single command. Divide it into small modules, each with a single responsibility, so that they can be reused. Cover each module with tests.

AI models already write small helper scripts in the background to process data. Do not discard these drafts; turn them into tools.

- **In software:** a tested script handles a recurring data task instead of a new AI request each time.
- **In everyday life:** a saved spreadsheet with working formulas replaces the same manual calculation every month.

**Why this approach**
A more precise prompt is still a new attempt each time, and every attempt carries a new risk of error. A script is verified once and then behaves the same way every time. Because the AI already produces such scripts as drafts, keeping them costs very little.

**What you gain**
A verified result, reuse from the very first day, and a growing library of reliable actions. The time spent writing a script is not lost: the procedure is verified once and works every time afterwards. The goal is not to save time, but to use your resources well.

---

## 7. Keep related things together

**The problem**
The AI builds something that already exists, simply because it looked in the wrong place.

**Why it happens**
It could not see what was already there. Related parts were scattered, or the same thing appeared under different names.

**How to solve it**
Organise your work as a **tree**, in which related items sit side by side and each carries a short description.

- **Finding things:** search by keyword first. If that fails, walk the tree, which is the reliable path.
- **Guidance along the way:** at every level of the tree, provide hints and links to related branches.
- **Consistent names:** give each thing a single name. Different names for the same thing break the search.
- **Readability for people:** alongside the structure, keep short maps, diagrams, or mockups.

Examples:

- **In software:** modules are grouped by area, each with a short description, and the project has a simple map.
- **In everyday life:** a shopping list grouped by aisle ensures you do not forget the item next to the one you came for. In a shop, department signs and shelf labels lead you to the right place. In a second-hand shop, however, you will not find a "T-shirt" if it is hanging under "tank top".

**Why this approach**
Search alone fails whenever the same thing carries a different name. A tree alone is reliable but slow. Searching first saves time; falling back to the tree adds certainty. A complete list of every name and synonym is not the answer either: with a lot of data, it grows too large to maintain.

**What you gain**
Existing work is found instead of rebuilt. People and AI find their way faster and create fewer duplicates.

---

## 8. Treat human-verified material as the foundation

**The problem**
A growing share of content is produced by machines, and it is easy to build on material that no one has actually verified.

**Why it happens**
Machine-generated content is fast and abundant. Human-verified material takes longer to create and is harder to find.

**How to solve it**
Treat human-verified material, including working solutions, templates, rules, formulas, and scripts, as your foundation. Collect it, maintain it, and give it to the AI as the basis for new work.

The developers of AI models face the same challenge. Research published in *Nature* in 2024 showed that models trained repeatedly on content generated by other models gradually lose the less common parts of the original data and degrade with each generation; the authors call this "model collapse" and conclude that data from genuine human activity becomes more valuable as machine-generated content spreads ([Shumailov et al., *AI models collapse when trained on recursively generated data*, Nature 631, 2024](https://doi.org/10.1038/s41586-024-07566-y)).

**Why this approach**
Material that no one has verified cannot serve as a reference: there is nothing to compare a result against. Human-verified material provides that reference. Without it, errors pass from one piece of work into the next unnoticed.

**What you gain**
Cleaner context, faster solutions, and results that are easier to verify, because they can be compared with material already known to work.

---

## Summary

| Principle | In one sentence |
|---|---|
| Proven parts | Build from what has already been proven. |
| Self-explaining interfaces | The interface is the instruction. |
| Two kinds of rules | Context guides; fixed rules verify. |
| Errors as guidance | A visible error is better than a silent guess. |
| Separate checks | The reviewer must not share the author's blind spots. |
| Scripts | Verify a procedure once, then reuse it. |
| Tree structure | Keep related things together, under consistent names. |
| Human-verified material | The foundation on which everything else is built. |
