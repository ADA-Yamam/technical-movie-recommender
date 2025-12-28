# 🎬 Technical Movie Recommender — Data Engineering Portfolio Project

## 📌 Project Overview

This is a **technical data engineering portfolio project** designed to demonstrate core competencies in building end-to-end data systems. The project showcases the ability to design, build, and integrate a complete data pipeline using Python, SQL, APIs, and machine learning, resulting in an automated and reproducible system.

The focus is on **technical execution and system architecture** rather than deep statistical analysis or business insights. This represents a **foundation system** that can be easily extended with additional data and more sophisticated logic.

---

## 🎯 Project Objectives

- Work with external APIs as data sources
- Design and manage relational databases (SQLite)
- Build a complete ETL (Extract, Transform, Load) pipeline
- Process and clean data using Python
- Automate data workflows and transformations
- Implement a content-based machine learning recommendation model
- Expose results through a REST API (FastAPI)
- Visualize outputs using an interactive dashboard (Streamlit)
- Demonstrate reproducibility and code organization

---

## 🧠 System Architecture

The project follows an end-to-end technical workflow:

### 1. **Data Source**
- Movie data retrieved from external APIs or stored in local SQLite database
- Structured data format with movie metadata

### 2. **ETL Pipeline**
- **Extract**: Load raw movie data from source
- **Transform**: Clean, validate, and prepare data using Python (Pandas, NumPy)
- **Load**: Store processed data in SQLite database

### 3. **Machine Learning Model**
- **Type**: Content-based recommendation system
- **Features**: Movie rating, release year
- **Algorithm**: Cosine similarity for movie-to-movie similarity computation
- **Scaling**: StandardScaler for feature normalization
- **Purpose**: Demonstrate ML integration, not deep model complexity

### 4. **API Layer**
- **Framework**: FastAPI (modern, fast Python web framework)
- **Functionality**: REST endpoints for recommendations
- **Documentation**: Auto-generated Swagger UI at `/docs`
- **Purpose**: Programmatic access to recommendation engine

### 5. **Visualization Layer**
- **Framework**: Streamlit (interactive data app framework)
- **Features**: 
  - Interactive controls for recommendation parameters
  - Tabular display of results
  - Real-time model output visualization
- **Purpose**: User-friendly interface for exploring recommendations

---

## 🗂️ Project Structure

```
technical-movie-recommender/
│
├── movies.db                    # SQLite database with movie data
├── recommender_model.py         # ML recommendation logic
├── movie_platform_api.py        # FastAPI REST API application
├── dashboard.py                 # Streamlit interactive dashboard
├── prepare_db.py                # Database initialization and ETL script
├── test_recommender.py          # Model testing and validation script
├── run_server.bat               # Batch script to start API server
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore configuration
└── README.md                    # Project documentation
```

---

## 🗃️ Database Schema

### Movies Table

| Column | Type | Description |
|--------|------|-------------|
| MovieID | INTEGER (PK) | Unique movie identifier |
| Title | TEXT | Movie title |
| ReleaseYear | INTEGER | Year of release |
| Rating | REAL | Movie rating (0-10 scale) |

---

## 🤖 Machine Learning Model

### Model Type
**Content-Based Recommendation System**

### Features
- Movie rating (numerical)
- Release year (numerical)

### Techniques
- Feature scaling using StandardScaler
- Cosine similarity for similarity computation
- K-nearest neighbors approach for recommendations

### Design Philosophy
The model is intentionally simple to focus on **system integration and automation** rather than model complexity. This demonstrates the ability to:
- Integrate ML into production systems
- Handle data preprocessing
- Expose model predictions through APIs
- Validate model outputs

---

## 📊 Dashboard Features

The Streamlit dashboard provides:
- **Interactive Controls**: Adjust recommendation parameters
- **Data Display**: Tabular view of recommended movies
- **Real-time Results**: Instant model output visualization
- **User-Friendly Interface**: Clean, intuitive design

