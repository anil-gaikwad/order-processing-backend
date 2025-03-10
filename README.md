# 📦 Order Processing API  

## 📝 Assignment: Backend System for Order Processing  

### 🎯 **Objective**  
This project is a backend system designed to manage and process orders in an e-commerce platform. It demonstrates proficiency in building modular, maintainable, and scalable systems, covering database design, queuing, distributed system fundamentals, and metrics reporting.  

---

## 🏗️ **Problem Statement**  

The system should:  

### **1️⃣ Core Functionality**  
✅ Provide a RESTful API to accept orders with fields such as:  
- `user_id`  
- `order_id`  
- `item_ids`  
- `total_amount`  

✅ Simulate **asynchronous order processing** using an **in-memory queue** (`queue.Queue`).  

✅ Provide an API to check the status of orders:  
- `Pending`  
- `Processing`  
- `Completed`  

✅ Implement an API to fetch key metrics, including:  
- Total number of orders processed.  
- Average processing time for orders.  
- Count of orders in each status:  
  - `Pending`  
  - `Processing`  
  - `Completed`  

### **2️⃣ Constraints**  
✅ **Database**: SQLite / PostgreSQL / MySQL  
✅ **Queue**: In-memory queue for asynchronous processing  
✅ **Scalability**: Simulate handling of **1,000 concurrent orders**  

---

## 📁 **Project Structure**  
```
order-processing-api/
│── main.py              # FastAPI application entry point
│── database.py          # Database connection and initialization
│── models.py            # SQLAlchemy ORM models
│── schema.py            # Pydantic validation models
│── routes/              # API Endpoints (Routers)
│   ├── __init__.py
│   ├── orders.py        # Order-related endpoints
│   ├── metrics.py       # Metrics endpoints
│
│── services/            # Business logic (Service Layer)
│   ├── __init__.py
│   ├── order_service.py # Order logic
│   ├── metrics_service.py # Metrics calculation
│
│── workers/             # Background processing (Queue worker)
│   ├── __init__.py
│   ├── queue_worker.py  # Order processing worker
│
│── config.py            # Environment settings
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
│
│── tests/               # Unit tests
│   ├── test_orders.py
│   ├── test_metrics.py
│
│── .env                 # Environment variables
│── docker-compose.yml   # Docker setup
│── Dockerfile           # Container setup
│── .gitignore           # Ignored files



---

## 🛠️ **Installation & Setup**  

### **1️⃣ Prerequisites**  
- **Python 3.9+**  
- **PostgreSQL or SQLite**  
- **Docker (Optional for deployment)**  

### **2️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
