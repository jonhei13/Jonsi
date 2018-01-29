#include <iostream>
#include <string>
using namespace std;



const string tens[8] = {"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
const string units[19] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};


int Getinfo();
void Modulus(int& first, int& last, int index);
void displayvalueunits(int index,int last, int first);




int main(){

int first, last, index;

do{

    index = Getinfo();
    Modulus(first, last, index);
    displayvalueunits(index,first,last);

}while (index > 0 && index < 100);

}

int Getinfo(){
    int index;
    cout << "Input number: ";
    cin >> index;
    return index;


}



void Modulus(int& first, int& last, int index){
    if (index >= 20){
    last = index % 10;
    first = (index - last) / 10;
    }

}

void displayvalueunits(int index,int last, int first){

    if (index < 20 && index > 0){
        cout << units[index - 1] << endl;
    }

    else if ((index > 20 && index < 30) || (index > 30 && index < 40) || (index > 40 && index < 50) || (index > 50 && index < 60) || (index > 60
             && index < 70) || (index > 70 && index < 80) || (index > 80 && index < 90) ||(index > 90 && index < 100)){
        cout << tens[last - 2] << "-" << units[first - 1] << endl;
    }

    else if (index == 20 || index == 30 || index == 40 || index == 50 || index == 60 || index == 70 || index == 80 || index == 90){
        cout << tens[last - 2] << endl;
    }

}
