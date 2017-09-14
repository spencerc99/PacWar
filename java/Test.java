class Test {

	public static void main(String[] args) {
		PacGene pg1,pg2;
		DuelResults dr;

		try {
			pg1=new PacGene("11111111111111111111111111111111111111111111111111");
			pg2=new PacGene("13131313131313131313131313131313131313131313131313");
			dr=PacWarGuts.duel(pg1,pg2,500);
			System.out.println("Rounds: "+dr.rounds+" Gene1: "+dr.count1+" Gene2: "+dr.count2);
		} catch(Exception e) {
			System.err.println("Error: "+e);
		}
	}
}
