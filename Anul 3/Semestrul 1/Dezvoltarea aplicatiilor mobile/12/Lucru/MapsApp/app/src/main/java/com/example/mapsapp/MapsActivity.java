package com.example.mapsapp;

import androidx.annotation.NonNull;
import androidx.fragment.app.FragmentActivity;

import android.os.Bundle;
import android.widget.Toast;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptor;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.Circle;
import com.google.android.gms.maps.model.CircleOptions;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.example.mapsapp.databinding.ActivityMapsBinding;
import com.google.android.gms.maps.model.Polyline;
import com.google.android.gms.maps.model.PolylineOptions;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mMap;
    private ActivityMapsBinding binding;
    private Marker myMarker;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        binding = ActivityMapsBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
    }

    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        LatLng bucuresti = new LatLng(44.43, 26.09);
        LatLng anywhere = new LatLng(50.00, 50.00);
        LatLng anywhere2 = new LatLng(15, 50.00);

        PolylineOptions myLineOptions = new PolylineOptions()
                .add(bucuresti)
                .add(anywhere)
                .add(anywhere2)
                ;

        Polyline myLine = mMap.addPolyline(myLineOptions);

        CircleOptions myCircleOptions = new CircleOptions()
                .radius(1000000)
                .center(bucuresti)
                .fillColor(R.color.white)
                ;

        Circle myCircle = mMap.addCircle(myCircleOptions);

        myMarker = mMap.addMarker(new MarkerOptions()
                .position(bucuresti)
                .title("Marker in Bucuresti")
                .snippet("Europe")
                .icon(BitmapDescriptorFactory.fromResource(R.drawable.car)
                ));

        mMap.addMarker(new MarkerOptions()
                .position(anywhere)
                .title("Marker anywhere")
                .snippet("Asia")
        );

        mMap.addMarker(new MarkerOptions().position(anywhere2).title("Marker anywhere").snippet("Asia"));

        mMap.moveCamera(CameraUpdateFactory.newLatLng(bucuresti));

        mMap.setOnMarkerClickListener(new GoogleMap.OnMarkerClickListener() {
            @Override
            public boolean onMarkerClick(@NonNull Marker marker) {
                Toast.makeText(MapsActivity.this, myMarker.getTitle() + myMarker.getPosition(), Toast.LENGTH_SHORT).show();
                return false;
            }
        });

        mMap.setOnMapClickListener(new GoogleMap.OnMapClickListener() {
            @Override
            public void onMapClick(@NonNull LatLng latLng) {
                Toast.makeText(MapsActivity.this, "Am apasat pe harta", Toast.LENGTH_SHORT).show();
            }
        });
    }
}