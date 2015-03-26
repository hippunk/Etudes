package behaviours.deplacements;

import jade.core.Agent;
import jade.core.behaviours.TickerBehaviour;

import java.util.List;

import agents.player.ExploAgent;
import env.Attribute;
import env.Environment;
import env.Environment.Couple;

public class ExploWalkBehaviour extends TickerBehaviour{
	/**
	 * When an agent choose to move
	 *  
	 */
	private static final long serialVersionUID = 9088209402507795289L;

	private boolean finished=false;
	private Environment realEnv;
	private ExploAgent myagent;

	public ExploWalkBehaviour (final Agent myagent,Environment realEnv) {
		super(myagent, 2000);
		this.realEnv=realEnv;
		this.myagent = (ExploAgent) myagent;
	}

	@Override
	public void onTick() {
		String myPosition=myagent.getCurrentPosition();
		if(myagent.objectif.equals(myPosition))
			myagent.objectif = "unset";
		
		if (myPosition!=""){
			List<Couple<String,List<Attribute>>> lobs=myagent.observe(myPosition);
			System.out.println("lobs: "+lobs+"pos :"+myPosition);
						
			//Ajout noeud exploré
			Boolean exp = myagent.addExploredNode(myPosition);

			
			List<String> successorNodes = myagent.getSuccessors(myPosition,lobs);
			//if(exp){
				//Ajout Noeuds inexplorées dans graphe (seulement si pas déjà explorées)
				
				//System.out.println(successorNodes);
				if(myagent.noeudPrecedent != null && lobs.get(0).getR().contains(Attribute.WIND) && myagent.noeudPrecedent.getR().contains(Attribute.WIND)){
						myagent.addSuspectNodes(myPosition, successorNodes);
				}
				else{
					myagent.addUnexpNodes(myPosition,successorNodes);
					
					//Envoi Message noeud non explorés si plus d'un noeud dans la liste
					myagent.sendNodesInfos(myPosition,successorNodes);
				}
			//}
			
			
			
			List<String> suspects = myagent.getFlagedNodes("Suspect");
			for(String s : suspects)
				successorNodes.remove(s);
			
			List<String> unexpNodes = myagent.getUnexploredSuccessor(lobs);
			if(!unexpNodes.isEmpty()){ //Si il existe un suivant unexplored
				if(!myagent.moveToRandUnexpNode(myPosition,unexpNodes))	{
					//System.out.println("resolve");
					while(!myagent.randMove(myPosition, successorNodes));
				}
			}
			else{ //Si objectif défini
				//System.out.println(objectif);
				//Dijkstra
				if(!myagent.nextStepToClosestUnexplored(myPosition)){
					//System.out.println("resolve");
					while(!myagent.randMove(myPosition, successorNodes));
				}

			}
			
			
			//Gestion des puits
			if(myagent.noeudPrecedent != null)
				System.out.println("Actuel : "+ lobs.get(0).getR()+" Precedent : "+myagent.noeudPrecedent.getR());

			if(myagent.noeudPrecedent != null && lobs.get(0).getR().contains(Attribute.WIND) && myagent.noeudPrecedent.getR().contains(Attribute.WIND))
				System.out.println("A coté d'un puit");
			
			myagent.noeudPrecedent = lobs.get(0);

		}
	}
}
