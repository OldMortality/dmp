package examples;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

import com.exlibris.alma.sdk.AlmaWebServices;

public class LoanWSExample {

    public static final String GET_USER_LOANS = "getUserLoans";
    public static final String RENEW_USER_LOANS = "renewUserLoans";
    public static final String WS_LINK = "LoanWebServices";

    public static void main(String[] args) {
        LoanWSExample example = new LoanWSExample();
        example.testLocal();
    }

    private void testLocal() {

        try {
            FileInputStream fstream = new FileInputStream("c:\\loan_renew_items.xml");
            DataInputStream in = new DataInputStream(fstream);
            BufferedReader br = new BufferedReader(new InputStreamReader(in));
            String strLine;
            String loanRenewItems = "";
            while ((strLine = br.readLine()) != null) {
                loanRenewItems += strLine;
            }

            // Close the input stream
            in.close();

            AlmaWebServices aws = AlmaWebServices.create("web service URL", "user name", "user password",
                    "institution code");

            // testRenewUserLoans(aws,loanRenewItems );
            testGetLoanInfo(aws, "user name", "userName", "0", "30");
        } catch (Exception e) {

        }

    }

    private void testGetLoanInfo(AlmaWebServices aws, String userIdentifier, String identifierType, String from,
            String maxResult) {
        System.out.println("\n LoanWebServices userIdentifier: " + userIdentifier + ", identifierType: "
                + identifierType);
        System.out.println("---------------------");
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, userIdentifier);
        if (identifierType != null) {
            paramsMap.put(AlmaWebServices.INPUT_PARAM_2, identifierType);
        } else {
            paramsMap.put(AlmaWebServices.INPUT_PARAM_2, "");
        }
        paramsMap.put(AlmaWebServices.INPUT_PARAM_3, from);
        paramsMap.put(AlmaWebServices.INPUT_PARAM_4, maxResult);

        invokeWS(aws, GET_USER_LOANS, paramsMap);
        System.out.println("---------------------");
    }

    private void testRenewUserLoans(AlmaWebServices aws, String loanIds) {
        System.out.println("\n LoanWebServices renewUserLoans: ");
        System.out.println("---------------------");
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, loanIds);
        invokeWS(aws, RENEW_USER_LOANS, paramsMap);
        System.out.println("---------------------");
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
