package com.example.timesbar;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.SeekBar;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ListView listView = findViewById(R.id.timesValue);
        SeekBar seekBar = findViewById(R.id.timesBar);

        int max = 20;
        int progress = 10;

        seekBar.setMax(max);
        seekBar.setProgress(10);

        ArrayList<String> timesValue = new ArrayList<>();

        for(int j=1;j<=20;j++)
            timesValue.add(Integer.toString(j*progress));

        ArrayAdapter<String> adapter = new ArrayAdapter<>(MainActivity.this,android.R.layout.simple_expandable_list_item_1, timesValue);

        listView.setAdapter(adapter);

        seekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                int timesNumber;

                timesNumber = progress;

                Toast.makeText(MainActivity.this, "Value" + Integer.toString(progress), Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });
    }
}
