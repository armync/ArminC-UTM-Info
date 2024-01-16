package com.example.recyclerviewapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    RecyclerView recyclerView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.recyclerView);

        ArrayList<ItemModel> list = new ArrayList<>();
        list.add(new ItemModel(R.drawable.fruit,"Fruit", "Fresh fruit from garden"));
        list.add(new ItemModel(R.drawable.vegetables,"Vegetables", "Fresh vegetables from garden"));
        list.add(new ItemModel(R.drawable.milk,"Milk", "Fresh milk"));
        list.add(new ItemModel(R.drawable.bread,"Bread", "Fresh bread"));
        list.add(new ItemModel(R.drawable.popcorn,"Popcorn", "Popcorn 'n chips"));

        LinearLayoutManager layoutManager = new LinearLayoutManager(this);
        recyclerView.setLayoutManager(layoutManager);

        MyAdaptor myAdaptor = new MyAdaptor(list);
        recyclerView.setAdapter(myAdaptor);
    }
}