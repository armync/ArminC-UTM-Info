#include<iostream>
#include "punct.h"

using namespace std;

Punct::Punct()
{
    x=y=0;
}

Punct::Punct(double x, double y)
{
    this->x=x;
    this->y=y;
}

void Punct::setX(double x)
{
   this->x=x;
}

 void Punct::setY(double y)
 {
     this->y=y;
 }

 ostream& operator<<(ostream& out,Punct ob)
 {
     out<<"("<<ob.x<<","<<ob.y<<")"<<endl;
     return out;
 }


