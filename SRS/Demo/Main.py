from FileManager import File_Manager
from PreProcessing import Pre_Processing
from FeatureExtraction import FeatureExtraction
import csv
from Processing import Processing
import numpy as np
# Executing and reading the File
FileManager_Object = File_Manager('Dataset.csv')
FileManager_Object.Read_CSV_File()

#Filling the Lists From The FileManager Object

UserIDList = FileManager_Object.userIDList
PostList = FileManager_Object.PostList
QuestionList = FileManager_Object.QuesList
AnswerList = FileManager_Object.AnsList
AskerList = FileManager_Object.AskerList
Ans1List = FileManager_Object.Ans1List
Severity1List = FileManager_Object.Severity1List
del Severity1List[0]
del Severity1List[1]
Bully1List = FileManager_Object.Bully1List
Ans2List = FileManager_Object.Ans2List
Severity2List = FileManager_Object.Severity2List
Bully2List = FileManager_Object.Bully2List
Ans3List = FileManager_Object.Ans3List
Severity3List = FileManager_Object.Severity3List
Bully3List = FileManager_Object.Bully3List
#Pre_Processing and Getting the Output From It
PreProcessing_Object = Pre_Processing(AnswerList)
AnswerList = PreProcessing_Object.MainFunction()
#Feature Extraction
FeatureExtraction_Object = FeatureExtraction(AnswerList)
TFIDFList = FeatureExtraction_Object.tfidf()
FeatureExtractionList = [[]]
for item in TFIDFList:
    x=item[0].tolist()
    FeatureExtractionList.append(item[0])

for i in range(len(Severity1List)):
    if Severity1List[i] == "None":
        Severity1List[i] = 0
    elif Severity1List[i] == "n/a":
        Severity1List[i] = 0
    else:
        x = int(Severity1List[i])
        if x>0:
            Severity1List[i] = 1
        else:
            Severity1List[i] = 0
Greatest=len(FeatureExtractionList[0])
for i in range(len(FeatureExtractionList)):
    if len(FeatureExtractionList[i])>Greatest:
        Greatest = len(FeatureExtractionList[i])
print(Greatest)
for i in range(len(FeatureExtractionList)):
    if len(FeatureExtractionList[i])<Greatest:
        for x in range(Greatest-len(FeatureExtractionList[i])):
            np.append(FeatureExtractionList[i],[0.0])
del FeatureExtractionList[0]
for i in range(len(FeatureExtractionList)):
    FeatureExtractionList[i] = FeatureExtractionList[i].tolist()
for i in range(len(FeatureExtractionList)):
    for j in range(Greatest-len(FeatureExtractionList[i])):
        FeatureExtractionList[i].append(0.0)
#Training
Processing_Object  = Processing(FeatureExtractionList,Severity1List)
Processing_Object.Processing()