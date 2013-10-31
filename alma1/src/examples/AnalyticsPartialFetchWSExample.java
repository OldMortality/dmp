package examples;
import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.soap.SOAPException;

import org.w3c.dom.Document;

import com.exlibris.alma.sdk.AlmaWebServices;

public class AnalyticsPartialFetchWSExample {

    // xml nodes
    private static final String RESULT_XML_XML_NODE = "ResultXml";
    private static final String IS_FINISHED_XML_NODE = "IsFinished";
    private static final String RESUMPTION_TOKEN_XML_NODE = "ResumptionToken";

    // alma analytics web service
    private static final String FETCH_NEXT_WS_FUNCTION = "fetchNext";
    private static final String GET_ANALYTICS_RESULTS_AS_XML_WS_FUNCTION = "getAnalyticsResultsAsXml";
    private static final String ANALYTICS_WEB_SERVICES_NAME = "AnalyticsWebServices";

    private static final String URL = "[ ALMA Web Service URL ]";
    private static final String USER_NAME = "[ user name ]";
    private static final String USER_PASSWORD = "[ user password ]";
    private static final String INSTITUTION_CODE = "[ institution code ]";

    // for example: "/shared/Main Campus/Reports/test";
    private static final String OBI_OBJECT_FULL_PATH = "[Obi object full path]";

    /**
     * The entry point to the code which tests the ALMA ANALYTICS web services
     *
     * @param args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {

        String filterXml = new String("<sawx:expr xsi:type=\"sawx:logical\" "
                + "op=\"and\" xmlns:saw=\"com.siebel.analytics.web/report/v1.1\" "
                + "xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" "
                + "xmlVersion=\"200705140\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" "
                + "xmlns:sawx=\"com.siebel.analytics.web/expression/v1.1\"></sawx:expr>");

        // use "partial fetch" to bring only "n" rows each time
        // (30 rows, in this example)
        partialFetch(URL, USER_NAME, USER_PASSWORD, INSTITUTION_CODE, OBI_OBJECT_FULL_PATH, filterXml, 30);

    }

    /**
     * Get an ALMA OBI object using partial fetch
     *
     * @param url
     *            String holding the ALMA Web Service URL
     * @param userName
     *            String holding the user name
     * @param userPassword
     *            String holding the user password
     * @param institutionCode
     *            String holding the institution code
     * @param obiObjectFullPath
     *            String holding the full path to the OBI object at the OBI
     *            server
     * @param filterFullPath
     *            String holding the full path to the filter xml file
     * @param maxRowsInFetch
     *            int indicating what is the maximum number of rows to return at
     *            each fetch
     * @throws Exception
     *             in any error
     */
    private static void partialFetch(String url, String userName, String userPassword, String institutionCode,
            String obiObjectFullPath, String filterFullPath, int maxRowsInFetch) throws Exception {

        // get first query and save the resumption token and "isFinished" flag
        String firstQuery = getAnalyticsResultsAsXml(url, userName, userPassword, institutionCode, obiObjectFullPath,
                filterFullPath, maxRowsInFetch + "");

        // Here is a basic parsing, for keeping this example simple.
        // Of course you'd better use a better parser/parsing to get the values
        // from the returned XML
        // Don't forget to catch errors when parsing (the string you are
        // parsing might be an error message)
        DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();

        Document document = documentBuilder.parse(new ByteArrayInputStream(firstQuery.getBytes("UTF-8")));
        String resumptionToken = document.getElementsByTagName(RESUMPTION_TOKEN_XML_NODE).item(0).getTextContent();
        boolean isFinished = new Boolean(document.getElementsByTagName(IS_FINISHED_XML_NODE).item(0).getTextContent())
                .booleanValue();
        String resultsXML = document.getElementsByTagName(RESULT_XML_XML_NODE).item(0).getTextContent().trim();

        System.out.println("------------------- 1 -------------------");
        System.out.println(resultsXML);
        System.out.println("-------------------------------------------------------------");

        // now bring the rest of the results, if exists
        int i = 2;
        // loop through results till they are finished
        while (!isFinished) {
            // fetch the next result, using the resumption token
            String result = fetchNext(url, userName, userPassword, institutionCode, resumptionToken);
            // Here is a basic parsing, for keeping this example simple.
            // Of course you'd better use a better parser/parsing to get the
            // values from the returned XML
            document = documentBuilder.parse(new ByteArrayInputStream(result.getBytes("UTF-8")));
            isFinished = new Boolean(document.getElementsByTagName(IS_FINISHED_XML_NODE).item(0).getTextContent());
            resultsXML = document.getElementsByTagName(RESULT_XML_XML_NODE).item(0).getTextContent().trim();

            System.out.println("------------------- " + i + " -------------------");
            System.out.println(resultsXML);
            i++;
        }
    }

