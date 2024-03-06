#include<iostream>
using namespace std;
class Punct
{
    double x,y;
public:
    Punct();
    Punct(double x,double y);


    void setX(double x);
    void setY(double y);

    friend ostream& operator<<(ostream& out,Punct ob);
};
