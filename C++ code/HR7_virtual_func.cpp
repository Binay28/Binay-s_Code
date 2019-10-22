class Person
{
    public:
        string name;
        int age;
        int id{};
        virtual void putdata() = 0;
        virtual void getdata() = 0;
};

class Professor : public Person
{   
    private:
    unsigned int publications;

    
    public:
        
        static int cur_id;
        Professor()
        {
            id = ++cur_id;
        }
        void putdata() override
        {
            cout << name << " " << age << " " << publications << " " << id << endl;
        }
        void getdata() override
        {
        cin >> name >> age >> publications;
        }

};

class Student : public Person
{
    private:
    int marks[6];
    int sum;
    //int id;
    

    public:
        static int cur_id;
        Student()
        {
            id = ++cur_id;
        }
        void putdata() override
        {
            cout << name << " " << age << " " << sum << " " << id << endl;
        }
        
        void getdata() override
        {
            cin >> name >> age;
            for (int i=0; i<6; i++) 
            {
                cin >> marks[i];
                sum+=marks[i];
            }        
        }
};


int Professor::cur_id = 0;
int Student::cur_id = 0;
