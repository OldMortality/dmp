package examples;
import java.util.HashMap;
import java.util.Map;

import com.exlibris.alma.sdk.AlmaWebServices;

public class RequestWSExample {

    public static final String CANCEL_REQUESTS = "cancelUserRequests";
    public static final String GET_USER_REQUESTS = "getUserRequests";
    public static final String WS_LINK = "RequestWebServices";

    public static void main(String[] args) {
        System.out.println("Starting RequestWSExample");
        RequestWSExample example = new RequestWSExample();
        example.testWebService();
        System.out.println("Ending RequestWSExample");
    }

    private void testWebService() {

        try {
            // Create AlmaWebService object:
            AlmaWebServices aws = AlmaWebServices.create("web service URL", "user name", "user password",
                    "institution code");

            // *** Getting user requests (2 examples) ***

            // Get ALL user requests (max 10 results):
            getUserRequests(aws, "user name", "userName", "", "0", "10");

            // Get only "HOLD" user requests:
            getUserRequests(aws, "user name", "userName", "HOLD", "0", "10");

            // *** Canceling user requests ***

            // Cancel user requests:
            String idsOfRequestsToCancel = "75981070000121 , 70694990000121"; // IDs
                                                                              // as
                                                                              // CSV
            cancelRequests(aws, "user name", "userName", idsOfRequestsToCancel);

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    private void cancelRequests(AlmaWebServices aws, String userIdentifier, String identifierType,
            String requestIdsToCancel) {
        System.out.println("*************************************");
        System.out.println("getUserRequests userIdentifier: " + userIdentifier + ", identifierType: " + identifierType);
        System.out.println("-----------------------------------");
        // Setting params:
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, userIdentifier);
        if (identifierType != null) {
            paramsMap.put(AlmaWebServices.INPUT_PARAM_2, identifierType);
        } else {
            paramsMap.put(AlmaWebServices.INPUT_PARAM_2, "");
        }
        paramsMap.put(AlmaWebServices.INPUT_PARAM_3, requestIdsToCancel);

        // Invoke Web Service:
        invokeWS(aws, CANCEL_REQUESTS, paramsMap);
        System.out.println("*************************************");
    }

    private void getUserRequests(AlmaWebServices aws, String userIdentifier, String identifierType, String requestType,
            String from, String numOfResults) {
        System.out.println("*************************************");
        System.out.println("getUserRequests userIdentifier: " + userIdentifier + ", identifierType: " + identifierType
                + ", Request Type =" + requestType);
        System.out.println("-----------------------------------");
        // Setting params:
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, userIdentifier);
        if (identifierType != null) {
            paramsMap.put(AlmaWebServices.INPUT_PARAM_2, identifierType);
        } else {
            paramsMap.put(AlmaWebServices.INPUT_PARAM_2, "");
        }
        paramsMap.put(AlmaWebServices.INPUT_PARAM_3, requestType);
        paramsMap.put(AlmaWebServices.INPUT_PARAM_4, from);
        paramsMap.put(AlmaWebServices.INPUT_PARAM_5, numOfResults);

        // Invoke Web Service:
        invokeWS(aws, GET_USER_REQUESTS, paramsMap);
        System.out.println("*************************************");
    }

    private void invokeWS(AlmaWebServices aws, String wsMethod, Map<String, String> params) {
        try {
            String result = aws.invoke(WS_LINK, wsMethod, params);
            System.out.println(result);

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

}
