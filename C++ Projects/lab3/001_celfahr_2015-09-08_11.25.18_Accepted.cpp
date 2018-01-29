#include <iostream>

using namespace std;

double CelsiusTofahrenheit(double celsius){

    double fahrenheit = celsius * 9/5 + 32;

    return fahrenheit;

}

int inputcelsius (){

    int celsius;
    cout << "Input maximum celsius: ";
    cin >> celsius;


    return celsius;
}


int main(){

    int celsius = 0;

    celsius = inputcelsius();


for (int i = 0; celsius >= i; i++){

    cout << i << " " << CelsiusTofahrenheit(i) << endl;

}



return 0;
}