    /**
     * Get an ALMA Analytics object as xml
     *
     * @param url
     *            String holding the ALMA Web Service URL
     * @param userName
     *            String holding the user name
     * @param userPassword
     *            String holding the user password
     * @param institutionCode
     *            String holding the institution code
     * @param obiObjectFullPath
     *            String holding the full path to the OBI object at the OBI
     *            server
     * @param filterFullPath
     *            String holding the full path to the filter xml file
     * @param maxRowsInFetch
     *            int indicating what is the maximum number of rows to return at
     *            each fetch
     * @return String the ALMA Analytics object as xml
     * @throws SOAPException
     *             in any SOAP error
     */
    private static String getAnalyticsResultsAsXml(String url, String userName, String userPassword,
            String institutionCode, String obiObjectFullPath, String filterFullPath, String maxRowsInFetch)
            throws SOAPException {
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, obiObjectFullPath);
        paramsMap.put(AlmaWebServices.INPUT_PARAM_2, filterFullPath);
        paramsMap.put(AlmaWebServices.INPUT_PARAM_3, maxRowsInFetch);
        return invokeAlmaWebServices(url, userName, userPassword, institutionCode,
                GET_ANALYTICS_RESULTS_AS_XML_WS_FUNCTION, paramsMap);
    }

    /**
     * Fetch the next bulk of results
     *
     * @param url
     *            String holding the ALMA Web Service URL
     * @param userName
     *            String holding the user name
     * @param userPassword
     *            String holding the user password
     * @param institutionCode
     *            String holding the institution code
     * @param resumptionToken
     *            String holding the resumption token returned by the first
     *            fetch
     * @return String the ALMA Analytics object as xml
     * @throws SOAPException
     *             in any SOAP error
     */
    private static String fetchNext(String url, String userName, String userPassword, String institutionCode,
            String resumptionToken) throws SOAPException {
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, resumptionToken);
        return invokeAlmaWebServices(url, userName, userPassword, institutionCode, FETCH_NEXT_WS_FUNCTION, paramsMap);
    }

    /**
     * Invokes an ALMA web service
     *
     * @param url
     *            String holding the ALMA Web Service URL
     * @param userName
     *            String holding the user name
     * @param userPassword
     *            String holding the user password
     * @param institutionCode
     *            String holding the institution code
     * @param wsFunction
     *            String holding the web service function to invoke
     * @param paramsMap
     *            Map<String, String> of parameters to use when invoking the web
     *            service function
     * @return String the ALMA Analytics object xml String
     * @throws SOAPException
     *             in any SOAP error
     */
    private static String invokeAlmaWebServices(String url, String userName, String userPassword,
            String institutionCode, String wsFunction, Map<String, String> paramsMap) throws SOAPException {
        // create an AlmaWebServices Object
        AlmaWebServices aws = AlmaWebServices.create(url, userName, userPassword, institutionCode);
        // invoke the web service function using the service and parameters
        String result = aws.invoke(ANALYTICS_WEB_SERVICES_NAME, wsFunction, paramsMap);
        // return the result
        return result;
    }

}
