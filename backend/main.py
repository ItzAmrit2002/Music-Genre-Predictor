import pickle
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.responses import JSONResponse
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
import librosa
import numpy as np
import pandas as pd
import joblib
from librosa.feature import rhythm
import tempfile

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

def extract_features(filename):
    y, sr = librosa.load(filename, duration=3)

    features = {
        'chroma_stft_mean': np.mean(librosa.feature.chroma_stft(y=y, sr=sr)),
        'chroma_stft_var': np.var(librosa.feature.chroma_stft(y=y, sr=sr)),
        'rms_mean': np.mean(librosa.feature.rms(y=y)),
        'rms_var': np.var(librosa.feature.rms(y=y)),
        'spectral_centroid_mean': np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)),
        'spectral_centroid_var': np.var(librosa.feature.spectral_centroid(y=y, sr=sr)),
        'spectral_bandwidth_mean': np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr)),
        'spectral_bandwidth_var': np.var(librosa.feature.spectral_bandwidth(y=y, sr=sr)),
        'rolloff_mean': np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr)),
        'rolloff_var': np.var(librosa.feature.spectral_rolloff(y=y, sr=sr)),
        'zero_crossing_rate_mean': np.mean(librosa.feature.zero_crossing_rate(y)),
        'zero_crossing_rate_var': np.var(librosa.feature.zero_crossing_rate(y)),
        'harmony_mean': np.mean(librosa.effects.harmonic(y)),
        'harmony_var': np.var(librosa.effects.harmonic(y)),
        'perceptr_mean': np.mean(librosa.effects.percussive(y)),
        'perceptr_var': np.var(librosa.effects.percussive(y)),
        'tempo': librosa.feature.rhythm.tempo(y=y, sr=sr)[0],
    }

    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    for i in range(1, 21):
        features[f'mfcc{i}_mean'] = np.mean(mfcc[i-1])
        features[f'mfcc{i}_var'] = np.var(mfcc[i-1])

    return pd.DataFrame([features])


@app.post("/")
async def predict(lyrics: Lyrics):
    fitted_vectorizer = pickle.load(open("models/transformer.sav", "rb"))
    model = pickle.load(open("models/fixedmodel.sav", "rb"))
    lyrics_text = lyrics.lyrics
    prediction = model.predict(fitted_vectorizer.transform([lyrics_text]))[0]
    print(prediction)
    return prediction


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    # Save the uploaded file to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    data = await file.read()
    with open(temp_file.name, 'wb') as f:
        f.write(data)

    # Extract features and create a DataFrame row
    features_df = extract_features(temp_file.name)

    # Load the model and scaler
    model = joblib.load('models/knn_best.joblib')
    scaler = joblib.load('models/scaler.joblib')

    # Scale the features
    features_df = pd.DataFrame(features_df)
    features_df = features_df.sort_index(axis=1)
    features_df = scaler.transform(features_df)

    # Predict using the pre-trained model
    prediction = model.predict(features_df)

    return JSONResponse(content={"Predicted label": str(prediction[0])})
