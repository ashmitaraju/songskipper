from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

import pandas as pd
import pickle 
import random

data = pd.read_csv("data\\final_data.csv")

X = data.iloc[:,:-1]
Y = data['label']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state = 101,test_size  = 0.3)

SVM = SGDClassifier(random_state=42)
SVMModel = SVM.fit(X_train, Y_train)
with open("svm_model.pkl", "wb") as f: 
    pickle.dump(SVMModel, f)
    
# predictions = SVMModel.predict(X_test)

# print(accuracy_score(Y_test,predictions))
# print(classification_report(Y_test,predictions))
# print(confusion_matrix(Y_test,predictions))