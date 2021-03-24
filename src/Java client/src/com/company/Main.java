package com.company;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Base64;

public class Main {


    public static void main(String[] args) {
        Client client = new Client();
        try{
            client.logInfo();
            boolean finish = true;
            while (finish){
                finish = client.process();
            }
        }catch (Exception e){
            e.printStackTrace();
        }
    }


}
