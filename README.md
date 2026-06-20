
# 🚀 FastAPI JWT Blog API

### A secure, scalable, and production-ready Blog API built with FastAPI, featuring JWT authentication, PostgreSQL integration, and full CRUD functionality for users and posts.

---

## 🚀 Live Demo

👉 **Live API:** [FastAPI JWT Blog API](https://fastapi-jwt-blog-api.onrender.com?utm_source=chatgpt.com)

📄 **Swagger UI Documentation:** [API Docs](https://fastapi-jwt-blog-api.onrender.com/docs?utm_source=chatgpt.com)

> ⚠️ Note: Hosted on Render free tier — initial request may take a few seconds due to cold start.

---

## 🛠 Technologies Used

* **Backend Framework:** FastAPI
* **Database:** PostgreSQL (Neon )
* **ORM:** SQLAlchemy
* **Authentication:** JWT (python-jose)
* **Password Hashing:** Passlib (bcrypt)
* **Server:** Uvicorn
* **Validation:** Pydantic
* **Environment Management:** Python-dotenv

---

## 💡 Features

* User registration and login system
* JWT-based authentication system
* Secure password hashing using bcrypt
* Create, read, update, and delete blog posts
* Protected routes for authenticated users
* User-specific post management
* Ownership validation for update and delete operations
* RESTful API architecture
* Interactive Swagger UI documentation

---

## 📂 Project Structure

```
fastapi-jwt-blog-api/
├── main.py 📝 FastAPI routes, authentication & business logic
├── models.py 📦 Database models (User, Post)
├── database.py 🔗 Database connection & session setup
├── requirements.txt 📄 Project dependencies
├── .env 🔐 Environment variables (not included in repo)
└── .gitignore 🚫 Ignored files
```

---

## ⚡ Installation & Local Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/PavanSurisetti/fastapi-jwt-blog-api
```

---

### 2️⃣ Navigate into the project

```bash
cd fastapi-jwt-blog-api
```

---

### 3️⃣ Create virtual environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Configure environment variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=your_postgresql_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
```

---

### 6️⃣ Run the application

```bash
uvicorn main:app --reload
```

---

### 7️⃣ Open in browser

```
http://127.0.0.1:8000/docs
```

---

## 🔗 API Endpoints

### Authentication

| Method | Endpoint    | Description           |
| ------ | ----------- | --------------------- |
| POST   | `/register` | Register new user     |
| POST   | `/login`    | Login & get JWT token |

---

### Posts

| Method | Endpoint         | Description                 |
| ------ | ---------------- | --------------------------- |
| POST   | `/posts`         | Create post (Auth required) |
| GET    | `/posts`         | Get all posts (Public)      |
| GET    | `/posts/private` | Get user-specific posts     |
| GET    | `/post/{id}`     | Get post by ID              |
| PUT    | `/posts/{id}`    | Update post (Auth required) |
| DELETE | `/posts/{id}`    | Delete post (Auth required) |

---

## 🔐 Authentication Flow

1. User registers via `/register`
2. User logs in via `/login`
3. Server returns JWT access token
4. Token is added in Authorization header
5. Protected routes validate token before access

---

## 🧠 How It Works

* FastAPI handles API requests
* SQLAlchemy manages database operations
* PostgreSQL stores user and post data
* Pydantic validates incoming request data
* JWT secures authentication system
* Passlib bcrypt hashes passwords
* Render hosts the deployed backend

---

## 🚀 Deployment

* **Platform:** Render
* **Live API:** [FastAPI JWT Blog API](https://fastapi-jwt-blog-api.onrender.com?utm_source=chatgpt.com)
* **Database:** PostgreSQL ( Neon)
* **Environment Variables:** Managed via Render dashboard

---

## 🚀 Future Improvements

* JWT refresh token system
* Role-based access control (Admin/User)
* Pagination for posts
* Like & comment system
* Docker containerization
* Rate limiting & security enhancements

---

## 📫 Contact

* GitHub: [PavanSurisetti](https://github.com/PavanSurisetti)
* LinkedIn: [Pavan Surisetti](https://www.linkedin.com/in/pavan-surisetti-b3281228b/)

---

## 📄 License

This project is licensed under the **MIT License**.
