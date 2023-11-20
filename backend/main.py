import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Lyrics(BaseModel):
    lyrics: str


@app.post("/")
async def predict(lyrics: Lyrics):
    fitted_vectorizer = pickle.load(open("models/transformer.sav", "rb"))
    model = pickle.load(open("models/fixedmodel.sav", "rb"))
    lyrics_text = lyrics.lyrics
    prediction = model.predict(fitted_vectorizer.transform([lyrics_text]))[0]
    print(prediction)
    return prediction