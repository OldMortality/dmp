package alma1;

import java.util.HashMap;
import java.util.Map;

import com.exlibris.alma.sdk.AlmaWebServices;

public class UserWSExample {

    public static void main(String[] args) {
        UserWSExample example = new UserWSExample();
        example.testLocal();
    }

    private void testLocal() {
        AlmaWebServices aws = AlmaWebServices.create("web service URL", "user name", "user password",
                "institution code");

        testGetUserInfo(aws, "userIdentifier", "identifierType");

        // example when there is no identifierType
        testGetUserInfo(aws, "userIdentifier", null);

    }

    private void testGetUserInfo(AlmaWebServices aws, String userIdentifier, String identifierType) {

        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, userIdentifier);
        if (identifierType != null) {
            paramsMap.put(AlmaWebServices.INPUT_PARAM_2, identifierType);
        } else {
            // there is no identifierType
            paramsMap.put(AlmaWebServices.INPUT_PARAM_2, "");
        }

        invokeWS(aws, AlmaWebServices.GET_USER_DETAILS, paramsMap);

    }

    private void invokeWS(AlmaWebServices aws, String wsMethod, Map<String, String> params) {
        try {
            String result = aws.invoke(AlmaWebServices.GET_USER_DETAILS_WS_LINK, wsMethod, params);
            System.out.println(result);

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}