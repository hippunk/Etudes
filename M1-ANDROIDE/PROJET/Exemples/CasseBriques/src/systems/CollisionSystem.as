package systems 
{
	import com.ktm.genome.core.data.component.IComponentMapper
	import com.ktm.genome.core.entity.family.Family;
	import com.ktm.genome.core.entity.family.matcher.allOfGenes;
	import com.ktm.genome.core.entity.IEntity;
	import com.ktm.genome.core.logic.system.System;
	import com.ktm.genome.render.component.Transform;
	import com.ktm.genome.resource.component.TextureResource;
	import components.Ball;
	import components.Collision;
	import components.Dimension;
	import components.Duration;
	import components.Movable;
	import flash.display.Stage;
	
	/**
	 * ...
	 * @author Arthur
	 */
	public class CollisionSystem extends System
	{
		private var stage:Stage;
		private var ballEntities:Family;
		private var racketEntities:Family;
		private var brickEntities:Family;
		private var transformMapper:IComponentMapper;
		private var movableMapper:IComponentMapper;
		private var ballMapper:IComponentMapper;
		private var dimensionMapper:IComponentMapper;
		private var durationMapper:IComponentMapper;
		
		public function CollisionSystem(stage:Stage) {
			this.stage = stage;
		}
		override protected function onConstructed():void {
			super.onConstructed();
			ballEntities = entityManager.getFamily(allOfGenes(Transform, TextureResource, Ball, Movable));
			racketEntities = entityManager.getFamily(allOfGenes(Transform, TextureResource, Collision, Movable));
			brickEntities = entityManager.getFamily(allOfGenes(Transform, TextureResource, Collision, Duration));
			
			transformMapper = geneManager.getComponentMapper(Transform);
			movableMapper = geneManager.getComponentMapper(Movable);
			ballMapper = geneManager.getComponentMapper(Ball);
			dimensionMapper = geneManager.getComponentMapper(Dimension);
			durationMapper = geneManager.getComponentMapper(Duration);
		}
		override protected function onProcess(delta:Number):void {
			var ball:Ball;
			var transformBall:Transform;
			var movableBall:Movable;
			var dimensionBall:Dimension;
			var transformBrick:Transform;
			var dimensionBrick:Dimension;
			var durationBrick:Duration;
			var transformRacket:Transform;
			var movableRacket:Movable;
			var dimensionRacket:Dimension;
			var iBall:int;
			var Iball:int = ballEntities.members.length;
			var iBrick:int;
			var IBrick:int = brickEntities.members.length;
			var iRacket:int;
			var IRacket:int = racketEntities.members.length;
			
			for (iBall = 0; iBall < Iball; iBall++ ) {

				var e:IEntity = ballEntities.members[iBall];
				transformBall = transformMapper.getComponent(e);
				dimensionBall = dimensionMapper.getComponent(e);
				movableBall = movableMapper.getComponent(e);
				ball = ballMapper.getComponent(e);
				var posBallX:int = transformBall.x;
				var posBallY:int = transformBall.y;
				var ballWidth:Number = dimensionBall.width;
				var ballHeight:Number = dimensionBall.height;
				
				for (iBrick = 0; iBrick < IBrick; iBrick++) {
					//2 inti var briques fix
					
					var b:IEntity = brickEntities.members[iBrick];
					transformBrick = transformMapper.getComponent(b);
					dimensionBrick = dimensionMapper.getComponent(b);
					durationBrick = durationMapper.getComponent(b);
					var posBrickX:int = transformBrick.x;
					var posBrickY:int = transformBrick.y;
					var brickWidth:int = dimensionBrick.width;
					var brickHeight:int = dimensionBrick.height;
					
					//3 collision balle briques
					
					if ((ball.orientation < 0) && (posBallX + ballWidth / 2 >= posBrickX) && (posBallX + ballWidth / 2 <= posBrickX + brickWidth) && (posBallY + ballHeight >= posBrickY) && (posBallY <= posBrickY)) {
						ball.orientation = - ball.orientation;
						durationBrick.duration -= 1;
					}
					else if ((((ball.orientation < -90) && (ball.orientation > -180)) || ((ball.orientation > 90) && (ball.orientation < 180))) && ((posBallX >= posBrickX + brickWidth - ballWidth / 2) && (posBallX <= posBrickX + brickWidth) && (posBallY + ballHeight / 2 <= posBrickY + brickHeight) && (posBallY + ballHeight / 2 >= posBrickY))) {
						if (ball.orientation > 0) ball.orientation = 180 - ball.orientation;
						else ball.orientation = -ball.orientation -180;
						durationBrick.duration -= 1;
					}
					else if ((((ball.orientation < 0) && (ball.orientation > -90)) || ((ball.orientation > 0) && (ball.orientation < 90))) && ((posBallX + ballWidth >= posBrickX) && (posBallX <= posBrickX + brickWidth/2) && (posBallY + ballHeight / 2 <= posBrickY + brickHeight) && (posBallY + ballHeight / 2 >= posBrickY))) {
						if (ball.orientation > 0) ball.orientation = 180 - ball.orientation;
						else ball.orientation = -ball.orientation -180;
						durationBrick.duration -= 1;
					}
					else if ((ball.orientation > 0) && (posBallX + ballWidth / 2 >= posBrickX) && (posBallX + ballWidth / 2 <= posBrickX +brickWidth) && (posBallY + ballHeight >= posBrickY + brickHeight) && (posBallY <= posBrickY + brickHeight)) {
						ball.orientation = - ball.orientation;
						durationBrick.duration -= 1;
						if (movableBall.velocity < 10) movableBall.velocity += 1;
					}
					
					
					//4 destruct brique
					if (durationBrick.duration == 0) entityManager.killEntity(b);
					
				}
				for (iRacket = 0; iRacket < IRacket; iRacket++ ) {
					// 5 init var racket
					var r:IEntity = racketEntities.members[iRacket];
					transformRacket = transformMapper.getComponent(r);
					movableRacket = movableMapper.getComponent(r);
					dimensionRacket = dimensionMapper.getComponent(r);
					var posRacketX:int = transformRacket.x;
					var posRacketY:int = transformRacket.y;
					var racketWidth:Number = dimensionRacket.width;
					var racketHeight:Number = dimensionRacket.height;
					// 6 collision balle racket
					if ((posBallX + ballWidth / 2 >= posRacketX) && (posBallX + ballWidth / 2 <= posRacketX + racketWidth) && (posBallY + ballHeight >= posRacketY)) {
						ball.orientation = - ball.orientation;
						transformBall.y = stage.stageHeight - racketHeight - ballHeight;
						if (movableRacket.velocity < 15) movableRacket.velocity += 1;
					}
				}
				// 7 colli balle bords
				if (posBallY < 0 && ball.orientation > 0) {
					ball.orientation = - ball.orientation;
				}
				else if (posBallX > (stage.stageWidth - ballWidth) && ball.orientation < 90 && ball.orientation > -90) {
					if (ball.orientation > 0) ball.orientation = 180 - ball.orientation;
					else ball.orientation = - ball.orientation -180;
					
				}
				else if (posBallX < 0) {
					if (ball.orientation > 0) ball.orientation = 180 - ball.orientation;
					else ball.orientation = - ball.orientation -180;
				}
				// 8 correction angle
				if (ball.orientation > 180) ball.orientation = ball.orientation -360;
				else if (ball.orientation < -180) ball.orientation = ball.orientation +360;
			}
		}
		
	}

}