#include <iostream>
#include<map>
#include<string>
#include<fstream>

using namespace std;

int main()
{
    //key - numele, value - nrTel
    map<string, string> agenda;
    ifstream fin("aagenda.in");

    char nume[20];
    char nrTel[14];

    while(fin>>nume>>nrTel)
    {
        string numeString(nume);
        string nrTelString(nrTel);
        //cout<<numeString<<endl;

        agenda.insert(pair<string, string>(numeString, nrTelString));
    }

    map<string, string>:: iterator it;


    for(it = agenda.begin(); it!=agenda.end(); ++it)
        cout<<it->first<<" are nr de tel: "<<it->second<<endl;

   cout<<"Nume: ";
   cin>>nume;

   string numeCautat(nume);


   it= agenda.find(numeCautat);//O(log)
   if(it!= agenda.end())
    cout<<it->second;
   else
    cout<<"Persoana cautat nu se afla in agenda!";



    return 0;
}
