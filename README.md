# Notes API: учебно приложение за курса по DevOps

**Български** · [English](#notes-api--devops-course-starter-app)

Малко приложение за бележки, написано на Python с FastAPI. То е отправната точка за всички упражнения в курса: в него ще добавяте контейнери, база данни, автоматични проверки, внедряване и т.н. Самото приложение нарочно е просто: целта на курса е всичко около него.

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
docs/             # документация на услугата (Упражнение 2)
mkdocs.yml        # сайт от документацията: `pip install -r requirements-docs.txt`, после `mkdocs serve`
```

## Локално стартиране

Нужен е Python 3.12.

```bash
python3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

uvicorn app.main:app --reload
```

Приложението е на http://127.0.0.1:8000, а автоматично генерираната документация е на http://127.0.0.1:8000/docs.

Тестове и проверка на стила на кода:

```bash
pytest
ruff check .
```

`requirements.txt` съдържа само нужното за работа на приложението, а `requirements-dev.txt` добавя инструментите за тестове и проверка.

## Упражнение 2: работа в екип

В Упражнение 2 кодът не се пипа. Работи се върху документацията в папка `docs/`: описание на услугата, runbook, решения и дежурства. Стъпките са в страницата на упражнението в Moodle.

---

# Notes API: DevOps course starter app

[Български](#notes-api--учебно-приложение-за-курса-по-devops) · **English**

A small notes application written in Python with FastAPI. It is the starting point for every lab in the course: you will add containers, a database, automated checks, deployment and more around it. The app itself is deliberately simple: the course is about everything around it.

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
docs/             # service documentation (Lab 2)
mkdocs.yml        # a site from the docs: `pip install -r requirements-docs.txt`, then `mkdocs serve`
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

## Lab 2: teamwork

In Lab 2 the code is not touched. You work on the documentation in the `docs/` folder: the service description, the runbook, decisions and on-call. The steps are on the lab page in Moodle.
