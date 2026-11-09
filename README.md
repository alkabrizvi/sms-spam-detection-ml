# SMS Spam Detection System

An end-to-end Machine Learning project that classifies SMS messages as Spam or Ham (Not Spam) using Natural Language Processing (NLP).

## Project Overview

This project uses machine learning and NLP techniques to detect unwanted or fraudulent SMS messages. Users can enter a message through a web interface and receive a prediction.

## Features

- SMS text preprocessing
- Exploratory Data Analysis (EDA)
- TF-IDF feature extraction
- Multiple machine learning models
- Linear Support Vector Classifier (LinearSVC)
- Custom text preprocessing transformer
- Scikit-learn Pipeline
- FastAPI backend
- HTML, CSS and JavaScript frontend

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- NLTK
- FastAPI
- HTML
- CSS
- JavaScript

## Project Structure

```text
sms-spam-detection-ml/
│
├── app.py
├── preprocessor.py
├── spam_detector.pkl
├── index.html
├── style.css
├── script.js
├── Untitled.ipynb
└── README.md
```

## Machine Learning Models

The following models were evaluated:

- Logistic Regression
- Multinomial Naive Bayes
- Random Forest
- LinearSVC

**Best performing model:** LinearSVC

- Accuracy: 98.26%
- Spam Precision: 97%
- Spam Recall: 89%
- Spam F1-score: 93%

*Results are based on the project's current train-test split.*

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/alkabrizvi/sms-spam-detection-ml.git
```

### 2. Open project directory

```bash
cd sms-spam-detection-ml
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn scikit-learn nltk joblib pandas numpy matplotlib
```

### 4. Download NLTK stopwords

```python
import nltk
nltk.download('stopwords')
```

### 5. Start FastAPI

```bash
python -m uvicorn app:app --reload
```

### 6. Open API documentation

Visit:

http://127.0.0.1:8000/docs

Open `index.html` using VS Code Live Server to access the frontend.

## Future Improvements

- Improve model generalization
- Add more diverse SMS datasets
- Deploy the application online
- Improve frontend user experience
- Add model monitoring

## Author

**Alkab Rizvi**

GitHub: https://github.com/alkabrizvi