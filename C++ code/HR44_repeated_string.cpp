#include <bits/stdc++.h>

using namespace std;

// Complete the repeatedString function below.
long repeatedString(string s, long n) 
{
    int count=0;
    for(int i=0;i<s.size();i++)
    {
        if(s[i]=='a'){count++;}
    }
if(n%s.size()==0)
{   
return (n/s.size())*count;
}
else
{
    int count2=0;
    for (int i = 0; i <n%s.size(); i++) 
    {
      if (s[i] == 'a') {count2++;}
    }
    return((n/s.size())*count)+count2;
}
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    long n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    long result = repeatedString(s, n);

    fout << result << "\n";

    fout.close();

    return 0;
}
//count the no. of a's in an infinite string given the string which is repeated infinite number of times
