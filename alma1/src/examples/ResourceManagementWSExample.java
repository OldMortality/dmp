package examples;
import java.util.HashMap;
import java.util.Map;

import org.apache.commons.lang.StringUtils;

import com.exlibris.alma.sdk.AlmaWebServices;

public class ResourceManagementWSExample {

    public static final String RETRIEVE_HOLDINGS_INFORMATION_METHOD = "retrieveHoldingsInformation";
    public static final String WS_LINK = "repository/ResourceManagementWebServices";
    public static final String INPUT_PARAM_1 = "arg0";

    public static void main(String[] args) {
        ResourceManagementWSExample example = new ResourceManagementWSExample();
        example.testLocal();
    }

    private void testLocal() {

        AlmaWebServices aws = AlmaWebServices.create("web service URL", "user name", "user password",
                "institution code");
        testRetrieveHoldingsInformation(aws, "992704730000121,2211562730000121");
    }

    private void testRetrieveHoldingsInformation(AlmaWebServices aws, String mmsIds) {
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(INPUT_PARAM_1, StringUtils.isEmpty(mmsIds) ? "" : mmsIds);
        invokeWS(aws, RETRIEVE_HOLDINGS_INFORMATION_METHOD, paramsMap);
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
