#include <iostream>
#include <deque>
#include<cstdio>
using namespace std;

void printKMax(int arr[], int n, int k)
{
	//Write your code here.
    //deque<int> q;
    int max=0;
    for(int i=0;i<n-1;i++)
    {
        for(int j=i;j<i+k;j++)
        {
            if(arr[j]>max)
            {max=arr[j];}
        }
        cout<<max<<" ";
        max=0;
    }cout<<endl;
}

int main(){
  
	int t;
	cin >> t;
	while(t>0) {
		int n,k;
    	cin >> n >> k;
    	int i;
    	int arr[n];
    	for(i=0;i<n;i++)
      		cin >> arr[i];
    	printKMax(arr, n, k);
    	t--;
  	}
  	return 0;
}

