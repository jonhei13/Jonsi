package S5;

import edu.princeton.cs.algs4.BinaryIn;
import edu.princeton.cs.algs4.BinaryOut;
import edu.princeton.cs.algs4.StdOut;

import java.util.Arrays;


public class BurrowsWheeler {

	private static final int BITS = 8;
	// apply Burrows-Wheeler transform, reading from standard input and writing to standard output
	public static void transform(BinaryIn in, BinaryOut out) {
		String input = in.readString();
		CircularSuffixArray s = new CircularSuffixArray(input);
		for (int i = 0; i < s.length(); i++){
			if (s.index(i) == 0){
				out.write(i);
				break;
			}
		}
		for (int i = 0; i < s.length(); i++) {
			int index = s.index(i);
			if (s.index(i) == 0)
				out.write(input.charAt(input.length()-1),BITS);
			else
				out.write(input.charAt(index-1), BITS);
		}
		out.flush();

}
	
	// apply Burrows-Wheeler inverse transform, reading from standard input and writing to standard output
	public static void inverseTransform(BinaryIn in, BinaryOut out) {
		int FirstNumber = in.readInt();
		String s = in.readString();
		char[] Sort = s.toCharArray();
		char[] input = s.toCharArray();
		int[] next = new int[input.length];
		for (int i = 0; i < input.length; i++){
			next[i] = -1;
		}
		Arrays.sort(Sort);
		int count = 0;
		for (int i = 0; i < input.length; i++) {
			for (int j = 0; j < input.length; j++) {
				if (i >= 1){
					if (Sort[i] == Sort[i-1]) {
						 j = count + 1;
						while (input[j] != Sort[i]){
							j++;
						}
						count = j;
					}
					else
						count = 0;
				}
				if (input[j] == Sort[i]){
						next[i] = j;
					count = j;
					break;
				}
			}
		}
		for (int i = 0, Current = FirstNumber; i < input.length; i++, Current = next[Current]){
			out.write(Sort[Current]);
		}
		out.flush();



	}

	public static void main(String[] args) {
		if (args.length < 3) {
			StdOut.println("Usage: java BurrowsWheeler (-|+) <infile> <outfile>");
			return;
				}
		BinaryIn in = new BinaryIn(args[1]);
		BinaryOut out = new BinaryOut(args[2]);
		char ch = args[0].charAt(0);
		if (ch == '-')
			transform(in, out);
		else if (ch == '+')
			inverseTransform(in,out);
		else if (ch == 'b') { // Do both encode then decode
			transform(in, out);
			out.close();
			BinaryIn in2 = new BinaryIn(args[2]);
			out = new BinaryOut(args[2]+".out");
			inverseTransform(in2,out);
		}
		out.close();
	}

}
