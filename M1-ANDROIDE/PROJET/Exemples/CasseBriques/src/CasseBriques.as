package
{
	import com.ktm.genome.core.logic.process.ProcessPhase;
	import com.ktm.genome.core.logic.system.ISystemManager;
	import com.ktm.genome.render.system.RenderSystem;
	import com.ktm.genome.resource.manager.ResourceManager;
	import com.ktm.genome.resource.component.EntityBundle;
	import com.ktm.genome.core.IWorld
	import com.ktm.genome.core.BigBang
	
	import components.Duration;
	import managers.DimensionManager;
	
	import systems.BallMovingSystem;
	import systems.RacketMovingSystem;
	import systems.CollisionSystem;
	
	import flash.display.Sprite;
	import flash.events.Event;
	
	/**
	 * ...
	 * @author Arthur
	 */
	public class CasseBriques extends Sprite 
	{
		private var duration:Duration;
		
		public function CasseBriques() 
		{
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void 
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			// entry point
			var world:IWorld = BigBang.createWorld(stage);	
			var sm:ISystemManager = world.getSystemManager();
						
			world.setLogic(DimensionManager);
			
			sm.setSystem(ResourceManager).setProcess(ProcessPhase.TICK, int.MAX_VALUE);
			sm.setSystem(new RenderSystem(this)).setProcess(ProcessPhase.FRAME);			
			sm.setSystem(new BallMovingSystem(this.stage)).setProcess();
			sm.setSystem(new RacketMovingSystem(this.stage)).setProcess();
			sm.setSystem(new CollisionSystem(this.stage)).setProcess();
			

			
			var aliasURL:String = 'xml/alias.entityBundle.xml'
			var gameURL:String = 'xml/game.entityBundle.xml'
			
			EntityFactory.createResourcedEntity(world.getEntityManager(), aliasURL, "alias", EntityBundle);
			EntityFactory.createResourcedEntity(world.getEntityManager(), gameURL, "game", EntityBundle);
		}
		
	}
	
}