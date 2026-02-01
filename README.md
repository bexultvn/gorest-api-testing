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
│   └── test_cases.md
│
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore

