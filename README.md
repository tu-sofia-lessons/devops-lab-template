# Notes API — учебно приложение за курса по DevOps

**Български** · [English](#notes-api--devops-course-starter-app)

Малко приложение за бележки, написано на Python с FastAPI. То е отправната точка за всички упражнения в курса: в него ще добавяте контейнери, база данни, автоматични проверки, внедряване и т.н. Самото приложение нарочно е просто — целта на курса е всичко около него.

Данните засега се пазят в паметта и се губят при рестарт. База данни ще добавим в упражнение 4.

## Какво може приложението

| Метод | Адрес | Описание |
|-------|-------|----------|
| GET | `/health` | Проверка дали приложението работи: `{"status": "ok"}` |
| GET | `/version` | Версията от променливата на средата `APP_VERSION` (по подразбиране `0.1.0`) |
| GET | `/notes` | Списък с всички бележки |
| POST | `/notes` | Създава бележка. `title` е задължително (от 1 до 100 знака), `body` не е |
| GET | `/notes/{id}` | Една бележка; 404, ако не съществува |

Пример за създаване на бележка:

```bash
curl -X POST http://127.0.0.1:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "Първа бележка", "body": "Здравей"}'
```

## Структура

```
app/
  main.py         # адресите на приложението
  models.py       # описание на данните (Pydantic)
  repository.py   # съхранение на бележките (засега в паметта)
tests/            # тестове с pytest
```

## Локално стартиране

Нужен е Python 3.12.

```bash
python3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

uvicorn app.main:app --reload
```

Приложението е на http://127.0.0.1:8000, а автоматично генерираната документация — на http://127.0.0.1:8000/docs.

Тестове и проверка на стила на кода:

```bash
pytest
ruff check .
```

`requirements.txt` съдържа само нужното за работа на приложението, а `requirements-dev.txt` добавя инструментите за тестове и проверка.

## Задачи за екипа

Всяка задача е отделна, малка и независима от останалите. Разпределете ги в екипа (по една или две на човек) и за всяка:

1. Създайте задача (issue) в GitHub с описанието по-долу.
2. Направете нов клон от `main`, например `feature/delete-note`.
3. Реализирайте промяната **и добавете поне един тест** за нея.
4. Уверете се, че `pytest` и `ruff check .` минават.
5. Добавете ред във `CHANGELOG.md` под „Unreleased“, който описва промяната.
6. Отворете заявка за сливане (pull request), свържете я със задачата и помолете съотборник да я прегледа.

### 1. Изтриване на бележка

`DELETE /notes/{id}` изтрива бележката и връща код 204 без съдържание. Ако бележката не съществува — 404. След изтриване `GET /notes/{id}` връща 404.

### 2. Редактиране на бележка

`PUT /notes/{id}` заменя заглавието и текста на съществуваща бележка и връща обновената бележка. Важат същите правила за `title`, както при създаване. Ако бележката не съществува — 404.

### 3. Търсене по заглавие

`GET /notes?q=текст` връща само бележките, чието заглавие съдържа търсения текст, без значение от малки и главни букви. Без `q` поведението остава както досега.

### 4. Брой бележки

`GET /notes/count` връща `{"count": N}` — броя на бележките. Подсказка: внимавайте за реда, в който са описани адресите в `main.py`.

### 5. Време на създаване

Всяка бележка получава поле `created_at` — момента на създаване в UTC, във формат ISO 8601 (например `2026-10-05T12:00:00Z`). Полето се попълва от сървъра, а не от клиента.

### 6. Почистване на заглавието

Интервалите в началото и края на `title` се премахват преди запис. Заглавие, което съдържа само интервали, се отхвърля с код 422, както празното.

---

# Notes API — DevOps course starter app

[Български](#notes-api--учебно-приложение-за-курса-по-devops) · **English**

A small notes application written in Python with FastAPI. It is the starting point for every lab in the course: you will add containers, a database, automated checks, deployment and more around it. The app itself is deliberately simple — the course is about everything around it.

Data is kept in memory for now and is lost on restart. A database comes in Lab 4.

## What the app does

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Liveness check: `{"status": "ok"}` |
| GET | `/version` | Version from the `APP_VERSION` environment variable (default `0.1.0`) |
| GET | `/notes` | List all notes |
| POST | `/notes` | Create a note. `title` is required (1 to 100 characters), `body` is optional |
| GET | `/notes/{id}` | A single note; 404 if it does not exist |

Example of creating a note:

```bash
curl -X POST http://127.0.0.1:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "First note", "body": "Hello"}'
```

## Layout

```
app/
  main.py         # the app's endpoints
  models.py       # data shapes (Pydantic)
  repository.py   # note storage (in memory for now)
tests/            # pytest tests
```

## Running locally

Python 3.12 is required.

```bash
python3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

uvicorn app.main:app --reload
```

The app runs at http://127.0.0.1:8000 and the generated API docs are at http://127.0.0.1:8000/docs.

Tests and lint:

```bash
pytest
ruff check .
```

`requirements.txt` holds only what the app needs to run; `requirements-dev.txt` adds the test and lint tools.

## Team tasks

Each task is separate, small and independent of the others. Split them within the team (one or two per person) and for each one:

1. Create a GitHub issue with the description below.
2. Create a new branch from `main`, for example `feature/delete-note`.
3. Implement the change **and add at least one test** for it.
4. Make sure `pytest` and `ruff check .` pass.
5. Add a line to `CHANGELOG.md` under "Unreleased" describing the change.
6. Open a pull request, link it to the issue and ask a teammate to review it.

### 1. Delete a note

`DELETE /notes/{id}` deletes the note and returns 204 with no content. If the note does not exist — 404. After deletion, `GET /notes/{id}` returns 404.

### 2. Edit a note

`PUT /notes/{id}` replaces the title and body of an existing note and returns the updated note. The same `title` rules apply as on creation. If the note does not exist — 404.

### 3. Search by title

`GET /notes?q=text` returns only the notes whose title contains the search text, case-insensitively. Without `q` the behaviour stays as before.

### 4. Note count

`GET /notes/count` returns `{"count": N}` — the number of notes. Hint: pay attention to the order in which the routes are declared in `main.py`.

### 5. Creation time

Every note gets a `created_at` field — the moment of creation in UTC, in ISO 8601 format (for example `2026-10-05T12:00:00Z`). The server sets it, not the client.

### 6. Trim the title

Leading and trailing whitespace is removed from `title` before saving. A title that contains only whitespace is rejected with 422, just like an empty one.
