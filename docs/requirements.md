# GoREST API — Test Requirements (Users)

## 1. General Requirements

REQ-001  
The API shall require a valid Bearer Token for all write operations.

REQ-002  
The API shall return appropriate HTTP status codes according to the request result.

REQ-003  
The API shall validate request payloads for required fields and data formats.

---

## 2. GET /users

REQ-010  
The API shall return a list of users.

REQ-011  
The API shall return HTTP 200 for a valid GET request.

REQ-012  
Each user object shall contain:
- id
- name
- email
- gender
- status

---

## 3. GET /users/{id}

REQ-020  
The API shall return a user for an existing user ID.

REQ-021  
The API shall return HTTP 404 for a non-existing user ID.

---

## 4. POST /users

REQ-030  
The API shall create a new user with valid input data.

REQ-031  
The API shall return HTTP 201 when a user is created successfully.

REQ-032  
The API shall reject empty payloads.

REQ-033  
The API shall reject payloads with missing required fields.

REQ-034  
The API shall reject payloads with invalid email format.

REQ-035  
The API shall return HTTP 422 for validation errors.

REQ-036  
The API shall return HTTP 401 when authorization token is missing or invalid.

---

## 5. PUT /users/{id}

REQ-040  
The API shall update an existing user.

REQ-041  
The API shall return HTTP 404 for a non-existing user ID.

REQ-042  
The API shall validate update payload fields.

---

## 6. DELETE /users/{id}

REQ-050  
The API shall delete an existing user.

REQ-051  
The API shall return HTTP 204 after successful deletion.

REQ-052  
The API shall return HTTP 404 for a non-existing user ID.

REQ-053  
The API shall return HTTP 401 if authorization is missing.
