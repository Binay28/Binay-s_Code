#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

// Complete the migratoryBirds function below.
int migratoryBirds(vector<int> arr) 
{ map<int,int> bird;
  map<int,int>::iterator itr,itr1;
  int max=0;
    for(int i=0;i<arr.size();i++)
    {
        //if(bird.count(arr[i]>0)){}
        if(bird.find(arr[i])!=bird.end()){ itr=bird.find(arr[i]);itr->second+=1;}
        else{bird.insert(make_pair(arr[i],1));}
    }
    itr1=bird.begin();
    for(itr=bird.begin();itr!=bird.end();itr++)
    {   if(itr==bird.begin()){max=itr->second;}
     else if (itr->second > max) {itr1 = itr;max=itr->second;} 
     else if (itr->second == max && itr->first<itr1->first) {itr1 = itr;}
    }
    return itr1->first;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string arr_count_temp;
    getline(cin, arr_count_temp);

    int arr_count = stoi(ltrim(rtrim(arr_count_temp)));

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split(rtrim(arr_temp_temp));

    vector<int> arr(arr_count);

    for (int i = 0; i < arr_count; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    int result = migratoryBirds(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
