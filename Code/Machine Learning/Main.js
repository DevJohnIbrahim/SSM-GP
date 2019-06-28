var admin = require("firebase-admin");

var serviceAccount = require("./AdminSDK.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "database name"
});

var db = admin.firestore();
db.collection("NeedClassification").onSnapshot(snapshot=>{
  let changes = snapshot.docChanges();
  changes.forEach(change =>{
    if (change.type == "added"){
      console.log("Message Found and is being classified now Please hold on");
      data = change.doc.data();
      var Message = data['message']
      var From = data['from']
      var Time = data['time']
      var chatID = data['ChatID']

      var spawn = require('child_process').spawn,
      py    = spawn('python', ['FirebaseCommunication.py']),
      data = [Message , From , Time , chatID],
      dataString = '';
      py.stdout.on('data', function(data){
      dataString += data.toString();
      });
      py.stdout.on('end', function(){
      console.log(dataString);
      });
      py.stdin.write(JSON.stringify(data));
      py.stdin.end();
      db.collection("NeedClassification").doc(change.doc.id).delete();
      }
      else{
      }

      })
      })
