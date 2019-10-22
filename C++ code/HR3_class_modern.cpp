#include <iostream>
#include <sstream>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/
class Student{
    private :
    int age,stand;
    string first_name,last_name;
    public :
    void set_age(int x){age=x;}
    void set_standard(int s){stand=s;}
    void set_first_name(string fname){first_name=fname;}
    void set_last_name(string lname){last_name=lname;}
    int get_age(){return age;}
    string get_last_name(){return last_name;}
    string get_first_name(){return first_name;}
    int get_standard(){return stand;}
    string to_string()
    {
        stringstream x;
        //y<<stand;x<<age;
        //string str1=x.str(),str2=y.str();
        //strcat(str1,",",first_name,",",last_name,",",str2);
        //strcat(strcat(str1, ","), strcat(first_name, ","), last_name, ",", str2);
        x<<age<<','<<first_name<<','<<last_name<<','<<stand;
        return x.str();

    }
};

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}

