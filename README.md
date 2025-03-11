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
```bash
order-processing-api/
│── app.py               # FastAPI application entry point
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
│   ├── order_service.py # Functions for handling order logic
│   ├── metrics_service.py # Functions for metrics calculation
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
```

## 🛠️ **Installation & Setup**  

#### **1️⃣ Clone the Repository** 
```bash
https://github.com/anil-gaikwad/order-processing-backend.git
cd order-processing-api
```

#### **2️⃣ Create a Virtual Environment** 
 ```bash
 python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

 ```

#### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **4️⃣ Configure the Database**
- **Edit .env file to set up SQLite.**
- **Initialize the database:**
```bash
python database.py
```

#### **5️⃣ Run the Application**  
```bash
uvicorn app:app --host 0.0.0.0 --port 3000 --reload
```

#### **6️⃣ Run with Docker (Optional)**  
```sh
docker-compose up --build
```

## 🛠 **API Endpoints**
#### 1️⃣ **Create an Order**

📌 Endpoint: POST
```bash
 http://localhost:3000/api/order
```
📌 Request Body (JSON):
```json
{
  "order_id": 101,
  "user_id": 5001,
  "item_ids": [12, 34, 56],
  "total_amount": 250.75
}
```

📌 Response:
```json
{
  "message": "Order received",
  "order_id": 101
}
```

#### 2️⃣ **Get Order Status**
📌 Endpoint: GET 

```bash
http://localhost:3000/api/order/{order_id}
```
📌 Response:
```json
{
  "order_id": 101,
  "status": "Processing"
}
```

#### 3️⃣ **Get Metrics**
📌 Endpoint: GET

```bash
http://localhost:3000/api/metrics
```
📌 Response:

```json
{
  "total_orders": 1000,
  "orders_pending": 200,
  "orders_processing": 500,
  "orders_completed": 300,
  "average_processing_time": 2.5
}
```
