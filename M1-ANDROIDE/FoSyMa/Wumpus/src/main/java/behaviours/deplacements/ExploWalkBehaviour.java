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
		super(myagent, 1000);
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
			
			//Ajout Noeud exploré dans graphe agent
			myagent.addExploredNode(myPosition);
			
			//Envoi Message noeud exploré
			myagent.sendExploredNodeInfo(myPosition);
						
			//Ajout Noeuds inexplorées dans graphe (seulement si pas déjà explorées)
			List<String> unexpNodes = myagent.getUnexploredSuccessor(lobs);
			myagent.addUnexploredNodes(myPosition,unexpNodes);
			
			//Envoi Message noeud non explorés si plus d'un noeud dans la liste
			myagent.sendUnexploredNodeInfo(myPosition,unexpNodes);
			
			if(!unexpNodes.isEmpty()){ //Si il existe un suivant unexplored
				myagent.moveToRandUnexpNode(myPosition,unexpNodes);
			}
			else if(myagent.objectif.equals("unset")){ //Si non définir objectif
				
				myagent.objectif = myagent.chooseRandUnexpNode();
			}
			else{ //Si objectif défini
				//System.out.println(objectif);
				//Dijkstra
				String next = myagent.nextStepToObjective(myPosition);
				System.out.println("Noeud suivant :"+next);
			    myagent.move(myPosition, next);
			}

		}
	}
}
