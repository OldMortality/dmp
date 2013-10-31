package examples;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Map;

import javax.xml.soap.SOAPException;

import com.exlibris.alma.sdk.AlmaWebServices;

public class AnalyticsWSExample {

    private static final String PATH = "[Obi object full path]";
    // for example: "/shared/Main Campus/Reports/test";

    private static final String XML_FILE = "[file location of the xml filter]";

    // for example: "c:\\Analytics\\Filter.xml";

    public static void main(String[] args) {
        try {
            System.out.println(testGetObjectAsXml(PATH, file2string(XML_FILE)));
        } catch (Exception e) {
            e.printStackTrace();

        }
    }

    private static String testGetObjectAsXml(String path, String filter) throws SOAPException {
        AlmaWebServices aws = AlmaWebServices.create("web service URL", "user name", "user password",
                "institution code");
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, path);
        paramsMap.put(AlmaWebServices.INPUT_PARAM_2, filter);
        return aws.invoke("AnalyticsWebServices", "getObjectAsXml", paramsMap);
    }

    // use this method to read filter from xml file (optional - you can take is
    // as string)
    private static String file2string(String file) {
        StringBuilder sb = new StringBuilder();
        try {
            BufferedReader br = new BufferedReader(new FileReader(new File(file)));
            String line;

            while ((line = br.readLine()) != null) {
                sb.append(line);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return (sb != null) ? sb.toString() : "";
    }
}