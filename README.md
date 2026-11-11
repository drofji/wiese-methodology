# Wiese Methodology

> **A practical way to work with AI safely and with confidence.**
> *Small steps, checks outside the model, and real-world software development experience.*

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC_BY--NC--ND_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Documentation](https://img.shields.io/badge/Docs-GitBook-blue)](https://alexander-wiese.gitbook.io/wiese-methodology/)

---

## 📌 Overview

Maybe you've tried AI and got burned: it leaked something it shouldn't have seen, did something you never asked for, or made up a fact with a perfectly straight face. Or maybe you never tried, because you expected exactly that. Either way, this is for you.

The **Wiese Methodology** is a way of working with AI that makes those risks visible and keeps them under control. It doesn't promise a model that never makes mistakes, because no method can promise that. What it does is make sure far fewer of those mistakes ever reach your result. It works with whichever AI assistant you use, and while most examples come from software development, the thinking behind them fits any kind of work.

---

## 🎯 Key Principles

The work runs as a **pipeline**: you cut it into small tasks, and each one takes the same short path from context through strict generation and automated validation to integration, so every task gets only what it needs and the AI produces only what was asked for. Then come the **quality gates**: every step ends with a checklist and with automatic checks that live outside the model, so nothing reaches the main project unchecked, and a person looks where a mistake would cost the most. And all of it stays **pragmatic**, rooted in real freelancing and production work rather than in theory, built from patterns that held up in the field.

---

## 🚀 Quick Start

Start with the [Manifesto](docs/01-introduction/manifesto.md) to see why unstructured prompting causes trouble and how the methodology answers each fear. Then read [Writing a Task for AI](docs/05-toolkit/prompt-templates.md) and put rule files and system prompts into your own AI assistant. Before you rely on a result, walk it through the [quality gates](docs/03-quality-gates/automated-gates.md) and the [human review](docs/03-quality-gates/human-checklist.md).

📖 **[Read the full book on GitBook](https://alexander-wiese.gitbook.io/wiese-methodology/)**

---

## 🤝 Contributing

Feedback and ideas are very welcome. Have a look at [`CONTRIBUTING.md`](CONTRIBUTING.md) to see how you can share them or propose an improvement through a pull request.

---

## 📄 License & Attribution

Author: **Alexander Wiese**
Copyright © 2026 Alexander Wiese.

This methodology is licensed under **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**. You're free to share, copy and pass the material on in any medium or format, as long as you give credit to **Alexander Wiese** with a link to this repository, don't use it for commercial purposes or resale, and don't distribute a changed or remixed version without permission.

For the details, see [`LICENSE.md`](LICENSE.md).
