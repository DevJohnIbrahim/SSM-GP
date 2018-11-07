import csv
class File_Manager:
    def __init__(self, FileName):
        self.Filename = FileName

    def Read_File(self):
        f = open(self.Filename, 'rt')
        Reading = csv.reader(f)
        self.List = []
        for row in Reading:
            self.List.append(row)
        return self.List