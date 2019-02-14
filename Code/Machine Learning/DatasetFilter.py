class Filters:
    def __init__(self , Answers , Severity):
        self.Answers = Answers
        self.Severity = Severity
    def SizeFilter(self):
        x=0
        Size = len(self.Answers)
        while x < Size:
            if len(self.Answers[x]) < 15:
                del self.Answers[x]
                del self.Severity[x]
                Size = Size-1
            else:
                x = x+1
    def DatasetBalancing(self):
        BullyingSize = 0
        NonBullyingSize = 0
        for x in self.Severity:
            if x == 0:
                NonBullyingSize = NonBullyingSize+1
            else:
                BullyingSize = BullyingSize+1
        DeleteSize = NonBullyingSize - BullyingSize
        y=0
        Size = len(self.Severity)
        while x < Size:
            if y < DeleteSize:
                if self.Severity[x] == 0:
                    del self.Severity[x]
                    del self.Answers[x]
                    Size = Size-1
                    y = y+1
                else:
                    x = x+1
            else:
                break
