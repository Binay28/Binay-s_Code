#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n,k;
    cin>>n;
    vector<int>list(n);
    for(int i=0;i<n;i++)
    cin>>list[i];
    cin>>k;
    list.erase(list.begin()+k-1);
    cin>>n>>k;
    list.erase(list.begin()+n-1,list.begin()+k-1);
    cout<<list.size()<<endl;
    for(int i=0;i<list.size();i++)
    cout<<list[i]<<" ";
    return 0;
}
