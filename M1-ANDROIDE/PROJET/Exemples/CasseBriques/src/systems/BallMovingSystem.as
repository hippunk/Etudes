package systems 
{
	import com.ktm.genome.core.data.component.IComponentMapper;
	import com.ktm.genome.core.entity.family.Family;
	import com.ktm.genome.core.entity.family.matcher.allOfGenes;
	import com.ktm.genome.core.entity.IEntity;
	import com.ktm.genome.core.logic.system.System;
	import com.ktm.genome.render.component.Transform;
	import com.ktm.genome.resource.component.TextureResource;
	import components.Ball;
	import components.Movable;
	import flash.display.Stage;
	/**
	 * ...
	 * @author Arthur
	 */
	public class BallMovingSystem extends System
	{
		private var ballEntities:Family;
		private var transformMapper:IComponentMapper;
		private var textureMapper:IComponentMapper;
		private var movableMapper:IComponentMapper;
		private var ballMapper:IComponentMapper;
		private var stage:Stage;
		
		public function BallMovingSystem(stage:Stage) {
			this.stage = stage;
		}
		
		override protected function onConstructed():void {
			super.onConstructed();
			ballEntities = entityManager.getFamily(allOfGenes(Transform, TextureResource, Ball, Movable));
			ballEntities.entityAdded.add(onBallAdded);
			transformMapper = geneManager.getComponentMapper(Transform);
			textureMapper = geneManager.getComponentMapper(TextureResource);
			movableMapper = geneManager.getComponentMapper(Movable);
			ballMapper = geneManager.getComponentMapper(Ball);
		}
		
		private function onBallAdded(e:IEntity):void {
			setRandomOrientation(e);
		}
		
		private function setRandomOrientation(e:IEntity):void {
			var ball:Ball;
			ball = ballMapper.getComponent(e);
			do {
				var k:Number = Math.round(Math.random() * 60);
				ball.orientation = -120 + k;
			}while (k > 27 && k < 33);
		}
		
		override protected function onProcess(delta:Number):void {
			var transform:Transform;
			var movable:Movable;
			var ball:Ball;
			var i:int = 0;
			var I:int = ballEntities.members.length;
			
			for (i; i < I;i++ ) {
				var e:IEntity = ballEntities.members[i];
				movable = movableMapper.getComponent(e);
				ball = ballMapper.getComponent(e);
				transform = transformMapper.getComponent(e);
				transform.x += Math.cos(Math.PI * ball.orientation / 180) * movable.velocity;
				transform.y -= Math.sin(Math.PI * ball.orientation / 180) * movable.velocity;
				if (transform.y > stage.stageHeight) {
					transform.y = 0;
					transform.x = Math.round(Math.random() * (stage.stageWidth - 100) + 50);
					setRandomOrientation(e);
					//entityManager.killEntity(e);
					
					
				}
			}
		}
		
	}

}