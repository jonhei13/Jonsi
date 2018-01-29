#include <iostream>


using namespace std;



int main(){

int N = 0;                                      // Breyta fyrir inntakið
int i = 0;                                      // SKilgreini breytu fyrir fyrsta for loop
int k = 0;                                      // Skilgreini breytu fyrir nested for loop



cout << "Input an integer: ";
cin >> N;

for (i = 0; i <= N; i++){                       // Nota nested for loop til að fá rétta fjölda * við jafn marga lína sem N
                                                // gildið tekur inn.
        for (k = 1; N+1-k > i; k++ ){

        cout << "*";
        }
        cout << endl;
}

}
