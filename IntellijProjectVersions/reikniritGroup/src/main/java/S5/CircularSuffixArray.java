
package S5;

import java.util.Arrays;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

public class CircularSuffixArray {
    private static class IndexOfString implements Comparable<IndexOfString>{
        private int index;
        private String text;
        IndexOfString(int i, String s) {
            index = i;
            text = s;
        }
        public int length() {
            return text.length();
        }
        public int index() {
            return index;
        }
        private char FindChar(int i){
            return text.charAt((i + index) % text.length());
        }
        public int compareTo(IndexOfString o) {
            if (this == o)
                return 0;
            int n = this.length();
            for (int i = 0; i < n; i++)
            {
                if (this.FindChar(i) < o.FindChar(i))
                    return -1;
                if (this.FindChar(i) > o.FindChar(i))
                    return 1;
            }
            return this.length() - o.length();
        }
    }
    private IndexOfString[] Array;
    private String text;
    private int[] index;
    CircularSuffixArray(String s)
    {
        if (s == null)
            throw new java.lang.NullPointerException();
        int length = s.length();
        text = s;
        Array = new IndexOfString[s.length()];
        for (int i = 0; i < length; i++)
        {
            Array[i] = new IndexOfString(i, text);
        }
        Arrays.sort(Array);
        index = new int[Array.length];
        for (int i = 0; i < Array.length; i++)
        {
            index[i] = Array[i].index();
        }
    }


    /**
     * Returns the length of the input string.
     * @return the length of the input string
     */
    public int length() // length of s
    {
        return text.length();
    }

    /**
     * Returns the index into the original string of the <em>i</em>th smallest circular suffix.
     * That is, {@code text.substring(sa.index(i))} is the <em>i</em>th smallest circular suffix.
     * @param i an integer between 0 and <em>n</em>-1
     * @return the index into the original string of the <em>i</em>th smallest suffix
     * @throws java.lang.IndexOutOfBoundsException unless {@code 0 <= i < n}
     */
    public int index(int i) // returns index of ith sorted suffix
    {
        if (i < 0 || i > length())
            throw new IllegalArgumentException();
        return index[i];
    }

    public static void main(String[] args) // unit testing
    {

        In in = new In(args[0]);
        String s = in.readAll();  // Read whole file
        String pair = s + s;
        CircularSuffixArray suffix = new CircularSuffixArray(s);

        StdOut.println("  i ind select");
        StdOut.println("-------------------");

        for (int i = 0; i < s.length(); i++) {
            int index = suffix.index(i);
            String ith = "\"" + pair.substring(index, index+Math.min(index + 50, s.length())) + "\"";
            StdOut.printf("%3d %3d %s\n", i, index, ith);
        }
    }

}
