from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = FastAPI()

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Load the model and vectorizer
try:
    with open('artifact/bug_severity_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('artifact/tfidf_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
except FileNotFoundError:
    raise HTTPException(status_code=500, detail="Model or vectorizer file not found. Please ensure the model is trained and saved.")

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    return ' '.join([word for word in tokens if word.isalnum() and word not in stop_words])

class BugDescription(BaseModel):
    description: str

@app.post("/predict")
def predict_severity(bug: BugDescription):
    processed_description = preprocess_text(bug.description)
    vectorized_description = vectorizer.transform([processed_description])
    prediction = model.predict(vectorized_description)
    return {"severity": str(prediction[0])}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Bug Severity Predictor API"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)