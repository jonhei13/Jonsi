/**
 * Created by Alex on 23-Feb-17.
 * Position has an x coordinate and y-coordinate
 */
public class Position {

    public int x;
    public int y;

    public Position(int x, int y) {
        this.x = x; this.y = y;
    }
    public Position(){

    }

    public String toString() {
        return "(" + x + ", " + y + ")";
    }


    public boolean equals(Object o){
        Position p = (Position)o;
        return this.x == p.x && this.y == p.y;
    }

    public int hashCode() {
        return 11*x+y;
    }
}

