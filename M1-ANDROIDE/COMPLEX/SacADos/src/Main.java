import java.util.List;


public class Main {

	public static void main(String[] args) {
		GenerateurObjets gen = new GenerateurObjets(10,10,3,18,1000);
		gen.genererListe();
		gen.afficherListe();
		List<Objet> liste = gen.getListe();
	}

}
