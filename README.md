# 🛍️ E-commerce API (Django + DRF)

This is a RESTful API for an E-commerce platform built with **Django** and **Django REST Framework**.  
It supports user authentication, product management, category filtering, and token-based authentication.

---

## 🚀 Features
- User Registration & Login (Token Authentication)
- Create, Read, Update, Delete (CRUD) Products
- Category Management
- Search & Filter Products
- Pagination Support
- Secure Endpoints with Token Authentication

---

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework
- **Authentication:** Token Authentication
- **Database:** SQLite (default, can be replaced with PostgreSQL/MySQL)
- **Tools:** Postman for API testing

---

Get Token: POST /api/auth/login/ 
body 
{ 
"username": "john1", 
"password": "mypassword123" 
}
{
  "username": "ayo2",
  "password": "mypassword123",
  "email": "ayo@example.com"
}
Authorization: Token your_generated_token

🧪 API Endpoints
Method	Endpoint	Description
POST	/api/auth/register/	Register a new user
POST	/api/auth/login/	Login and get token
GET	/api/products/	List all products
POST	/api/products/	Create new product (auth)
GET	/api/products/{id}/	Get product details
PUT	/api/products/{id}/	Update product (auth)
DELETE	/api/products/{id}/	Delete product (auth)


POST http://127.0.0.1:8000/api/auth/register/
POST http://127.0.0.1:8000/api/auth/token/
GET http://127.0.0.1:8000/api/products/
http://127.0.0.1:8000/api/auth/login/
http://127.0.0.1:8000/api/auth/profile/

### ✅ Key Features Implemented:
- Created a custom permission `IsAdminOrReadOnly`.
- Applied permission to `ProductViewSet`:
  - **Read (GET)** → Allowed for everyone (authenticated users).
  - **Write (POST, PUT, DELETE)** → Only allowed for **admins**.

### ✅ Testing via Postman
1. Register/Login to get token.
2. Test with normal user:
   - GET `/api/products/` → ✅ Works.
   - POST `/api/products/` → ❌ Fails with **403 Forbidden**.
3. Test with admin:
   - Create admin user in Django Admin or shell.
   - Use admin token → ✅ POST works.
