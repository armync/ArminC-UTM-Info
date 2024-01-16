package com.example.recyclerviewapp;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class MyAdaptor extends RecyclerView.Adapter{

    List<ItemModel> listItem;

    public MyAdaptor(List<ItemModel> listItem){
        this.listItem = listItem;
    }

    // insert layout for an item in RC item
    @NonNull
    @Override
    public MyHolderView onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {

        View viewItem = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_layout, parent, false);
        return new MyHolderView(viewItem);
    }

    @Override
    public void onBindViewHolder(@NonNull RecyclerView.ViewHolder holder, int position) {
        ItemModel itemCrt = listItem.get(position);
        ((MyHolderView)holder).imageView.setImageResource(itemCrt.getIdImage());
        ((MyHolderView)holder).textViewDes.setText(itemCrt.getDes());
        ((MyHolderView)holder).textViewTitle.setText(itemCrt.getTitle());
    }

    @Override
    public int getItemCount(){
        return listItem.size();
    }

    public class MyHolderView extends RecyclerView.ViewHolder {
        public ImageView imageView;
        public TextView textViewTitle;
        public TextView textViewDes;
        public MyHolderView(@NonNull View itemView) {
            super(itemView);
            imageView = itemView.findViewById(R.id.desImageView);
            textViewTitle = itemView.findViewById(R.id.titleTextView);
            textViewDes = itemView.findViewById(R.id.desTextView);
        }
    }
}
