package com.benjdragocreations.trialapplication2;

import android.net.Uri;
import android.os.Build;
import android.util.JsonReader;
import android.util.Log;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import androidx.annotation.RequiresApi;

//Select employee_name from Employee where EmployeeID =
//https://www.googleapis.com/books/v1/volumes?
//
public class NetworkLinks {

    private static final String Log_tag = NetworkLinks.class.getSimpleName();

    // Base URL : Enter the URL for your online Database here .
    private static final String BASE_URL = "http://dummy.restapiexample.com/api/v1/employees";
    // Parameter for the search string.
    //private static final String QUERY_PARAM = "Select employee_name from Employee where EmployeeID =";
    private static final String QUERY_PARAM = "q";
    // Parameter that limits search results.
    //private static final String MAX_RESULTS = "maxResults";
    // Parameter to filter by print type.
    //private static final String PRINT_TYPE = "printType";

    //@RequiresApi(api = Build.VERSION_CODES.KITKAT)
    static String Permissioninfo(String ID)  {
        HttpURLConnection httpURLConnection= null;
        BufferedReader bufferedReader = null;
        String IDJSONString = null;

        try {
            /*URL builtURI = URL.Parse(BOOK_BASE_URL).buildUpon()
                    .appendQueryParameter(QUERY_PARAM, ID)
                    .appendQueryParameter(MAX_RESULTS, "10")
                    .appendQueryParameter(PRINT_TYPE, "books")
                    .build();*/
            //Uri uri = Uri.parse(BASE_URL).buildUpon().appendQueryParameter(QUERY_PARAM,ID).build();
            Uri uri = Uri.parse(BASE_URL).buildUpon().build();
            URL url = new URL(uri.toString());
            httpURLConnection = (HttpURLConnection) url.openConnection();
            httpURLConnection.setRequestMethod("GET");
            httpURLConnection.connect();

            //Inputstream
            InputStream inputStream = httpURLConnection.getInputStream();

            //inputstream buffered reader
            bufferedReader = new BufferedReader(new InputStreamReader(inputStream));

            //stringbuilder
            StringBuilder stringBuilder = new StringBuilder();

            String line;
            while ((line = bufferedReader.readLine()) != null) {
                stringBuilder.append(line);
                // Since it's JSON, adding a newline isn't necessary (it won't
                // affect parsing) but it does make debugging a *lot* easier
                // if you print out the completed buffer for debugging.
                stringBuilder.append("\n");
            }

            if (stringBuilder.length() == 0) {
                // Stream was empty. No point in parsing.
                return null;
            }

            IDJSONString = stringBuilder.toString();

        }

        catch (Exception e) {
            e.printStackTrace();
        }

        finally {

            if(httpURLConnection!= null)
            {
                httpURLConnection.disconnect();
            }

            if (bufferedReader != null) {

                try {
                    bufferedReader.close();
                }

                catch (IOException e) {
                    e.printStackTrace();
                }

            }
        }

        Log.d(Log_tag,IDJSONString);

        return IDJSONString;
        //return ("Employee not found");

    }

}
