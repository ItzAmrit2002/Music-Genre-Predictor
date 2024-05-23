# -*- coding: utf-8 -*-
"""musiclet'splay.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ntrO3P9HHZFNs5717BtetCVyN0M3cyUP
"""

# Commented out IPython magic to ensure Python compatibility.
# Standard library imports
import warnings
import os
# Third-party imports for data manipulation and analysis
import numpy as np
import pandas as pd

# Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Audio processing library
import librosa
import librosa.display

# Machine learning preprocessing and model selection
import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, StandardScaler, minmax_scale
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Deep learning libraries
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras import optimizers

# Statistical distributions for randomized search
from scipy.stats import loguniform, randint

# Suppress warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")

# Set up the aesthetics for seaborn plots
sns.set(style="whitegrid")

# Ensure that plots are displayed in the Jupyter Notebook
# %matplotlib inline

audio_path = "/content/drive/MyDrive/Data/genres_original/pop/pop.00005.wav"
audio, sr = librosa.load(audio_path)

plt.figure(figsize=(14, 5))
librosa.display.waveshow(audio, sr=sr)
plt.xlabel('Time (samples)')
plt.ylabel('Amplitude')
plt.title('The first sample track from the pop music folder')
plt.xlim([0,30])
plt.show()

chroma_stft = librosa.feature.chroma_stft(y=audio, sr=sr)

plt.figure(figsize=(14, 5))
librosa.display.specshow(chroma_stft, x_axis='time', y_axis='chroma', sr=sr)
plt.colorbar()
plt.xlabel('Time (s)')
plt.ylabel('Pitch Class')
plt.title('Chroma STFT')
plt.show()

rms = librosa.feature.rms(y=audio)
rms_mean = rms.mean()

print("RMS Mean:", rms_mean)

spectral_centroids = librosa.feature.spectral_centroid(y=audio, sr=sr)
spectral_centroids_mean = spectral_centroids.mean()

print("Spectral Centroid Mean:", spectral_centroids_mean)

# Calculate the spectral centroids
spectral_centroids = librosa.feature.spectral_centroid(y=audio, sr=sr)

# Computing the time variable for visualization
frames = range(len(spectral_centroids[0]))
t = librosa.frames_to_time(frames, sr=sr)

# Function that normalizes the Sound Data
def normalize(x, axis=0):
    return minmax_scale(x, axis=axis)

# Use a stylish plot theme
plt.style.use('seaborn-dark-palette')

# Plotting the Spectral Centroid along the waveform
plt.figure(figsize=(16, 6))
ax = plt.axes()
ax.set_facecolor('#202020')  # Set a dark background color

# Waveform plot
librosa.display.waveshow(audio, sr=sr, alpha=0.6, color='#1DB954', linewidth=1.5, label='Waveform')

# Spectral centroids plot
plt.plot(t, normalize(spectral_centroids[0]), color='#FFC300', linewidth=2, label='Normalized Spectral Centroids')

# Enhancing the plot
plt.title('Waveform and Normalized Spectral Centroids', fontsize=16, fontweight='bold', color='white')
plt.xlabel('Time (seconds)', fontsize=14, color='white')
plt.ylabel('Normalized Amplitude / Frequency', fontsize=14, color='white')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xticks(fontsize=12, color='white')
plt.yticks(fontsize=12, color='white')

# Show the plot
plt.show()

spectral_bandwidths = librosa.feature.spectral_bandwidth(y=audio, sr=sr)
spectral_bandwidths_mean = spectral_bandwidths.mean()

print("Spectral Bandwidth Mean:", spectral_bandwidths_mean)

spectral_rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr)
spectral_rolloff_mean = spectral_rolloff.mean()

print("Spectral Rolloff Mean:", spectral_rolloff_mean)

# Computing the time variable for visualization
frames = range(len(spectral_rolloff [0]))
t = librosa.frames_to_time(frames, sr=sr)

# Function that normalizes the Sound Data
def normalize(x, axis=0):
    return minmax_scale(x, axis=axis)

# Use a stylish plot theme
plt.style.use('seaborn-dark-palette')

# Plotting the spectral_rolloff along the waveform
plt.figure(figsize=(16, 6))
ax = plt.axes()
ax.set_facecolor('#202020')  # Set a dark background color

