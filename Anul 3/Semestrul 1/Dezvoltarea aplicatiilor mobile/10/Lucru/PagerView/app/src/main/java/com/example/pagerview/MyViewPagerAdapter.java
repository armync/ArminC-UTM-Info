package com.example.pagerview;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.lifecycle.Lifecycle;
import androidx.viewpager2.adapter.FragmentStateAdapter;

import java.util.ArrayList;
import java.util.List;

public class MyViewPagerAdapter extends FragmentStateAdapter {
    private List<Fragment> listFragments = new ArrayList<>();

    public MyViewPagerAdapter(@NonNull FragmentManager fragmentManager, @NonNull Lifecycle lifecycle) {
        super(fragmentManager, lifecycle);
    }

    @NonNull
    @Override

    public Fragment createFragment(int position){
        return listFragments.get(position);
    }

    @Override
    public int getItemCount() {
        return listFragments.size();
    }

    public void addFragmentToList(Fragment fragment){
        listFragments.add(fragment);
    }
}
