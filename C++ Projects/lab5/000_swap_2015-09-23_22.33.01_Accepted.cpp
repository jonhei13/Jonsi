#include <iostream>

using namespace std;

int GetInputSize();
void getInputArr(int a[], int InputSize);
void swapFrontBack(int a[], int InputSize);
void dispayResault(const int a[],int InputSize);

const int MIN = 1;
const int MAX = 20;
const int INVALID = -1;


int main(){

int arr[MAX];
int Size = GetInputSize();
getInputArr(arr, Size);
swapFrontBack(arr,Size);
dispayResault(arr,Size);

return 0;
}

int GetInputSize(){
    int InputSize;
    cout << "Input size of array: ";
    cin >> InputSize;
    if (InputSize <= MAX && InputSize >= MIN){
        return InputSize;
    }
    else{
        cout << "Invalid size!" << endl;
        return INVALID;
        }

    return InputSize;
}

void getInputArr(int a[], int InputSize){
    if (InputSize <= MAX && InputSize >= MIN)
        cout << "Input " << InputSize << " elements: ";
    for (int i = 0; i < InputSize; i++){
        cin >> a[i];
    }

}



void swapFrontBack(int a[], int InputSize){
    int First = 0;
    int Last = 0;
    for (int i = 0;  i <= InputSize - 1 ; i++){
        if (a[i] == a[0])
            First = a[i];

    }
    for (int i = 0; i <= InputSize - 1; i++){
        if (a[i] == a[InputSize - 1] )
            Last = a[i];
    }
a[0] = Last;
a[InputSize - 1] = First;
}



void dispayResault(const int a[], int InputSize){
    for (int i = 0; i < InputSize; i++)
        cout << a[i] << " ";
    }


