#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,q,k,i;
    cin>>n>>q;
    vector<vector<int>> a(n);
    for(int i=0;i<n;i++)
    {
        cin>>k;
        a[i].resize(k);
        for(int j=0;j<k;j++)
          cin>>a[i][j];
    }
    for(int i=0;i<q;i++)
    {
        int r1,r2;
        cin>>r1>>r2;
        cout<<a[r1][r2]<<endl;
    }

    
    return 0;
}
/*
creating a multidimensional vector:
vector<vector<int>>vec(4,vector<int>(4));
writing into the vector:
vec[2][3]=10;
reading from the vector:
int a=vec[2][3];
here vec is a variable of vector<vector<int>> type and the vector is like a 4*4 matrix
*/
