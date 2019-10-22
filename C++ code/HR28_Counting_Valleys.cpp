#include <bits/stdc++.h>

using namespace std;

// Complete the countingValleys function below.
int countingValleys(int n, string s) 
{int level=0,mount=0,valley=0;bool culev;
//stringstream str(s);
//string word;
//vector<char> steps;
//for(int i=0;i<steps.size();i++){}
//while(str>>word)
for(int i=0;i<s.length();i++)
{
if(s[i]=='U' || s[i]=='u'){level++;}
else{level--;}
if(level>0){culev=1;}
else if(level<0){culev=0;}
else if(level==0)
{
    if(culev){mount++;}
    else {valley++;}
    }
}
return valley;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}
