import static org.junit.Assert.*;
import org.junit.Test;


public class Giai_PTB1Test {
	
	@Test
	public void test1() {
		Giai_PTB1 test = new Giai_PTB1();
		float kq=test.giai_ptb1(10, -90);
		assertEquals(9, kq, 0);
	}
	
	@Test
	public void test2() {
		Giai_PTB1 test = new Giai_PTB1();
		float kq=test.giai_ptb1(10, 0);
		assertEquals(0, kq, 0);
	}
}
