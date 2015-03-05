package agents.player;

import java.io.IOException;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Random;

import org.graphstream.graph.Node;

import agents.abstractAgent;
import behaviours.communication.EnvoiMessage;
import behaviours.communication.Message;
import behaviours.communication.ReceptionMessage;
import behaviours.communication.TypeMessage;
import behaviours.deplacements.RandomWalkBehaviour;
import env.Attribute;
import env.Environment;
import env.Environment.Couple;
import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.SimpleBehaviour;
import jade.core.behaviours.TickerBehaviour;
import jade.domain.DFService;
import jade.domain.FIPAException;
import jade.domain.FIPAAgentManagement.DFAgentDescription;
import jade.domain.FIPAAgentManagement.ServiceDescription;
import jade.lang.acl.ACLMessage;


public class DummyExploAgent extends abstractAgent{


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
		sd.setType( "DummyExplorer" ); /* il faut donner des noms aux services qu'on propose (ici explorer)*/
		sd.setName(getLocalName() );
		dfd.addServices(sd);
		        
		try {  
		      DFService.register(this, dfd );  
		}
		catch (FIPAException fe) { fe.printStackTrace(); }
		
		/*List<String> test = new LinkedList<String>();
		test.add("Pouet");
		test.add("Yolo");
		Message message = new Message(TypeMessage.Smell,test);*/
		
		//Add the behaviours
		addBehaviour(new RandomWalkBehaviour(this,realEnv));
		//addBehaviour(new EnvoiMessage(this,"explorer",message));
		//addBehaviour(new ReceptionMessage(this));

		System.out.println("the agent "+this.getLocalName()+ " is started");

	}

	/**
	 * This method is automatically called after doDelete()
	 */
	protected void takeDown(){

	}

}
