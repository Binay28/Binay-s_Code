#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the timeConversion function below.
 */
string timeConversion(string s) 
{
    /*
     * Write your code here.
     */
     if(s[8]=='A' || s[8]=='a')
      {
        if(s[0]=='1' && s[1]=='2'){s[0]='0';s[1]='0';}
	cout<<"am";
      }
    if(s[8]=='P' || s[8]=='p')
    {
      stringstream x;
      /*string  str=s.split_string(':');
      str>>x;*/
      cout<<"pm";
    int hour=stoi(s.substr(0,2));
     if(hour!=12)
     { hour+=12;
       cout<<hour;
       //s.substr(0,2)=to_string(hour);
       x<<hour;s[0]=x.str()[0];s[1]=x.str()[1];}
    }
    cout<<s;
    return s.substr(0,8);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
