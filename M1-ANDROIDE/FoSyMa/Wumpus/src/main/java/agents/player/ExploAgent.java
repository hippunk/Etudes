package agents.player;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Random;
import java.util.Map.Entry;

import jade.domain.DFService;
import jade.domain.FIPAException;
import jade.domain.FIPAAgentManagement.DFAgentDescription;
import jade.domain.FIPAAgentManagement.ServiceDescription;
import behaviours.communication.EnvoiMessage;
import behaviours.communication.Message;
import behaviours.communication.ReceptionMessage;
import behaviours.communication.TypeMessage;
import behaviours.deplacements.ExploWalkBehaviour;
import env.Attribute;
import env.Environment;
import env.Environment.Couple;
import agents.abstractAgent;

import org.graphstream.algorithm.Dijkstra;
import org.graphstream.graph.*;
import org.graphstream.graph.implementations.*;

public class ExploAgent extends abstractAgent{


	/**
	 * 
	 */
	private static final long serialVersionUID = -5759287597054385630L;
	public Graph graph = new SingleGraph("Map");
	public HashMap<String,String> nodeMap = new HashMap<String,String>();
	public String objectif = "unset";
	public Couple<String,List<Attribute>> noeudPrecedent = null;

	/**
	 * This method is automatically called when "agent".start() is executed.
	 * Consider that Agent is launched for the first time. 
	 * 			1 set the agent attributes 
	 *	 		2 add the behaviours
	 *          
	 */
	protected void setup(){

		super.setup();

		//get the parameters given into the object[]
		final Object[] args = getArguments();
		if(args[0]!=null){
			realEnv = (Environment) args[0];
			realEnv.deployAgent(this.getLocalName());

		}else{
			System.out.println("Erreur lors du tranfert des parametres");
		}		
		
		//Enregistrement sur le df
		DFAgentDescription dfd = new DFAgentDescription();
		dfd.setName(getAID()); /* getAID est l'AID de l'agent qui veut s'enregistrer*/
		ServiceDescription sd  = new ServiceDescription();
		sd.setType( "Explorer" ); /* il faut donner des noms aux services qu'on propose (ici explorer)*/
		sd.setName(getLocalName() );
		dfd.addServices(sd);
		        
		try {  
		      DFService.register(this, dfd );  
		}
		catch (FIPAException fe) { fe.printStackTrace(); }
		
		//Add the behaviours
		addBehaviour(new ExploWalkBehaviour(this,realEnv));
		//addBehaviour(new EnvoiMessage(this,"explorer",message));
		addBehaviour(new ReceptionMessage(this));
		System.out.println("the agent "+this.getLocalName()+ " is started");
		graph.display();

	}

	/**
	 * This method is automatically called after doDelete()
	 */
	protected void takeDown(){

	}
	
	public Boolean addExploredNode(String node){
		Boolean exp = true;
		if(!nodeMap.containsKey(node)){
			graph.addNode(node).addAttribute("ui.label", node);
			graph.getNode(node).addAttribute("ui.style", "fill-color: rgb(0,0,255);");
			nodeMap.put(node, "Explored");
		}
		else if(nodeMap.get(node).equals("Unexplored")){
			nodeMap.replace(node, "Explored");
			graph.getNode(node).addAttribute("ui.style", "fill-color: rgb(0,0,255);");
		}
		else
			exp = false;
		
		return exp;
	}
	
	public List<String> getUnexploredSuccessor(List<Couple<String,List<Attribute>>> lobs){
		List<String> liste = new LinkedList<String>();
		for(Couple<String, List<Attribute>> s : lobs){
			if(!nodeMap.containsKey(s.getL()) || nodeMap.get(s.getL()).equals("Unexplored")){

				liste.add(s.getL());	
			}
		}		
		
		return liste;
	}
	
	public void addUnexpNodes(String position,List<String> nodes){
		for(String s : nodes){
			if(!nodeMap.containsKey(s)){ //
				graph.addNode(s).addAttribute("ui.label", s);
				nodeMap.put(s, "Unexplored");
				
			}
			else if(nodeMap.get(s).equals("Suspect")){
				nodeMap.replace(s, "Unexplored");
				graph.getNode(s).addAttribute("ui.style", "fill-color: rgb(0,0,0);");
			}
			if(graph.getEdge(position+","+s) == null && graph.getEdge(s+","+position) == null && position != s){
				graph.addEdge(position+","+s, position, s).addAttribute("length", 1);
			}
			else if(graph.getEdge(position+","+s) == null && position != s){
				graph.getEdge(s+","+position).addAttribute("length", 1);
			}
			else if(graph.getEdge(s+","+position) == null && position != s){
				graph.getEdge(position+","+s).addAttribute("length", 1);
			}
		}
	}
	
