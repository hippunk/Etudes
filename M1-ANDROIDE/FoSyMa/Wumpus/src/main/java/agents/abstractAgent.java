package agents;

import java.util.List;

import env.Attribute;
import env.Environment;
import env.Environment.Couple;
import jade.core.Agent;

public class abstractAgent extends Agent {
	
	protected Environment realEnv;
	
	/**
	 * 
	 * @return The agent current position in the environment
	 */
	public String getCurrentPosition(){
		return this.realEnv.getCurrentPosition(this.getLocalName());
	}
	
	/**
	 * 
	 * @param nodeId my current position
	 * @return the available observations, null if the given position does not correspond to the one 
	 * of the agent.
	 */
	public List<Couple<String,List<Attribute>>> observe(String nodeId){
		return this.realEnv.observe(nodeId,this.getLocalName());
	}

	/**
	 * 
	 * @param myPosition the agent current position's ID in the environment
	 * @param myDestination the targeted nodeId
	 * @return true is the move is legit and done, false otherwise
	 */
	public boolean move(String myPosition, String myDestination){
		return this.realEnv.move(this,this.getLocalName(),myPosition,myDestination);
	}
	
	/**
	 * 
	 * @return the amount of wealth that the agent was able to pick. 0 if there is no treasure at this place or if the agent's 
	 * 	carrying capacity is already reached.
	 */
	public int pick(){
		return this.realEnv.pick(this.getLocalName(),getCurrentPosition());
	}
	
	/**
	 * 
	 * @return the available carrying capacity of the agent 
	 */
	public int getBackPackFreeSpace(){
		return this.realEnv.getBackPackFreeSpace(this.getLocalName());
	}
	
}

