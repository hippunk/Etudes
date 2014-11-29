public class Objet {

	private int valeur;
	private int poids;
			
	public Objet(int valeur, int poids){
		this.valeur = valeur;
		this.poids = poids;		
	}

	@Override
	public String toString() {
		return "Objet [valeur=" + valeur + ", poids=" + poids + "]";
	}

	public int getValeur() {
		return valeur;
	}

	public void setValeur(int valeur) {
		this.valeur = valeur;
	}

	public int getPoids() {
		return poids;
	}

	public void setPoids(int poids) {
		this.poids = poids;
	}	
}
