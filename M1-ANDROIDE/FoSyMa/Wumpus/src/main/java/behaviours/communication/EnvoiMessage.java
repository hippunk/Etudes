package behaviours.communication;

import java.io.IOException;
import java.io.Serializable;
import java.util.LinkedList;
import java.util.List;

import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.SimpleBehaviour;
import jade.domain.DFService;
import jade.domain.FIPAException;
import jade.domain.FIPAAgentManagement.DFAgentDescription;
import jade.domain.FIPAAgentManagement.ServiceDescription;
import jade.lang.acl.ACLMessage;

public class EnvoiMessage extends SimpleBehaviour{
	/**
	 * When an agent choose to communicate with others agents in order to reach a precise decision, 
	 * it tries to form a coalition. This behaviour is the first step of the paxos
	 *  
	 */
	private static final long serialVersionUID = 9088209402507795289L;

	private boolean finished=false;
	private String cibles;
	private Agent myagent;
	private List<AID> listeCibles = new LinkedList<AID>();
	private Message message;
	
	public EnvoiMessage(final Agent myagent, String cibles,Message message) {
		super(myagent);
		this.myagent = myagent;
		this.cibles = cibles;
		this.message = message;

	}


	public void action() {
		//Create a message in order to send it to the choosen agent
		final ACLMessage msg = new ACLMessage(ACLMessage.INFORM);
		msg.setSender(this.myAgent.getAID());
		//msg.setLanguage(MyOntology.LANGUAGE);
		//msg.setOntology(MyOntology.ONTOLOGY_NAME);
		//msg.setProtocol(MyOntology.PAXOS_PREPARE);
		

		//Recuperation liste Agents
		DFAgentDescription dfd = new DFAgentDescription();
		ServiceDescription sd  = new ServiceDescription();
		sd.setType( cibles ); /* le même nom de service que celui qu'on a déclaré*/
		dfd.addServices(sd);
		            
		DFAgentDescription[] result = null;
		try {
			result = DFService.search(myagent, dfd);
		} catch (FIPAException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		//Chargement des AID dans une liste
		if(result.length>0){
			for(DFAgentDescription agent : result){
						listeCibles.add(agent.getName());
			}
		}
		
		//On retire l'AID de l'agent courant de la liste
		listeCibles.remove(myagent.getAID());
		
		//Si la liste n'est pas vide on envoie le message
		if(!listeCibles.isEmpty()){
			for(AID aid : listeCibles)
				msg.addReceiver(aid);

			try {
				msg.setContentObject((Serializable)message);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	
			this.myAgent.send(msg);
			this.finished=true;
			System.out.println("----> Message sent to "+msg.getAllReceiver().next()+" ,content= "+message);
		}
	}

	public boolean done() {
		return finished;
	}

}
