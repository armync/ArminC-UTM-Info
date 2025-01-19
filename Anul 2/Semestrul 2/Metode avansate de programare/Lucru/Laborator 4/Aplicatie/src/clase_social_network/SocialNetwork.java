package clase_social_network;

import java.util.ArrayList;

public class SocialNetwork {
    private String name;
    private ArrayList<User> listUsers;

    public SocialNetwork(String name, ArrayList<User> listUsers) {
        this.name = name;
        //compozitie
        this.listUsers = new ArrayList<>();
        for(int i=0; i<listUsers.size(); i++)
            this.listUsers.add(listUsers.get(i));
    }

    public SocialNetwork() {
        this("anonim", new ArrayList<>());
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ArrayList<User> getListUsers() {
        return listUsers;
    }

    public void setListUsers(ArrayList<User> listUsers) {
        this.listUsers = listUsers;
    }

    @Override
    public String toString() {
        return "SocialNetwork{" +
                "name='" + name + '\'' +
                ", listUsers=" + listUsers +
                '}';
    }

    public void addUser(User user)
    {
        this.listUsers.add(user);
    }

    public void deleteUser(User user)
    {
        this.listUsers.remove(user);
    }

    /*
    public User getUser(String name) {

    }
    */

}
