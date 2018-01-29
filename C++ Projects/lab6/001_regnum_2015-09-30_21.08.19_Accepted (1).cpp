#include <iostream>
#include <string>

using namespace std;


string PromptInput();

void SortingRegistration(string& str,string& Faculty, string& Course,string& Campus,string& Registered_year);
void DisplayRegistration(string Faculty, string Course,string Campus,string Registered_year);


int main(){
    string str = PromptInput();
    string Faculty, Course, Campus, Registered_year;

    SortingRegistration(str,Faculty, Course, Campus, Registered_year);
    DisplayRegistration(Faculty, Course, Campus, Registered_year);

}

string PromptInput(){
    string str;
    cin >> str;
    return str;

}
void SortingRegistration(string& str,string& Faculty, string& Course,string& Campus,string& Registered_year){

int x;

    x = str.find("/");
    Faculty = str.substr(0,x);
    str.erase(0,x+1);

    x = str.find("/");
    Course = str.substr(0,x);
    str.erase(0,x+1);

    x = str.find("/");
    Campus = str.substr(0,x);
    str.erase(0,x+1);

    x = str.find(".");
    str.erase(0,x+1);
    Registered_year = str;


}
void DisplayRegistration(string Faculty, string Course,string Campus,string Registered_year){

    cout << "Registered_year: " << Registered_year << endl;
    cout << "Campus: " << Campus << endl;
    cout << "Course: " << Course << endl;
    cout << "Faculty: " << Faculty << endl;


}

