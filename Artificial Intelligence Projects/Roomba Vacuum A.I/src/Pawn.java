
/**
 * Created by Alex on 23-Feb-17.
 */

/**
 * A pawn has a color, position and if it's alive
 * It can move forward or one diagonally in each direction.
 */

enum Color{
    WHITE, BLACK
}

public class Pawn {
    public Position pos;
    public Color color;
    public boolean isAllive;


    public Pawn(Position p, Color c, boolean a){
        this.pos = p;
        this.color = c;
        this.isAllive = a;
    }


}
