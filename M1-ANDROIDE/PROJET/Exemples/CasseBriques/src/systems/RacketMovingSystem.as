package systems 
{
	import com.ktm.genome.core.data.component.IComponentMapper
	import com.ktm.genome.core.entity.family.Family;
	import com.ktm.genome.core.entity.family.matcher.allOfGenes;
	import com.ktm.genome.core.entity.IEntity;
	import com.ktm.genome.core.logic.system.System;
	import com.ktm.genome.render.component.Transform
	import com.ktm.genome.resource.component.TextureResource;
	import components.Controlable;
	import components.Movable;
	import components.Dimension;
	import flash.display.Stage;
	import flash.events.KeyboardEvent;
	import flash.ui.Keyboard;
	
	/**
	 * ...
	 * @author Arthur
	 */
	public class RacketMovingSystem extends System
	{
		
		private var racketEntities:Family;
		private var transformMapper:IComponentMapper;
		private var textureMapper:IComponentMapper;
		private var movableMapper:IComponentMapper;
		private var dimensionMapper:IComponentMapper;
		private var stage:Stage;
		private var left:Boolean = false;
		private var right:Boolean = false;
		
		public function RacketMovingSystem(stage:Stage)	{
			this.stage = stage;
			this.stage.addEventListener(KeyboardEvent.KEY_DOWN, keyDownHandler);
			this.stage.addEventListener(KeyboardEvent.KEY_UP, keyUpHandler);
		}
		
		override protected function onConstructed():void {
			super.onConstructed();
			racketEntities = entityManager.getFamily(allOfGenes(Transform, TextureResource, Movable, Controlable));
			transformMapper = geneManager.getComponentMapper(Transform);
			textureMapper = geneManager.getComponentMapper(TextureResource);
			movableMapper = geneManager.getComponentMapper(Movable);
			dimensionMapper = geneManager.getComponentMapper(Dimension);
			racketEntities.entityAdded.add(onRacketAdded);
			right = false; left = false;
		}
		
		private function keyDownHandler(event:KeyboardEvent):void {
			switch(event.keyCode) {
				case 81 : { left = true; break; }
				case Keyboard.LEFT : { left = true; break; }
				case 68 : { right = true; break; }
				case Keyboard.RIGHT : { right = true; break; }
				default : break;
			}
			
		}
		
		private function keyUpHandler(event:KeyboardEvent):void {
			switch(event.keyCode) {
				case 81 : { left = false; break; }
				case Keyboard.LEFT : { left = false; break; }
				case 68 : { right = false; break; }
				case Keyboard.RIGHT : { right = false; break; }
				default : break;
			}
		}
		
		override protected function onProcess(delta:Number):void {
				
			var transform:Transform;
			var movable:Movable;
			var texture:TextureResource;
			var i:int = 0;
			var I:int = racketEntities.members.length;
			var dimension:Dimension;
			
			for (i; i < I; i++) {
				var e:IEntity = racketEntities.members[i];
					movable = movableMapper.getComponent(e);
					transform = transformMapper.getComponent(e);
					dimension = dimensionMapper.getComponent(e);
					if (left) transform.x -= movable.velocity;
					if (right) transform.x += movable.velocity;
					if (transform.x < 0) transform.x = 0;
					if (transform.x > stage.stageWidth-dimension.width) transform.x = stage.stageWidth-dimension.width;
			}
		}
		
		private function onRacketAdded(e:IEntity):void {
			var transform:Transform = transformMapper.getComponent(e);
			var dimension:Dimension = dimensionMapper.getComponent(e);
			transform.x = stage.stageWidth/2-dimension.width/2
			transform.y = stage.stageHeight-dimension.height
		}
		
	}

}