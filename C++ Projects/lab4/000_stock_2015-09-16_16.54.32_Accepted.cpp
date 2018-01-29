#include <iostream>

using namespace std;

const char YES = 'y';

int NumberOfShares(){
    int shares;
    cout << "Enter number of shares: ";
    cin >> shares;
    return shares;
}


void Price(int& dollars, int& numerator, int& denominator){

    cout << "Enter price (dollars, numerator, denominator): ";
    cin >> dollars;
    cin >> numerator;
    cin >> denominator;
}

double CalcValue(int shares, int dollars, double numerator, double denominator){

    return shares * (dollars + (numerator / denominator));
}

void Total(int shares, int dollars, int numerator, int denominator, double Calcstock){

    cout << shares
         << " shares with market price "
         << dollars
         << " "
         << numerator
         << "/"
         << denominator
         << " have value $"
         << Calcstock;


}

char KeepGoing(){
    char Go;
    cout << endl;
    cout << "Continue: ";
    cin >> Go;
    return Go;



}


int main(){
    cout.setf(ios::fixed);
    cout.setf(ios::showpoint);
    cout.precision(2);

    int shares,dollars, numerator,denominator;
    char Continue;

    do{
        shares = NumberOfShares();
        Price(dollars,numerator,denominator);
        double Calcstock = CalcValue(shares,dollars,numerator,denominator);
        Total(shares, dollars, numerator,denominator, Calcstock);
        Continue = KeepGoing();
    }while (Continue == YES);



}