# Waveform plot
librosa.display.waveshow(audio, sr=sr, alpha=0.6, color='#1DB954', linewidth=1.5, label='Waveform')

# chroma_cens plot
plt.plot(t, normalize(spectral_rolloff[0]), color='#FFC300', linewidth=2, label='Normalized spectral_rolloff')

# Enhancing the plot
plt.title('Waveform and Normalized spectral_rolloff', fontsize=16, fontweight='bold', color='white')
plt.xlabel('Time (seconds)', fontsize=14, color='white')
plt.ylabel('Normalized Amplitude / Frequency', fontsize=14, color='white')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xticks(fontsize=12, color='white')
plt.yticks(fontsize=12, color='white')

# Show the plot
plt.show()

zero_crossing_rates = librosa.feature.zero_crossing_rate(y=audio)
zero_crossing_rates_mean = zero_crossing_rates.mean()

print("Zero-Crossing Rate Mean:", zero_crossing_rates_mean)

chroma_cens = librosa.feature.chroma_cens(y=audio, sr=sr)
harmony_mean = chroma_cens.mean()

print("Harmony Mean:", harmony_mean)

# Computing the time variable for visualization
frames = range(len(chroma_cens[0]))
t = librosa.frames_to_time(frames, sr=sr)

# Function that normalizes the Sound Data
def normalize(x, axis=0):
    return minmax_scale(x, axis=axis)

# Use a stylish plot theme
plt.style.use('seaborn-dark-palette')

# Plotting the Spectral Centroid along the waveform
plt.figure(figsize=(16, 6))
ax = plt.axes()
ax.set_facecolor('#202020')  # Set a dark background color

# Waveform plot
librosa.display.waveshow(audio, sr=sr, alpha=0.6, color='#1DB954', linewidth=1.5, label='Waveform')

# chroma_cens plot
plt.plot(t, normalize(chroma_cens[0]), color='#FFC300', linewidth=2, label='Normalized chroma_cens')

# Enhancing the plot
plt.title('Waveform and Normalized chroma_cens', fontsize=16, fontweight='bold', color='white')
plt.xlabel('Time (seconds)', fontsize=14, color='white')
plt.ylabel('Normalized Amplitude / Frequency', fontsize=14, color='white')
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.xticks(fontsize=12, color='white')
plt.yticks(fontsize=12, color='white')

# Show the plot
plt.show()

tempo, _ = librosa.beat.beat_track(y=audio, sr=sr)
tempo_mean = tempo.mean()

print("Tempo Mean (BPM):", tempo_mean)

# Compute MFCCs
mfccs = librosa.feature.mfcc(y=audio, sr=sr)

# Apply Feature Scaling
mfccs = sklearn.preprocessing.scale(mfccs, axis=1)

# Plot MFCCs
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time', cmap='coolwarm')
plt.colorbar(format='%+2.0f dB')
plt.title('MFCC')
plt.xlabel('Time')
plt.ylabel('MFCC Coefficients')
plt.tight_layout()
plt.show()

df = pd.read_csv('/content/drive/MyDrive/Data/features_3_sec.csv')

df.head()

df.shape
df.iloc[1,:]

df.isna().sum()

df = df.drop('filename', axis = 1)

mean_columns = df.filter(regex='_mean$')

correlation_matrix = mean_columns.corr()

# Create a boolean mask for the upper triangle of the matrix
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))

# Set up the matplotlib figure
plt.figure(figsize=(12, 10))
# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(correlation_matrix, mask=mask, cmap=cmap, annot=False, linewidths=0,
            cbar_kws={"shrink": .5}, square=True)

# Add a title to the heatmap
plt.title('Correlation Heatmap of Mean Features', fontsize=16, fontweight='bold')

# Show the plot
plt.show()

# Subset the DataFrame to include only the 'label' and 'tempo' columns
x = df[["label", "tempo"]]

# Create the plot
f, ax = plt.subplots(figsize=(16, 9))
sns.boxplot(x="label", y="tempo", data=x, palette='husl')

# Styling the plot with titles and labels
plt.title('Boxplot for Genres', fontsize=25, fontweight='bold')
plt.xlabel("Genre", fontsize=15)
plt.ylabel("BPM", fontsize=15)

