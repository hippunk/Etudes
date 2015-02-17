package {
	import com.ktm.genome.core.entity.IEntity;
	import com.ktm.genome.core.entity.IEntityManager;
	import com.ktm.genome.render.component.Transform;
	import com.ktm.genome.render.component.Layered;
	import com.ktm.genome.resource.component.TextureResource;
	import components.Obstacle;
	
	public class EntityFactory {
		static public function createResourcedEntity(em:IEntityManager, source:String, id:String, resourceType:Class, e:IEntity = null):IEntity {
			e = e ||= em.create();
			em.addComponent(e, resourceType, {id:id,source:source,toBuild:true } );
			return e;
		}
		
		static public function createSquare(em:IEntityManager, x:int, y:int, layer:String, type:String):IEntity {
			var e:IEntity = em.create();
			em.addComponent(e, Transform, { x:x, y:y } );
			em.addComponent(e, Layered, { layerId:layer} );
			em.addComponent(e, TextureResource, { source:"pictures/" + type + ".jpg", id:type } );
			return e;
		}	
		
		static public function creationObstacle(em:IEntityManager, x:int, y:int, layer:String, type:String):IEntity {
			var valx:int = x / 100;
			var valy:int = y / 100;
			var e:IEntity = createSquare(em, x, y, layer, type);
			em.addComponent(e, Obstacle, { posX:valx, posY:valy } );
			return e;
		}
	}	
}