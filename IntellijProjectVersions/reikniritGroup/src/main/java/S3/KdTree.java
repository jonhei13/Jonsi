package S3;
/*************************************************************************
 *************************************************************************/


import java.awt.*;
import java.text.DecimalFormat;
import java.util.ArrayList;

import edu.princeton.cs.algs4.*;

import java.util.Arrays;

public class KdTree {
    //uncomment for point precision in draw.
    DecimalFormat numberFormat = new DecimalFormat("#0.00");
    // construct an empty set of points
    private static class Node {
        private Point2D p; // the point
        private RectHV rect; // the axis-aligned rectangle
        private Node lb; // the left/bottom subtree
        private Node rt; // the right/top subtree
        private Node(RectHV rect, Point2D p){
            this.p = p;
            this.rect = rect;
        }
        public boolean isHorizontal;
    }
    private Node root;
    private int size;


    public Node min(Node n, Node nd, Point2D p){
        if (n.p.distanceSquaredTo(p) < nd.p.distanceSquaredTo(p))
            return n;
        else
            return nd;
    }

    public KdTree() {
        root = null;
        size = 0;
    }

    // is the set empty?
    public boolean isEmpty() {
        return (root == null);
    }

    // number of points in the set
    public int size() {
        return size;
    }

    // add the point p to the set (if it is not already in the set)
    public void insert(Point2D p) {

        root = insert(root, p, 0.0, 0.0, 1.0, 1.0, true);

    }

    private Node insert(Node node, Point2D p, double x0, double y0, double x1, double y1, boolean VERTICAL) {
        if (node == null) {
            RectHV rect = new RectHV(x0, y0, x1, y1);
            Node NewNode = new Node(rect, p);
            NewNode.isHorizontal = VERTICAL;
            size++;
            return (NewNode);
        }
        else if (node.p.x() == p.x() && node.p.y() == p.y())
            return node;
        if (VERTICAL) {
            if (node.p.x() > p.x())
                node.lb = (insert(node.lb, p, x0, y0, node.p.x(), y1, !VERTICAL));
            else
                node.rt = (insert(node.rt, p, node.p.x(), y0, x1, y1, !VERTICAL));
        } else {
            if (node.p.y() > p.y())
                node.lb = (insert(node.lb, p, x0, y0, x1, node.p.y(), !VERTICAL));
            else
                node.rt = (insert(node.rt, p, x0, node.p.y(), x1, y1, !VERTICAL));
        }
        return node;
    }

    // does the set contain the point p?
    public boolean contains(Point2D p) {return (contains(root,p));}
    private boolean contains(Node node, Point2D p) {
        if (node == null)
            return false;
        if (p.compareTo(node.p) == 0)
            return true;
        if (contains(node.lb, p) || contains(node.rt, p))
        {
            return true;
        }
        return false;
    }
    // draw all of the points to standard draw
    public void draw() {
        // draw canvas border
        StdDraw.setPenColor(StdDraw.BLACK);
        StdDraw.line(0, 0, 1, 0);
        StdDraw.line(1, 0, 1, 1);
        StdDraw.line(1, 1, 0, 1);
        StdDraw.line(0, 1, 0, 0);
        StdDraw.setPenColor(StdDraw.LIGHT_GRAY);
        StdDraw.filledSquare(0, 0, 1.0);
        StdDraw.setPenColor(StdDraw.BLACK);

        draw(root, null);
    }

    private void draw(Node node, Node parent){
        if (node == null) {
            return;
        }

        StdDraw.setPenColor(StdDraw.BLACK);
        node.p.draw();

        double x = node.p.x();
        double y = node.p.y();

        if (node.isHorizontal == true) {
            StdDraw.setPenRadius();
            StdDraw.setPenColor(StdDraw.RED);
            StdDraw.line(x, node.rect.ymin(), x, node.rect.ymax());
            StdDraw.setPenRadius(0.008);
            StdDraw.setPenColor(StdDraw.BLACK);
            StdDraw.point(x,y);
            StdDraw.setFont(new Font("Verdana", Font.ITALIC, 11));
            StdDraw.text(x <= 0.45 ? x+(0.06)  : x-(0.06),y < 0.5 ? y+(0.02) : y-(0.02),
                    "(" + numberFormat.format(x) + ", " + numberFormat.format(y) + ")");

        }
        else {
            StdDraw.setPenRadius();
            StdDraw.setPenColor(StdDraw.BLUE);
            StdDraw.line(node.rect.xmin(), y, node.rect.xmax(), y);
            StdDraw.setPenRadius(0.008);
            StdDraw.setPenColor(StdDraw.BLACK);
            StdDraw.point(x,y);
            StdDraw.setFont(new Font("Verdana", Font.ITALIC, 10));
            StdDraw.text(x <= 0.45 ? x+(0.06)  : x-(0.06),y < 0.5 ? y+(0.02) : y-(0.02),
                    "(" + numberFormat.format(x) + ", " + numberFormat.format(y) + ")");
        }

        draw(node.lb, node);
        draw(node.rt, node);
    }

    // all points in the set that are inside the rectangle
    public Iterable<Point2D> range(RectHV rect) {
        ArrayList<Point2D> pList = new ArrayList<Point2D>();
        pList = range(rect, root, pList);
        return pList;
    }
    private ArrayList<Point2D> range (RectHV rect, Node node, ArrayList<Point2D> points)
    {
        if (node == null)
        {
            return points;
        }
        if (rect.contains(node.p))
        {
            points.add(node.p);
        }
        if (rect.intersects(node.rect))
        {
            range(rect, node.lb, points);
            range(rect, node.rt, points);
        }
        return points;
    }

    // a nearest neighbor in the set to p; null if set is empty
    public Point2D nearest(Point2D p) {
        Point2D best = root.p;
        return nearest(root, p, best);
    }
    private Point2D nearest(Node node, Point2D p, Point2D best){
        if (node == null)
            return best;
        if (node.p.distanceSquaredTo(p) < best.distanceSquaredTo(p))
            best = node.p;
        if (node.rect.distanceSquaredTo(p) < best.distanceSquaredTo(p))
        {
            best = nearest(node.lb, p, best);
            best = nearest(node.rt, p, best);
        }
        return best;
    }
    /*******************************************************************************
     * Test client
     ******************************************************************************/

    public static void main(String[] args) {
        for (int it = 0; it < args.length; it++) {
            String filename = args[it];
            In in = new In(filename);
            Out out = new Out();
            int N = in.readInt(), C = in.readInt(), T = 50;
            Point2D[] queries = new Point2D[C];
            KdTree tree = new KdTree();
            out.printf("Inserting %d points into tree\n", N);
            for (int i = 0; i < N; i++) {
                tree.insert(new Point2D(in.readDouble(), in.readDouble()));
            }
            out.printf("tree.size(): %d\n", tree.size());
            out.printf("Testing `nearest` method, querying %d points\n", C);

            for (int i = 0; i < C; i++) {
                queries[i] = new Point2D(in.readDouble(), in.readDouble());
                out.printf("%s: %s\n", queries[i], tree.nearest(queries[i]));
            }
            for (int i = 0; i < T; i++) {
                for (int j = 0; j < C; j++) {
                    tree.nearest(queries[j]);
                }
            }
        }
    }

}
