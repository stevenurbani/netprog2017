package com.example.bhawiyuga.progjarapp;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    Button buttonHitung = null;
    EditText editTextAngkaSatu = null;
    EditText editTextAngkaDua = null;
    TextView textHasil = null;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        buttonHitung = (Button) findViewById(R.id.buttonHitung);
        editTextAngkaSatu = (EditText) findViewById(R.id.editTextAngkaSatu);
        editTextAngkaDua = (EditText) findViewById(R.id.editTextAngkaDua);
        textHasil = (TextView) findViewById(R.id.textHasil);

        buttonHitung.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int angkaSatu = Integer.parseInt(editTextAngkaSatu.getText().toString());
                int angkaDua = Integer.parseInt(editTextAngkaDua.getText().toString());
                int hasil = angkaSatu + angkaDua;
                textHasil.setText(String.valueOf(hasil));
            }
        });

    }
}
