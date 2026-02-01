# GoREST API — Test Plan

## 1. Introduction

This document describes the test plan for the **GoREST public REST API**.
The purpose of testing is to verify correctness, validation, error handling,
and stability of the API under normal and negative scenarios.

The API behaves as a real backend service with authentication,
strict validation, and proper HTTP error responses.

---

## 2. Scope of Testing

### In Scope
- CRUD operations for core resources
- Authentication and authorization
- Input validation and error handling
- HTTP status codes and response structure
- Negative and boundary testing
- Integration testing using chained requests

### Out of Scope
- UI testing
- Performance and load testing
- Security / penetration testing
- Database-level testing

---

## 3. API Resources Under Test

| Resource | Endpoints |
|--------|----------|
| Users | `/users` |
| Authentication | Bearer Token |
| Posts (optional) | `/posts` |
| Comments (optional) | `/comments` |

---

## 4. Test Types

- **Functional Testing** — validation of API functionality
- **CRUD Testing** — Create, Read, Update, Delete operations
- **Negative Testing** — invalid input, missing fields, invalid IDs
- **Boundary Testing** — edge cases for field values
- **Integration Testing** — multi-step API flows

---

## 5. Test Scenarios

---

## 5.1 Users API

### GET /users

**Positive Scenarios**
- Verify response status code is `200`
- Verify response body is a list
- Verify user object contains:
  - `id`
  - `name`
  - `email`
  - `gender`
  - `status`

---

### GET /users/{id}

**Positive Scenarios**
- Existing user ID → `200`
- Correct user data returned

**Negative Scenarios**
- Non-existing user ID → `404`
- Invalid ID format → `404`

---

### POST /users

**Positive Scenarios**
- Create user with valid payload
- Verify response status code `201`
- Verify returned user ID
- Verify returned fields match request payload

**Negative Scenarios**
- Empty payload → `422`
- Missing required fields → `422`
- Invalid email format → `422`
- Duplicate email → `422`
- Missing authorization token → `401`

---

### PUT /users/{id}

**Positive Scenarios**
- Update existing user
- Verify updated fields in response

**Negative Scenarios**
- Update non-existing user → `404`
- Invalid payload → `422`
- Missing authorization token → `401`

---

### DELETE /users/{id}

**Positive Scenarios**
- Delete existing user → `204`

**Negative Scenarios**
- Delete non-existing user → `404`
- Missing authorization token → `401`

---

## 6. Data Validation

- Validate required fields presence
- Validate field data types
- Validate field constraints:
  - email format
  - gender values
  - status values

---

## 7. HTTP Validation

- Verify correct HTTP methods
- Verify correct status codes:
  - `200 OK`
  - `201 Created`
  - `204 No Content`
  - `401 Unauthorized`
  - `404 Not Found`
  - `422 Unprocessable Entity`

---

## 8. Test Environment

| Parameter | Value |
|---------|------|
| API Base URL | https://gorest.co.in/public/v2 |
| Environment | Public API |
| Authentication | Bearer Token |
| Test Tool | pytest |

---

## 9. Entry and Exit Criteria

### Entry Criteria
- API is available
- Authentication token is valid
- Test environment is stable

### Exit Criteria
- All planned test cases executed
- Critical defects identified and documented
- Test results summarized

---

## 10. Deliverables

- Automated API test suite (pytest)
- Test Plan document
- Test execution results
- GitHub repository with source code
