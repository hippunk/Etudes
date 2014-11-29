import java.util.Random;
import java.util.List;
import java.util.LinkedList;

/* ======================================================================
GENERATOR.c, David Pisinger   april 1994
====================================================================== */

/* Le code du générateur d'objet :
*
*   D. Pisinger
*   Core problems in Knapsack Algorithms
*   Operations Research (accepted for publication)
*
* Further details on the project can also be found in
*
*   D. Pisinger
*   Algorithms for Knapsack Problems
*   Report 95/1, DIKU, University of Copenhagen
*   Universitetsparken 1
*   DK-2100 Copenhagen
*
* The current code generates randomly generated instances and
* writes them to a file. Different capacities are considered to
* ensure proper testing.
*
* The code has been tested on a hp9000/735, and conforms with the
* ANSI-C standard apart from some of the timing routines (which may
* be removed). To compile the code use:
*
*   cc -Aa -O -o generator generator.c -lm
* 
* The code is run by issuing the command
*
*   generator n r type i S
*
* where n: number of items, 
*       r: range of coefficients, 
*       type: 1=uncorr., 2=weakly corr., 3=strongly corr., 4=subset sum
*       i: instance no
S: number of tests in series (typically 1000)
* output will be written to the file "test.in".
*
* Please do not re-distribute. A new copy can be obtained by contacting
* the author at the adress below. Errors and questions are refered to:
*
*   David Pisinger, associate professor
*   DIKU, University of Copenhagen,
*   Universitetsparken 1,
*   DK-2100 Copenhagen.
*   e-mail: pisinger@diku.dk
*   fax: +45 35 32 14 01
*/

public class GenerateurObjets {
	private Random rand = null;
	private List<Objet> listeObjet;
	private int nbObjet;
	private int typeGen;
	private int seed;
	private int range;
	private int noTest;
	private int resultTest = 0;
	
	public GenerateurObjets(int nbObjet,int range,int typeGen,int seed,int noTest){
		this.nbObjet = nbObjet;
		this.typeGen = typeGen;
		this.seed = seed;
		this.range = range;
		this.noTest = noTest;
		
		rand = new Random(this.seed);
		listeObjet = new LinkedList<Objet>();
	}

	public void afficherListe(){
		for (Objet obj : listeObjet)
		    System.out.println(obj);
		System.out.println(resultTest);
	}
	
	public void genererListe(){

		int r1 = this. range/10;
		int valeur = 0;
		int poids = 0;
		int sum = 0;
		for(int i = 0;i< nbObjet;i++)
		{
			poids = rand.nextInt(range) +1;
			switch(typeGen){
				case 1:
					valeur = rand.nextInt(seed+1);
					break;
				case 2:
					valeur = rand.nextInt(2*r1+1)+poids-r1;
					if (valeur <= 0) 
						valeur = 1;
					break;
				case 3:
					valeur = poids+10;
					break;
				case 4:
					valeur = poids;
					break;
			}
			listeObjet.add(new Objet(valeur,poids));
			sum += poids;
		}
		
		resultTest = (seed*sum)/(noTest+1);
		if(resultTest <= range)
			resultTest = range+1;
	}
	
	public List<Objet> getListe(){
		return listeObjet;
	}
}
