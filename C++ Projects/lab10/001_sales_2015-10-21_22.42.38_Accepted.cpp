#include <iostream>
#include <vector>
#include <fstream>
#include <cstdlib>

using namespace std;

class Sales{
public:
    Sales(vector<double> x);
    double getAverage();
    void addSales(double AddData);

private:
    vector<double>read;
};

void readSales(vector<double>&data);



int main(){
    vector<double> data;
    readSales(data);
    Sales sales(data);

    cout.setf(ios::fixed);
    cout.setf(ios::showpoint);
    cout.precision(2);
    cout << "Average sales: " << sales.getAverage() << endl;
    sales.addSales(78.5);
    cout << "Average sales: " << sales.getAverage() << endl;

    return 0;
}


double Sales::getAverage(){
    double sum;
    for (unsigned int i = 0; i < read.size(); i++){
            sum = read[i] + sum;
    }

    double average = sum / read.size();
    return average;

}

void readSales(vector<double>&data){
    double numb;
    ifstream numbers;
        numbers.open("sales.dat");
    if (numbers.fail()){

        cout <<  "Error in opening File";
        exit(1);
    }

       while(numbers >> numb){
        data.push_back(numb);
   }
}
void Sales::addSales(double AddData){
    read.push_back(AddData);



}

Sales::Sales(vector<double>x){
    read = x;


}


