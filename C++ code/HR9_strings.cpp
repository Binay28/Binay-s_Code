#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a,b;
    char swap;
    getline(cin,a);
    getline(cin,b);
    cout<<a.size()<<" "<<b.size()<<endl;
    cout<<a+b<<endl;
    swap=a[0];a[0]=b[0];b[0]=swap;
    cout<<(a+" "+b)<<endl;
    return 0;
}
