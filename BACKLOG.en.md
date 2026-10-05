# Backlog: Lab 2 (teamwork on GitHub)

You work in pairs: **A** and **B**. Every task is a separate issue, a separate branch and a separate pull request reviewed by your partner. The application code is not touched.

## Sprint 0: setup (together, 15 min)

- **T01.** A creates the repository from the template, adds B as a collaborator and protects `main`: only through a PR with 1 approval.
- **T02.** Labels `docs`, `conflict`, `decision`. Milestone `v0.2.0`. A GitHub Project with columns Todo / In progress / Done. Create issues for T03–T15, assign them, add a label and the milestone.

## Sprint 1: flow without conflicts (25 min)

| Task | Who | File | Done when |
|---|---|---|---|
| T03 | A | `docs/service.md` | No TODO left; all endpoints described. |
| T04 | B | `docs/runbook.md` | No TODO left; every step is an exact command. |
| T05 | A | `.github/CODEOWNERS` | Line `* @A @B` (with your GitHub usernames). Then turn on "Require review from Code Owners" in the rule for `main`. |
| T06 | B | `CONTRIBUTING.md` (new) | How we name branches, how we write commits, PR rules. Last line: `Branching strategy: TBD`. |

In at least one review use **Suggest changes**, and the author accepts it with **Commit suggestion**.

## Sprint 2: conflicts with merge (35 min)

| Task | Who | File | Done when |
|---|---|---|---|
| T07 | A | `docs/glossary.md` | Added Artifact, Container, Pipeline, Rollback, Tag, each in its alphabetical place. |
| T08 | B | `docs/glossary.md` | Added Branch, Commit, Merge, Release, Runner, each in its alphabetical place. |
| T09 | A | `docs/adr/0002-*.md` | Decision "Database for Lab 4" from `template.md`; a row in `docs/adr/index.md`; the page in `mkdocs.yml`. |
| T10 | B | `docs/adr/0002-*.md` | Decision "Where the service runs" from `template.md`; a row in `docs/adr/index.md`; the page in `mkdocs.yml`. |
| T11 | A and B | `docs/oncall.md` | Each signs up as on call for weeks 5 and 6. In the end every week 5–8 has an on-call person and a backup. |

The second PR in each pair of tasks will have a conflict. You resolve it **locally in the terminal** (`git fetch`, `git merge origin/main`). In T09/T10 you both took number 0002: the second one renames their file to 0003 (`git mv`) and fixes the links.

## Sprint 3: rebase, suggestions, revert (30 min)

| Task | Who | What |
|---|---|---|
| T12 | A and B | In `CONTRIBUTING.md` each replaces the line `Branching strategy: TBD` with their own proposal (GitHub Flow, GitFlow, trunk-based) and an argument. The conflict is resolved by the person who did **not** resolve the glossary conflict, with `git rebase origin/main` and `git push --force-with-lease`. The final line holds what you agreed on. |
| T13 | A | PR "Use port 9000 in the runbook": change the port in `docs/runbook.md` to 9000. B approves it and it is merged. |
| T14 | B | The app runs on 8000, so T13 was a mistake. Undo it with the **Revert** button on the merged PR and merge the reverting PR. |

## Sprint 4: release (10 min)

- **T15.** In `CHANGELOG.md` "Unreleased" becomes "0.2.0" (through a PR). Close the `v0.2.0` milestone. A release with tag `v0.2.0` and **Generate release notes**.

## Bonus (if there is time)

- **T16.** A draft PR that becomes ready for review. A commit with two authors (`Co-authored-by:`).
- **T17.** Local preview of the site: `pip install -r requirements-docs.txt`, then `mkdocs serve`.
