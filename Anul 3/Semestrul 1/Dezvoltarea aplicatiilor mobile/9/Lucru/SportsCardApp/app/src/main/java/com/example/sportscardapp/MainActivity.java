package com.example.sportscardapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    List<Sport> sportList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        RecyclerView recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        sportList = new ArrayList<>();
        sportList.add(new Sport("Football", R.drawable.football));
        sportList.add(new Sport("Pingpong", R.drawable.ping));
        sportList.add(new Sport("Basketball", R.drawable.basketball));
        sportList.add(new Sport("Tennis", R.drawable.tennis));

        CustomAdaptor customAdaptor = new CustomAdaptor(sportList);
        recyclerView.setAdapter(customAdaptor);
    }
}