The dashboard demonstrates **technical visualization skills** and ability to create user-facing interfaces for data systems.

---

## 🚀 How to Run the Project

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Initialize the Database
```bash
python prepare_db.py
```

This script:
- Creates SQLite database
- Initializes schema
- Loads sample movie data
- Prepares data for recommendations

### 3️⃣ Test the Recommendation Model
```bash
python test_recommender.py
```

This script:
- Loads the trained model
- Tests recommendations for sample movies
- Validates model outputs
- Demonstrates model functionality

### 4️⃣ Run the API Server
```bash
uvicorn movie_platform_api:app --reload
```

Access the API:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **API Base**: http://127.0.0.1:8000

### 5️⃣ Run the Dashboard
```bash
streamlit run dashboard.py
```

Access the dashboard:
- **Dashboard**: http://localhost:8501

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| **Language** | Python 3.8+ |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn |
| **Database** | SQLite |
| **API Framework** | FastAPI |
| **Dashboard** | Streamlit |
| **Testing** | Python unittest/pytest |

---

## 📈 Technical Skills Demonstrated

### Data Engineering
- ETL pipeline design and implementation
- Database schema design and management
- Data cleaning and validation
- Automated data workflows

### Python Development
- Object-oriented programming
- Data structures and algorithms
- Error handling and logging
- Code organization and modularity

### Machine Learning
- Feature engineering and scaling
- Similarity metrics and algorithms
- Model evaluation and testing
- ML system integration

### API Development
- REST API design principles
- FastAPI framework usage
- API documentation
- Error handling and validation

### Data Visualization
- Interactive dashboards
- Data presentation
- User interface design
- Real-time data updates

---

## 🧪 Testing

Run the test script to validate the recommendation model:
```bash
python test_recommender.py
```

Expected output:
- Sample movie recommendations
- Similarity scores
- Model performance metrics

---

## 📚 Project Scope & Limitations

### Intentional Limitations
- **Small Dataset**: Sample movie data for demonstration
- **Simple ML Model**: Content-based approach for clarity
- **Limited Features**: Rating and release year only
- **No User Personalization**: System-wide recommendations

### Design Rationale
These limitations are **intentional** to:
- Keep the project focused and maintainable
- Emphasize technical architecture over data science complexity
- Demonstrate ability to build complete systems with limited resources
- Provide a clear foundation for future enhancements

---

## 🔮 Future Improvements

### Data Enhancements
- Integrate larger movie datasets
- Add genre and cast information
- Include user ratings and preferences

### Model Improvements
- Implement collaborative filtering
- Add deep learning approaches
- Develop hybrid recommendation systems

### System Enhancements
- Add user authentication
- Implement caching mechanisms
- Deploy to cloud platforms (AWS, GCP, Azure)
- Add automated testing and CI/CD

### Feature Additions
- User preference learning
- Recommendation explanations
- A/B testing framework
- Analytics and monitoring

---

## 📝 Project Documentation

### Code Comments
All Python files include:
- Function docstrings
- Inline comments for complex logic
- Type hints for clarity

### API Documentation
- Auto-generated Swagger UI
- Endpoint descriptions
- Request/response schemas

### Database Documentation
- Schema descriptions in README
- Column definitions and types

---

## 🎓 Learning Outcomes

This project demonstrates:
1. **System Design**: Building integrated data systems
2. **Full-Stack Development**: From data to API to UI
3. **Data Engineering**: ETL, databases, automation
4. **Software Engineering**: Code quality, organization, testing
5. **Technical Communication**: Documentation, comments, design clarity

---

## 📄 License

This project is provided as-is for portfolio and educational purposes.

---

## 👤 Author

**Technical Data Engineer / Data Analyst**

This project represents technical competency in data engineering, Python development, and building end-to-end data systems.

---

## 📞 Questions & Feedback

For questions about the technical implementation or project structure, please refer to the code comments and inline documentation.

---

**Last Updated**: December 2024  
**Status**: Complete and Production-Ready  
**Version**: 1.0.0
