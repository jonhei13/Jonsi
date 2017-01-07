package S4;

import edu.princeton.cs.algs4.Digraph;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by Erick on 2016-10-10.
 */
public class SAPTest {

    @Before
    public void setUp() {
        //TODO initialize stuff for tests

    }

    @Test
    public void lengthTest(String args[]) {
        In in = new In(args[0]);
        int vertex = in.readInt();
        int edge = in.readInt();
        Digraph G = new Digraph(in);
        SAP sap = new SAP(G);
        for (int i = 0; i < edge; i++){
            int v = in.readInt();
            int w = in.readInt();
            StdOut.println(sap.length(v,w));
        }
    }

    @Test
    public void ancestorTest() {

    }
}