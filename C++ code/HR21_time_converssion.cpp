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
      }
    if(s[8]=='P' || s[8]=='p')
    {
        
    }

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
