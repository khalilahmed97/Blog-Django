
# 📝 Django Blogging API with JWT Authentication

Welcome to Django-powered Blogging API, designed for building robust and secure blog platforms. This repository includes essential APIs for user registration, login, creating new blog posts, and commenting. The implementation is done utilizing Django REST Framework, emphasizes security through JWT (JSON Web Token), and utilizes PostgreSQL for enhanced performance.

## 🚀 Key Features:

#### User Registration by Email: 
Account creation with email validation and duplicate username/email checks.

#### Login via Email and Password.

#### JWT token generation upon successful login.

#### Creating a New Blog Post:

#### Post creation with required authentication using JWT.

#### Comment on blog posts.

## 🔐 API Endpoints used in the project:

### Authentication and Token Generation API Endpoints:

#### http://localhost:3000/api/token/generate
#### http://localhost:3000/api/token/verify
#### http://localhost:3000/api/token/refresh

#### http://localhost:3000/api/login/
#### http://localhost:3000/api/register/
#### http://localhost:3000/api/logout/

### Blog API Endpoints:

### GET REQUEST:

#### http://localhost:3000/blog/category/new/
#### http://localhost:3000/blog/post/new/
#### http://localhost:3000/blog/post/comment/

### POST REQUEST:

#### http://localhost:3000/blog/post/all/
#### http://localhost:3000/blog/category/all/
#### http://localhost:3000/blog/post/comment/all/


## JWT Authentication: Secures sensitive operations and endpoints.
Password Hashing: User passwords are securely hashed before storage.

## 🗺️ Database:

### PostgreSQL Database:

PostgreSQL is employed for storing data, improving both scalability and performance within an online platform Railway.


## References:

### Railway Website:

https://railway.app/

### Simple-JWT:

https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

### Django REST Framework:

https://www.django-rest-framework.org/
