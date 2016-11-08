package JonTesting;

import edu.princeton.cs.algs4.TarjanSCC;
import javafx.scene.control.Tab;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

/**
 * Created by jonsi on 10/24/2016.
 */
@SuppressWarnings("Duplicates")
public class verkefni10 {
    private static ArrayList<String> Tables;
    private static ArrayList<String> Keys1;
    private static ArrayList<String> Keys2;
    private static ArrayList<String> Keys3;
    private static ArrayList<String> Keys4;

    public static void main(String[] Args) throws IOException {
        Tables = new ArrayList<String>();
        Keys1 = new ArrayList<String>();
        Keys2 = new ArrayList<String>();
        Keys3 = new ArrayList<String>();
        Keys4 = new ArrayList<String>();


        PrintWriter out = new PrintWriter(new FileWriter("C:\\Users\\jonsi\\Desktop\\Assignment10-2.txt"));
        String func;
        Tables.add("Persons");
        Tables.add("Boats");
        Tables.add("Projects");
        Tables.add("Courses");


        Keys1.add("ID");
        Keys1.add("PN");
        Keys1.add("DID");
        Keys1.add("DN");
        Keys1.add("SSN");
        Keys1.add("Z");
        Keys1.add("T");

        Keys2.add("BL");
        Keys2.add("bNo");
        Keys2.add("Z");
        Keys2.add("T");
        Keys2.add("BN");
        Keys2.add("SSN");


        Keys3.add("ID");
        Keys3.add("PID");
        Keys3.add("DID");
        Keys3.add("DN");
        Keys3.add("PN");
        Keys3.add("DM");


        Keys4.add("CID");
        Keys4.add("TID");
        Keys4.add("BID");
        Keys4.add("SID");
        Keys4.add("TN");
        Keys4.add("SN");
        Keys4.add("SY");

        for (int i = 0; i < Tables.size(); i++) {
            if (i == 0) {
                for (int k = 0; k < Keys1.size(); k++) {
                    for (int j = 0; j < Keys1.size(); j++) {

                        if (Keys1.get(k) != Keys1.get(j)) {
                            func = "SELECT " + "'" + Tables.get(i) + ": ";
                            func += Keys1.get(k) + "-->" + Keys1.get(j) + "' AS FUNCDEPENDANT, CASE WHEN COUNT(*)=0 THEN 'FUNCTIONAL DEPENDANT' ELSE 'NOT FUNCTIONAL DEPENDANT' END \n";
                            func += "FROM (";
                            func += "SELECT " + Keys1.get(k) + "\n";
                            func += "FROM " + Tables.get(i) + "\n";
                            func += "GROUP BY " + Keys1.get(k) + "\n";
                            func += "HAVING COUNT(DISTINCT " + Keys1.get(j) + ") > 1\n";
                            func += ") X;";
                            out.println(func);
                        }
                    }
                }

            }


            if (i == 2) {
                for (int k = 0; k < Keys2.size(); k++) {
                    for (int j = 0; j < Keys2.size(); j++) {

                        if (Keys2.get(k) != Keys2.get(j)) {
                            func = "SELECT " + "'" + Tables.get(i) + ": ";
                            func += Keys2.get(k) + "-->" + Keys2.get(j) + "' AS FUNCDEPENDANT, CASE WHEN COUNT(*)=0 THEN 'FUNCTIONAL DEPENDANT' ELSE 'NOT FUNCTIONAL DEPENDANT' END \n";
                            func += "FROM (";
                            func += "SELECT " + Keys2.get(k) + "\n";
                            func += "FROM " + Tables.get(i) + "\n";
                            func += "GROUP BY " + Keys2.get(k) + "\n";
                            func += "HAVING COUNT(DISTINCT " + Keys2.get(j) + ") > 1\n";
                            func += ") X;";
                            out.println(func);
                        }
                    }
                }

            }
            if (i == 3) {
                for (int k = 0; k < Keys3.size(); k++) {
                    for (int j = 0; j < Keys3.size(); j++) {

                        if (Keys3.get(k) != Keys3.get(j)) {
                            func = "SELECT " + "'" + Tables.get(i) + ": ";
                            func += Keys3.get(k) + "-->" + Keys3.get(j) + "' AS FUNCDEPENDANT, CASE WHEN COUNT(*)=0 THEN 'FUNCTIONAL DEPENDANT' ELSE 'NOT FUNCTIONAL DEPENDANT' END \n";
                            func += "FROM (";
                            func += "SELECT " + Keys3.get(k) + "\n";
                            func += "FROM " + Tables.get(i) + "\n";
                            func += "GROUP BY " + Keys3.get(k) + "\n";
                            func += "HAVING COUNT(DISTINCT " + Keys3.get(j) + ") > 1\n";
                            func += ") X;";
                            out.println(func);
                        }
                    }
                }

            }
            if (i == 4) {
                for (int k = 0; k < Keys4.size(); k++) {
                    for (int j = 0; j < Keys4.size(); j++) {

                        if (Keys4.get(k) != Keys4.get(j)) {
                            func = "SELECT " + "'" + Tables.get(i) + ": ";
                            func += Keys4.get(k) + "-->" + Keys4.get(j) + "' AS FUNCDEPENDANT, CASE WHEN COUNT(*)=0 THEN 'FUNCTIONAL DEPENDANT' ELSE 'NOT FUNCTIONAL DEPENDANT' END \n";
                            func += "FROM (";
                            func += "SELECT " + Keys4.get(k) + "\n";
                            func += "FROM " + Tables.get(i) + "\n";
                            func += "GROUP BY " + Keys4.get(k) + "\n";
                            func += "HAVING COUNT(DISTINCT " + Keys4.get(j) + ") > 1\n";
                            func += ") X;";
                            out.println(func);
                        }
                    }
                }


            }

            out.close();
        }

    }
}