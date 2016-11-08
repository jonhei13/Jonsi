// Move-to-front
// 11 October 2016, Magnus M. Halldorsson
package S5;
import edu.princeton.cs.algs4.*;

import java.util.ArrayList;

@SuppressWarnings("Duplicates")
public class MoveToFront {

	private static final int R = 256;
	private static final int Bits = 8;
	// apply move-to-front encoding
	public static void encode(BinaryIn in, BinaryOut out) {
		ArrayList<Integer> Arr = new ArrayList<Integer>();
		for (int i = 0; i < R; i++)
			Arr.add(i);
		String Input = in.readString();
		char[] Convert = Input.toCharArray();
		for (int IndexData : Convert){
			for (int x = 0; x < Arr.size(); x++) {
				if (Arr.get(x) == IndexData) {
					int ToFront = Arr.get(x);
					Arr.remove(x);
					Arr.add(0, ToFront);
					out.write(x, Bits);
					break;
				}
			}
		}
		out.flush();
	}
	
	// apply move-to-front decoding
	public static void decode(BinaryIn in, BinaryOut out) {
		ArrayList<Integer> Arr = new ArrayList<Integer>();
		for (int i = 0; i < R; i++)
			Arr.add(i);
		String Input = in.readString();
		char[] Convert = Input.toCharArray();
		for (int IndexData : Convert) {
				int remove = Arr.remove(IndexData);
				Arr.add(0, remove);
				out.write(remove, Bits);
		}
		out.flush();
	}
	// if args[0] is '-', apply move-to-front encoding
	// if args[0] is '+', apply move-to-front decoding
	// if args[0] is 'b', perform both
	public static void main(String[] args) {
		if (args.length < 1) {
			StdOut.println("Usage: java MoveToFront (-|+|b) <infile> <outfile>");
			return;
		}
		BinaryIn in = new BinaryIn(args[1]);
		BinaryOut out = new BinaryOut(args[2]);
		char ch = args[0].charAt(0);
		if (ch == '-')
			encode(in, out);
		else if (ch == '+')
			decode(in,out);
		else if (ch == 'b') { // Do both encode then decode
			encode(in,out);
			out.close();
			BinaryIn in2 = new BinaryIn(args[2]);
			out = new BinaryOut(args[2]+".out");
			decode(in2,out);
		}
		out.close(); 
	}

}
