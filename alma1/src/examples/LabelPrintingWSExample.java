package examples;
import java.util.HashMap;
import java.util.Map;

import com.exlibris.alma.sdk.AlmaWebServices;

public class LabelPrintingWSExample {

    public static void main(String[] args) {
        LabelPrintingWSExample example = new LabelPrintingWSExample();
        example.testLocal();
    }

    private void testLocal() {
        AlmaWebServices aws = AlmaWebServices.create("web service URL", "user name", "user password",
                "institution code");
        testLabel(aws, "234999960000121", "false");
    }

    private void testLabel(AlmaWebServices aws, String value, String isBarcode) {
        System.out.println("\nLabel for Printing for value: " + value);
        System.out.println("---------------------");
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, "1.0");
        paramsMap.put(AlmaWebServices.INPUT_PARAM_2, value);
        paramsMap.put(AlmaWebServices.INPUT_PARAM_3, isBarcode);

        invokeWS(aws, AlmaWebServices.LABEL_PRINTING_GET_METHOD, paramsMap);
    }

    private void invokeWS(AlmaWebServices aws, String wsMethod, Map<String, String> params) {
        try {
            String labelDetails = aws.invoke(AlmaWebServices.LABEL_PRINTING_WS, wsMethod, params);
            System.out.println(labelDetails);

        } catch (Exception e) {
            Throwable ex = e.getCause();

            System.out.println(e.getMessage());
        }
    }
}
