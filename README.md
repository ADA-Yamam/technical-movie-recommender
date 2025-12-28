 

# 🎬 Technical Movie Recommender

### Data Engineering Portfolio Project

---

## 📌 Project Overview

This is a **technical data engineering portfolio project** designed to demonstrate core competencies in building **end-to-end data systems**.

The project focuses on **system architecture, automation, and integration** rather than deep statistical analysis or business-driven insights. It represents a **foundation technical system** that can be easily extended with larger datasets, richer features, and more advanced logic.

The project integrates **APIs, SQL, Python, ETL pipelines, machine learning, REST services, and data visualization** into a single reproducible workflow.

---

## 🎯 Project Objectives

* Work with external APIs as data sources
* Design and manage relational databases (SQLite)
* Build a complete ETL (Extract, Transform, Load) pipeline
* Process and clean data using Python
* Automate data workflows and transformations
* Implement a simple content-based machine learning recommendation model
* Expose results through a REST API (FastAPI)
* Visualize outputs using an interactive dashboard (Streamlit)
* Demonstrate reproducibility, modular code, and clean project structure

---

## 🧠 System Architecture

The project follows a **full end-to-end technical workflow**:

---

### 1️⃣ Data Source

* Movie data retrieved from an external API
* Data includes movie titles, release years, and ratings
* API data is stored locally for reproducibility

---

### 2️⃣ ETL Pipeline (Jupyter Notebook)

The **ETL process is implemented inside a Jupyter Notebook**, intentionally separated from the API layer.

**Why Jupyter?**

* Enables exploratory inspection of raw API data
* Allows controlled transformations and validation
* Makes the pipeline transparent and auditable

**ETL Steps:**

* **Extract**: Fetch raw movie data from API
* **Transform**: Clean, validate, normalize data using Pandas & NumPy
* **Load**: Persist structured data into SQLite database

This separation reflects real-world data engineering practices where ETL and serving layers are decoupled.

---

### 3️⃣ API Key Limitations & Handling

The external movie API enforces:

* Request limits per minute
* Daily quota restrictions

**How this project handles API limits:**

* ETL pipeline is executed manually (not on every API call)
* Data is persisted locally in SQLite
* The API and dashboard read from the database, **not directly from the external API**
* This prevents unnecessary API calls and avoids quota exhaustion

This approach mirrors production systems where APIs are used for ingestion, not real-time serving.

---

### 4️⃣ Machine Learning Model

**Model Type**
Content-Based Recommendation System

**Features Used**

* Movie rating (numerical)
* Release year (numerical)

**Techniques**

* Feature scaling using `StandardScaler`
* Cosine similarity for movie-to-movie similarity
* Top-N recommendation logic

**Design Philosophy**
The model is intentionally simple to emphasize:

* ML integration into data systems
* Feature preprocessing pipelines
* Model reproducibility
* API and dashboard integration

The goal is **system demonstration**, not predictive optimization.

---

### 5️⃣ API Layer

**Framework**: FastAPI

**Responsibilities**

* Serve recommendations via REST endpoints
* Interface with the ML model
* Read data from SQLite database
* Provide auto-generated documentation

**Documentation**

* Swagger UI available at `/docs`
* Clear request/response structure

The API demonstrates how ML systems are exposed programmatically.

---

### 6️⃣ Visualization Layer

**Framework**: Streamlit

**Features**

* Interactive slider for recommendation parameters
* Tabular display of recommended movies
* Real-time interaction with ML outputs

The dashboard provides a **user-facing interface** for exploring recommendations without touching code.

---

## 🗂️ Project Structure

```
technical-movie-recommender/
│
├── movies.db                    # SQLite database
├── recommender_model.py         # ML recommendation logic
├── movie_platform_api.py        # FastAPI application
├── dashboard.py                 # Streamlit dashboard
├── prepare_db.py                # Database initialization
├── test_recommender.py          # Model testing
├── jupyter.ipynb                # ETL pipeline (API → DB)
├── run_server.bat               # API startup automation
├── requirements.txt             # Dependencies
├── .gitignore                   # Git configuration
└── README.md                    # Documentation
```

---

## 🗃️ Database Schema

### Movies Table

| Column      | Type         | Description             |
| ----------- | ------------ | ----------------------- |
| MovieID     | INTEGER (PK) | Unique movie identifier |
| Title       | TEXT         | Movie title             |
| ReleaseYear | INTEGER      | Year of release         |
| Rating      | REAL         | Movie rating (0–10)     |

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Prepare the Database

```bash
python prepare_db.py
```

### 3️⃣ Run ETL (Jupyter)

Open `jupyter.ipynb` and execute all cells to:

* Fetch API data
* Clean and transform
* Load into SQLite

### 4️⃣ Test the Model

```bash
python test_recommender.py
```

### 5️⃣ Run the API

```bash
uvicorn movie_platform_api:app --reload
```

Access:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 6️⃣ Run the Dashboard

```bash
streamlit run dashboard.py
```

Access:

* Dashboard: [http://localhost:8501](http://localhost:8501)

---

## 📈 Technical Skills Demonstrated

* ETL pipeline design
* API integration and rate-limit handling
* SQL database design
* Machine learning system integration
* REST API development
* Interactive data visualization
* Automation and reproducibility
* Clean project organization

---

## 📚 Project Scope & Limitations

**Intentional Limitations**

* Small dataset
* Simple ML logic
* Limited features
* No personalization

**Rationale**

* Emphasize system architecture
* Keep project maintainable
* Provide a strong technical foundation

---

## 🔮 Future Improvements

* Larger datasets
* Genre and cast features
* Collaborative filtering
* Cloud deployment
* CI/CD pipelines
* Monitoring and logging

---

## 👤 Author

**Technical Data Analyst / Data Engineer**

This project demonstrates the ability to design and implement **production-style data systems** using Python, SQL, APIs, and machine learning.


