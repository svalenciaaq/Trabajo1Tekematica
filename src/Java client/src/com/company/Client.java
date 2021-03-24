package com.company;

import jdk.nashorn.internal.ir.debug.JSONWriter;
import jdk.nashorn.internal.parser.JSONParser;

import java.io.*;
import java.net.Socket;
import java.util.Arrays;
import java.util.Base64;

public class Client {

    private Socket client;

    private BufferedReader input;
    private PrintWriter output;

    private String userName;

    private final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    public Client(){ }

    public void logInfo() throws Exception{
        //accept connection from client
        client = new Socket("localhost", 1233);
        input = new BufferedReader(new InputStreamReader(client.getInputStream()));

        //open printwriter for writing data to client
        output = new PrintWriter(new OutputStreamWriter(client.getOutputStream()));

        String line;

        System.out.println("User:");
        String user = reader.readLine();
        userName = user;
        String encodedUser = Base64.getEncoder().encodeToString(user.getBytes());
        output.write(encodedUser);
        output.flush();
        System.out.println("password:");
        String password = reader.readLine();
        String encodedPassword = Base64.getEncoder().encodeToString(password.getBytes());
        output.write(encodedPassword);
        output.flush();

        if((line = input.readLine()) != null) {
            if(line.contains("Login Failed")){
                System.out.println("User or password wrong");
                logInfo();
            }
        }
    }

    private String encodeString(String msg){
        return Base64.getEncoder().encodeToString(msg.getBytes());
    }
    private String decodeString(String msg){ return String.valueOf(Base64.getDecoder().decode(msg)); }

