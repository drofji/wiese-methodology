# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
History before this file was created lives in the git log.

## [Unreleased]

### Added
- "The Manifesto & Challenges" page: why the methodology exists, the three common fears about AI (data leaks, wrong work, hallucinations) and how the methodology answers each, who it is for, and the plain-language principle.
- "Docs check" CI workflow on pushes and pull requests to `main`: validates `gitbook-docs.yaml` against GitBook's published schema and import rules, and fails when `SUMMARY.md` links a missing file or lists a file twice. Run it locally with `python .github/scripts/check_gitbook.py`.

### Fixed
- The author's GitHub link on the "Contributors & Attribution" page now points to the real account (@drofji).
- GitBook site sync: `gitbook-docs.yaml` now follows GitBook's site configuration schema, so the documentation site can publish from the repository instead of failing every sync with "Failed to parse site configuration".
- The "Prompt Templates" entry in the table of contents now points to an existing page (the file name had a typo).
- The table of contents no longer links the non-existent `CONTRIBUTORS.md`; contributors and attribution live on a single page.
