package social_network;

import clase_social_network.Post;
import clase_social_network.Profil;
import clase_social_network.SocialNetwork;
import clase_social_network.User;

import java.util.ArrayList;

public class SocialNetworkApp {
    public static void main(String[] args) {
        SocialNetwork ourNetwork = new SocialNetwork("An 2", new ArrayList<>());
        User user1 = new User("User1", "user1@utm.ro", "23", new Profil());
        Profil profil = new Profil();
        user1.setProfil(profil);
        profil.getPosts().add(new Post("Post1", "Content"));

        ourNetwork.addUser(user1);

        System.out.println(ourNetwork);
    }
}
