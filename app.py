import joblib
import __main__

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from preprocessor import TextPreprocessor

# Custom transformer registration
__main__.TextPreprocessor = TextPreprocessor

# Load trained model
model = joblib.load("spam_detector.pkl")

# FastAPI application
app = FastAPI(title="SMS Spam Detector")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MessageInput(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "SMS Spam Detector API is running!"}


@app.post("/predict")
def predict(data: MessageInput):

    prediction = model.predict([data.message])[0]
    score = model.decision_function([data.message])[0]

    print("Input Message:", data.message)
    print("Prediction:", prediction)
    print("Decision Score:", score)

    result = "Spam" if prediction == 1 else "Ham"

    return {
        "message": data.message,
        "prediction": result,
        "decision_score": float(score)
    }