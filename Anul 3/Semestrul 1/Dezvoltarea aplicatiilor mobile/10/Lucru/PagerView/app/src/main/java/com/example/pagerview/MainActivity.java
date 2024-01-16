package com.example.pagerview;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager2.widget.ViewPager2;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    ViewPager2 viewPager2;
    MyViewPagerAdapter myAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        viewPager2 = findViewById(R.id.viewPager2);

        myAdapter = new MyViewPagerAdapter(getSupportFragmentManager(), getLifecycle());
        myAdapter.addFragmentToList(new Fragment1());
        myAdapter.addFragmentToList(new Fragment2());
        myAdapter.addFragmentToList(new Fragment3());

        viewPager2.setOrientation(ViewPager2.ORIENTATION_HORIZONTAL);
        viewPager2.setAdapter(myAdapter);
   }
}