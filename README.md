# K1CORE - Django + FastAPI Application  

## 📌 Project Overview  
This project integrates **Django** and **FastAPI** to fetch and store the latest blocks for **BTC** (from CoinMarketCap) and **ETH** (from BlockChair). It uses **PostgreSQL** as the database, **Redis** as the message broker, and **Celery** for periodic tasks.  

## 🚀 Features  
✅ Django Admin Panel  
✅ FastAPI for high-performance API endpoints  
✅ Fetch latest BTC and ETH blocks every minute using Celery  
✅ Store block data in PostgreSQL  
✅ Authentication (User Signup & Login)  
✅ API endpoints for retrieving block data with filtering and pagination  
✅ Dockerized setup for easy deployment  

---

## 🔧 Installation & Setup  

### **Prerequisites**  
- Install **Docker** & **Docker Compose**  
- Clone the repository
- Starting the Application:
  ```bash
  docker-compose up --build  

This will:
✔️ Build and start the Django + FastAPI application
✔️ Set up the PostgreSQL database
✔️ Start Redis as the message broker
✔️ Start Celery worker and beat scheduler


### **API Endpoints (FastAPI)**

Once the application is running, visit the API docs:
📜 Swagger UI: http://127.0.0.1:8000/docs
📜 ReDoc: http://127.0.0.1:8000/redoc

### **📌 Usage Guide**

Access Django Admin Panel
Once the application is running, access the Django Admin panel at:
👉 http://127.0.0.1:8000/django/admin/

Create an Admin User

If you need to create a superuser for the Django admin panel, run:
```bash
  docker exec -it django_fastapi python manage.py createsuperuser


