//DISPLAY 7.12 Sorting an Array
//Tests the procedure sort.
#include <iostream>
using namespace std;

const int MAX_SIZE = 20;

void fillArray(int a[], int size, int& numberUsed);
// Fills the array a[] with data for a[0] through a[numberUsed -1].
// size is the size of the array

void sort(int a[], int numberUsed);
//sorts the array a[] such that a[0] <= a[1] <= ... <= a[numberUsed - 1].

void swapValues(int& v1, int& v2);
//Interchanges the values of v1 and v2.

//Returns the index i such that a[i] is the smallest of the values
//a[startIndex], a[startIndex + 1], ..., a[numberUsed - 1].

void displayArray(const int a[], int numberUsed);
//Displays the contents of the array

int main( )
{


    int sampleArray[MAX_SIZE], numberUsed;

    fillArray(sampleArray, MAX_SIZE, numberUsed);
    sort(sampleArray, numberUsed);
    cout << "In sorted order the numbers are:\n";
    displayArray(sampleArray, numberUsed);

    return 0;
}

void fillArray(int a[], int size, int& numberUsed)
{
    cout << "Enter up to " << size << " nonnegative whole numbers.\n"
         << "Mark the end of the list with a negative number.\n";
    int next, index = 0;
    cin >> next;
    while ((next >= 0) && (index < size))
    {
        a[index] = next;
        index++;
        cin >> next;
    }
    numberUsed = index;
}

void sort(int a[], int numberUsed)
{
    int b;
    int temp;
    for (int index = 1; index < numberUsed; index++){
        b = index;

        while(b > 0 && a[b-1] > a[b]){

            temp = a[b];
            a[b] = a[b-1];
            a[b-1] = temp;

            b--;
        }
        for (int index = 0; index < numberUsed; index++)
                cout << a[index] << " ";
                cout << endl;

    }

}





void displayArray(const int a[], int numberUsed)
{
    for (int index = 0; index < numberUsed; index++)
        cout << a[index] << " ";
    cout << endl;
}





