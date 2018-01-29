#include <iostream>
#include <vector>


using namespace std;

typedef int* IntPtr;

void getVector(vector<int>& Value, int& Size);
void PrintArrayEqual(IntPtr& p, vector<int> Value);
void SwapValues(IntPtr& p, int Size);
void PrintArraySwap(IntPtr& p, int Size);


int main(){
    vector<int> value;
    int Size = 0;
    getVector(value,Size);
    IntPtr p;
    p = new int[Size];
    PrintArrayEqual(p, value);
    SwapValues(p, Size);
    PrintArraySwap(p, Size);
    delete[]p;


}



void getVector(vector<int>& Value, int& Size){
    int x;
    cin >> x;
    while (x >= 0){
        if (x % 2 == 0){
            Size++;
            Value.push_back(x);
            cin >> x;
        }
        else{
            Value.push_back(x);
            cin >> x;
        }
    }
}

void PrintArrayEqual(IntPtr& p, vector<int> Value){
    int temp = 0;
    for (unsigned int i = 0; i < Value.size(); i++){
            if (Value[i] % 2 == 0){
                p[temp] = Value[i];
                cout << p[temp] << " ";
                temp++;
            }
    }
}


void SwapValues(IntPtr& p, int Size){
    int temp = 0;
    for(int i = 1; i < Size; i = i+2){
        temp = p[i-1];
        p[i-1] = p[i];
        p[i] = temp;
    }
}

void PrintArraySwap(IntPtr& p, int Size){
    cout << endl;
    for (int i = 0; i < Size; i++){
            cout << p[i] << " ";



    }


}
