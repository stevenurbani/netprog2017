package com.example.bhawiyuga.progjarapp;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class UdpClient extends AppCompatActivity {

    Button buttonYesterday, buttonToday, buttonTomorrow;
    TextView textTanggal;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_udp_client);

        // Inisialisasi komponen
        buttonYesterday = (Button) findViewById(R.id.buttonYesterday);
        buttonToday = (Button) findViewById(R.id.buttonToday);
        buttonTomorrow = (Button) findViewById(R.id.buttonTomorrow);
        textTanggal = (TextView) findViewById(R.id.textTanggal);

        buttonToday.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                new UdpClientTask(textTanggal).execute();
            }
        });


    }
}
