# Conversational AI BackEnd API – Usage Guide

This guide explains how to use the deployed API through **Swagger UI**, how to authorize requests, and interact with endpoints.

> The full API documentation is also available in the [`API_Documentation`](./API_Documentation) folder in this repository. Click the link to view all API docs.

---

## 1. Accessing Swagger UI

Open your browser and go to the deployed Swagger UI link:
```
    
```

- You will see an interactive interface listing all available endpoints.
- You can **expand each endpoint**, see its parameters, try requests, and view responses.

---

## 2. Authorizing Requests (Login)

Some endpoints require authentication using **OAuth2 password flow (Bearer token)**.

### Steps to authorize:

1. Click the **Authorize** button at the top-right corner of Swagger UI.  
2. In the modal, enter your username and login
3. Click **Authorize** and close the modal.  
4. All authorized endpoints will now include your token automatically.
