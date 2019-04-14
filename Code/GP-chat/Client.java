package com.example.ssm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;

public class Client {
    final MainActivity mm;
    Socket S= null;
    InputStream Is;
    OutputStream Os;
    String msg="";
    BufferedReader bf;
    PrintWriter pw;
    boolean cond =false;
    public Client(MainActivity ma){
        mm=ma;
        new Thread(new Runnable() {
            @Override
            public void run() {

                    try {
                        S = new Socket("137.117.32.213", 12345);

                        Os = S.getOutputStream();
                        pw = new PrintWriter(Os, true);
                        Is = S.getInputStream();
                        bf = new BufferedReader(new InputStreamReader(Is));
                        cond = true;
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

            }
        }).start();

    }

    public void sendMessage() {
            new Thread(new Runnable() {
                @Override
                public void run() {
                    if(cond!=false) {
                        pw.println(msg);
                    }
                }
            }).start();

    }
    public void receiveMessage(){
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    while(true) {
                        if(cond!=false) {
                            String NewMessage = bf.readLine();
                            //int classification = Integer.parseInt(bf.readLine());
                            mm.receiveChatMessage(NewMessage);
                        }
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }






}