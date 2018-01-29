#include <iostream>

using namespace std;

int main(){

int N  = 0;
cout << "input n: ";
cin >> N;

while (N >= 1){

    if (N % 2 == 0)
        cout << N << " is even" << endl;
    else
        cout << N << " is odd" << endl;

    N = N-1;

}
return 0;
}

