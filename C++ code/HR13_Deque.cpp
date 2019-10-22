#include <iostream>
#include <deque> 
#include<algorithm>
using namespace std;

void printKMax(int arr[], int n, int k)
{
	//Write your code here.
    deque<int> q;
    int max=0;
    for(int i=0;i<n;i++)
    {q.push_back(arr[i]);}
    while(q.size()>=k)
    {
    for(int i=0;i<k;i++)
    {
        /*for(int j=i;j<i+k;j++)
        {
            if(arr[j]>max)
            {max=arr[j];}
        }*/
         if(q.at(i)>max)
            {max=q.at(i);}
    }
        cout<<max<<" ";
        max=0;
        q.pop_front();
        //cout<<*max_element(arr,arr);

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

