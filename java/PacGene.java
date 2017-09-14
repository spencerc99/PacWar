
public class PacGene {

	private char[] u=new char[4];
	private char[] v=new char[16];
	private char[] w=new char[3];
	private char[] x=new char[3];
	private char[] y=new char[12];
	private char[] z=new char[12];

	public PacGene(String a, String b, String c, String d, String e, String f) throws Exception {
		if(a.length()!=4) throw new Exception("U must be 4 chars");
		if(b.length()!=16) throw new Exception("V must be 16 chars");
		if(c.length()!=3) throw new Exception("W must be 3 chars");
		if(d.length()!=3) throw new Exception("X must be 3 chars");
		if(e.length()!=12) throw new Exception("Y must be 12 chars");
		if(f.length()!=12) throw new Exception("Z must be 12 chars");
		u=a.toCharArray();
		v=b.toCharArray();
		w=c.toCharArray();
		x=d.toCharArray();
		y=e.toCharArray();
		z=f.toCharArray();
	}

	public PacGene(String s) throws Exception {
		if(s.length()!=50) throw new Exception("Gene must be 50 chars");
		s.getChars(0,4,u,0);
		s.getChars(4,20,v,0);
		s.getChars(20,23,w,0);
		s.getChars(23,26,x,0);
		s.getChars(26,38,y,0);
		s.getChars(38,50,z,0);
	}

	public String toString() {
		return (new String(u)+new String(v)+new String(w)+new String(x)+new String(y)+new String(z));
	}
}