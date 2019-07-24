import sys 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import pandas as pd
import librosa
import numpy as np 
import pickle
import moviepy
import json

def convert_to_wav(filename):
    
    audioclip = AudioFileClip(filename)
    print('FILENAME ', filename)
    new_filename = filename.rsplit('.')[0] + '.wav'
    new_filename = new_filename.replace(':', '_')
    audioclip.write_audiofile("movies\\" + new_filename)
    return new_filename

def get_mfcc_features(filename): 
    start_time = 0
    interval = 10
    features = []
    duration = librosa.core.get_duration(filename = "movies\\" + filename)
    while (start_time + interval < duration):
        data, sample_rate = librosa.load( "movies\\" + filename, sr = None, mono = True, offset = start_time, duration = interval)
        mfcc = np.mean(librosa.feature.mfcc( y = data, sr = sample_rate, n_mfcc = 40).T,axis=0)
        features.append(mfcc)
        start_time += interval
    
    return features

def predict(features):
    with open("svm_model.pkl", "rb") as f: 
        model = pickle.load(f) 
    
    prediction_probs = model.decision_function(features)
    predictions = model.predict(features)

    return prediction_probs, predictions 

if __name__== "__main__": 
    filename = sys.argv[1]

    sliding_window_size = 6
    with open('web\\app\\utils\\timings.json','r') as f:
        timings = json.load(f)
    
    timings[filename] = []

    # filename = "song_half_Badtameez_Dil_mono.wav"

    if not filename.endswith(".wav"):
        new_filename = convert_to_wav(filename)
    else:
        new_filename = filename

    features = get_mfcc_features(new_filename) 
    prediction_probs, predictions = predict(features)
    print(prediction_probs) 
    print(predictions)

    df = pd.DataFrame(predictions) 
    df['col1'] = prediction_probs

    predictions = predictions.tolist()
    first_occurence = predictions.index(1)
    if first_occurence >= 5:
        starting_index = first_occurence - 5
    song_start = 0
    stop_time = len(predictions) * 10

    for i in range(starting_index,len(predictions)):
        
        if song_start == 0 and sum(predictions[i:i+ int(sliding_window_size)]) >= sliding_window_size/2:
            start_time = i*10
            i = first_occurence
            song_start = 1
        
        if song_start == 1 and sum(predictions[i:i + int(sliding_window_size/2)]) == 0:
            stop_time = (i + sliding_window_size/2 - 1 )*10
            timing = {'start': start_time,'stop':stop_time}
            timings[filename].append(timing)
            start_time = 0
            stop_time = len(predictions) * 10
            song_start = 0
    
    if song_start == 1:
        timing = {'start': start_time,'stop':stop_time}
        timings[filename].append(timing)

    with open('web/app/utils/timings.json','w') as f:
        json.dump(timings,f)






   # df.to_csv("predictions_2.csv")
    # sliding window algo

    # write the values in the JSON 



