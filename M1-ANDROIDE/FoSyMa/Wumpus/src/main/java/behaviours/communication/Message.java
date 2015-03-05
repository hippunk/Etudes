package behaviours.communication;

import java.io.Serializable;
import java.util.LinkedList;
import java.util.List;



public class Message implements Serializable{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	public TypeMessage type;
	public List<String> contenu= null;
	
	public Message (TypeMessage type,List<String> contenu) {
		this.type = type;
		this.contenu = contenu;
	}
	
	public String toString(){
		String str = "Message {Type="+type.name()+" contenu=";
		if(contenu != null && !contenu.isEmpty()){
			str += contenu.toString()+"}";
		}
		else{
			str += "[]}";	
		}
		
		return str;
		
	}
}
