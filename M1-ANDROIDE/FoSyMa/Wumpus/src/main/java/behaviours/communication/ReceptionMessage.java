package behaviours.communication;

import java.awt.TrayIcon.MessageType;
import java.io.Serializable;

import agents.player.ExploAgent;
import jade.core.Agent;
import jade.core.behaviours.TickerBehaviour;
import jade.lang.acl.ACLMessage;
import jade.lang.acl.MessageTemplate;
import jade.lang.acl.UnreadableException;

public class ReceptionMessage extends TickerBehaviour{
	/**
	 * When an agent choose to communicate with others agents in order to reach a precise decision, 
	 * it tries to form a coalition. This behaviour is the first step of the paxos
	 *  
	 */
	private static final long serialVersionUID = 9088209402507795289L;

	private boolean finished=false;
	private ExploAgent myagent;

	public ReceptionMessage(final ExploAgent myagent) {
		
		super(myagent,500);
		this.myagent = myagent;
	}


	public void onTick() {
		//1) receive the message
		final MessageTemplate msgTemplate = MessageTemplate.MatchPerformative(ACLMessage.INFORM);
			//MessageTemplate.and(
				//MessageTemplate.MatchPerformative(ACLMessage.DISCONFIRM),
				//MessageTemplate.and(
				//		MessageTemplate.MatchProtocol(MyOntology.PAXOS_QUIT_COALITION),
				//		MessageTemplate.and(
				//				MessageTemplate.MatchLanguage(MyOntology.LANGUAGE),
				//				MessageTemplate.MatchOntology(MyOntology.ONTOLOGY_NAME))
				//)
		
		//Traitement de la boite aux lettres
		ACLMessage msg = this.myAgent.receive(msgTemplate);
		while(msg!=null){	
				Message message = null;
				try {
					message = (Message) msg.getContentObject();
				} catch (UnreadableException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				//System.out.println("<----Message received from "+msg.getSender()+" ,content= "+message);
				switch(message.type){
					case Explored:
						myagent.addExploredNode(message.contenu.get(0));
						break;
					case Safe:
						break;
					case Smell:
						break;
					case Suspect:
						break;
					case Treasure:
						break;
					case Unexplored:
						String pos = message.contenu.get(0);
						message.contenu.remove(pos);
						myagent.addUnexploredNodes(pos, message.contenu);
						break;
					default:
						break;
				
				}

				msg = this.myAgent.receive(msgTemplate);
		}
	}
}