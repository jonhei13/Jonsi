#include <iostream>

using namespace std;

const int PAYMENT = 50;

int main(){

    int cost = 0;
    int months = 1;
    double debt = 0;
    double paid = 0;
    double interest = 0;
    double sum_interest = 0;

    cout.setf(ios::fixed);
    cout.setf(ios::showpoint);
    cout.precision(2);


    cout << "Input the cost of the item in $: ";
    cin >> cost;
    cout << endl;
    if(cost <= 1000){
        interest = 0.015;
    }
    else{
        interest = 0.02;
    }

    debt = cost;

    do{

        paid = debt * interest;
        debt = debt - PAYMENT + paid;

        cout << "Month: "
        << months
        << ", Interest paid: "
        << paid
        << ", "
        << "Remaining debt: "
        << debt;
        cout << endl;
        months++;
        sum_interest += paid;

    }while(debt >= 0);

    cout << endl;
    cout << "Number of months: " << months - 1 << endl;
    cout << "Total interest paid: " << sum_interest << endl;

}
