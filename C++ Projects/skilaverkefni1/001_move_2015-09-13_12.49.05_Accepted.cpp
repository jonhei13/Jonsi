/* Skilaverkefni 1
Jón Heiðar Sigmundsson
*/


#include <iostream>

using namespace std;

const int STARTPOINT = 1;
const int ENDPOINT = 10;
const char LEFT = 'l';
const char RIGHT = 'r';

int InputPosition(){

    cout << "Input an position between " << STARTPOINT << " and " << ENDPOINT << ": ";
    int position;
    cin >> position;
    return position;

}

void Instructions(){

    cout << "l - for moving left" << endl;
    cout << "r - for moving right" << endl;
    cout << "Any other letter for quitting" << endl;
}

char Readletter(){

    cout << "Input your choice: ";
    char letter;
    cin >> letter;
    return letter;


}

int NewPosition(int position){
    cout << "New position is: " << position << endl;
    return position;

}

int MovingX(char letter, int position){

        if (letter == RIGHT && position < ENDPOINT ){

            position = position + 1;
            return position;
        }

        else if (letter == LEFT && position > STARTPOINT
                 ){
            position = position - 1;
            return position;
        }
        else{
            return position;
        }
}



int main (){

    char Letter;
    int newposi;

    int position = InputPosition();

    do{
        Instructions();
        Letter = Readletter();
        newposi = MovingX(Letter, position);
        position = NewPosition(newposi);

    }while (Letter == RIGHT || Letter == LEFT);






}
