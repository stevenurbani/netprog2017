package com.example.bhawiyuga.progjarapp;

import android.os.AsyncTask;
import android.util.Log;
import android.widget.TextView;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.UnknownHostException;

/**
 * Created by bhawiyuga on 07/03/17.
 */

public class UdpClientTask extends AsyncTask<String, Void, String> {

    TextView textHasil=null;

    public UdpClientTask(TextView text){
        this.textHasil = text;
    }

    @Override
    protected String doInBackground(String[] ip) {
        DatagramSocket sock = null;


            try {
                InetAddress inetAddress = InetAddress.getByName("10.34.8.59");
                sock = new DatagramSocket();
                String data="today";
                DatagramPacket packet = new DatagramPacket(data.getBytes(),0, data.length(),inetAddress, 7777);
                sock.send(packet);

                byte[] buffer = new byte[256];
                DatagramPacket packetTerima = new DatagramPacket(buffer,0, buffer.length);
                sock.receive(packetTerima);
                String text = new String(buffer, 0, packetTerima.getLength());
                Log.d("terima",text);
                return text;
            } catch (UnknownHostException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }


        return "";
    }

    @Override
    protected void onPostExecute(String s) {
        textHasil.setText(s);
    }
}
