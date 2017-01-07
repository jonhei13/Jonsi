package S2;


import com.sun.xml.internal.bind.v2.TODO;
import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * @author Erick on 11/09/16.
 */
public class PointTest {

    private static final double DELTA = 0.0001;
    Point p;
    Point that;

    public PointTest() {
        p = new Point(3,5);
        that = new Point(4,7);
    }

    @Test
    public void slopeTo() throws Exception {
        Assert.assertEquals(2.0, p.slopeTo(that), DELTA);
    }

    @Test(expected = IllegalStateException.class)
    public void compareTo() throws Exception {
        p.compareTo(new Point(2,5));
    }


    @Test
    public void toStringOutputTrue() throws Exception {
        assertEquals("(3, 5)", p.toString());
    }

    @Test
    public void main() throws Exception {
        //TODO run array of files to main
    }

}