# Social Media Feed Optimization

A **Flask-based API** that serves a personalized content feed, ranking posts for a given user using a lightweight scoring algorithm.  
This project demonstrates **backend API development**, **system design**, **caching strategies**, and **unit testing**.

---

## 📌 Features
- **Personalized Feed Ranking** – Returns ranked posts tailored to a specific `user_id`.
- **Memoization / Caching** – Avoids recomputation for repeat requests, reducing latency.
- **Health Check Endpoint** – Simple `/health` endpoint to verify API liveness.
- **Lightweight & Extensible** – Easy to plug in more complex ranking algorithms.
- **Unit Testing** – Ensures functionality with automated tests.
- **Clean Architecture** – Separation of routes, logic, and configuration.

---

## 🛠 Tech Stack
- **Backend**: Python 3, Flask
- **Caching**: In-memory dictionary (extensible to Redis)
- **Testing**: `unittest`
- **Package Management**: `pip` + `requirements.txt`

---

## 📂 Project Structure
```bash
social-media-feed-optimization/
├── app.py              # Flask app with /feed and /health endpoints
├── requirements.txt    # Python dependencies
├── tests/
│   └── test_app.py     # Unit tests for /feed
└── README.md           # Project documentation
```

---

## 🚀 API Endpoints

### `/feed?user_id=<id>`
- **Description**: Returns ranked posts for the given user.
- **Method**: `GET`
- **Example**:
```bash
curl http://localhost:5000/feed?user_id=123
```

### `/health`
- **Description**: Health check endpoint.
- **Method**: `GET`
- **Example**:
```bash
curl http://localhost:5000/health
```

---

## ⚙️ Setup & Run

### 1️⃣ Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Start the server
```bash
python app.py
```
Server runs at: `http://localhost:5000`

---

## 🧪 Running Tests
```bash
python -m unittest discover tests
```

---

## 📈 Future Enhancements
- Integrate **Redis** for distributed caching.
- Add **JWT authentication** for secure endpoints.
- Implement **machine learning-based ranking**.
- Deploy to **Docker + Kubernetes** for scalability.
