# 🏠 Real Estate Price Predictor

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://real-estate-price-predictor-1-d5hf.onrender.com)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange)](https://mlflow.org)
[![ZenML](https://img.shields.io/badge/ZenML-Pipeline-purple)](https://zenml.io)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Live Demo

**Try the app here:** 👉 [**real-estate-price-predictor-1-d5hf.onrender.com**](https://real-estate-price-predictor-1-d5hf.onrender.com)


## 📌 Overview

A **production-grade machine learning system** that predicts real estate prices based on property features (area, bedrooms, bathrooms, location). The project includes:

- ✅ **End-to-end ML pipeline** using ZenML for orchestration
- ✅ **Experiment tracking** with MLflow (logs parameters, metrics, models)
- ✅ **Model training** with Random Forest Regressor (R² = 0.92)
- ✅ **Interactive web app** built with Streamlit
- ✅ **Live deployment** on Render.com

## 📊 Model Performance

After training on 5,000 synthetic property records, the model achieves:

| Metric | Value |
|--------|-------|
| **Model** | Random Forest Regressor |
| **R² Score** | **0.92** |
| **Mean Absolute Error (MAE)** | ₹4.5 Lakhs |
| **Training samples** | 4,000 |
| **Test samples** | 1,000 |
| **Features used** | Area, bedrooms, bathrooms, location |

### Feature Importance
Area ████████████████████ 65%

Location ██████ 18%

Bedrooms ███ 10%

Bathrooms ██ 7%


## 🛠️ Tech Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **ML Framework** | Scikit-learn (Random Forest) | Model training & inference |
| **ML Pipeline** | ZenML | Pipeline orchestration |
| **Experiment Tracking** | MLflow | Logging & model registry |
| **Frontend** | Streamlit | Interactive UI |
| **Data Processing** | Pandas, NumPy | Data manipulation |
| **Deployment** | Render.com | Hosting (Python 3.9) |
| **Version Control** | Git & GitHub | Code management |

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9 or 3.10
- Git

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/sahelidgp/real-estate-price-predictor.git
   cd real-estate-price-predictor
   ```
2. **Create a virtual environment**
 ```
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

```
3. **Install dependencies**
```
pip install -r requirements.txt
```
4. **Run the app**
```
streamlit run app.py
```
5. **Open browser to** http://localhost:5000
   
# 🧠 Training the Model
The model is trained using a ZenML pipeline. To retrain:

```
python run_pipeline.py
```
This will:

- Generate synthetic training data (or load your own from data/)

- Preprocess and one‑hot encode location

- Train a Random Forest Regressor

- Log parameters & metrics to MLflow (mlruns/)

- Save the best model as trained_model.pkl

# MLflow Dashboard
```
mlflow ui
```
Then open http://localhost:5000 to explore logged runs.

# 📁 Project Structure
```
real-estate-price-predictor/
├── app.py                    # Streamlit frontend + API
├── trained_model.pkl         # Trained Random Forest model
├── requirements.txt          # Dependencies
├── runtime.txt               # Python version (3.9.18)
├── render.yaml               # Render deployment config
│
├── run_pipeline.py           # ZenML training pipeline
├── pipelines/                # Pipeline definitions
├── steps/                    # Pipeline steps (data prep, train, eval)
├── mlruns/                   # MLflow experiment tracking
├── analysis/                 # EDA notebooks
├── data/                     # Raw & processed datasets
├── tests/                    # Unit tests
└── README.md                 # This file
```
# 🌐 Deployment
The app is deployed on Render.com using a custom render.yaml configuration and Python 3.9 (to avoid compatibility issues with Python 3.14).

## Deployment steps (automated):

- Git push triggers a new build

- Render installs dependencies

- Starts Streamlit with --server.port $PORT

# 📈 Future Improvements
- Add real‑world dataset (Kaggle: Bangalore / USA housing)

- Include more features: age of property, floor number, proximity to metro

- Implement A/B testing for model versions

- Add user authentication to save search history

- Deploy on a dedicated domain with HTTPS

# 🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check the issues page.

# 📄 License
Distributed under the MIT License. See LICENSE for more information.

# 👩‍💻 Author
Saheli Mahanty

GitHub: @sahelidgp

Project Link: https://github.com/sahelidgp/real-estate-price-predictor

Live Demo: https://real-estate-price-predictor-1-d5hf.onrender.com

# 🙏 Acknowledgements
- [Streamlit](https://streamlit.io/) – amazing frontend framework

- [ZenML](https://www.zenml.io/) – MLOps pipeline orchestration

- [MLflow](https://mlflow.org/) – experiment tracking

- [Render](https://render.com/) – free hosting



   
