package managers 
{
	
	import com.ktm.genome.core.data.component.IComponentMapper;
	import com.ktm.genome.core.data.gene.GeneManager;
	import com.ktm.genome.core.entity.family.Family;
	import com.ktm.genome.core.entity.family.matcher.allOfGenes;
	import com.ktm.genome.core.entity.IEntity;
	import com.ktm.genome.core.entity.IEntityManager;
	import com.ktm.genome.core.logic.impl.LogicScope;
	import externals.Node;
	import components.GrilleComponent;
	/**
	 * ...
	 * @author Arthur
	 */
	public class GrilleManager extends LogicScope
	{
		[Inject] public var entityManager:IEntityManager;
		[Inject] public var geneManager:GeneManager;
		private var grilleEntities:Family;
		private var grilleMapper:IComponentMapper;
		private var XX1:int = -1;
		private var YY1:int = -1;
		private var XX2:int = -1;
		private var YY2:int = -1;
		
		override protected function onConstructed():void {
			super.onConstructed();
			grilleEntities = entityManager.getFamily(allOfGenes(GrilleComponent));
			grilleMapper = geneManager.getComponentMapper(GrilleComponent);
			grilleEntities.entityAdded.add(ajout);
		}
		
		protected function ajout(e:IEntity):void {
			var grille:GrilleComponent = grilleMapper.getComponent(e);
			var longueur:int = grille.tailleX;
			var hauteur:int = grille.tailleY;
			grille.occupation = new Vector.<Vector.<int>>(hauteur);
			grille.obstacle = new Vector.<Vector.<int>>(hauteur);
			for (var j:int = 0; j < hauteur; j++) {
				grille.occupation[j] = new Vector.<int>(longueur);
				grille.obstacle[j] = new Vector.<int>(longueur);
				for (var i:int = 0; i < longueur;i++) {
					if (grille.grille[j][i] == 0) {
						EntityFactory.createSquare(entityManager, grille.pixels * i, grille.pixels * j, "gameLayer", "blanc");
						grille.occupation[j][i] = 0;
						grille.obstacle[j][i] = 0;
					}
					else if (grille.grille[j][i] == 1) {
						EntityFactory.createSquare(entityManager, grille.pixels * i, grille.pixels * j, "gameLayer", "couleur");
						grille.occupation[j][i] = 0;
						grille.obstacle[j][i] = 0;
					}
					else if (grille.grille[j][i] == 2 || grille.grille[j][i] == 3) {
						EntityFactory.createSquare(entityManager, grille.pixels * i, grille.pixels * j, "gameLayer", "porte");
						grille.occupation[j][i] = grille.grille[j][i];
						grille.obstacle[j][i] = 0;
						if (grille.grille[j][i] == 2) { XX1 = i; YY1 = j; }
						else { XX2 = i; YY2 = j; }
					}	
					else {
						EntityFactory.createSquare(entityManager, grille.pixels * i, grille.pixels * j, "gameLayer", "obstacle");
						grille.occupation[j][i] = grille.grille[j][i];
						grille.obstacle[j][i] = 1;
					}
				}

			}
		}
		
		
		public function getDepartX():int {
			return XX1;
		}
		public function getDepartY():int {
			return YY1;
		}
		public function getArriveeX():int {
			return XX2;
		}
		public function getArriveeY():int {
			return YY2;
		}
		
		public function getRealGraph():Array {
			var realGraphe:Array = new Array();
			if (grilleEntities.members.length <= 0)
				return realGraphe;
			else {
				var g:IEntity = grilleEntities.members[0];
				var grille:GrilleComponent = grilleMapper.getComponent(g);
				var ligne:Array = new Array(grille.obstacle[0]) as Array;
				var maxcol:int = grille.obstacle[0].length;
				var maxline:int = grille.obstacle.length;
				for (var i:int = 0; i < maxline; i++) {
					var line:Array = new Array();
					for (var j:int = 0; j < maxcol; j++) {
						var node:Node = new Node();
						if (grille.obstacle[i][j] == 1) {
							node.walkable = false;
						}
						node.col = j; node.line = i;
						line.push(node);
					}
					realGraphe.push(line);
				}
				return realGraphe;	
			}
				
		}

	}

}