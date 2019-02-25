from __future__ import absolute_import, division, print_function
import keras.backend as K
import numpy as np
import csv
from FileManager import File_Manager
from DatasetFilter import Filters
from PreProcessing import Pre_Processing
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras

from sklearn.feature_extraction.text import CountVectorizer
def read_csv_file(filename):
    Class = []
    Data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            Class.append(row[0])
            Data.append(row[1])

    return Data,Class

Data,Class = read_csv_file("data.csv")
del(Data[0])
del(Class[0])
Data=np.array(Data)
Class=np.array(Class)

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
Answers=np.concatenate((Answers, Data), axis=0)
Severity=np.concatenate((Severity, Class), axis=0)

#Pre Processing
PreProcessing = Pre_Processing(Answers)
Answers = PreProcessing.MainFunction()
del Answers[0]
print(Answers)
print(Severity)

#model = word2vec.Word2Vec(Answers, min_count=1)
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(Answers).toarray()

training_data, testing_data, training_class, testing_class = train_test_split(x, Severity, test_size=0.40, random_state=10)

training_data=keras.preprocessing.sequence.pad_sequences(training_data, maxlen=256, padding='post', truncating='pre')
testing_data=keras.preprocessing.sequence.pad_sequences(testing_data, maxlen=256, padding='post', truncating='pre')
print(training_data.shape)

model = keras.Sequential()
model.add(keras.layers.Embedding(10000,64))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation=tf.nn.relu))
model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))


def mean_pred(y_true, y_pred):
    return K.mean(y_pred)

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy', mean_pred])
history = model.fit(training_data,
                    training_class,
                    epochs=20,
                    batch_size=512,
                    validation_data=(testing_data, testing_class),
                    verbose=1)
results = model.evaluate(testing_data, testing_class)
model.metrics

print(results)
