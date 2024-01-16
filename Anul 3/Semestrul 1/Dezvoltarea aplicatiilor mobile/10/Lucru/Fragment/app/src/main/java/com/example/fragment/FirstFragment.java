package com.example.fragment;

import android.content.Context;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class FirstFragment extends Fragment {
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_first, container, false);

        TextView textView = view.findViewById(R.id.txt_frag1);
        Button button = view.findViewById(R.id.btn_frag1);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(getActivity(), "This is the first fragment", Toast.LENGTH_LONG).show();
            }
        });
        return view;
    }
    @Override
    public void onAttach(@NonNull Context context) {
        Toast.makeText(context, "When the fragment is attached", Toast.LENGTH_SHORT).show();
        super.onAttach(context);
    }

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        Toast.makeText(getActivity(), "When the fragment is called", Toast.LENGTH_SHORT).show();
        super.onCreate(savedInstanceState);
    }
}