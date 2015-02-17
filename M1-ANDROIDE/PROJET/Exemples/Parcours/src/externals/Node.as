package externals
{
	public class Node
	{
		private var m_g:int;
		private var m_h:int;
		private var m_f:int;
		private var m_col:int;
		private var m_line:int;
		private var m_walkable:Boolean;
		private var m_parent:Node;
 
		public function Node()
		{
			walkable = true;
			g = h = f = 0;
			parent = this;
		}
 
 
 
		public function set parent( param_node:Node ):void{ m_parent = param_node; }
		public function set walkable( param_walkable:Boolean ):void{ m_walkable = param_walkable; }
		public function set g( param_g:int ):void{ m_g = param_g; }
		public function set f( param_f:int ):void{ m_f = param_f; }
		public function set h( param_h:int ):void{ m_h = param_h; }
		public function set col( param_col:int ):void{ m_col = param_col; }
		public function set line( param_line:int ):void{ m_line = param_line; }
 
		public function get parent():Node{ return m_parent; }
		public function get walkable():Boolean{ return m_walkable; }
		public function get g():int{ return m_g; }
		public function get f():int{ return m_f; }
		public function get h():int{ return m_h; }
		public function get col():int{ return m_col; }
		public function get line():int { return m_line; }
 
	}
}
