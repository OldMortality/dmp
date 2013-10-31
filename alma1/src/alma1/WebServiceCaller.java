package alma1;

import java.util.HashMap;
import java.util.Map;

import org.jdom2.Element;

import com.exlibris.alma.sdk.AlmaWebServices;

public class WebServiceCaller {

	
	AlmaWebServices aws = AlmaWebServices.create(
			"https://ap01.alma.exlibrisgroup.com", "webserviceuser",
			"Fredfred123", "64OTAGO_INST");

	
	void addUser(Element userRecord) {

	
    	Map<String, String> paramsMap = new HashMap<String, String>();
		paramsMap.put(AlmaWebServices.INPUT_PARAM_1, userRecord.toString());
		
		invokeWS(aws, AlmaWebServices.CREATE_USER, paramsMap);

	}

	private void invokeWS(AlmaWebServices aws, String wsMethod,
			Map<String, String> params) {
		try {
			String result = aws.invoke(
					AlmaWebServices.GET_USER_DETAILS_WS_LINK, wsMethod, params);
			System.out.println(result);

		} catch (Exception e) {
			System.out.println(e.getMessage());
		}
	}

}
