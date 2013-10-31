package alma1;

import java.io.File;
import java.io.IOException;
import java.util.List;

import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.jdom2.Document;
import org.jdom2.Element;
import org.jdom2.JDOMException;
import org.jdom2.Namespace;
import org.jdom2.input.SAXBuilder;
 
/**
 * Reads the sample files, and calls the web service for each user record
 * 
 * @author michel
 *
 */
public class ReadXMLFile2 {
	
	
	private static Logger logger = Logger
			.getLogger("ReadXMLFile.class");
	
	
	public static void main(String[] args) {
 
	  SAXBuilder builder = new SAXBuilder();
	  File xmlFile = new File("polytestpatronsNew.xml");
 
	  try {
		 
		logger.log(Level.INFO,"Starting to read the file " );
		logger.log(Level.INFO,"Filename is: " + xmlFile );
		
		  
		Document document = (Document) builder.build(xmlFile);
		Element rootNode = document.getRootElement();
		
		Namespace ns = Namespace.getNamespace("http://com/exlibris/digitool/repository/extsystem/xmlbeans");
	
		List<Element> list = rootNode.getChildren("userRecord",ns);
 
		for (int i = 0; i < list.size(); i++) {
 
		   Element node = (Element) list.get(i);
		   //logger.log(Level.DEBUG,"Node: " + node.getName() + ":" +  node.getNamespace()) ;
		   
		   WebServiceCaller caller = new WebServiceCaller(); 
		   caller.addUser(node);
		    
		}
 
	  } catch (IOException io) {
		System.out.println(io.getMessage());
	  } catch (JDOMException jdomex) {
		System.out.println(jdomex.getMessage());
	  }
	  
	  logger.log(Level.INFO,"Finished reading the file." );
		
	  
	}
	
	
	
	
}