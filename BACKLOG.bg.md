# Backlog: Упражнение 2 (работа в екип в GitHub)

Работите по двойки: **А** и **Б**. Всяка задача е отделен Issue, отделен клон и отделен Pull Request с ревю от партньора. Кодът на приложението не се пипа.

## Спринт 0: подготовка (заедно, 15 мин)

- **T01.** А създава хранилището от шаблона, добавя Б като collaborator и защитава `main`: само през PR с 1 одобрение.
- **T02.** Labels `docs`, `conflict`, `decision`. Milestone `v0.2.0`. GitHub Project с колони Todo / In progress / Done. Създайте Issue за T03–T15, разпределете ги, сложете label и milestone.

## Спринт 1: поток без конфликти (25 мин)

| Задача | Кой | Файл | Готово, когато |
|---|---|---|---|
| T03 | А | `docs/service.md` | Няма TODO; описани са всички адреси. |
| T04 | Б | `docs/runbook.md` | Няма TODO; всяка стъпка е точна команда. |
| T05 | А | `.github/CODEOWNERS` | Ред `* @А @Б` (с вашите GitHub имена). После в правилото за `main` включете „Require review from Code Owners“. |
| T06 | Б | `CONTRIBUTING.md` (нов) | Как именуваме клони, как пишем комити, правила за PR. Последен ред: `Branching strategy: TBD`. |

Поне в едно ревю използвайте **Suggest changes**, а авторът го приема с **Commit suggestion**.

## Спринт 2: конфликти със сливане (35 мин)

| Задача | Кой | Файл | Готово, когато |
|---|---|---|---|
| T07 | А | `docs/glossary.md` | Добавени Artifact, Container, Pipeline, Rollback, Tag, всеки на мястото си по азбучен ред. |
| T08 | Б | `docs/glossary.md` | Добавени Branch, Commit, Merge, Release, Runner, всеки на мястото си по азбучен ред. |
| T09 | А | `docs/adr/0002-*.md` | Решение „База данни за Упражнение 4“ от `template.md`; ред в `docs/adr/index.md`; страницата в `mkdocs.yml`. |
| T10 | Б | `docs/adr/0002-*.md` | Решение „Къде работи услугата“ от `template.md`; ред в `docs/adr/index.md`; страницата в `mkdocs.yml`. |
| T11 | А и Б | `docs/oncall.md` | Всеки се записва като дежурен за седмици 5 и 6. Накрая всяка седмица 5–8 има дежурен и резерва. |

Вторият PR във всяка двойка задачи ще има конфликт. Решавате го **локално в терминала** (`git fetch`, `git merge origin/main`). При T09/T10 двамата сте взели номер 0002: вторият преименува своя файл на 0003 (`git mv`) и оправя линковете.

## Спринт 3: rebase, предложения, отмяна (30 мин)

| Задача | Кой | Какво |
|---|---|---|
| T12 | А и Б | В `CONTRIBUTING.md` всеки заменя реда `Branching strategy: TBD` със своето предложение (GitHub Flow, GitFlow, trunk-based) и аргумент. Конфликта решава този, който **не** е решавал конфликта в речника, с `git rebase origin/main` и `git push --force-with-lease`. В крайния ред стои договореното. |
| T13 | А | PR „Use port 9000 in the runbook“: смяна на порта в `docs/runbook.md` на 9000. Б го одобрява и се слива. |
| T14 | Б | Приложението работи на 8000, значи T13 е грешка. Отменете я с бутона **Revert** на слетия PR и слейте отменящия PR. |

## Спринт 4: издание (10 мин)

- **T15.** В `CHANGELOG.md` „Unreleased“ става „0.2.0“ (през PR). Затворете milestone `v0.2.0`. Release с таг `v0.2.0` и **Generate release notes**.

## Бонус (ако остане време)

- **T16.** Draft PR, който става Ready for review. Комит с два автора (`Co-authored-by:`).
- **T17.** Локален преглед на сайта: `pip install -r requirements-docs.txt`, после `mkdocs serve`.
