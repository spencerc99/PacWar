
public class PacWarGuts {

	static {
		try {
			System.loadLibrary("PacWarGuts");
		} catch(Exception e) {
			System.err.println("Failed to load library");
			System.exit(1);
		}
	}

	public static DuelResults duel(PacGene g1, PacGene g2, int maxRounds) {
		return fastDuel(g1.toString(),g2.toString(),maxRounds);
	}

	public static DuelResults duel(String g1, String g2, int maxRounds) {
		return fastDuel(g1,g2,maxRounds);
	}

	private static native DuelResults fastDuel(String s1, String s2, int maxRounds);
}