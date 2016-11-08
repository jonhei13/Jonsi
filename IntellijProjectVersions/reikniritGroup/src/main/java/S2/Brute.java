package S2;

import edu.princeton.cs.algs4.*;

import java.util.ArrayList;
import java.util.Collections;

public class Brute {

    private ArrayList<Point> pointArray;
    private ArrayList<ArrayList<Point>> collinearArray;
    public Brute(){

        pointArray = new ArrayList<Point>();
        collinearArray = new ArrayList<ArrayList<Point>>();
    }

    public void addToPointArray(Point p) {
        this.pointArray.add(p);
    }


    private boolean isCollinear(Point one, Point two, Point three, Point four) {
        return one.slopeTo(two) == one.slopeTo(three) && one.slopeTo(three) == one.slopeTo(four);
    }


    private void prettyPrint(){
        //TODO implement
        for (int i = 0; i < collinearArray.size();i++) {
            StdOut.println("(" + collinearArray.get(i).get(0).x + ", " + collinearArray.get(i).get(0).y + ") -> ("
                    + collinearArray.get(i).get(1).x + ", " + collinearArray.get(i).get(1).y + ") -> ("
                    + collinearArray.get(i).get(2).x + ", " + collinearArray.get(i).get(2).y + ") -> ("
                    + collinearArray.get(i).get(3).x + ", " + collinearArray.get(i).get(3).y + ")");
        }
    }

    public void isStackCollinear(){
    	
    	Collections.sort(pointArray);
        if (pointArray.size() >= 3) {
        	for (int i = 0; i < pointArray.size(); i++)
        	{
        		for (int k = i + 1; k < pointArray.size(); k++)
        		{
            		double First = pointArray.get(i).slopeTo(pointArray.get(k));
            		
            		for (int j = k + 1; j < pointArray.size(); j++)
            		{
            			double Second = pointArray.get(i).slopeTo(pointArray.get(j));
            		
            		if (First == Second)
            		{
            			for (int l = j + 1; l < pointArray.size(); l++)
            			{
            				double Third = pointArray.get(i).slopeTo(pointArray.get(l));
            				if (Second == Third)
            				{
            					ArrayList<Point> TempArray = new ArrayList<Point>(4);
            					TempArray.add(pointArray.get(i));
            					TempArray.add(pointArray.get(k));
            					TempArray.add(pointArray.get(j));
            					TempArray.add(pointArray.get(l));
            					collinearArray.add(TempArray);
            				}
            			}
            		}
            		
            		}
        		}
        		
        	}
       }
 }

    public static void main(String[] args) {
        // TODO Auto-generated method stub
    	
        In in = new In();
        Brute brute = new Brute();
        int n = in.readInt();
        for (int i = 0; i < n; i++) {
            int x = in.readInt(), y = in.readInt();
            Point points = new Point(x, y);
            brute.addToPointArray(points);
            
        }
        brute.isStackCollinear();
        brute.prettyPrint();
    }
}
    	
    	/*
        for (int j = 0; j < args.length;j++) {
            Brute brute = new Brute();
            StdOut.println("Test "+ j + " running with input file: " + args[j]);
       	 	In in = new In();
            int N = in.readInt();
            for (int i = 0; i < N; i++) {
                int x = in.readInt();
                int y = in.readInt();
                Point p = new Point(x, y);
                brute.addToPointArray(p);
            }
           brute.isStackCollinear();
           brute.prettyPrint();
        }
    }
    */
            



