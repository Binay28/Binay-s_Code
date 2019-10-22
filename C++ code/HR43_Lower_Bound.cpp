#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n,k,min=0,ind=0;
    bool f=0;
    cin>>n;
    vector<int>list(n);
    for(int i=0;i<n;i++)
    cin>>list[i];
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>k;
        min=*lower_bound(list.begin(),list.end(),k);
	f=0;
        for(int j=0;j<list.size();j++)
        {
            if(list[j]==k)
            {
                cout<<"Yes "<<j+1<<endl;
                f=1;break;
            }
            else if(list[j]-k<min && list[j]-k>0)
            {
                min=list[j]-k;
                ind=j+1;
            }
        }
        if(!f){ cout<<"No "<<ind<<endl;}
    }

    return 0;
}
