package d4;

import edu.princeton.cs.algs4.Digraph;
import edu.princeton.cs.algs4.Queue;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class BreadthFirstPaths {
    private static final int INFINITY = Integer.MAX_VALUE;
    private boolean[] marked; 	    // marked[v] = is there an s->v path?
    private int[] edgeTo;      	    // edgeTo[v] = last edge on shortest s->v path.
    private int[] distTo;    	    // distTo[v] = length of shortest s->v path.
    private int[] shortestPaths; 	// shortestPaths[v] = number of shortest paths s->v.
    private int[] minDist; 			// minDist[v] = minumum distance s->v.

    public BreadthFirstPaths(Digraph G, int s) {
        marked = new boolean[G.V()];
        distTo = new int[G.V()];
        edgeTo = new int[G.V()];
        for (int v = 0; v < G.V(); v++)
            distTo[v] = INFINITY;
        bfs(G, s);
    }

    // BFS from single source
    private void bfs(Digraph G, int s) {
        shortestPaths = new int[G.V()];
        shortestPaths[s] = 1; //node has a path to it self
        minDist = new int[G.V()];
        for (int i = 0; i < G.V(); i++){
            minDist[i] = 0;
        }

        Queue<Integer> q = new Queue<Integer>();
        marked[s] = true;
        distTo[s] = 0;
        q.enqueue(s);
        while (!q.isEmpty()) {
            int v = q.dequeue();
            for (int w : G.adj(v)) {
                if (!marked[w]) {
                    edgeTo[w] = v;
                    distTo[w] = distTo[v] + 1;
                    marked[w] = true;
                    minDist[w] = minDist[v] + 1;
                    shortestPaths[w] = shortestPaths[v];
                    q.enqueue(w);
                }
                else{
                    if(distTo[w] -1 == distTo[v]){
                        shortestPaths[w] += shortestPaths[v];
                    }
                }
            }
        }
    }

    // BFS from multiple sources
    private void bfs(Digraph G, Iterable<Integer> sources) {
        Queue<Integer> q = new Queue<Integer>();
        for (int s : sources) {
            marked[s] = true;
            distTo[s] = 0;
            q.enqueue(s);
        }
        while (!q.isEmpty()) {
            int v = q.dequeue();
            for (int w : G.adj(v)) {
                if (!marked[w]) {
                    edgeTo[w] = v;
                    distTo[w] = distTo[v] + 1;
                    marked[w] = true;
                    q.enqueue(w);
                }
            }
        }
    }

    public boolean hasPathTo(int v) {
        return marked[v];
    }

    private int countShortestPaths(int v) {
        return shortestPaths[v];
    }

    public static void main(String[] args) {
        int in = Integer.parseInt(StdIn.readString());
        int verteces = Integer.parseInt(StdIn.readString());
        Digraph G = new Digraph(in);
        for(int i = 0; i < verteces; i++){
            int from = StdIn.readInt();
            int to = StdIn.readInt();
            G.addEdge(from, to);
        }

        int s = Integer.parseInt(StdIn.readString());
        for(int i = 0; i < s; i++){
            int from = StdIn.readInt();
            int to = StdIn.readInt();
            BreadthFirstPaths bfs = new BreadthFirstPaths(G, from);
            if (bfs.hasPathTo(to)) {
                StdOut.println(bfs.countShortestPaths(to));
            }
            else {
                StdOut.println("0");
            }
        }
    }
}
