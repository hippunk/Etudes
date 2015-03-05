package agents.mobs;

import java.io.IOException;
import java.util.Iterator;
import java.util.List;
import java.util.Random;

import org.graphstream.graph.Node;

import agents.abstractAgent;
import env.Attribute;
import env.Environment;
import env.Environment.Couple;
import jade.core.AID;
import jade.core.Agent;
import jade.core.behaviours.SimpleBehaviour;
import jade.core.behaviours.TickerBehaviour;
import jade.lang.acl.ACLMessage;


public class DummyWumpusAgent extends abstractAgent{


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
			realEnv.deployWumpus((String) args[1]);

		}else{
			System.out.println("Erreur lors du tranfert des parametres");
		}

		//Add the behaviours
		addBehaviour(new RandomWalkBehaviour(this,realEnv));

		System.out.println("the  agent "+this.getLocalName()+ " is started");

	}

	/**
	 * This method is automatically called after doDelete()
	 */
	protected void takeDown(){

	}


	/**************************************
	 * 
	 * 
	 * 				BEHAVIOURS
	 * 
	 * 
	 **************************************/


	public class RandomWalkBehaviour extends TickerBehaviour{
		/**
		 * When an agent choose to move
		 *  
		 */
		private static final long serialVersionUID = 9088209402507795289L;

		private boolean finished=false;
		private Environment realEnv;

		public RandomWalkBehaviour (final Agent myagent,Environment realEnv) {
			super(myagent,2000);
			//super(myagent);
			this.realEnv=realEnv;
		}

		@Override
		public void onTick() {

			String myPosition=getCurrentPosition();
			if (myPosition!=""){
				List<Couple<String,List<Attribute>>> lobs=observe(myPosition);
				//System.out.println("lobs: "+lobs);

//				try {
//					System.out.println("Press a key to move to the next step agents");
//					System.in.read();
//				} catch (IOException e) {
//					// TODO Auto-generated catch block
//					e.printStackTrace();
//				}



				Random r= new Random();

				int moveId=r.nextInt(lobs.size());

				move(myPosition, lobs.get(moveId).getL());
			}else{
				System.out.println("Probleme, position vide");
				System.exit(D_UNKNOWN);
			}

		}

	}


}
