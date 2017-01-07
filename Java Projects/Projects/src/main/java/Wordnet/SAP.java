package S4;

import edu.princeton.cs.algs4.*;

import java.util.ArrayList;

/**
 * Created by Erick on 2016-10-10.
 */
@SuppressWarnings({"Duplicates", "SpellCheckingInspection"})
public class SAP {

    private BreadthFirstDirectedPaths bfdV;
    private BreadthFirstDirectedPaths bfdW;
    private Digraph G;

    // constructor takes a digraph (not necessarily a DAG)
    public SAP(Digraph G){
        DirectedCycle Test = new DirectedCycle(G);
        try{
            if (Test.hasCycle())
                throw new Exception();
       }catch (Exception ex)
       {
           throw new IllegalArgumentException("Graph is not acyclic");
       }
       try {
           int count = 0;
           for (int i = 0; i < G.V(); i++) {
               if (G.outdegree(i) == 0)
                   count++;
           }
           if (count > 1)
               throw new Exception();
       }catch (Exception ex)
       {
           throw new IllegalArgumentException("Graph is not rooted");
       }
       this.G = G;

    }
    // length of shortest ancestral path between v and w; -1 if no such path
    public int length(int v, int w){
        int ancestor = ancestor(v, w);
        if (ancestor == -1)
            return -1;
        return bfdV.distTo(ancestor) + bfdW.distTo(ancestor);
    }

    // a common ancestor of v and w that participates in a shortest ancestral path; -1 if no such path
    public int ancestor(int v, int w){
        bfdV = new BreadthFirstDirectedPaths(G,v);
        bfdW = new BreadthFirstDirectedPaths(G, w);
        int mindist = Integer.MAX_VALUE;
        int ancestor = -1;
        for (int i = 0; i < G.V(); i++) {
            if (bfdV.hasPathTo(i) && bfdW.hasPathTo(i)){
                int dist = bfdV.distTo(i) + bfdW.distTo(i);
                if (mindist >= dist) {
                    mindist = dist;
                    ancestor = i;
                }
            }
        }
       return ancestor;
    }

    // length of shortest ancestral path between any vertex in v and any vertex in w; -1 if no such path
    public int length(Iterable <Integer > v, Iterable <Integer > w){
        int ancestor = ancestor(v, w);
        if (ancestor == -1)
            return -1;
        return bfdV.distTo(ancestor) + bfdW.distTo(ancestor);
    }


    // a common ancestor that participates in shortest ancestral path; -1 if no such path
    public int ancestor(Iterable <Integer > v, Iterable <Integer > w){
        bfdV = new BreadthFirstDirectedPaths(G,v);
        bfdW = new BreadthFirstDirectedPaths(G, w);
        int mindist = Integer.MAX_VALUE;
        int ancestor = -1;
        for (int i = 0; i < G.V(); i++) {
            if (bfdV.hasPathTo(i) && bfdW.hasPathTo(i)){
                int dist = bfdV.distTo(i) + bfdW.distTo(i);
                if (mindist >= dist) {
                    mindist = dist;
                    ancestor = i;
                }
            }
        }
        return ancestor;
    }

    // do unit testing of this class
    public static void main(String[] args){
        In in = new In();
        Digraph G = new Digraph(in);
        SAP sap = new SAP(G);
        ArrayList<Integer> v = new ArrayList<Integer>();
        ArrayList<Integer> w = new ArrayList<Integer>();
        for (int i = 0; i < G.V(); i++) {
            v.add(in.readInt());
            w.add(in.readInt());
            StdOut.println("Len " + sap.length(v, w) + " " + "Anc " + sap.ancestor(v, w));

        }
    }
}
