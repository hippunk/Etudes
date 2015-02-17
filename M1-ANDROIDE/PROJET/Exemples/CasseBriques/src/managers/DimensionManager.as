package managers 
{
	import com.ktm.genome.core.data.component.IComponentMapper;
	import com.ktm.genome.core.data.gene.GeneManager;
	import com.ktm.genome.core.entity.family.Family;
	import com.ktm.genome.core.entity.family.matcher.allOfGenes;
	import com.ktm.genome.core.entity.IEntity;
	import com.ktm.genome.core.entity.IEntityManager;
	import com.ktm.genome.core.logic.impl.LogicScope;
	import com.ktm.genome.render.component.Transform;
	import com.ktm.genome.resource.component.TextureResource;
	import components.Dimension;
	
	public class DimensionManager extends LogicScope
	{
		[Inject] public var entityManager:IEntityManager;
		[Inject] public var geneManager:GeneManager;
		private var dimensionEntities:Family;
		private var transformMapper:IComponentMapper;
		private var textureMapper:IComponentMapper;
		private var dimensionMapper:IComponentMapper;
		
		override protected function onConstructed():void {
			super.onConstructed();
			dimensionEntities = entityManager.getFamily(allOfGenes(TextureResource, Transform, Dimension));
			transformMapper = geneManager.getComponentMapper(Transform);
			textureMapper = geneManager.getComponentMapper(TextureResource);
			dimensionMapper = geneManager.getComponentMapper(Dimension);
			dimensionEntities.entityAdded.add(onDimensionAdded);
		}
		
		private function onDimensionAdded(e:IEntity):void {
			var transform:Transform = transformMapper.getComponent(e);
			var texture:TextureResource = textureMapper.getComponent(e);
			var dimension:Dimension = dimensionMapper.getComponent(e);
			
			dimension.width = texture.bitmapData.width * transform.scaleX;
			dimension.height = texture.bitmapData.height * transform.scaleY;
		}
	}
}