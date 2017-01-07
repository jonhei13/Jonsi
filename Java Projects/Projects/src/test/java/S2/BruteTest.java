package S2;

import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Stopwatch;
import org.junit.Test;

/**
 * @author Erick on 15/09/16.
 */
public class BruteTest {

    private int top = 32768;
    private int bot = 0;
    private int n;
    In in;
    Brute brute;

    public BruteTest(){
        brute = new Brute();
        in = new In();
    }

    private int genXY(){
        return StdRandom.uniform(bot, top);
    }

    private void addPointsToTestArray(int n) {
        this.n = n;
        for (int i = 0; i < n; i++) {
            Point points = new Point(genXY(), genXY());
            brute.addToPointArray(points);
        }
    }

    @Test(timeout = 1000000)
    public void Nis150(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(150);
        brute.isStackCollinear();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis200(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(200);
        brute.isStackCollinear();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis300(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(300);
        brute.isStackCollinear();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis400(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(400);
        brute.isStackCollinear();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis800(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(800);
        brute.isStackCollinear();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis1600(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(1600);
        brute.isStackCollinear();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis3200(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(3200);
        brute.isStackCollinear();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis6400(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(6400);
        brute.isStackCollinear();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    @Test
    public void Nis12800(){
        Stopwatch s = new Stopwatch();
        addPointsToTestArray(12800);
        brute.isStackCollinear();
        System.out.println("DEBUG: Logic A toke " + s.elapsedTime() + " seconds");
    }

    /*
    *       N       brute       sorting
 ---------------------------------
    150
    200
    300
    400
    800
   1600
   3200
   6400
  12800
     */
}