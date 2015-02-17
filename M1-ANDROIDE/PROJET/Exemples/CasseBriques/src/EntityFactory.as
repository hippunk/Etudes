package {
	import com.ktm.genome.core.entity.IEntity;
	import com.ktm.genome.core.entity.IEntityManager;
	
	public class EntityFactory {
		static public function createResourcedEntity(em:IEntityManager, source:String, id:String, resourceType:Class, e:IEntity = null):IEntity {
			e = e ||= em.create();
			em.addComponent(e, resourceType, {id:id,source:source,toBuild:true } );
			return e;
		}
	}
	
}