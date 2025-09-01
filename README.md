This project is a RESTful API for an e-commerce platform built with Django REST Framework.
It supports:
User Registration & Authentication
Product & Category Management
Filtering & Searching
Cart & Order Management

Tech Stack
Python 3
Django & Django REST Framework
SQLite (default)
Postman (for testing)
Token Authentication


Authentication

Token-based authentication

Obtain token:
POST /api/auth/token/
Body:
{
  "username": "john1",
  "password": "mypassword123"
}
Authorization: Token your_generated_token

User registration
POST /api/auth/register/
Body:
{
  "username": "ayo2",
  "password": "mypassword123",
  "email": "ayo@example.com"
}

Endpoints
User
POST /api/auth/register/    – Register new user
POST /api/auth/login/       – Login and get token
POST /api/auth/token/       – Obtain token

Products & Categories
GET /api/products/ – List products
POST /api/products/ – Add product
GET /api/categories/ – List categories

Cart
GET /api/cart/ – View cart
POST /api/cart/ – Add to cart

{
  "product": 1,
  "quantity": 2
}

DELETE /api/cart/<id>/ – Remove item

Orders
GET /api/orders/ – View orders
POST /api/orders/ – Place order

Features Implemented

✔ User Authentication
✔ Product & Category CRUD
✔ Filtering & Search
✔ Cart Management
✔ Order Placement & Stock Deduction