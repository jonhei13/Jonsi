package S4;

import edu.princeton.cs.algs4.*;
import java.util.ArrayList;
import java.util.HashMap;

/**
 * Created by Erick on 2016-10-10.
 */
@SuppressWarnings("SpellCheckingInspection")
public class WordNet {


    private HashMap<String, ArrayList<Integer>> SetsOfId;
    private HashMap<Integer, String> SetsOfsyns;
    private Digraph G;
    private SAP sap;

    // constructor takes the name of the two input files
    public WordNet(String synsets, String hypernyms) {

        SetsOfId = new HashMap<String, ArrayList<Integer>>();
        SetsOfsyns = new HashMap<Integer, String>();
        int SynsLines = synSetter(synsets);
        hypernyms(hypernyms, SynsLines);
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
    }

    private int synSetter(String synsets) {
        In in = new In(synsets);
        int count = 0;
        ArrayList<Integer> Ids = new ArrayList<Integer>();
        while (in.hasNextLine()) {
            String line = in.readLine();
            String[] Sep = line.split(",");
            int SynsId = Integer.valueOf(Sep[0]);
            String synset = String.valueOf(Sep[1]);
            String[] Syns = synset.split(" ");
            for (String K : Syns) {
                Ids = SetsOfId.get(K);
                if (Ids == null) {
                    ArrayList<Integer> NewId = new ArrayList<Integer>();
                    NewId.add(SynsId);
                    SetsOfId.put(K, NewId);
                }
                else {
                    Ids.add(SynsId);
                    SetsOfId.put(K, Ids);
                }
                SetsOfsyns.put(SynsId, synset);
            }

            count++;
        }
        return count;
    }

    private void hypernyms(String hypernyms, int Lines) {
        In in = new In(hypernyms);
        G = new Digraph(Lines);
        while (in.hasNextLine()) {
            String line = in.readLine();
            String[] hyp = line.split(",");
            int SynsId = Integer.valueOf(hyp[0]);
            for (int i = 1; i < hyp.length; i++) {
                int w = Integer.parseInt(hyp[i]);
                G.addEdge(SynsId, w);
            }
        }
        sap = new SAP(G);
    }

    // returns all WordNet nouns
    public Iterable<String> nouns() {
        return SetsOfId.keySet();
    }

    // is the word a WordNet noun?
    public boolean isNoun(String word) {
        return SetsOfId.containsKey(word);
    }

    // distance between nounA and nounB (defined below)
    public int distance(String nounA, String nounB) {
        NounChecker(nounA, nounB);
        int dist = sap.length(SetsOfId.get(nounA), SetsOfId.get(nounB));
        return dist;
    }

    private void NounChecker(String nounA, String nounB)
    {
        if (!isNoun(nounA) && !isNoun(nounB))
            throw new java.lang.IllegalArgumentException();
    }
    // a synset (second field of synsets.txt) that is the common ancestor of nounA and nounB
    // in a shortest ancestral path (defined below)
    public String sap(String nounA, String nounB) {
        NounChecker(nounA, nounB);
        int ancestor = sap.ancestor(SetsOfId.get(nounA), SetsOfId.get(nounB));
        return SetsOfsyns.get(ancestor);
    }

    // do unit testing of this class
    public static void main(String[] args) {
        String hypernyms = args[0];
        String synsets = args[1];
        WordNet W = new WordNet(synsets, hypernyms);
        // Contains Test
        StdOut.println(W.isNoun("mileage"));
        StdOut.println(W.isNoun("Black_Plague"));
        StdOut.println(W.isNoun("black_marlin"));
        StdOut.println(W.isNoun("American_water_spaniel"));
        StdOut.println(W.isNoun("Nowaihose"));

        // Distance Test
        StdOut.println(W.distance("white_marlin","mileage"));
        StdOut.println(W.distance("Black_Plague","black_marlin"));
        StdOut.println(W.distance("American_water_spaniel","histology"));
        StdOut.println(W.distance("Brown_Swiss","barrel_roll"));
        StdOut.println(W.sap("worm", "bird"));
        StdOut.println(W.distance("worm","bird"));


        //(distance = 23) white_marlin, mileage
        //(distance = 33) Black_Plague, black_marlin
        //(distance = 27) American_water_spaniel, histology
        // (distance = 29) Brown_Swiss, barrel_rol

    }
}
