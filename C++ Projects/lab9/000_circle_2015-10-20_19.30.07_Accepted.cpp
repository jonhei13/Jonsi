#include<iostream>
using namespace std;


const double pi = 3.14159;
class Circle{
public:
    Circle(double x);
    double area();
    double perimeter();
    void setRadius(double rad);
    double getRadius();


private:
    double radius;
};





void circleInfo(Circle& circle) {
cout << "Area: " << circle.area() << endl;
cout << "Perimeter: " << circle.perimeter() << endl;
}

int main()
{

double radius;
cout << "Radius of circle: ";
cin >> radius;

Circle circle(radius);
circleInfo(circle);
circle.setRadius(circle.getRadius() + 1.0);
circleInfo(circle);


return 0;
}

double Circle::area(){

    return pi*radius*radius;

}
double Circle::perimeter(){

    return pi*2*radius;

}
void Circle::setRadius(double rad){

    radius = rad;

}

double Circle::getRadius(){

    return radius;

}

Circle::Circle(double x){

    radius = x;

}
