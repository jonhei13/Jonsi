package S2;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.Stopwatch;
import org.junit.Test;



/**
 * @author Erick on 16/09/16.
 */
public class fastTest {
    private final int top = 32768;
    private final int bot = 0;
    private int n;
    In in;
    fast Fast;

    public fastTest(){
        Fast = new fast();
        in = new In();
    }

    private int genXY(){
        return StdRandom.uniform(bot, top);
    }

    private void addPointsToTestArray(int n) {
        this.n = n;
        for (int i = 0; i < n; i++) {
            Point points = new Point(genXY(), genXY());
            Fast.addToPointArray(points);
        }
    }

    @Test(timeout = 1000000)
    public void Nis150(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(150);
        Fast.FastSlope();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis200(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(200);
        Fast.FastSlope();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis300(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(300);
        Fast.FastSlope();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis400(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(400);
        Fast.FastSlope();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis800(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(800);
        Fast.FastSlope();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis1600(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(1600);
        Fast.FastSlope();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis3200(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(3200);
        Fast.FastSlope();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis6400(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(6400);
        Fast.FastSlope();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis12800(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(12800);
        Fast.FastSlope();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

}