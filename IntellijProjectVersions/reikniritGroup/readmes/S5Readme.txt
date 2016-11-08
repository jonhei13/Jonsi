/******************************************************************************
 *  Name: Jón Heiðar Sigmundsson	
 *  LoginID: jonhei13
 *  Group#:    
 *
 *  Partner Name:       
 *  Partner Login ID:      
 *  Partner Group#:    
 *
 *  Hours to complete assignment (optional): about 15-20
 *
 ******************************************************************************/



/******************************************************************************
 *  List in table format which input files you used to test your program.
 *  Fill in columns for how long your program takes to compress and
 *  decompress these instances (by applying BurrowsWheeler, MoveToFront,
 *  and Huffman in succession). Also, fill in the third column for
 *  the compression ratio (number of bytes in compressed message 
 *  divided by the number of bytes in the message).
 *****************************************************************************/

File     			Encoding Time    Decoding time      Compression ratio
------------------------------------------------------------------------
amendments.txt		0.051				0,064				18kb / 16kb = 	1.125			
alphanum.txt		0.017				0.017				1kb / 1kb = 	1
mobydick.txt		2.159				3.373				1195kb / 409kb =  2.9

/******************************************************************************
 *  Compare the results of your program (compression ratio and running
 *  time) on mobydick.txt to that of the most popular Windows
 *  compression program (pkzip) or the most popular Unix/Mac one (gzip).
 *  If you don't have pkzip, use 7zip and compress using zip format.
 *****************************************************************************/
Type						File				Encoding 			Decoding		Compression ratio
Burrows-Move-Huff		 	MobyDick.txt 		2.159				3.373				1195kb / 409kb =  2.9
7zip						MobyDick.txt												1195kb / 394kb =  3.03

/******************************************************************************
 *  Give the order of growth of the running time of each of the 6
 *  methods as a function of the input size N and the alphabet size R
 *  both in practice (on typical English text inputs) and in theory
 *  (in the worst case), e.g., N, N + R, N log N, N^2, or R N.
 *
 *  Include the time for sorting circular suffixes in the
 *  Burrows-Wheeler encoder.
 *****************************************************************************/

                                      typical            worst
---------------------------------------------------------------------
BurrowsWheeler transform()			  2N				 2N
BurrowsWheeler inverseTransform()	  3N			     N + N * (N-1) 
MoveToFront encode()				  R+N				 R*N
MoveToFront decode()				  R+N				 R*N
Huffman compress()                    N + R log R        N + R log R
Huffman expand()                      N                  N





/******************************************************************************
 *  Known bugs / limitations.
 *****************************************************************************/
Coult not get the worst case order of growth in burrowsWheeler inverse, to proper performance requirment.


/******************************************************************************
 *  Describe whatever help (if any) that you received.
 *  Don't include readings, lectures, and precepts, but do
 *  include any help from people (including course staff, lab TAs,
 *  classmates, and friends) and attribute them by name.
 *****************************************************************************/
Only readings from piazza.

/******************************************************************************
 *  Describe any serious problems you encountered.                    
 *****************************************************************************/
i had serious problem with inverse transformation in burrows wheel i made a mistake with the one if sentence instead of saying i >= 1 i had i > 1
wich gave the correct values for every input with only 1 line. But soon as i was testing amendments it gave wrong output put the right words, except not the right lines.
So it took me a good time to figure out how and where the error was, since it was rather hard to debug.


/******************************************************************************
 *  If you worked with a partner, assert below that you followed
 *  the protocol as described on the assignment page. Give one
 *  sentence explaining what each of you contributed.
 *****************************************************************************/



/******************************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing the assignment, and whether    
 *  you enjoyed doing it.                                             
 *****************************************************************************/
Really fun project and made you think alot 