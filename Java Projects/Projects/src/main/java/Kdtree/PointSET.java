
/****************************************************************************
 *  Compilation:  javac PointSET.java
 *  Execution:    
 *  Dependencies:
 *  Author:
 *  Date:
 *
 *  Data structure for maintaining a set of 2-D points, 
 *    including rectangle and nearest-neighbor queries
 *
 *************************************************************************/
package S3;
import edu.princeton.cs.algs4.*;

import java.util.ArrayList;
import java.util.Arrays;

public class PointSET {

    public SET<Point2D> point;
    // construct an empty set of points
    public PointSET() {
        point = new SET<Point2D>();
    }

    // is the set empty?
    public boolean isEmpty() {
        return point.size() == 0;
    }

    // number of points in the set
    public int size() {
        return point.size();
    }

    // add the point p to the set (if it is not already in the set)
    public void insert(Point2D p) {
        point.add(p);
    }

    // does the set contain the point p?
    public boolean contains(Point2D p) {
       return point.contains(p);
    }

    // draw all of the points to standard draw
    public void draw() {
        for (Point2D drawP : point)
            drawP.draw();
    }

    // all points in the set that are inside the rectangle
    public Iterable<Point2D> range(RectHV rect) {
        ArrayList<Point2D> list = new ArrayList<Point2D>();
        for (Point2D d : point)
        {
            if (rect.contains(d)){
                list.add(d);
            }
        }
        return list;
    }

    // a nearest neighbor in the set to p; null if set is empty
    public Point2D nearest(Point2D p) {
        if (isEmpty())
            return null;
        Point2D nearest = p;
        for (Point2D item : point) {
            if (nearest == p)
                nearest = item;
            else {
                if (nearest.distanceSquaredTo(p) <= item.distanceSquaredTo(p));
                    //DO NOTHING
                else {
                    nearest = item;
                }
            }
        }
        return nearest;
    }

    public static void main(String[] args) {
        for (int j = 0; j < args.length; j++) {
            String filename = args[j];
            In in = new In(filename);
            Out out = new Out();
            int nrOfRecangles = in.readInt();
            int nrOfPointsCont = in.readInt();
            int nrOfPointsNear = in.readInt();
            RectHV[] rectangles = new RectHV[nrOfRecangles];
            Point2D[] pointsCont = new Point2D[nrOfPointsCont];
            Point2D[] pointsNear = new Point2D[nrOfPointsNear];
            for (int i = 0; i < nrOfRecangles; i++) {
                rectangles[i] = new RectHV(in.readDouble(), in.readDouble(),
                        in.readDouble(), in.readDouble());
            }
            for (int i = 0; i < nrOfPointsCont; i++) {
                pointsCont[i] = new Point2D(in.readDouble(), in.readDouble());
            }
            for (int i = 0; i < nrOfPointsNear; i++) {
                pointsNear[i] = new Point2D(in.readDouble(), in.readDouble());
            }
            PointSET set = new PointSET();
            for (int i = 0; !in.isEmpty(); i++) {
                double x = in.readDouble(), y = in.readDouble();
                set.insert(new Point2D(x, y));
            }
            for (int i = 0; i < nrOfRecangles; i++) {
                // Query on rectangle i, sort the result, and print
                Iterable<Point2D> ptset = set.range(rectangles[i]);
                int ptcount = 0;
                for (Point2D p : ptset)
                    ptcount++;
                Point2D[] ptarr = new Point2D[ptcount];
                int k = 0;
                for (Point2D p : ptset) {
                    ptarr[k] = p;
                    k++;
                }
                Arrays.sort(ptarr);
                out.println("Inside rectangle " + (i + 1) + ":");
                for (k = 0; k < ptcount; k++)
                    out.println(ptarr[j]);
            }
            out.println("Contain test:");
            for (int i = 0; i < nrOfPointsCont; i++) {
                out.println((i + 1) + ": " + set.contains(pointsCont[i]));
            }

            out.println("Nearest test:");
            for (int i = 0; i < nrOfPointsNear; i++) {
                out.println((i + 1) + ": " + set.nearest(pointsNear[i]));
            }

            out.println();

        }
    }
}
