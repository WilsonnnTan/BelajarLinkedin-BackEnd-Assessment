# Technical Test - Conversational AI Application

This document provides an overview and API documentation for this BackEnd built for the technical assessment.

---

## API Documentation

The API is the core of this application, It's designed to be simple and RESTful.

### 1. Register

Register new user.

* **Endpoint:** `/auth/register`
* **Method:** `POST`
* **Request Body:** 
    ```json
    {
        "username": "string",
        "email": "string@gmail.com",
        "password": "string"
    }
    ```
* **Response 201:**
    ```json
    {
        "msg": "User registered successfully"
    }
    ```
---

### 2. Login

Login user and obtain an access token.
This endpoint follows the OAuth2 Password Flow, so in Swagger UI you can click “Authorize” and paste the token, or it will be auto-handled after login.

* **Endpoint:** `/auth/login`
* **Method:** `POST`
* **Request Body:** 
    ```URL-encoded
    username=johndoe&password=securepassword
    ```
* **Response 200:**
    ```json
    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMDI0MjVhYy1lNTRhLTQ0ZmItYjJiMi02NWE2ZTkxMTljMTMiLCJ1c2VybmFtZSI6IndpbHNvbjEyMyIsImV4cCI6MTc1NTY4Mzk4M30.Y0Zz0bOeWHwTm-UAgO6n6IbtrAx0d5tzXEpNnJNR2bw",
        "token_type": "bearer"
    }
    ```
---

### 3. Get All Classes

Retrieves all available classes.

* **Endpoint:** `/class`
* **Method:** `GET`
* **Response 200:**
    ```json
    {
        "data": [
            {
            "id": "c66e0170-7580-4b6f-88b0-3df917d2515a",
            "detail": "testing",
            "name": "kelas1"
            },
            {
            "id": "4b1e66ea-2bdd-4a2e-8c25-3cd3fb33732f",
            "detail": "tes ke-2",
            "name": "kelas2"
            }
        ],
        "message": "Classes retrieved successfully"
    }
    ```

---

### 4. Get Class by ID

Retrieves class according to ID.

* **Endpoint:** `/class/{class_id}`
* **Method:** `GET`
* **Path Parameter:**
  - `class_id` (UUID): The unique identifier of the class
* **Response 200:**
    ```json
    {
        "data": {
            "id": "4b1e66ea-2bdd-4a2e-8c25-3cd3fb33732f",
            "detail": "tes ke-2",
            "name": "kelas2"
        },
        "message": "Classes retrieved successfully"
    }
    ```

---

### 5. Add Classes

Add new class.

* **Endpoint:** `/class`
* **Method:** `POST`
* **Request:** 
    ```json
    {
        "name": "kelas2",
        "detail": "tes ke-2"
    }
    ```
* **Response 201:**
    ```json
    {
        "message": "Class added successfully"
    }
    ```

---

### 6. Edit Classes

Edit class.

* **Endpoint:** `/class/{class_id}`
* **Method:** `PUT`
* **Path Parameter:**
  - `class_id` (UUID): The unique identifier of the class
* **Request:** 
    ```json
    {
        "name": "kelasubah2",
        "detail": "kelas diubah"
    }
    ```
* **Response 204 No Content:**
    This endpoint returns no response body when successful, only headers:
    ```
        content-type: application/json 
        date: Wed,20 Aug 2025 09:55:25 GMT 
        server: uvicorn 
    ```

---

### 7. Delete Classes

Delete class (ON CASCADE).

* **Endpoint:** `/class/{class_id}`
* **Method:** `DELETE`
* **Path Parameter:**
  - `class_id` (UUID): The unique identifier of the class
* **Response 204 No Content:**
    This endpoint returns no response body when successful, only headers:
    ```
        content-type: application/json 
        date: Wed,20 Aug 2025 10:14:11 GMT 
        server: uvicorn 
    ```