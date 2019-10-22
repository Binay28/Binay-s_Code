#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    //vector<int> list;
    int n;
    cin>>n;
    vector<int>list(n);
    /*while(cin>>n)
    {   cout<<n;
        list.push_back(n);
    }*/
    for(int i=0;i<n;i++)
    cin>>list[i];
    sort(list.begin(),list.end());
    for(int i=0;i<list.size();i++)
    { cout<<list[i]<<" ";}
    return 0;
}
// the commented while loop was entering an extra element in the vector list due to which the sort function also gave wrong results
