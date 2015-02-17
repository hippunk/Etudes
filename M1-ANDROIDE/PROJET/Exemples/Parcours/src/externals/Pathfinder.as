 
package externals
{
  import externals.Node;
 
  public class Pathfinder
  {
    public static const NODE_DISTANCE_VALUE:int = 10;
 
    private static var m_openList:Array;
    private static var m_closeList:Array;
 
    public static function findPath( param_graphe:Array, param_start:Node, param_end:Node ):Array
    {
      // on cr�e les listes ferm�es et les listes ouvertes
      m_openList = new Array();
      m_closeList = new Array();
 
      // on cr�e la variable qui va accueillir le chemin final
 
      var finalPath:Array = new Array();
 
 
      //  traitement
 
      /**
        - Ajout du node de d�part � la liste ouverte.
        - Entr�e dans la boucle suivante:  
          - R�cup�ration du node avec le plus petit F contenu dans la liste ouverte. On le nommera CURRENT.
          - Basculer CURRENT dans la liste ferm�e.
          - Pour chacun des 4 nodes adjacents � CURRENT appliquer la m�thode suivante:
 
          * Si le node est un obstacle ou est dans la liste ferm�e ignorez-le et 
        passer � l'analyse d'un autre node.
 
          * Si le node n'est pas dans la liste ouverte, ajoutez-le � ladite liste 
            et faites de CURRENT son parent(P). Calculez et enregistrez 
            ses propri�t�s F, G et H.
 
          * Si le node est d�j� dans la liste ouverte, recalculez son G, s'il est inf�rieur 
            � l'ancien, faites de CURRENT son parent(P) et recalculez et enregistrez 
            ses propri�t�s F et H.
 
          * Stopper la boucle de recherche si vous ajoutez le node d'arriv�e � la liste ferm�e ou si la liste ouverte est vide, 
        dans ce dernier cas, il n'y a pas de chemin possible entre A et B.
 
        - Prenez le node d'arriv�e et reconstruisez le chemin � rebours, c�d en bouclant sur les propri�t�s parentes
        jusqu'� ce que le parent soit CURRENT.
      */
 
      addToOpenList( param_start );
 
      var currentNode:Node = null;
 
      while( m_openList.length > 0 ) //  stopper la boucle si la liste ouverte est vide
      {
        // a. R�cup�ration du node avec le plus petit F contenu dans la liste ouverte. On le nommera CURRENT.
        currentNode = getCurrentNode(); 
 
        //  stopper la boucle si n ajoute le noeud d'arriv�e � la liste ferm�e
        if( currentNode == param_end ) 
          break;
 
        // b. Basculer CURRENT dans la liste ferm�e.
        addToCloseList( currentNode ); 
 
        //  r�cup�ration des voisins de CURRENT
        var neighbours:Array = getNeighbours( currentNode, param_graphe ); 
        var maxi:int = neighbours.length;
 
        // Pour chacun des 8 nodes adjacents � CURRENT appliquer la m�thode suivante:
        for( var i:int = 0; i < maxi; ++i )
        {
          var node:Node = neighbours[i];
 
          //Si le node est un obstacle ou est dans la liste ferm�e ignorez-le et passer � l'analyse d'un autre node.
          if( isOnCloseList( node ) || node.walkable == false ) 
            continue;
 
          /* on calcule le nouveau g */
          var newG:int;
          newG = node.parent.g + NODE_DISTANCE_VALUE;
 
          /*on calcule le nouveau h */
          var newH:int = ( Math.abs( param_end.line - node.line ) + Math.abs( param_end.col - node.col ) ) * NODE_DISTANCE_VALUE;
 
          /*on calcule le nouveau F*/
          var newF:int = newH + newG;
 
 
 
          if( isOnOpenList( node ) )
          {
            //Si le node est d�j� dans la liste ouverte, recalculez son G, s'il est inf�rieur � l'ancien, 
            //faites de CURRENT  son parent(P) et recalculez et enregistrez ses propri�t�s F et H.
 
            if( newG < node.g )
            {
              node.parent = currentNode;
              node.g = newG;
              node.h = newH;
              node.f = newF;
            }
 
          }
          else 
          {
            //Si le node n'est pas dans la liste ouverte, ajoutez-le � la dite liste et faites de CURRENT son parent(P). 
            //Calculez et enregistrez ses propri�t�s F, G et H.
            addToOpenList( node );
            node.parent = currentNode;
            node.g = newG;
            node.h = newH;
            node.f = newF;
          }
        }
 
      }
 
 
      // on est sorti de la liste, on a deux solutions, soit la liste ouverte est vide dans ces cas l� il 
      // n'y a pas de solutions et on retoure directement finalPath;
 
      if( m_openList.length == 0 )
        return finalPath;
 
 
      // Soit on maintenant on construit le chemin � rebours;
 
      var lastNode:Node = param_end;
      while( lastNode != param_start )
      {
        trace( lastNode.parent );
        finalPath.push( lastNode );
        lastNode = lastNode.parent;
      }
 
 
      // on retourne le chemin final
 
      return finalPath.reverse();
    }
 
 
    private static function removeFromCloseList( param_node:Node ):void
    {
      var tmpList:Array = new Array();
      var maximum:int =  m_closeList.length;
 
      for( var i:int = 0; i < maximum; ++i )
      {
        if( m_closeList[i] != param_node )
          tmpList.push( m_closeList[i] );
      }
 
      m_closeList = tmpList;
    }
 
 
    private static function removeFromOpenList( param_node:Node ):void
    {
      var tmpList:Array = new Array();
      var maximum:int = m_openList.length;
 
      for( var i:int = 0; i < maximum; ++i )
      {
        if( m_openList[i] != param_node )
          tmpList.push( m_openList[i] );
      }
 
      m_openList = tmpList;
    }
 
 
    private static function addToCloseList( param_node:Node ):void
    {
      removeFromOpenList( param_node );
      m_closeList.push( param_node );
    }
 
 
    private static function addToOpenList( param_node:Node ):void
    {
      removeFromCloseList( param_node );
      m_openList.push( param_node );
    }
 
 
    private static function getCurrentNode():Node
    {
      var tmpList:Array = new Array();
      var maximum:int = m_openList.length;
      var minF:int = 1000000;
      var curNode:Node = null;
 
      for( var i:int = 0; i < maximum; ++i )
      {
        var node:Node = m_openList[i] as Node;
 
        if( node.f < minF )
        {
          minF = node.f;
          curNode = node;
        }
      }
 
      return curNode;
    }
 
 
    private static function getNeighbours( param_node:Node, param_graphe:Array ):Array
    {
      var neighbours:Array = new Array();
      var maxcol:int = param_graphe[0].length;
      var maxline:int = param_graphe.length;
 
 
      // on calcule l'indice de la ligne au dessus de la ligne du node
      var indiceUp:int = param_node.line - 1; 
 
      // on calcule l'indice de la ligne au dessus de la ligne du node
      var indiceBottom:int = param_node.line + 1; 
 
      // on calcule l'indice de la colonne � gauche de la colonne du node
      var indiceLeft:int = param_node.col - 1; 
 
      // on calcule l'indice de la colonne � droite de la colonne du node
      var indiceRight:int = param_node.col + 1;
 
 
      // si la ligne du dessus existe alors le node du dessus existe on ajoute alors le  node du dessus
      if( indiceUp > -1 ) 
        neighbours.push( param_graphe[indiceUp][param_node.col]);
 
      // si la ligne du dessous existe alors le node du dessous existe on ajoute alors le  node du dessous  
      if( indiceBottom < maxline ) 
        neighbours.push( param_graphe[indiceBottom][param_node.col]);
 
      // si la colonne de gauche existe alors le node de gauche existe on ajoute alors le  node de gauche
      if( indiceLeft > -1 )
        neighbours.push( param_graphe[param_node.line][indiceLeft]);
 
      // si la colonne de droite existe alors le node de droite existe on ajoute alors le  node de droite
      if( indiceRight < maxcol ) 
        neighbours.push( param_graphe[param_node.line][indiceRight]);
 
 
      return neighbours;
    }
 
 
    private static function isOnOpenList( param_node:Node ):Boolean
    {
      var maximum:int = m_openList.length;
 
      for( var i:int = 0; i < maximum; ++i )
      {
        if( m_openList[i] == param_node )
          return true;
      }
 
      return false;
    }
 
 
    private static function isOnCloseList( param_node:Node ):Boolean
    {
      var maximum:int = m_closeList.length;
 
      for( var i:int = 0; i < maximum; ++i )
      {
        if( m_closeList[i] == param_node )
          return true;
      }
 
      return false;
    }
 
 
  }
}
