package systems 
{
	import com.ktm.genome.core.data.component.IComponentMapper;
	import com.ktm.genome.core.entity.family.Family;
	import com.ktm.genome.core.entity.family.matcher.allOfGenes;
	import com.ktm.genome.core.entity.IEntity;
	import com.ktm.genome.core.logic.system.System;
	import com.ktm.genome.render.component.Transform;
	import components.GrilleComponent;
	import flash.display.Stage;
	import flash.events.MouseEvent;
	import externals.Node;
	import externals.Pathfinder;
	import managers.GrilleManager;
	import components.Personnage;
	
	/**
	 * ...
	 * @author Arthur
	 */
	public class ObstacleCreationSystem extends System 
	{
		private var stage:Stage;
		private var click:Boolean;
		private var x:int;
		private var y:int;
		private var grilleEntities:Family;
		private var grilleMapper:IComponentMapper;
		private var transformMapper:IComponentMapper;
		[Inject] public var grilleManager:GrilleManager;
		private var personnageEntities:Family;
		private var personnageMapper:IComponentMapper;
		
		public function ObstacleCreationSystem(stage:Stage) 
		{
			this.stage = stage;
			this.stage.addEventListener(MouseEvent.MOUSE_DOWN, onMouseDown);
			this.stage.addEventListener(MouseEvent.MOUSE_UP, onMouseUp);
			click = false;
		}
		
		override protected function onConstructed():void {
			super.onConstructed();
			grilleEntities = entityManager.getFamily(allOfGenes(GrilleComponent));
			grilleMapper = geneManager.getComponentMapper(GrilleComponent);
			transformMapper = geneManager.getComponentMapper(Transform);
			
			personnageEntities = entityManager.getFamily(allOfGenes(Personnage));
			personnageMapper = geneManager.getComponentMapper(Personnage);
		}
		
		protected function onMouseDown(e:MouseEvent):void {
			click = true;
			x = e.stageX; y = e.stageY;
		}
		protected function onMouseUp(e:MouseEvent):void {
			click:false;
		}
		
		override protected function onProcess(delta:Number):void {
			var posX:int; var posY:int;
			super.onProcess(delta);
			if (click) {
				posX = (x - x % 100) / 100;
				posY = (y - y % 100) / 100;
				if (grilleEntities.members.length <= 0) return;
				var g:IEntity = grilleEntities.members[0];
				var grille:GrilleComponent = grilleMapper.getComponent(g);
				if (grille.occupation[posY][posX] == 0) {
					
					var ok:Boolean = true;
					grille.obstacle[posY][posX] = 1;
					
					var realGraphe:Array = grilleManager.getRealGraph();
					
					var start:Node = realGraphe[grilleManager.getDepartY()][grilleManager.getDepartX()];
					var end:Node = realGraphe[grilleManager.getArriveeY()][grilleManager.getArriveeX()];
					var chemin:Array = Pathfinder.findPath(realGraphe, start, end);
					
					if (chemin.length == 0) {
						ok = false; grille.obstacle[posY][posX] = 0;
					}
					
					if (ok) {
						var Ip:int = personnageEntities.members.length;
						for (var ip:int = 0; ip < Ip; ip++) {
								var p:IEntity = personnageEntities.members[ip];
								var pers:Personnage = personnageMapper.getComponent(p);
								start = realGraphe[pers.posY][pers.posX];
								end = realGraphe[grilleManager.getArriveeY()][grilleManager.getArriveeX()];
								chemin = Pathfinder.findPath(realGraphe, start, end);
								if (chemin.length == 0) {
									ok = false;
									grille.obstacle[posY][posX] = 0;
									break;
								}
								
						}
					}
					
					if (ok) {						
						EntityFactory.creationObstacle(entityManager, posX * 100, posY * 100, "personnageLayer", "obstacle");
						grille.occupation[posY][posX] = 4;
						grille.obstacle[posY][posX] = 1;
					}
				}
			}
		}
		
	}

}