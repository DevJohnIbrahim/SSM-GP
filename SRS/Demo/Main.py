from FileManager import File_Manager
from PreProcessing import Pre_Processing
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
