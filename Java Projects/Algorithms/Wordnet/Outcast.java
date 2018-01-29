package S4;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

/**
 * Created by Erick on 2016-10-10.
 */
public class Outcast {
    private WordNet word;

    // constructor takes a WordNet object
    public Outcast(WordNet wordnet){
        word = wordnet;
    }

    // given an array of WordNet nouns, return an outcast
    public String outcast(String[] nouns) {
        int maxDist = 0;
        String MaxOut = null;
        for (int i = 0; i < nouns.length; i++) {
            String n = nouns[i];
            int distance = 0;
            for (int k = 0 ; k < nouns.length; k++) {
                int dist = word.distance(n,nouns[k]);
                distance += dist;
            }
            if (maxDist < distance) {
                maxDist = distance;
                MaxOut = n;
            }
        }
        return MaxOut;
    }


    public static void main(String[] args) {
        // Mooshak gave errors with delivering with this main function so i commented it out
        // But it works in testing the code.
        /*
        WordNet wordnet = new WordNet(args[0], args[1]); Outcast outcast = new Outcast(wordnet);
        for (int t = 2; t < args.length; t++) {
            String[] nouns = In.readStrings(args[t]);
            StdOut.println(args[t] + ": " + outcast.outcast(nouns)); }
        */
    }
}
