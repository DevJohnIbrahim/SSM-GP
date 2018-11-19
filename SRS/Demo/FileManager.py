import csv
import pandas
class File_Manager:
    def __init__(self , FileName):
        self.Filename = FileName
        self.userIDList = []
        self.PostList = []
        self.QuesList = []
        self.AnsList = []
        self.AskerList = []
        self.Ans1List = []
        self.Severity1List = []
        self.Bully1List = []
        self.Ans2List = []
        self.Severity2List = []
        self.Bully2List = []
        self.Ans3List  = []
        self.Severity3List = []
        self.Bully3List = []

    def Read_CSV_File(self):
        with open(self.Filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')
            for row in csv_reader:
                self.userIDList.append(row[0])
                self.PostList.append(row[1])
                self.QuesList.append(row[2])
                self.AnsList.append(row[3])
                self.AskerList.append(row[4])
                self.Ans1List.append(row[5])
                self.Severity1List.append(row[6])
                self.Bully1List.append(row[7])
                self.Ans2List.append(row[8])
                self.Severity2List.append(row[9])
                self.Bully2List.append(row[10])
                self.Ans3List.append(row[11])
                self.Severity3List.append(row[12])
                self.Bully3List.append(row[13])