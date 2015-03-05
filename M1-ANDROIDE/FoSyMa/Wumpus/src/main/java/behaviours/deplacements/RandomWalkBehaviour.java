package behaviours.deplacements;

import jade.core.Agent;
import jade.core.behaviours.TickerBehaviour;

import java.util.List;
import java.util.Random;

import agents.abstractAgent;
import env.Attribute;
import env.Environment;
import env.Environment.Couple;

public class RandomWalkBehaviour extends TickerBehaviour{
	/**
	 * When an agent choose to move
	 *  
	 */
	private static final long serialVersionUID = 9088209402507795289L;

	private boolean finished=false;
	private Environment realEnv;
	private abstractAgent myagent;

	public RandomWalkBehaviour (final Agent myagent,Environment realEnv) {
		super(myagent, 1000);
		//super(myagent);
		this.realEnv=realEnv;
		this.myagent = (abstractAgent) myagent;


	}

	@Override
	public void onTick() {
		String myPosition=myagent.getCurrentPosition();

		if (myPosition!=""){
			List<Couple<String,List<Attribute>>> lobs=myagent.observe(myPosition);
			System.out.println("lobs: "+lobs);

//			try {
//				System.out.println("Press a key to move to the next step agents");
//				System.in.read();
//			} catch (IOException e) {
//				// TODO Auto-generated catch block
//				e.printStackTrace();
//			}


			//list of attribute associated to the currentPosition
			List<Attribute> lattribute= lobs.get(0).getR();


			Boolean b=false;
			for(Attribute a:lattribute){
				switch (a) {
				case TREASURE:
					System.out.println("My current backpack capacity is:"+ myagent.getBackPackFreeSpace());
					System.out.println("Value of the treasure on the current position: "+a.getValue());
					System.out.println("The agent grabbed :"+myagent.pick());
					System.out.println("the remaining backpack capacity is: "+ myagent.getBackPackFreeSpace());
					b=true;
					break;

				default:
					break;
				}
			}
			//test
			if (b){
				List<Couple<String,List<Attribute>>> lobs2=myagent.observe(myPosition);
				System.out.println("lobs after picking "+lobs2);
			}


			Random r= new Random();

			int moveId=r.nextInt(lobs.size());
			myagent.move(myPosition, lobs.get(moveId).getL());
		}

	}

}
