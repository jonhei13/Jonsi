import javafx.geometry.Pos;

import java.lang.reflect.Array;
import java.nio.channels.Pipe;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by Alex on 23-Feb-17.
 * State has an array of pawns.
 */
public class State {
    private Board board;
    private boolean whiteTurn;
    private Color myColor;
    public boolean hasKilled;



    public State(Board board, boolean whiteTurn, Color color){
        this.board = board;
        this.whiteTurn = whiteTurn;
        this.myColor = color;
        this.hasKilled = false;
    }

    public Board getBoard(){
        return board;
    }

    public boolean isLegalPosition(Position pos){
        if(pos.x < 1 || pos.x > board.width){
            return false;
        }

        else if(pos.y < 1 || pos.y > board.height){
            return false;
        }

        else{
            return true;
        }
    }


    public boolean isTerminal(ArrayList<State> successorStates){
        return successorStates.isEmpty();
    }


    // Our first Evaluation Function.
    public int getValue2(){
        Pawn mostAdvancedWhite = new Pawn(new Position(1,1), Color.WHITE, true);
        Pawn mostAdvancedBlack = new Pawn(new Position(board.width,board.height), Color.BLACK, true);
        for(Map.Entry<Position, Pawn> entry: board.pawns.entrySet()) {
            Position pos = entry.getKey();
            Pawn currPawn = entry.getValue();
            if (currPawn != null) {
                if (currPawn.color == Color.WHITE) {
                    if (pos.y == board.height) {
                        return 100;
                    }
                    if (currPawn.pos.y > mostAdvancedWhite.pos.y) {
                        mostAdvancedWhite = currPawn;
                    }
                } else {
                    if (pos.y == 1) {
                        return 100;
                    }
                    if (currPawn.pos.y < mostAdvancedBlack.pos.y) {
                        mostAdvancedBlack = currPawn;
                    }
                }
            }
        }
        if(this.myColor == Color.WHITE){
            return 50 - (board.height - mostAdvancedWhite.pos.y) + (1 - mostAdvancedBlack.pos.y);
        }
        else{
            return -(50 - (board.height - mostAdvancedWhite.pos.y) + (1 - mostAdvancedBlack.pos.y));
        }

    }



    // Used Evaluation function.
    public int getValue(){
        Pawn mostAdvancedWhite = new Pawn(new Position(1,1), Color.WHITE, true);
        Pawn mostAdvancedBlack = new Pawn(new Position(board.width,board.height), Color.BLACK, true);
        int totalValue = 0;
        int nrOfRemainingBlack = 0;
        int nrOfRemainingWhite = 0;

        for(Map.Entry<Position, Pawn> entry: board.pawns.entrySet()) {
            Position pos = entry.getKey();
            Pawn currPawn = entry.getValue();

            Position WhiteCanGetkilledLeft = new Position(currPawn.pos.x -  1, currPawn.pos.y + 1);
            Position WhiteCanGetkilledRight = new Position(currPawn.pos.x +  1, currPawn.pos.y + 1);
            Position WhiteCanGoOneForward = new Position(currPawn.pos.x, currPawn.pos.y + 1);

            Position BlackCanGetkilledLeft = new Position(currPawn.pos.x -  1, currPawn.pos.y - 1);
            Position BlackCanGetkilledRight = new Position(currPawn.pos.x +  1, currPawn.pos.y - 1);
            Position BlackCanGoOneForward = new Position(currPawn.pos.x, currPawn.pos.y - 1);

            if (currPawn != null) {
                if (currPawn.color == Color.WHITE) {
                    nrOfRemainingWhite++;
                    if (pos.y == board.height) {
                        return 100;
                    }
                    else {
                        totalValue += getPawnValue(currPawn);
                    }
                    if (currPawn.pos.y > mostAdvancedWhite.pos.y) {
                        mostAdvancedWhite = currPawn;
                    }
                    if(board.getPawns().containsKey(WhiteCanGetkilledLeft)){
                        totalValue -= 5;
                    }
                    if(board.getPawns().containsKey(WhiteCanGetkilledRight)){
                        totalValue -= 5;
                    }
                    if(!board.getPawns().containsKey(WhiteCanGoOneForward)){
                        totalValue += 3;
                    }


                } else {
                    nrOfRemainingBlack++;
                    if (pos.y == 1) {
                        return  -100;
                    }
                    else {
                        totalValue += getPawnValue(currPawn);
                    }
                    if(board.getPawns().containsKey(BlackCanGetkilledLeft)){
                        totalValue += 5;
                    }
                    if(board.getPawns().containsKey(BlackCanGetkilledRight)){
                        totalValue += 5;
                    }
                    if(!board.getPawns().containsKey(BlackCanGoOneForward)){
                        totalValue -= 3;
                    }
                    if (currPawn.pos.y < mostAdvancedBlack.pos.y) {
                        mostAdvancedBlack = currPawn;
                    }
                }
            }
        }

        if(this.myColor == Color.WHITE){
            totalValue +=  20 - (board.height - mostAdvancedWhite.pos.y) + (1 - mostAdvancedBlack.pos.y);
            totalValue -= (nrOfRemainingBlack- nrOfRemainingWhite)*1;
        }
        else{
            totalValue -= (nrOfRemainingWhite - nrOfRemainingBlack)*1;
            totalValue += -(20 - (board.height - mostAdvancedWhite.pos.y) + (1 - mostAdvancedBlack.pos.y));
        }

        return totalValue;
    }

    public int getPawnValue(Pawn currPawn) {

        int pawnValue = 0;

        if (currPawn.color == Color.WHITE) {
            if (currPawn.pos.y == board.height - 1) {
                pawnValue = 2;
            }
            if (currPawn.pos.y == board.height - 2) {
                pawnValue = 1;
            }
        }
        else {
            if (currPawn.pos.y == 2) {
                pawnValue = 2;
            }
            if (currPawn.pos.y == 3) {
                pawnValue = 1;
            }
        }

        if (pawnValue == 0) {
            if (this.myColor == currPawn.color) {
                return 1;
            }
            else {
                return - 1;
            }
        }
        else {
            if (this.myColor == currPawn.color) {
                return pawnValue;
            }
            else {
                return - pawnValue;
            }
        }
    }



}
