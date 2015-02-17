package systems 
{
	import com.ktm.genome.core.data.component.IComponentMapper;
	import com.ktm.genome.core.entity.family.Family;
	import com.ktm.genome.core.entity.family.matcher.allOfGenes;
	import com.ktm.genome.core.entity.IEntity;
	import com.ktm.genome.core.logic.system.System;
	import com.ktm.genome.render.component.Transform;
	import components.GrilleComponent;
	import components.Personnage;
	import managers.GrilleManager;
	import externals.Pathfinder;
	import externals.Node;
	
	/**
	 * ...
	 * @author Arthur
	 */
	public class PersonnageSystem extends System
	{
		[Inject] public var grilleManager:GrilleManager;
		private var grilleEntities:Family;
		private var personnageEntities:Family;
		private var grilleMapper:IComponentMapper;
		private var transformMapper:IComponentMapper;
		private var personnageMapper:IComponentMapper;
		private var time:int = 0;
		
		override protected function onConstructed():void {
			super.onConstructed();
			personnageEntities = entityManager.getFamily(allOfGenes(Transform, Personnage));
			transformMapper = geneManager.getComponentMapper(Transform);
			personnageMapper = geneManager.getComponentMapper(Personnage);
			
			grilleEntities = entityManager.getFamily(allOfGenes(GrilleComponent));
			grilleMapper = geneManager.getComponentMapper(GrilleComponent);
			personnageEntities.entityAdded.add(onPersonnageAdded);
		}
		
		private function onPersonnageAdded(e:IEntity):void {
			var personnage:Personnage = personnageMapper.getComponent(e);
			personnage.posX = grilleManager.getDepartX(); 
			personnage.posY = grilleManager.getDepartY();
			var transform:Transform = transformMapper.getComponent(e);
			var g:IEntity = grilleEntities.members[0];
			var grille:GrilleComponent = grilleMapper.getComponent(g);
			transform.x = personnage.posX * grille.pixels + 10;
			transform.y = personnage.posY * grille.pixels + 10;
			grille.occupation[personnage.posY][personnage.posX] = 1;
		}
		
		override protected function onProcess(delta:Number):void {
			time += delta; if (time < 1000) return;
			time -= 1000;
			if (grilleEntities.members.length <= 0) return;
			var g:IEntity = grilleEntities.members[0];
			var grille:GrilleComponent = grilleMapper.getComponent(g);
			var realGraphe:Array = grilleManager.getRealGraph();
			var Ip:int = personnageEntities.members.length;
			for (var ip:int = 0; ip < Ip; ip++) {
				var p:IEntity = personnageEntities.members[ip];
				var personnage:Personnage = personnageMapper.getComponent(p);
				var transform:Transform = transformMapper.getComponent(p);
				var start:Node = realGraphe[personnage.posY][personnage.posX];
				var end:Node = realGraphe[grilleManager.getArriveeY()][grilleManager.getArriveeX()];
				var chemin:Array = Pathfinder.findPath(realGraphe, start, end);
				if (chemin.length > 0) {
					var n:Node = chemin[0];
					if (n) {
						grille.occupation[personnage.posY][personnage.posX] = 0;
						personnage.posX = n.col;
						personnage.posY = n.line;
						transform.x = personnage.posX * grille.pixels + 10;
						transform.y = personnage.posY * grille.pixels + 10;
						grille.occupation[personnage.posY][personnage.posX] = 1;
					}
				}
			}
		}
	}

}