package com.example.convertorapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.EditText;
import android.view.View;
import android.widget.Toast;


public class MainActivity extends AppCompatActivity {

    public void Converteste(View view){
        EditText valoareEditText = findViewById(R.id.valoareEditText); // leagatura cu frond end
        String valoareString = valoareEditText.getText().toString(); // string
        double valoareRON = Double.parseDouble(valoareString);

        double valoareEUR = valoareRON/4.99;
        String valoareEURstring = String.format("%.2f",valoareEUR);

        Toast.makeText(this,valoareEURstring, Toast.LENGTH_LONG).show();

        valoareEditText.setText("");
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}