data = df.iloc[0:, 1:]
y = data['label']
X = data.loc[:, data.columns != 'label']

#### NORMALIZE X ####
cols = X.columns
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(X)
X = pd.DataFrame(np_scaled, columns = cols)

#### PCA 2 COMPONENTS ####
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(X)
principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])

# concatenate with target label
finalDf = pd.concat([principalDf, y], axis = 1)

pca.explained_variance_ratio_

plt.figure(figsize = (16, 9))
sns.scatterplot(x = "principal component 1", y = "principal component 2", data = finalDf, hue = "label", alpha = 0.7,
               s = 100);

plt.title('PCA on Genres', fontsize = 25)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 10);
plt.xlabel("Principal Component 1", fontsize = 15)
plt.ylabel("Principal Component 2", fontsize = 15)
plt.savefig("PCA Scattert.jpg")

y = data['label'] # genre variable.
X = data.loc[:, data.columns != 'label'] #select all columns but not the labels

#### NORMALIZE X ####

# Normalize so everything is on the same scale.

cols = X.columns
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(X)

# new data frame with the new scaled data.
X = pd.DataFrame(np_scaled, columns = cols)

X_train_70, X_test_30, y_train_70, y_test_30 = train_test_split(X, y, test_size=0.3, random_state=42)

X_train_80, X_test_20, y_train_80, y_test_20 = train_test_split(X, y, test_size=0.2, random_state=42)

X_train_75, X_test_25, y_train_75, y_test_25 = train_test_split(X, y, test_size=0.25, random_state=42)

def model_assess(model, title = "Default"):
    model.fit(X_train_70, y_train_70)
    preds = model.predict(X_test_30)
    print('Accuracy', title, ':', round(accuracy_score(y_test_30, preds), 5), '\n')

from sklearn.metrics import confusion_matrix

models = {
    'KNeighborsClassifier': KNeighborsClassifier(n_neighbors=19),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(n_estimators=1000, max_depth=10, random_state=0),
    'Support Vector Machine': SVC(kernel='rbf')
}

# Store results
results = {
    'Model': [],
    'Accuracy': [],
    'Precision': [],
    'Recall': [],
    'F1 Score': []
}

from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

