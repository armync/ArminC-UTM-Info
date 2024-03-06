#include <iostream>
#include<vector>
#include"punct.h"
#include<fstream>

using namespace std;

int main()
{
    vector<Punct>vp;
    ifstream fin("puncte.in");

    int x,y;
    while(fin>>x>>y)
    {
        Punct ob(x,y);
        vp.push_back(ob);
    }

    for(int i=0;i<vp.size();i++)
        cout<<vp[i];
    return 0;
}
