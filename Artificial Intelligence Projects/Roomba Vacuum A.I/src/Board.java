import javafx.geometry.Pos;

import java.util.ArrayList;
import java.util.HashMap;

/**
 * Created by Alex on 23-Feb-17.
 * Board has a width and a height.
 */
public class Board {
    public int width, height;
    public HashMap<Position, Pawn> pawns;

    public Board(int w, int h) {
        this.width = w;
        this.height = h;
        pawns = new HashMap<>();
        initArr();
    }

    public Board(HashMap<Position, Pawn> NewLocationPawns, int w, int h) {
        this.width = w;
        this.height = h;
        pawns = new HashMap<>(NewLocationPawns);
    }

    private void initArr() {
        for (int row = 1; row <= 2; row++) {
            for (int col = 1; col <= this.width; col++) {
                Position pos = new Position(col, row);
                pawns.put(pos, new Pawn(pos, Color.WHITE, true));
            }
        }
        for (int row = this.height - 1; row <= this.height; row++) {
            for (int col = 1; col <= this.width; col++) {
                Position pos = new Position(col, row);
                pawns.put(pos, new Pawn(pos, Color.BLACK, true));
            }
        }
    }
    public HashMap<Position, Pawn> getPawns(){
        return pawns;
    }

    public void setPawns (HashMap<Position, Pawn> setPawns){
        pawns = new HashMap<>(setPawns);
    }

}