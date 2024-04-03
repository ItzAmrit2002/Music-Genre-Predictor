# Music Genre Predictor Using Lyrics

## Overview
This project involves the development of a music genre detection app that predicts the genre of a song based on its lyrics. The application was built using React Js for the frontend and FastAPI in Python for the backend. The prediction model employs scikit-learn's Logistic Regression and LinearSVC algorithms to classify songs into different genres. Various techniques such as TfidfVectorizer, TfidfTransformer, and chi2 feature selection were utilized to preprocess the lyrics and improve the accuracy of genre classification.

## Technologies Used
- Frontend: React Js
- Backend: FastAPI (Python)
- Machine Learning: scikit-learn
- Algorithms: Logistic Regression, LinearSVC
- Text Processing: TfidfVectorizer, TfidfTransformer
- Feature Selection: chi2

## Implementation Details
- **Frontend Development**: The user interface was developed using React Js, providing an intuitive and responsive experience for users.
- **Backend Development**: FastAPI, a modern Python web framework, was utilized for the backend development, ensuring efficient API creation and handling.
- **Machine Learning Model**: Logistic Regression and LinearSVC algorithms were implemented to classify music genres based on song lyrics.
- **Text Processing**: Raw lyrics were transformed into numerical features using TfidfVectorizer and TfidfTransformer.
- **Feature Selection**: The chi2 method was employed for feature selection, enhancing classifier efficiency and prediction accuracy.

## Accuracy
The model achieved a classification accuracy of 77.8% in predicting music genres based on song lyrics.

## Duration
The development of this project spanned from August 2023 to November 2023.

