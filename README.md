# GoREST API Automated Tests (pytest)

This repository contains an **automated API testing project** for the
**GoREST public REST API**, implemented using **pytest** and **requests**.

The project demonstrates real-world **QA Automation practices**,
including authentication, strict validation testing, negative scenarios,
and proper error handling.

---

## Tech Stack

- **Language:** Python 3.10+
- **Testing Framework:** pytest
- **HTTP Client:** requests
- **Authentication:** Bearer Token
- **Test Types:** functional, CRUD, negative, boundary, integration
- **Environment:** virtualenv (venv)
- **Version Control:** Git, GitHub

---

## API Under Test

- Base URL: `https://gorest.co.in/public/v2`
- Authentication: Bearer Token
- Main Resource: `/users`

---

## Project Structure

```text
gorest-api-testing/
├── tests/
│   ├── test_users.py
│   └── conftest.py
│
├── utils/
│   └── api_client.py
│
├── docs/
│   ├── test_plan.md
│   ├── requirements.md
│   ├── test_cases.md
│   └── test_summary.md
│
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Run Tests

### 1. Clone the repository
```bash
git clone https://github.com/your-username/gorest-api-testing.git
cd gorest-api-testing
```
### 2. Create and activate a virtual environment
macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set GoREST API token


This project requires a valid GoREST Bearer Token.
macOS / Linux
```bash
export GOREST_TOKEN=your_token_here
```
Windows (PowerShell)
```bash
setx GOREST_TOKEN your_token_here
```
Restart the terminal after setting the environment variable.

### 5. Run all tests
```bash
pytest -v
```

### 6. Run tests by markers

Run smoke tests:
```bash

pytest -m smoke
```


Run negative tests:
```bash
pytest -m negative
```

Run authorization tests:
```bash
pytest -m auth
```

Run smoke tests excluding negative scenarios:
```bash
pytest -m "smoke and not negative"
```
### 7. View available pytest markers
```bash
pytest --markers
```