    public boolean process() throws IOException {
        System.out.println("Actions");
        System.out.println("Choose an Option");
        System.out.println("QUEUE OPTION");
        System.out.println("1. Create a queue ");
        System.out.println("2. Delete a qeueu ");
        System.out.println("3. Show my queues ");
        System.out.println("4. Show all queues");
        System.out.println("5. Send message to a queue");
        System.out.println("6. Pull message from a queue");
        System.out.println("7. Subscribe a queue");
        System.out.println("8. Create a chanel ");
        System.out.println("9. Delete a chanel");
        System.out.println("10. Show my chanels");
        System.out.println("11. Show all chanels");
        System.out.println("12. Send message to a chanel");
        System.out.println("13. Subscribe a chanel");
        System.out.println("14. Close Connection");

        String body = "";
        boolean result = true;
        System.out.println("Enter an option");
        String action = reader.readLine();
        if(action.equals("1")){
            System.out.println("Create Queue");
            System.out.println("Enter Queue Name:");
            String namequeue = reader.readLine();
            body = "{ \"cmd\": \"queue\", \"namequeu\": \""+ namequeue +"\" }";
            System.out.println(body);
            output.println(encodeString(body));
            output.flush();
            String response = input.readLine();
            if(response.contains("data")){
                System.out.println("No messages found in queue \"" + namequeue + "\"!");
            }else{
                System.out.println(response);
            }
            result = true;
        }

        if(action.equals("2")){
            System.out.println("Delete Queue");
            System.out.println("Enter Queue Name:");
            String namequeue = reader.readLine();
            body = " { \"cmd\": \"delete\", \"namequeu\": \""+ namequeue +"\" }";
            System.out.println("what i send \r\n" + body);
            output.println(encodeString(body));
            output.flush();
            String response = decodeString(input.readLine());
            if(response.equals("")){
                System.out.println("No messages found in queue \"" + namequeue + "\"!");
            }else{
                System.out.println("response:" + response);
            }
            result = true;
        }

        if(action.equals("3")){
            System.out.println("Listing my queues");
            body = "{ \"cmd\": \"showmq\" }";
            System.out.println("what i send \r\n" + body);
            output.println(encodeString(body));
            output.flush();
            String encodedReponse = input.readLine();
            String response = decodeString(encodedReponse);
            System.out.println("encoded"+encodedReponse);
            System.out.println("normal"+response.toString());
            result = true;
        }

        if(action.equals("4")){
            System.out.println("Showing all queues");
            body = "{ \"cmd\": \"showaq\" }";
            System.out.println("what i send \r\n" + body);
            output.println(encodeString(body));
            output.flush();
            String encodedReponse = input.readLine();
            String response = decodeString(encodedReponse);
            System.out.println("encoded"+encodedReponse);
            System.out.println("normal"+response.toString());
            result = true;
        }

        if(action.equals("5")){
            System.out.println("Send message to Queue");
            System.out.println("Enter Queue Name:");
            String namequeue = reader.readLine();
            System.out.println("Enter Message:");
            String message = reader.readLine();
            body = " { \"cmd\": \"sendq\", \"namequeu\": \""+ namequeue +"\", \"data\": \""+ message +"\", \"name\": \""+ userName + "\"}";
            System.out.println("what i send \r\n" + body);
            output.println(encodeString(body));
            output.flush();
            String response = decodeString(input.readLine());
            if(response.equals("")){
                System.out.println("No messages found in queue \"" + namequeue + "\"!");
            }else{
                System.out.println("response:" + response);
            }
            result = true;
        }

        if(action.equals("6")){
            System.out.println("Get message from queue");
            System.out.println("Enter Queue Name:");
            String namequeue = reader.readLine();
            body = " { \"cmd\": \"pullq\", \"namequeu\": \""+ namequeue +"\" }";
            System.out.println("what i send \r\n" + body);
            output.println(encodeString(body));
            output.flush();
            String response = decodeString(input.readLine());
            if(response.equals("")){
                System.out.println("No messages found in queue \"" + namequeue + "\"!");
            }else{
                System.out.println("response:" + response);
            }
            result = true;
        }

        if(action.equals("7")){
            System.out.println("Subscribe to queue");
            System.out.println("Enter Queue Name:");
            String namequeue = reader.readLine();
            body = " { \"cmd\": \"queuesubscriber\", \"namequeu\": \""+ namequeue +"\" }";
            System.out.println("what i send \r\n" + body);
            output.println(encodeString(body));
            output.flush();
            String response = decodeString(input.readLine());
            if(response.equals("")){
                System.out.println("Could not subscribe to this queue \"" + namequeue + "\"!");
            }else{
                System.out.println("response:" + response);
            }
            result = true;
        }

        if(action.equals("8")){
            System.out.println("Create Channel");
            System.out.println("Enter Channel Name:");
            String namechannel = reader.readLine();
            body = " { \"cmd\": \"channel\", \"channel\": \""+ namechannel +"\", \"user\": \"" + userName +"}";
            System.out.println("what i send \r\n" + body);
            output.println(encodeString(body));
            output.flush();
            String response = decodeString(input.readLine());
            if(response.equals("")){
                System.out.println("Could not create this channel \"" + namechannel + "\"!");
            }else{
                System.out.println("response:" + response);
            }
            result = false;
        }

        if(action.equals("9")){
            System.out.println("Delete Channel");
            System.out.println("Enter Channel Name:");
            String namechannel = reader.readLine();
            body = " { \"cmd\": \"deletec\", \"channel\": \""+ namechannel +"\"}";
            System.out.println("what i send \r\n" + body);
            output.println(encodeString(body));
            output.flush();
            String response = decodeString(input.readLine());
            if(response.equals("")){
                System.out.println("Could not delete this channel \"" + namechannel + "\"!");
            }else{
                System.out.println("response:" + response);
            }
            result = true;
        }

        if(action.equals("10")){
            System.out.println("Showing my channels");
            body = "{ \"cmd\": \"showmc\" }";
            System.out.println("what i send \r\n" + body);
            output.println(encodeString(body));
            output.flush();
            String encodedReponse = input.readLine();
            String response = decodeString(encodedReponse);
            System.out.println("encoded"+encodedReponse);
            System.out.println("normal"+response.toString());
            result = true;
        }

        if(action.equals("11")){
            System.out.println("Showing all channels");
            body = "{ \"cmd\": \"showac\" }";
            System.out.println("what i send \r\n" + body);
            output.println(encodeString(body));
            output.flush();
            String encodedReponse = input.readLine();
            String response = decodeString(encodedReponse);
            System.out.println("encoded"+encodedReponse);
            System.out.println("normal"+response.toString());
            result = true;
        }

        if(action.equals("12")){
            System.out.println("Send message to channel");
            System.out.println("Enter Channel Name:");
            String namequeue = reader.readLine();
            System.out.println("Enter Message:");
            String message = reader.readLine();
            body = " { \"cmd\": \"sendc\", \"namequeu\": \""+ namequeue +"\", \"data\": \""+ message +"\", \"name\": \""+ userName + "\"}";
            System.out.println("what i send \r\n" + body);
            output.println(encodeString(body));
            output.flush();
            String encodedReponse = input.readLine();
            String response = decodeString(encodedReponse);
            System.out.println("response:" + response);
            result = true;
        }

        if(action.equals("13")){
            System.out.println("Subscribe to channel");
            System.out.println("Enter Channel Name:");
            String namequeue = reader.readLine();
            body = " { \"cmd\": \"subscribec\", \"namequeu\": \""+ namequeue +"\"}";
            System.out.println("what i send \r\n" + body);
            output.println(encodeString(body));
            output.flush();
            String encodedReponse = input.readLine();
            String response = decodeString(encodedReponse);
            System.out.println("response:" + response);
            result = true;
        }


        if(action.equals("14")){
            System.out.println("Closing connection");
            body = " { \"cmd\": \"close\"}";
            output.println(encodeString(body));
            output.flush();
            String encodedReponse = input.readLine();
            String response = decodeString(encodedReponse);
            System.out.println("response:" + response);
        }
        return result;
    }
}
