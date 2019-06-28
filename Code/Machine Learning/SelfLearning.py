import firebase_admin
from firebase_admin import firestore , credentials
import pandas as pd
cred = credentials.Certificate("ssmproject-61dec-firebase-adminsdk-op5bp-d525c0a76e.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

UserFeedBack = db.collection("UserFeedback")
Messages = []
NeededClassification = []
DocumentID = []
RejectedDocumentID = []
Docs = UserFeedBack.stream()
print("Please Check the Following Messages and then Press Y/N to accept it or decline it to be retrained in the Classifier")
for Doc in Docs:
    data = Doc.to_dict()
    Message = ""
    if "(This is Cyberbullying) " in data['Message']:
        Message = data['Message'].replace("(This is Cyberbullying) " , "")
        print(Message+"     "+"Needs To be Classified As: "+data['UserRating'])
    else:
        Message = data['Message']
        print(Message+"     "+"Needs To be Classified As: "+data['UserRating'])
    choice = input()
    if choice == "y" or choice == "Y":
        Messages.append(Message)
        NeededClassification.append(data["UserRating"])
        DocumentID.append(Doc.id)
    else:
        RejectedDocumentID.append(Doc.id)
for i in range(len(NeededClassification)):
    if NeededClassification[i] == "NotCyberbullying":
        NeededClassification[i] = 0
    elif NeededClassification[i] == "Cyberbullying":
        NeededClassification[i] = 1
NeedClassification = pd.DataFrame(Messages)
NeedClassification[1] = NeededClassification
NeedClassification.to_csv("NewDataset.csv", mode="a", header=False)
for i in DocumentID:
    Deleteing = db.collection("UserFeedback").document(i)
    Deleteing.delete()
for i in RejectedDocumentID:
    Deleteing = db.collection("UserFeedback").document(i)
    Deleteing.delete()
