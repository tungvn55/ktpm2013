
public class Giai_PTB1 {
	public float giai_ptb1(int a, int b) {
		if(a==0.0 && b==0.0) {
			throw new IllegalArgumentException("Co vo so nghiem!");
		}
		else if(a==0.0) {
			throw new IllegalArgumentException("Vo nghiem!");
			}
			else return (float)-b/(float)a;
		
	}
}
