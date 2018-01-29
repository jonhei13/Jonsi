#include <iostream>
#include <string>
#include <vector>

using namespace std;



struct chessPlayers{
    int players;
    vector<string> name;
    vector<int> Year;
    vector<int> Rating;
};

void GetNumberOfPlayers(chessPlayers& play);
void Getname(vector<string>& n);
void Getyear(vector<int>& years);
void getratings(vector<int>& rating);
void buildvector (chessPlayers& kay);
void displayPlayers(const chessPlayers& s);
void displayHighestRank(const chessPlayers& Rank);
void displayAverageRating(const chessPlayers& rate);

int main(){
chessPlayers fillup;
buildvector(fillup);
displayPlayers(fillup);
displayHighestRank(fillup);
displayAverageRating(fillup);



}



void buildvector (chessPlayers& kay){
        GetNumberOfPlayers(kay);
        cout << "--- Reading players ---" << endl;
    for (int i = 0; i < kay.players; i++){
        Getname(kay.name);
        Getyear(kay.Year);
        getratings(kay.Rating);
        cout << endl;
    }
}
void GetNumberOfPlayers(chessPlayers& play){
    cout << "Number of players: ";
    cin >> play.players;
}


void Getname(vector<string>& n){
    string x;
    cout << "Name: ";
    cin >> x;
    n.push_back(x);
}
void Getyear(vector<int>& years){
    int year;
    cout << "Year: ";
    cin >> year;
    years.push_back(year);
}
void getratings(vector<int>& rating){
    int ratings;
    cout << "Rating: ";
    cin >> ratings;
    rating.push_back(ratings);
}

void displayPlayers(const chessPlayers& s){


    cout << " --- Displaying players --- " << endl;
    for (unsigned int i = 0; i < s.name.size(); i++){
        cout << "Name: " << s.name[i] << endl;
        cout << "Year: " << s.Year[i] << endl;
        cout << "Rating: " << s.Rating[i] << endl;
        cout << endl;
    }

    }
void displayHighestRank(const chessPlayers& Rank){
      int temp = 0;
      for (unsigned int i = 0; i < Rank.Rating.size(); i++){
        if (temp < Rank.Rating[i]){
            temp = Rank.Rating[i];
        }
      }
      for (unsigned int j = 0; j < Rank.Rating.size(); j++){
         if (temp == Rank.Rating[j]){
            cout << "Highest rated player: " << endl;
            cout << "Name: " << Rank.name[j] << endl;
            cout << "Year: " << Rank.Year[j] << endl;
            cout << "Rating: " << Rank.Rating[j] << endl;
            cout << endl;
            break;
         }
      }
}

void displayAverageRating(const chessPlayers& rate){
    double sum,average;
    for (unsigned int k = 0; k < rate.Rating.size(); k++){
        sum += rate.Rating[k];
        average = sum / rate.Rating.size();
        }
    cout << "Average rating: " << average << endl;


}
