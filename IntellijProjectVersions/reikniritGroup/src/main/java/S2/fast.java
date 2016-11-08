package S2;


import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

public class fast{

	private ArrayList<Point> pointArray;
    private LinkedList<Point> Checker;
	private LinkedList<LinkedList<Point>> CollSlope;
    LinkedList<Point> SlopeArr;

    public fast()
	{
		pointArray = new ArrayList<Point>();
		CollSlope = new LinkedList<LinkedList<Point>>();
        Checker = new  LinkedList<Point>();
	}
    public void addToPointArray(Point p) {
        pointArray.add(p);
    }
    
    public void FastSlope()
    {
    	boolean added = false;
        int j = 0;
        int k2 = 0;
    	Collections.sort(pointArray);
        for (int i = j+1; j < pointArray.size()-1; i++)
    	{
            SlopeArr = new LinkedList<Point>();

            for (int k = i+1; k < pointArray.size(); k++) {
                double p = pointArray.get(j).slopeTo(pointArray.get(i));
                double q = pointArray.get(i).slopeTo(pointArray.get(k));
                if (p == q && (!(j == i) && !(i == k) && !(j == k))) {

                    if (!Checker.contains(pointArray.get(k))) {
                        SlopeArr.add(pointArray.get(k));
                        Checker.add(pointArray.get(k));
                    }
                    added = true;
                }
              //  StdOut.println("J: " + j + "  i: " + i + "  k: " + k);

            }

    		if (added)
    		{
                SlopeArr.add(pointArray.get(i));
                SlopeArr.add(pointArray.get(j));
                Collections.sort(SlopeArr);
                if(!CollSlope.contains(SlopeArr) && SlopeArr.size() > 3)
                    CollSlope.add(SlopeArr);
    		}

            if(i == pointArray.size()-1){
                i = j+1;
                j++;
                Checker = new LinkedList<Point>();
            }

           // added = false;
    	}
    	Collections.sort(CollSlope, SortOrderList);

    }
    Comparator<LinkedList<Point>> SortOrderList = new Comparator<LinkedList<Point>>()
    {

		public int compare(LinkedList<Point> o1, LinkedList<Point> o2) {
	    	if (o1.isEmpty() || o2.isEmpty())
	    	{
	    		return -1;
	    	}
	    	else 
	    	{
	    		Point point1 = new Point(o1.getFirst().x,o1.getFirst().y);
	    		Point point2 = new Point(o2.getFirst().x,o2.getFirst().y);

	    		if(point1.compareTo(point2) == 0){
                    Point point3 = new Point(o1.getLast().x,o1.getLast().y);
                    Point point4 = new Point(o2.getLast().x,o2.getLast().y);
                    return point1.SLOPE_ORDER.compare(point3,point4);
                }
                else
                    return point1.compareTo(point2);
	    	}
    	
		}

    };
    
    int k = 0;
    private void prettyPrint(){

        for (int i = 0; i < CollSlope.size();i++) {
        	for (int j = 0; j < CollSlope.get(i).size(); j++)
        	{
        	    if(j == CollSlope.get(i).size()-1)
        		    StdOut.print("(" + CollSlope.get(i).get(j).x + ", " + CollSlope.get(i).get(j).y + ")" );
                else
                    StdOut.print("(" + CollSlope.get(i).get(j).x + ", " + CollSlope.get(i).get(j).y + ") -> " );
        	  //  k=j;
               // CollSlope.get(i).get(j).draw();

        	}

            StdOut.print("\n");
           // StdOut.println(CollSlope.get(i).get(1).slopeTo(CollSlope.get(i).get(2)));

        }
    }
	
	public static void main(String[] args) {
        
		In in = new In();
        fast Quick = new fast();
        String filename = args[0];
        in = new In(filename);
        int n = in.readInt();
        for (int i = 0; i < n; i++) {
            int x = in.readInt(), y = in.readInt();
            Point points = new Point(x, y);
            Quick.addToPointArray(points);
        }
        Quick.FastSlope();
        Quick.prettyPrint();
	}
}



