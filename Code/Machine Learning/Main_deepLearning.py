from __future__ import absolute_import, division, print_function
import keras.backend as K
import numpy as np
import csv

from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from FileManager import File_Manager
from DatasetFilter import Filters
from PreProcessing import Pre_Processing
from FeatureExtraction import FeatureExtraction
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras

from sklearn.feature_extraction.text import CountVectorizer


#Reading Dataset
FileManager_Object = File_Manager('Dataset.csv')
FileManager_Object.Read_CSV_File()
del FileManager_Object.AnsList[0]
del FileManager_Object.Severity1List[0]
Size = 0
for i in range(len(FileManager_Object.Severity1List)):
    if FileManager_Object.Severity1List[i] == "None":
        FileManager_Object.Severity1List[i] = 0
    elif FileManager_Object.Severity1List[i] == "n/a":
        FileManager_Object.Severity1List[i] = 0
    else:
        x = int(FileManager_Object.Severity1List[i])
        if x>0:
            FileManager_Object.Severity1List[i] = 1
        else:
            FileManager_Object.Severity1List[i] = 0
Filter = Filters(FileManager_Object.AnsList , FileManager_Object.Severity1List)
Filter.SizeFilter()
Filter.DatasetBalancing()
Answers = Filter.Answers
Severity = Filter.Severity


#Pre Processing
PreProcessing = Pre_Processing(Answers)
Answers = PreProcessing.MainFunction()
del Answers[0]


vectorizer = CountVectorizer()
x0 = vectorizer.fit_transform(Answers).toarray()

Features = FeatureExtraction(Answers)
x1 = Features.TFIDF()

x2,x3=Features.Sentiment()
x2=np.asarray(x2)
x3=np.asarray(x3)
x2=x2[:,None]
x3=x3[:,None]

Ans=np.concatenate((x0,x1,x2,x3),axis=1)
print(Ans.shape)

training_data, testing_data, training_class, testing_class = train_test_split(Ans, Severity, test_size=0.30, random_state=42)

print(training_data.shape)

model = keras.Sequential()
model.add(keras.layers.Dense(32, input_shape=(5814,)))
model.add(keras.layers.Dense(16, activation=tf.nn.relu))
model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))



def mean_pred(y_true, y_pred):
    return K.mean(y_pred)

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy', mean_pred])
history = model.fit(training_data,
                    training_class,
                    epochs=29,
                    batch_size=512,
                    validation_data=(testing_data, testing_class),
                    verbose=1)
y_pred = model.predict(testing_data)


print("Recall: ",recall_score(testing_class, y_pred.round(), average='macro'))
print("Accuracy: ",accuracy_score(testing_class, y_pred.round()))