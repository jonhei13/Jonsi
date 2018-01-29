#include <iostream>


using namespace std;

const int MAXMOVES = 5;
const int ROW = 3, COLUMN = 3;
const char Player1 = 'X', Player2 = 'O', DRAW = 'D';
void printOutMatrix(char TictacValues[][COLUMN]);
char InputPlayer1(char TictacValues[][COLUMN]);
char InputPlayer2(char TictacValues[][COLUMN]);
void SearchforValuePlayer1(char value, char TictacValues[][COLUMN]);
void SearchforValuePlayer2(char value, char TictacValues[][COLUMN]);
char WhoIsTheWinner(char TictacValues[][COLUMN]);
char LoopuntilWinnerIsfound(char value, char TictacValues[][COLUMN]);
void DisplayWinnerOrDraw(char winner);

int main(){
    char TictacValues[ROW][COLUMN] = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};
    char value, winner;
    printOutMatrix(TictacValues);
    value = InputPlayer1(TictacValues);
    SearchforValuePlayer1(value, TictacValues);
    printOutMatrix(TictacValues);
    value = InputPlayer2(TictacValues);
    SearchforValuePlayer2(value, TictacValues);
    printOutMatrix(TictacValues);
    winner = LoopuntilWinnerIsfound(value ,TictacValues);
    DisplayWinnerOrDraw(winner);

    return 0;
}


void printOutMatrix(char TictacValues[][COLUMN]){

    for (int i = 0; i < ROW; i ++){

        for (int j = 0; j < COLUMN; j++){
            cout << TictacValues[i][j] << " ";
        }
        cout << endl;
    }

}

char InputPlayer1(char TictacValues[][COLUMN]){
    char promptInput;
    cout << Player1 << " " << "position: ";
    cin >> promptInput;
    do{
        for (int i = 0; i < ROW; i++){
            for (int j = 0; j < COLUMN; j++){
                if (TictacValues[i][j] == promptInput && TictacValues[i][j] != Player1 && TictacValues[i][j] != Player2){
                   return promptInput;
                   break;
                }
            }
        }

        cout << "Illegal move!" << endl;
        cout << Player1 << " " << "position: ";
        cin >> promptInput;
    }while(1);
}
char InputPlayer2(char TictacValues[][COLUMN]){
    char promptInput;
    cout << Player2 << " " << "position: ";
    cin >> promptInput;
    do{
        for (int i = 0; i < ROW; i++){
            for (int j = 0; j < COLUMN; j++){
                if (TictacValues[i][j] == promptInput && TictacValues[i][j] != Player1 && TictacValues[i][j] != Player2){
                   return promptInput;
                   break;
                }
            }
        }

        cout << "Illegal move!" << endl;
        cout << Player2 << " " << "position: ";
        cin >> promptInput;
    }while(1);
}




void SearchforValuePlayer1(char value, char TictacValues[][COLUMN]){

     for (int i = 0; i < ROW; i++){

            for (int j = 0; j < COLUMN; j++){

                if (TictacValues[i][j] == value){
                    TictacValues[i][j] = Player1;
                }
            }
        }
}

void SearchforValuePlayer2(char value, char TictacValues[][COLUMN]){

     for (int i = 0; i < ROW; i++){

            for (int j = 0; j < COLUMN; j++){

                if (TictacValues[i][j] == value){
                    TictacValues[i][j] = Player2;
                }
            }
        }
}



char WhoIsTheWinner(char TictacValues[][COLUMN]){
    char winner;
    for (int i = 0 ; i < ROW; i++){
        if (TictacValues[i][0] == TictacValues[i][1] && TictacValues[i][1] == TictacValues[i][2]){
            winner = TictacValues[i][2];
            return winner;
        }
    }
    for (int i = 0; i < COLUMN; i++){
        if (TictacValues[0][i] == TictacValues[1][i] && TictacValues[1][i] == TictacValues[2][i]){
            winner = TictacValues[2][i];
            return winner;
        }
    }
    if ((TictacValues[0][0] == TictacValues[1][1] && TictacValues[1][1] == TictacValues[2][2]) || (TictacValues[2][0] == TictacValues[1][1]
        && TictacValues [1][1] == TictacValues[0][2])){
        winner = TictacValues[1][1];
        return winner;
        }

    return 0;

}
char LoopuntilWinnerIsfound(char value, char TictacValues[][COLUMN]){
    char winner;
    for (int i = 0; i < MAXMOVES; i++){
        value = InputPlayer1(TictacValues);
        SearchforValuePlayer1(value, TictacValues);
        printOutMatrix(TictacValues);
        winner = WhoIsTheWinner(TictacValues);
        if (winner == Player1)
            return Player1;
        else if (i == 3)
            return DRAW;
        else{
        value = InputPlayer2(TictacValues);
        SearchforValuePlayer2(value, TictacValues);
        printOutMatrix(TictacValues);
        winner = WhoIsTheWinner(TictacValues);
        }
        if (winner == Player2){
            return Player2;
        }
    }
    return 0;
}

void DisplayWinnerOrDraw(char winner){
    if (winner == Player1)
        cout << "Winner is: " << Player1;
    else if (winner == Player2)
        cout << "Winner is: " << Player2;
    else if (winner == DRAW)
        cout << "Draw!";
}

