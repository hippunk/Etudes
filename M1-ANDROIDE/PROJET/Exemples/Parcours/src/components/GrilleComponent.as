package components 
{
	import com.ktm.genome.core.data.component.Component;
	/**
	 * ...
	 * @author Arthur
	 */
	
	public class GrilleComponent extends Component
	{
		public var tailleX:int = 8;
		public var tailleY:int = 6;
		public var pixels:int = 100;
		public var grille:Vector.<Vector.<int>>;
		public var occupation:Vector.<Vector.<int>>;
		public var obstacle:Vector.<Vector.<int>>;
	}

}