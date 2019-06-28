import csv
class File_Manager:
    def __init__(self):
        self.PostList = []
        self.Ans1List = []
    def Read_CSV_File(self):
        with open("NewDataset.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.PostList.append(row[1])
                self.Ans1List.append(row[2])