#include <iostream>

using namespace std;

int main(){

int N = 0;
int N_initial = 1;
double scores = 0;
double total = 0;
double sum_total = 0;
double sum_scores = 0;

cout.setf(ios::fixed);                              // to specify fixed point notation.
cout.setf(ios::showpoint);                          // shows decimel number.
cout.precision(2);                                  // So it would be able to print out with 2 decimel number.




cout << "How many exercises to input: ";
cin >> N;
if (N < 1)
    cout << "Input at least one exercise!" << endl; // program stops if user enter below 1 or a int not number.
else{                                               //everything inside the else loop and calculates the program.
    do{
    cout << endl;
    cout << "Score received for exercise " << N_initial << ": ";
    cin >> scores;
    cout << "Total points possible for exercise " << N_initial << ": ";
    cin >> total;

    sum_scores += scores;
    sum_total += total;
    N_initial++;

    }while (N_initial <= N);

    cout << endl;
    cout << "Your total is "
    << sum_scores
    << " out of "
    << sum_total
    << ", or "
    << (sum_scores/sum_total) * 100
    << "%.";
}
return 0;

}

