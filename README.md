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