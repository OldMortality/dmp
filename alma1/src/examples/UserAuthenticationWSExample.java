package examples;

import java.util.HashMap;
import java.util.Map;

import com.exlibris.alma.sdk.AlmaWebServices;

public class UserAuthenticationWSExample {


    public static void main(String[] args) {
        UserAuthenticationWSExample example = new UserAuthenticationWSExample();
        example.testLocal();
    }

    private void testLocal() {
        AlmaWebServices aws = AlmaWebServices.create("web service URL", "user name",
                "user password", "institution code");

        testAuthenticateUser(aws, "user identifier", "user password");
    }

    private void testAuthenticateUser(AlmaWebServices aws, String userIdentifier, String password) {

        Map<String, String> paramsMap = new HashMap<String, String>();
        if (userIdentifier != null) {
            paramsMap.put(AlmaWebServices.INPUT_PARAM_1, userIdentifier);
        }else{
            //there is no username
            paramsMap.put(AlmaWebServices.INPUT_PARAM_1, "");
        }
        if (password != null) {
            paramsMap.put(AlmaWebServices.INPUT_PARAM_2, password);
        }else{
            //there is no password
            paramsMap.put(AlmaWebServices.INPUT_PARAM_2, "");
        }

        invokeWS(aws, AlmaWebServices.AUTHENTICATE_USER, paramsMap);
    }

    private void invokeWS(AlmaWebServices aws, String wsMethod, Map<String, String> params) {
        try {
            String result = aws.invoke(AlmaWebServices.AUTHENTICATE_USER_WS_LINK, wsMethod, params);
            System.out.println(result);

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
