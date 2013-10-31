package examples;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

import com.exlibris.alma.sdk.AlmaWebServices;

public class CourseWSExample {

    public static void main(String[] args) {
        CourseWSExample example = new CourseWSExample();
        example.testLocal();
    }

    private void testLocal(){
       AlmaWebServices aws = AlmaWebServices.create("web service URL", "user name", "user password", "institution code");

       testCreateCourse(aws,loadFile());
       testUpdateCourse(aws,loadFile());
       testDeleteCourse(aws,"course id");
       testCreateReadinglist(aws,"reading list id",loadFile());
       testUpdateReadinglist(aws,loadFile());
       testDeleteReadinglist(aws,"reading list id");
       testCreateCitation(aws,"reading list id",loadFile());
       testUpdateCitation(aws,loadFile());
       testDeleteCitation(aws,"citation id");
       testSearchCourseInfo(aws, "code=Code", "0", "20");
    }

    private String loadFile(){
        FileInputStream fstream = null;
        try {
            fstream = new FileInputStream("file");// file that contains an xml based on the relevant xsd (course, reading list or citation)


        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        DataInputStream in = new DataInputStream(fstream);
        BufferedReader br = new BufferedReader(new InputStreamReader(in));
        String strLine;
        String fileAsString="";
        try {
            while ((strLine = br.readLine()) != null)   {
                fileAsString+=strLine;
            }
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        return  fileAsString;

    }

    private void testUpdateCitation(AlmaWebServices aws,String xmlFile){
        System.out.println("\nUpdateCitation: ");
        System.out.println("---------------------");
        Map<String, String> paramsMap = new HashMap<String, String>();
               paramsMap.put(AlmaWebServices.INPUT_PARAM_1, xmlFile);


        invokeWS(aws, "updateCitation", paramsMap);
    }

    private void testCreateCourse(AlmaWebServices aws,String xmlFile){
        System.out.println("\nCreateCourse: ");
        System.out.println("---------------------");
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, xmlFile);


        invokeWS(aws, "createCourse", paramsMap);
    }

    private void testUpdateCourse(AlmaWebServices aws,String xmlFile){
        System.out.println("\nUpdateCourse: ");
        System.out.println("---------------------");
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, xmlFile);


        invokeWS(aws, "updateCourse", paramsMap);
    }


    private void testDeleteCourse(AlmaWebServices aws,String courseId){
        System.out.println("\nCreateCourse: ");
        System.out.println("---------------------");
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, courseId);


        invokeWS(aws, "deleteCourse", paramsMap);
    }

    private void testCreateReadinglist(AlmaWebServices aws,String courseId,String xmlFile){
        System.out.println("\nCreateReadingList: ");
        System.out.println("---------------------");
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, courseId);
        paramsMap.put(AlmaWebServices.INPUT_PARAM_2, xmlFile);


        invokeWS(aws, "createReadinglist", paramsMap);
    }

    private void testUpdateReadinglist(AlmaWebServices aws,String xmlFile){
        System.out.println("\nUpdateReadinglist: ");
        System.out.println("---------------------");
        Map<String, String> paramsMap = new HashMap<String, String>();

        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, xmlFile);


        invokeWS(aws, "updateReadinglist", paramsMap);
    }

    private void testDeleteReadinglist(AlmaWebServices aws,String readinglistId){
        System.out.println("\nDeleteReadinglist: ");
        System.out.println("---------------------");
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, readinglistId);


        invokeWS(aws, "deleteReadinglist", paramsMap);
    }


    private void testCreateCitation(AlmaWebServices aws,String readinglistId,String xmlFile){
        System.out.println("\nCreateCitation: ");
        System.out.println("---------------------");
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, readinglistId);
        paramsMap.put(AlmaWebServices.INPUT_PARAM_2, xmlFile);


        invokeWS(aws, "createCitation", paramsMap);
    }

    private void testDeleteCitation(AlmaWebServices aws,String citationId){
        System.out.println("\nDeleteCitation: ");
        System.out.println("---------------------");
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_1, citationId);



        invokeWS(aws, "deleteCitation", paramsMap);
    }


    private void testSearchCourseInfo(AlmaWebServices aws, String cql, String from, String to){
        System.out.println("\nSearchCourseInfo by: " + cql);
        System.out.println("---------------------");
        Map<String, String> paramsMap = new HashMap<String, String>();
        paramsMap.put(AlmaWebServices.INPUT_PARAM_CQL, cql);
        paramsMap.put(AlmaWebServices.INPUT_PARAM_FROM, from);
        paramsMap.put(AlmaWebServices.INPUT_PARAM_TO, to);

        invokeWS(aws, AlmaWebServices.COURSE_SEARCH_METHOD, paramsMap);
    }

    private void invokeWS(AlmaWebServices aws, String wsMethod, Map<String, String> params){
        try {
            String courseDetails = aws.invoke(AlmaWebServices.COURSE_WS,
                    wsMethod, params);
            System.out.println(courseDetails);

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
