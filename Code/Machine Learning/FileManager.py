import csv
class File_Manager:
    def __init__(self , FileName):
        self.Filename = FileName
        self.PostList = []
        self.Ans1List = []
    def Read_CSV_File(self):
        # with open(self.Filename) as csv_file:
        #     csv_reader = csv.reader(csv_file, delimiter='\t')
        #     for row in csv_reader:
        #         self.PostList.append(row[1])
        #         self.Ans1List.append(row[5])
        with open("data.csv") as csv_file:
            csv_reader = csv.reader(csv_file , delimiter = ',')
            for row in csv_reader:
                self.PostList.append(row[1])
                self.Ans1List.append(row[0])
        # with open("data1.csv") as csv_file:
        #     csv_reader = csv.reader(csv_file, delimiter=',')
        #     for row in csv_reader:
        #         self.PostList.append(row[1])
        #         self.Ans1List.append(row[0])