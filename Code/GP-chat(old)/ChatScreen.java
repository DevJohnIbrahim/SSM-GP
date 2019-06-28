package com.example.ssm;
import android.content.Context;
import android.database.DataSetObserver;
import android.graphics.drawable.ColorDrawable;
import android.graphics.drawable.Drawable;
import android.support.annotation.NonNull;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.AbsListView;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.PopupWindow;
import android.widget.TextView;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.EventListener;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.FirebaseFirestoreException;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;

import javax.annotation.Nullable;

import static com.example.ssm.R.drawable.rounded_shape_left;

public class ChatScreen extends AppCompatActivity
{
    
    DocumentRefrence mDocRef = FirebaseFirestore.getInstance().collection("sampledata").document("messages");
    
    private static final String TAG = "ChatActivity";

    private ChatArrayAdapter chatArrayAdapter;
    private ListView listView;
    private ListView listView1;
    private TextView friendname;
    private EditText chatText;
    private Button buttonSend;
    private FirebaseAuth Auth;
    private CollectionReference Database;
    private  String FriendName;
    private  String ChatID;
    private PopupWindow popupWindow;
    private EditText editText1;
    private Button yes, no;

    ChatScreen mm=this;
    @Override
    public void onStart()
    {
        super.onStart();
    }
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chat_screen);
        Bundle Message = getIntent().getExtras();
        FriendName = Message.getString("FriendName");
        ChatID = Message.getString("ChatID");

        friendname = findViewById(R.id.friendname);
        friendname.setText(FriendName);

        buttonSend = findViewById(R.id.buttonSend);

        listView = findViewById(R.id.listView1);

        chatArrayAdapter = new ChatArrayAdapter(getApplicationContext(), R.layout.activity_chat_singlemessage);
        listView.setTranscriptMode(AbsListView.TRANSCRIPT_MODE_ALWAYS_SCROLL);
        listView.setAdapter(chatArrayAdapter);
        chatText = (EditText) findViewById(R.id.chatText);
        Drawable drawable1 = ContextCompat.getDrawable(getApplicationContext(), rounded_shape_left);
        Drawable listDrawableBackground = listView.getBackground();


        listView.setOnItemClickListener(new AdapterView.OnItemClickListener()
        {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id)
            {
                final String selectedItem = (String) parent.getItemAtPosition(position);
                //instantiate the popup.xml layout file
                LayoutInflater layoutInflater = (LayoutInflater) ChatScreen.this.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
                View customView = layoutInflater.inflate(R.layout.popup, null);

                yes = (Button) customView.findViewById(R.id.yes);
                no = (Button) customView.findViewById(R.id.No);

                //instantiate popup window
                popupWindow = new PopupWindow(customView, AbsListView.LayoutParams.WRAP_CONTENT, AbsListView.LayoutParams.WRAP_CONTENT);
                if (drawable1.equals(listDrawableBackground))
                {
                    popupWindow.showAtLocation(listView, Gravity.CENTER, 0, 0);
                }
                //display the popup window

                yes.setOnClickListener(new View.OnClickListener()
                {
                    @Override
                    public void onClick(View v)
                    {
                        popupWindow.dismiss();
                    }
                });


                no.setOnClickListener(new View.OnClickListener()
                {
                    @Override
                    public void onClick(View v)
                    {

                        if (selectedItem.contains("This is Cyberbullying"))
                        {
                            String Message = selectedItem.getText().toString();
                            Map<String, Object> dataToSave = new HashMap<String, Object>();
                            dataToSave.put("Non-Cyberbullying", Message);

                            mDocRef.set(dataToSave).addOnSuccessListener(new OnSuccessListener<Void>() {
                                @Override
                                public void onSuccess(Void aVoid) {
                                    Log.d("Message", "Message has been saved");
                                }
                            }).addOnFailureListener(new OnFailureListener() {
                                @Override
                                public void onFailure(@NonNull Exception e) {
                                    Log.d("Message", "Message was not saved");
                                }
                            });
                            //hatotha fe msh non cyberbullying
                        }
                        else
                        {
                            String Message = selectedItem.getText().toString();
                            Map<String, Object> dataToSave = new HashMap<String, Object>();
                            dataToSave.put("Cyberbullying", Message);

                            mDocRef.set(dataToSave).addOnSuccessListener(new OnSuccessListener<Void>() {
                                @Override
                                public void onSuccess(Void aVoid) {
                                    Log.d("Message", "Message has been saved");
                                }
                            }).addOnFailureListener(new OnFailureListener() {
                                @Override
                                public void onFailure(@NonNull Exception e) {
                                    Log.d("Message", "Message was not saved");
                                }
                                popupWindow.dismiss();
                            });
                        }

                        //close the popup window on button click
                        yes.setOnClickListener(new View.OnClickListener()
                        {
                            @Override
                            public void onClick(View v)
                            {
                                popupWindow.dismiss();
                            }
                        });

                    }

                });

                buttonSend.setOnClickListener(new View.OnClickListener()
                {
                    @Override
                    public void onClick(View arg0)
                    {
                        String message = chatText.getText().toString();
                        if (!message.isEmpty())
                        {
                            Map<String, Object> ChatMSG = new HashMap<String, Object>();
                            ChatMSG.put("from", Auth.getUid());
                            ChatMSG.put("message", message);
                            Date date = new Date();
                            String CurrentDate = date.toString();
                            ChatMSG.put("time", CurrentDate);
                            ChatMSG.put("ChatID", ChatID);
                            chatText.setText("");
                            Database = FirebaseFirestore.getInstance().collection("NeedClassification");
                            Database.add(ChatMSG).addOnSuccessListener(new OnSuccessListener<DocumentReference>()
                            {
                                @Override
                                public void onSuccess(DocumentReference documentReference)
                                {
                                    Log.d(TAG, "Message Sent");

                                }
                            }).addOnFailureListener(new OnFailureListener()
                            {
                                @Override
                                public void onFailure(@NonNull Exception e)
                                {
                                    Log.w(TAG, "Message was not sent", e);
                                }
                            });

                        }
                    }
                });

                getchat();

            }
        });

        private void getchat()
        {
            Auth =FirebaseAuth.getInstance();
            Database = FirebaseFirestore.getInstance().collection("Chat/"+ChatID+"/chating");
            Database.orderBy("time").addSnapshotListener(   new EventListener<QuerySnapshot>()
            {
                @Override
                public void onEvent(@Nullable QuerySnapshot queryDocumentSnapshots, @Nullable FirebaseFirestoreException e)
                {
                    chatArrayAdapter = new ChatArrayAdapter(getApplicationContext(), R.layout.activity_chat_singlemessage);
                    listView.setTranscriptMode(AbsListView.TRANSCRIPT_MODE_ALWAYS_SCROLL);
                    listView.setAdapter(chatArrayAdapter);
                    chatArrayAdapter.registerDataSetObserver(new DataSetObserver()
                    {
                        @Override
                        public void onChanged()
                        {
                            super.onChanged();
                            listView.setSelection(chatArrayAdapter.getCount() - 1);
                        }
                    });

                    if (!queryDocumentSnapshots.isEmpty())
                    {

                        for (final QueryDocumentSnapshot document : queryDocumentSnapshots)
                        {
                            String senderid = document.getString("from");
                            String message = document.getString("message");
                            String Class = document.getString("Class");
                            if (Class.equals("0")) {
                                message = message;
                            } else {
                                message = "(This is Cyberbullying)" + " " + message;
                            }
                            if (senderid.equals(Auth.getUid())) {
                                chatArrayAdapter.add(new ChatMessage(false, message));
                            } else {
                                chatArrayAdapter.add(new ChatMessage(true, message));
                            }
                        }
                    }

                    else if (e != null)
                    {
                        Log.w(TAG, "Got exception", e);
                    }
                }
            });
        }
    }

}
