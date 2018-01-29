#include <iostream>


using namespace std;


class Time{
public:
    Time();
    Time(int hour, int minu, int sec);
    friend istream& operator >> (istream& ins, Time& t);
    friend ostream& operator << (ostream& outs, const Time& t);
    friend Time operator - (const Time& t, const Time& t2);
    friend Time operator + (const Time& t, const Time& t2);
    friend bool operator < (const Time& t, const Time& t2);

private:

    void normalize();
    int seconds;
    int minutes;
    int hours;
};


void Time::normalize()
{
    int s = seconds;
    int m = minutes;
    int h = hours;
    while(s < 0)
    {
        s += 60;
        m--;
    }
    while(m < 0)
    {
        m += 60;
        h--;
    }
    while(h < 0)
    {
        h = h + 24;
    }
    seconds = s % 60;
    minutes = (m + s/60) % 60;
    hours = (h + m/60 + s/3600) % 24;
}
int main()
{
    Time t1, t2, t3, t4;
    cin >> t1;
    cin >> t2;
    cin >> t3;
    cout << "Time1: " << t1;
    cout << "Time2: " << t2;
    cout << "Time3: " << t3;
    t4 = t1 + t2;
    cout << "Time4: " << t4;
    t1 = t3 - t4;
    cout << "Time1: " << t1;
    if (t1 < t3)
        cout << "Time1 < Time3" << endl;
    else
        cout << "Time3 >= Time1" << endl;
    Time t5 = t2 + Time(0,0,1);

    if (t5 < t2)
        cout << "Time5 < Time2" << endl;
    else
        cout << "Time5 >= Time2" << endl;
    cout << "Almost midnight: " << Time(0,0,0) - Time(0,0,1) << endl;

    return 0;

}

Time :: Time(){
   seconds = 0;
   minutes = 0;
   hours = 0;
}

Time :: Time(int hour, int minu, int sec){
    seconds = sec;
    minutes = minu;
    hours = hour;
    normalize();
}

istream& operator >>(istream& ins, Time& t){

    ins >> t.hours >> t.minutes >> t.seconds;
    t.normalize();
    return ins;
}
ostream& operator <<(ostream& outs, const Time& t){
    if (t.hours < 10){
        outs << "0" << t.hours;
    }
    else{
        outs << t.hours;
    }
    outs << ":";
    if (t.minutes < 10){
        outs << "0" << t.minutes;
    }
    else{
        outs << t.minutes;
    }
    outs << ":";
    if (t.seconds < 10){
        outs << "0" << t.seconds << endl;
    }
    else{
        outs << t.seconds << endl;
    }
    return outs;

}
Time operator - (const Time& t, const Time& t2){
    Time temp;
    temp.hours = (t.hours - t2.hours);
    temp.minutes =  (t.minutes - t2.minutes);
    temp.seconds =  (t.seconds - t2.seconds);
    temp.normalize();
    return temp;

}
Time operator + (const Time& t, const Time& t2){
    Time temp;
    temp.hours = (t.hours + t2.hours);
    temp.minutes = (t.minutes + t2.minutes);
    temp.seconds = (t.seconds + t2.seconds);
    temp.normalize();
    return temp;

}

bool operator < (const Time& t, const Time& t2){

/*
    if (t.hours < t2.hours)
        return true;
    else if (t.hours < t2.hours && t.minutes < t2.minutes)
        return true;
    else if (t.hours < t2.hours && t.minutes < t2.minutes && t.seconds < t2.seconds)
        return true;
    return false;
    */
    // VILLA I NORMALIZED T5 mun taka gildið 23.00.00 ef t2 er 23.59.59 og þess vegna þarf ég
    // að fara í þessa púslulausn!!! :)

    int hours = 60*60*t.hours;
    int minutes = 60*t.minutes;
    int total = hours + minutes;
    int hours2   = 60*60*t2.hours;
    int minutes2 = 60*t2.minutes;
    int total2 = hours2+minutes2;
    if (total < total2)
        return true;
    return false;




}
