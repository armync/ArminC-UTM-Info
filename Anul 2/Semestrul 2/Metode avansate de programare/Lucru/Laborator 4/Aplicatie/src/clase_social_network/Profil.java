package clase_social_network;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Profil {
    private ArrayList<Post> posts;
    //private User user;

    public Profil(ArrayList<Post> posts) {
        //compozitie
        this.posts = new ArrayList<>();
        for(int i=0; i<posts.size();i++)
            this.posts.add(posts.get(i));

    }

    public Profil() {
        this(new ArrayList<>());
    }

    public ArrayList<Post> getPosts() {
        return posts;
    }

    public void setPosts(ArrayList<Post> posts) {
        this.posts = posts;
    }

    @Override
    public String toString() {
        return "Profil{" +
                "posts=" + posts +
                '}';
    }
}
