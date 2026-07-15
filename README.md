# 🌊 Rising Waters: A Machine Learning Approach to Flood Prediction

## 📌 Project Overview

Rising Waters is a Machine Learning-based Flood Prediction System that predicts the likelihood of flood occurrence using weather and rainfall parameters. The system helps provide early flood risk assessment by analyzing historical rainfall and climate data.

The project includes a trained Machine Learning model and a user-friendly web application developed using Flask.

---

## 🚀 Features

- Predicts Flood Risk using Machine Learning
- User-friendly web interface
- Accepts real-time weather and rainfall inputs
- Displays Flood Risk prediction
- Displays prediction probability
- Fast prediction using a trained Random Forest model
- Stores prediction history (optional)

---

## 🛠 Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Random Forest Classifier

### Web Framework
- Flask

### Libraries
- Pandas
- NumPy
- Joblib
- HTML
- CSS

---

## 📂 Project Structure

```
Rising-Waters/
│
├── app.py
├── floods.save
├── scaler.save
├── prediction_history.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── dataset/
│   └── flood_dataset.csv
│
├── notebook/
│   └── Flood_Prediction.ipynb
│
├── README.md
└── requirements.txt
```

---

## 📊 Dataset Features

The model uses the following features:

- Temperature
- Humidity
- Cloud Cover
- Annual Rainfall
- Jan-Feb Rainfall
- Mar-May Rainfall
- Jun-Sep Rainfall
- Oct-Dec Rainfall
- Average June Rainfall
- Sub Rainfall

Target Variable:

- Flood (0 = No Flood, 1 = Flood)

---

## 🤖 Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Other algorithms tested:

- Decision Tree
- K-Nearest Neighbors (KNN)
- XGBoost

Random Forest was selected because it provided the best performance on the dataset.

---

## 📈 Model Performance

| Metric | Value |
|---------|-------|
| Accuracy | 95.65% |
| Precision | 96% |
| Recall | 96% |
| F1 Score | 95% |

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Rising-Waters.git
```

Move into project folder

```bash
cd Rising-Waters
```

Install required libraries

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open browser

```
http://127.0.0.1:5000
```

---

## 🔄 Project Workflow

1. Load Dataset
2. Data Preprocessing
3. Feature Selection
4. Train-Test Split
5. Data Standardization
6. Train Random Forest Model
7. Save Model using Joblib
8. Develop Flask Web Application
9. Predict Flood Risk
10. Display Prediction Result

---

## 📋 Future Enhancements

- Live Weather API Integration
- GIS-based Flood Mapping
- SMS Alert System
- Email Notifications
- Interactive Dashboard
- Mobile Application
- Real-time Rainfall Monitoring

---

## 🎯 Applications

- Disaster Management
- Government Flood Monitoring
- Agriculture Planning
- Smart Cities
- Environmental Monitoring
- Public Safety

---

## 👩‍💻 Developed By

**Navya Sri Suvvari**

B.Tech (Computer Science & Engineering - Data Science)

Anil Neerukonda Institute of Technology and Sciences (ANITS)

---

## 📜 License

This project is developed for internship and educational purposes.

---

## ⭐ Acknowledgements

- APSCHE
- SkillWallet
- SmartBridge
- AI TOOLS
- Python Community