	public void addSuspectNodes(String position,List<String> nodes){
		for(String s : nodes){
			if(!nodeMap.containsKey(s)){ //
				graph.addNode(s).addAttribute("ui.label", s);
				graph.getNode(s).addAttribute("ui.style", "fill-color: rgb(255,0,0);");
				nodeMap.put(s, "Suspect");
				
			}
			if(graph.getEdge(position+","+s) == null && graph.getEdge(s+","+position) == null && position != s){
				graph.addEdge(position+","+s, position, s).addAttribute("length", 9999);
			}
		}
	}	
	/*public void sendExploredNodeInfo(String node){
		List<String> liste = new LinkedList<String>();
		liste.add(node);
		//System.out.println("Liste Explored : "+liste);
		Message messageExplored = new Message(TypeMessage.Explored,liste);
		addBehaviour(new EnvoiMessage(this,"Explorer",messageExplored));
	}*/
	
	public void sendNodesInfos(String myPosition,List<String> nodes){
		List<String> liste = new LinkedList<String>(nodes);
		liste.add(0, myPosition);
		//System.out.println("unexp nodes"+nodes);
		//System.out.println("liste nodes + pos"+liste);

		//Envoi Message noeud non explorés si pas seulement MyPosition dans la liste
		if(nodes.size() > 1){
			Message messageUnexplored = new Message(TypeMessage.Unexplored,liste);
			addBehaviour(new EnvoiMessage(this,"Explorer",messageUnexplored));
		}
	}
	
	public Boolean moveToRandUnexpNode(String myPosition,List<String> unexpNodes){
		Random r= new Random();
		List<String> suspects = getFlagedNodes("Suspect");
		for(String s : suspects)
			unexpNodes.remove(s);
		int moveId=r.nextInt(unexpNodes.size());
		return move(myPosition, unexpNodes.get(moveId));	
	}
	
	public List<String> getFlagedNodes(String flag){
		List<String> liste = new LinkedList<String>();
		
		for(Entry<String,String> entry : nodeMap.entrySet()){
			if(entry.getValue().equals(flag)){
				liste.add(entry.getKey());					
			}	
		}
		
		return liste;
	}
	
	public String chooseRandUnexpNode(){
		List<String> liste = new LinkedList<String>();

		String s = "unset";
		
		liste = getFlagedNodes("Unexplored");
		if(!liste.isEmpty()){//Si il reste des noeuds inexplorées
			System.out.println("Coincé : "+liste);
			Random r= new Random();

			int moveId=r.nextInt(liste.size());
			s = liste.get(moveId);
			//graph.display();
		}
		
		else{ //Si non, explo terminée
			System.out.println("J'ai tout vu "+nodeMap); 
			//graph.display();

		}
		
		return s;
	}
	
	public Boolean randMove(String myPosition,List<String> liste){
		
		Random r= new Random();

		int moveId=r.nextInt(liste.size());
		String next = liste.get(moveId);
		return move(myPosition,next);
		
	}
	
	public Boolean nextStepToObjective(String myPosition){
		String next;
        Dijkstra dijkstra = new Dijkstra(Dijkstra.Element.EDGE, null, "length");
        
        // Compute the shortest paths in g from A to all nodes
        dijkstra.init(graph);
        dijkstra.setSource(graph.getNode(myPosition));
        dijkstra.compute();
         
        // Print the shortest path from A to B
        System.out.println("Path"+dijkstra.getPath(graph.getNode(objectif)));
        next = dijkstra.getPath(graph.getNode(objectif)).getNodePath().get(1).toString(); //On degage le dernier noeud qui est le noeud courant

        return move(myPosition, next);
	}
	
	public Boolean nextStepToClosestUnexplored(String myPosition){
		String next = "unset";
		int tmp = 9999;
		Path tmp2;
        Dijkstra dijkstra = new Dijkstra(Dijkstra.Element.EDGE, null, "length");
        
        // Compute the shortest paths in g from A to all nodes
        dijkstra.init(graph);
        dijkstra.setSource(graph.getNode(myPosition));
        dijkstra.compute();
        
        //Choose the closest unexplored node
        List<String> liste = getFlagedNodes("Unexplored");
        for(String s : liste){
        	tmp2 = dijkstra.getPath(graph.getNode(s));
        	if(tmp2.size() < tmp){
        		tmp = tmp2.size();
        		next = tmp2.getNodePath().get(1).toString();      		
        	}
        }
               
        // Print the shortest path from A to B
        //System.out.println("Path"+dijkstra.getPath(graph.getNode(objectif)));
        //next = dijkstra.getPath(graph.getNode(objectif)).getNodePath().get(1).toString(); //On degage le dernier noeud qui est le noeud courant
		//System.out.println("Noeud suivant :"+next);
	    return move(myPosition, next);
	}

	public List<String> getSuccessors(String myPosition,List<Couple<String, List<Attribute>>> lobs) {
		List<String> liste = new LinkedList<String>();
		for(Couple<String, List<Attribute>> s : lobs){
				liste.add(s.getL());	
				liste.remove(myPosition);
		}		
		
		return liste;
	}
}
