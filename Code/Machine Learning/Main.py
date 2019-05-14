from PreProcessing import Pre_Processing
from FeatureExtraction import FeatureExtraction
from Processing import Processing
import pandas as pd
import socket
import _thread
import os
import sys
import firebase_admin
from firebase_admin import credentials , firestore

SendingIPS = []
SendingConnections  = []
def ListenThread(Connection , Address):
    try:
        while True:
            Message = Connection.recv(1024).decode("utf-8")

            Answers = []
            Answers.append(Message)
            Answers2 = Answers
            PreProcessing = Pre_Processing(Answers)
            Answers = PreProcessing.MainFunction()
            del Answers[0]

            Answers2 = Answers2[0]
            Features = FeatureExtraction(Answers)
            Answers = Features.Test_TFIDF()
            Data = pd.DataFrame(Answers)
            Data = Data.fillna(0)
            SentimentList = Features.Sentiment()
            Data[44247] = SentimentList
            Processing_Object = Processing(Data)
            Results = Processing_Object.Testing()
            Results = str(Results[0])
            SendingConnection = None
            print(Message)
            for i in range(len(SendingIPS)):
                if Address != SendingIPS[i]:
                    SendingConnection = SendingConnections[i]
                    break
            SendThread(SendingConnection , Message , Results)
    except:
        # print("Client has Disconnected or un expected error ocurred please DEBUG!!!")
        # for i in range(len(SendingIPS)):
        #     if Address == SendingIPS[i]:
        #         Connection.close()
        #         del SendingIPS[i]
        #         print(len(SendingConnections))
        #         print(len(SendingIPS))
        #         break

        python = sys.executable
        os.execl(python, python, *sys.argv)
def SendThread(Connection , Message , Result):
    Connection.sendall(Message.encode("utf-8"))
    Connection.sendall(Result.encode("utf-8"))

def AcceptingSend(SendingSocket):
    print("Server is Waitting..")
    while True:
        Connection , Address = SendingSocket.accept()
        print(Address)
        SendingIPS.append(Address)
        SendingConnections.append(Connection)
        _thread.start_new_thread(ListenThread , (Connection , Address))
Socket = socket.socket()
Host = ""
Listeningport = 12345
Socket.bind((Host , Listeningport))
Socket.listen(0)
AcceptingSend(Socket)