# Train models and calculate metrics
for name, model in models.items():
    model.fit(X_train_70, y_train_70)
    y_pred = model.predict(X_test_30)
    accuracy = accuracy_score(y_test_30, y_pred)
    precision = precision_score(y_test_30, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test_30, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test_30, y_pred, average='weighted', zero_division=0)
    confusion_matr = confusion_matrix(y_test_30, y_pred) #normalize = 'true'
    plt.figure(figsize = (10, 6))
    sns.heatmap(confusion_matr, cmap="Blues", annot=True,
                xticklabels = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"],
              yticklabels=["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]);
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()
    results['Model'].append(name)
    results['Accuracy'].append(accuracy)
    results['Precision'].append(precision)
    results['Recall'].append(recall)
    results['F1 Scorce'].append(f1)

# Convert results to DataFrame for better formatting
df_results = pd.DataFrame(results)

# Print results in matrix form
print(df_results)

from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

# Train models and calculate metrics
for name, model in models.items():
    model.fit(X_train_80, y_train_80)
    y_pred = model.predict(X_test_20)
    accuracy = accuracy_score(y_test_20, y_pred)
    precision = precision_score(y_test_20, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test_20, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test_20, y_pred, average='weighted', zero_division=0)
    confusion_matr = confusion_matrix(y_test_20, y_pred) #normalize = 'true'
    plt.figure(figsize = (10, 6))
    sns.heatmap(confusion_matr, cmap="Blues", annot=True,
                xticklabels = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"],
              yticklabels=["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]);
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()
    results['Model'].append(name)
    results['Accuracy'].append(accuracy)
    results['Precision'].append(precision)
    results['Recall'].append(recall)
    results['F1 Scorce'].append(f1)

# Convert results to DataFrame for better formatting
df_results = pd.DataFrame(results)

# Print results in matrix form
print(df_results)

from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

# Train models and calculate metrics
for name, model in models.items():
    model.fit(X_train_75, y_train_75)
    y_pred = model.predict(X_test_25)
    accuracy = accuracy_score(y_test_25, y_pred)
    precision = precision_score(y_test_25, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test_25, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test_25, y_pred, average='weighted', zero_division=0)
    confusion_matr = confusion_matrix(y_test_25, y_pred) #normalize = 'true'
    plt.figure(figsize = (10, 6))
    sns.heatmap(confusion_matr, cmap="Blues", annot=True,
                xticklabels = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"],
              yticklabels=["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]);
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()
    results['Model'].append(name)
    results['Accuracy'].append(accuracy)
    results['Precision'].append(precision)
    results['Recall'].append(recall)
    results['F1 Scorce'].append(f1)

# Convert results to DataFrame for better formatting
df_results = pd.DataFrame(results)

# Print results in matrix form
print(df_results)

"""80-20               Model  Accuracy  Precision    Recall  F1 Score
0    KNeighborsClassifier  0.831331   0.836349  0.831331   0.831210
1           Decision Tree  0.649149   0.647239  0.649149   0.647419
2           Random Forest  0.816817   0.817608  0.816817   0.814492
3  Support Vector Machine  0.758759   0.756017  0.758759   0.755317

70-30               Model  Accuracy  Precision    Recall  F1 Score
0    KNeighborsClassifier  0.805806   0.813365  0.805806   0.806268
1           Decision Tree  0.637638   0.639308  0.637638   0.637632
2           Random Forest  0.814147   0.816764  0.814147   0.812406
3  Support Vector Machine  0.754087   0.751228  0.754087   0.751084

75-25               Model  Accuracy  Precision    Recall  F1 Score
0    KNeighborsClassifier  0.816653   0.823284  0.816653   0.816941
1           Decision Tree  0.636910   0.637430  0.636910   0.636392
2           Random Forest  0.814652   0.815611  0.814652   0.812238
3  Support Vector Machine  0.751401   0.748492  0.751401   0.748239



"""

labelencoder = LabelEncoder()

y_train_70 = labelencoder.fit_transform(y_train_70)
y_test_30 = labelencoder.transform(y_test_30)
len(labelencoder.classes_)

y_train_80 = labelencoder.fit_transform(y_train_80)
y_test_20 = labelencoder.transform(y_test_20)

y_train_75 = labelencoder.fit_transform(y_train_75)
y_test_25 = labelencoder.transform(y_test_25)

scaler = StandardScaler() # Standardize features by removing the mean and scaling to unit variance.
X_train_70 = scaler.fit_transform(X_train_70)
X_test_30 = scaler.transform(X_test_30)

scaler = StandardScaler() # Standardize features by removing the mean and scaling to unit variance.
X_train_80 = scaler.fit_transform(X_train_80)
X_test_20 = scaler.transform(X_test_20)

scaler = StandardScaler() # Standardize features by removing the mean and scaling to unit variance.
X_train_75 = scaler.fit_transform(X_train_75)
X_test_25 = scaler.transform(X_test_25)

# Define the parameter distribution for SVM
param_dist_svm = {
    'C': loguniform(1e-4, 1e+1),  # Narrower range for C
    'kernel': ['linear', 'rbf'],  # Only linear and RBF kernels
    # 'gamma': loguniform(1e-4, 1e-3)  # Consider removing if using a linear kernel
}

# Create the SVM classifier and randomized search object
svm = SVC(random_state=42)
random_search_svm = RandomizedSearchCV(
    svm, param_distributions=param_dist_svm, n_iter=50,  # Reduced number of iterations
    scoring='accuracy', n_jobs=-1, random_state=42  # Use all available cores
)
# Fit the randomized search to the data
random_search_svm.fit(X_train_70, y_train_70)

# Evaluate the SVM model with the best parameters on the test set
best_svm = random_search_svm.best_estimator_
y_pred_svm = best_svm.predict(X_test_30)

# Evaluate the SVM model on the training set
y_train_70_pred_svm = best_svm.predict(X_train_70)
train_accuracy_svm = accuracy_score(y_train_70, y_train_70_pred_svm)
test_accuracy_svm = accuracy_score(y_test_30, y_pred_svm)

print("Test Accuracy SVM:", test_accuracy_svm)
print("Train Accuracy SVM:", train_accuracy_svm)

# Define the parameter grid for the random search
param_grid = {
    'n_neighbors': randint(1, 15),  # Number of neighbors
    'weights': ['uniform', 'distance'],  # Weight function
    'p': [1, 2]  # Power parameter for the Minkowski distance metric
}

# Create the KNN classifier
knn = KNeighborsClassifier()
# Perform the random search
random_search_knn = RandomizedSearchCV(
    knn, param_distributions=param_grid, n_iter=10, cv=5, random_state=42
)
random_search_knn.fit(X_train_70, y_train_70)

# Evaluate the KNN model with the best parameters on the test set
best_knn = random_search_knn.best_estimator_
y_pred_knn = best_knn.predict(X_test_30)
test_accuracy_knn = accuracy_score(y_test_30, y_pred_knn)

# Evaluate the KNN model on the training set
y_train_70_pred_knn = best_knn.predict(X_train_70)
train_accuracy_knn = accuracy_score(y_train_70, y_train_70_pred_knn)

print("Train KNN Accuracy:", train_accuracy_knn)
print("Test KNN Accuracy:", test_accuracy_knn)

# Define the model architecture
model = Sequential()
model.add(Dense(units=256, activation='relu', input_dim=X_train_70.shape[1]))
model.add(Dropout(0.2))
model.add(Dense(units=256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=len(np.unique(y_train_70)), activation='softmax'))  # Adjusted to use np.unique for flexibility
model.summary()

# Compile the model
adam = optimizers.Adam(learning_rate=1e-4)
model.compile(optimizer=adam, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Fit the model
history = model.fit(X_train_70, y_train_70, epochs=50, batch_size=32,verbose=2,
                    validation_data=(X_test_30, y_test_30))

# Compile the model
adam = optimizers.Adam(learning_rate=1e-4)
model.compile(optimizer=adam, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Fit the model
history = model.fit(X_train_80, y_train_80, epochs=50, batch_size=32,verbose=2,
                    validation_data=(X_test_20, y_test_20))

# Compile the model
adam = optimizers.Adam(learning_rate=1e-4)
model.compile(optimizer=adam, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Fit the model
history75 = model.fit(X_train_75, y_train_75, epochs=50, batch_size=32,verbose=2,
                    validation_data=(X_test_25, y_test_25))

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test_30, y_test_30, verbose=2)
print(f"Test Accuracy: {accuracy:.4f}")

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test_20, y_test_20, verbose=2)
print(f"Test Accuracy: {accuracy:.4f}")

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test_25, y_test_25, verbose=2)
print(f"Test Accuracy: {accuracy:.4f}")

# Plot training & validation accuracy values
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

# Plot training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

plt.show()

# Plot training & validation accuracy values
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

# Plot training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

plt.show()

# Plot training & validation accuracy values
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history75.history['accuracy'], color='purple')
plt.plot(history75.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

# Plot training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(history75.history['loss'], color='purple')
plt.plot(history75.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

plt.show()

# Make predictions on the test set
y_pred = model.predict(X_test_30)
y_pred_classes = np.argmax(y_pred, axis=1)

# Confusion Matrix
confusion_matr = confusion_matrix(y_test_30, y_pred_classes) #normalize = 'true'
plt.figure(figsize = (10, 6))
sns.heatmap(confusion_matr, cmap="Blues", annot=True,
            xticklabels = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"],
           yticklabels=["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]);
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Make predictions on the test set
y_pred = model.predict(X_test_20)
y_pred_classes = np.argmax(y_pred, axis=1)

# Confusion Matrix
confusion_matr = confusion_matrix(y_test_20, y_pred_classes) #normalize = 'true'
plt.figure(figsize = (10, 6))
sns.heatmap(confusion_matr, cmap="Blues", annot=True,
            xticklabels = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"],
           yticklabels=["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]);
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Make predictions on the test set
y_pred = model.predict(X_test_25)
y_pred_classes = np.argmax(y_pred, axis=1)

# Confusion Matrix
confusion_matr = confusion_matrix(y_test_25, y_pred_classes) #normalize = 'true'
plt.figure(figsize = (10, 6))
sns.heatmap(confusion_matr, cmap="Blues", annot=True,
            xticklabels = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"],
           yticklabels=["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]);
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()