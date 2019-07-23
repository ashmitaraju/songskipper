import librosa
import pandas as pd
import numpy as np
import os
from sklearn import preprocessing
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression as LR
from sklearn.model_selection import train_test_split
import seaborn as sns

# sns.set(style="white")
# sns.set(style="whitegrid", color_codes=True)
#to trim use offset and duration parameter, both is in seconds
#first_parameter is filename path relative to current directory; should always have extension  
count = 0
mfccs = []
interval_length = 10
interval = interval_length
for filename in os.listdir("MoreDialogues\\"):
    # filename = filename.replace(" ", "_")
    start_time = 0
    print(filename)
    duration = librosa.core.get_duration(filename = "MoreDialogues\\" + filename)
    while (start_time + interval < duration):
        data, sample_rate = librosa.load( "MoreDialogues\\" + filename, sr = None, mono = True, offset = start_time, duration = interval_length)
        mfcc = np.mean(librosa.feature.mfcc( y = data, sr = sample_rate, n_mfcc = 40).T,axis=0)
        mfccs.append(mfcc)
        start_time += interval_length
        
pd.DataFrame(mfccs).to_csv("mfccs_dialogues.csv", index=False)

# MusicData = pd.read_csv('music_data.csv')
# MusicData['label'] = 1

# SpeechData = pd.read_csv('mfccs_dialogues.csv')
# SpeechData['label'] = 0

# TrainData = pd.concat([MusicData, SpeechData])

# TrainData.to_csv('Data.csv')

# X_train,y_train,X_test,y_test = train_test_split(TrainData,test_size = 0.3)
#print(mfccs)
# mfccs = np.mean(librosa.feature.mfcc( y = data, sr = sample_rate, n_mfcc=80).T,axis=0)
# logit_model=LR()
# model = logit_model.fit(X,y)
# result = model.predict(testing_data)
# print(result.summary2())


