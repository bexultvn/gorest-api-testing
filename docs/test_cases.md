# GoREST API — Test Cases (Users)

## TC-001 — Get users list
**Endpoint:** GET /users  
**Precondition:** Valid Bearer Token  
**Steps:**
1. Send GET request to /users  
**Expected Result:**
- HTTP 200
- Response body is a list
- Each user contains id, name, email, gender, status

---

## TC-002 — Get user by valid ID
**Endpoint:** GET /users/{id}  
**Steps:**
1. Send GET request with existing user ID  
**Expected Result:**
- HTTP 200
- Returned user ID matches request

---

## TC-003 — Get user by non-existing ID
**Endpoint:** GET /users/{id}  
**Steps:**
1. Send GET request with non-existing ID  
**Expected Result:**
- HTTP 404

---

## TC-004 — Create user with valid payload
**Endpoint:** POST /users  
**Precondition:** Valid Bearer Token  
**Steps:**
1. Send POST request with valid user data  
**Expected Result:**
- HTTP 201
- User ID is returned
- Returned fields match request

---

## TC-005 — Create user with empty payload
**Endpoint:** POST /users  
**Steps:**
1. Send POST request with empty body  
**Expected Result:**
- HTTP 422

---

## TC-006 — Create user with invalid email
**Endpoint:** POST /users  
**Steps:**
1. Send POST request with invalid email format  
**Expected Result:**
- HTTP 422
- Error message references email field

---

## TC-007 — Create user without authorization
**Endpoint:** POST /users  
**Steps:**
1. Send POST request without Bearer Token  
**Expected Result:**
- HTTP 401

---

## TC-008 — Update existing user
**Endpoint:** PUT /users/{id}  
**Steps:**
1. Send PUT request with valid payload  
**Expected Result:**
- HTTP 200
- Updated fields are returned

---

## TC-009 — Update non-existing user
**Endpoint:** PUT /users/{id}  
**Steps:**
1. Send PUT request with non-existing ID  
**Expected Result:**
- HTTP 404

---

## TC-010 — Delete existing user
**Endpoint:** DELETE /users/{id}  
**Steps:**
1. Send DELETE request with existing ID  
**Expected Result:**
- HTTP 204

---

## TC-011 — Delete non-existing user
**Endpoint:** DELETE /users/{id}  
**Steps:**
1. Send DELETE request with non-existing ID  
**Expected Result:**
- HTTP 404
