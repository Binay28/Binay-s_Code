package com.benjdragocreations.trialapplication2;

import android.content.Context;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

/*
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLEncoder;
*/

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.loader.content.AsyncTaskLoader;

public class BackgroundTask extends AsyncTaskLoader<String> {
    //Context context;
    private String EmpID;

    public BackgroundTask(@NonNull Context context,String ID) {

        super(context);
        EmpID = ID;
        //context=ctx;
    }

    //public static void execute(String ID) {// OutputStream outputStream = httpURLConnection.getOutputstream();}

    @Override
    protected void onStartLoading() {

        super.onStartLoading();
        forceLoad();
    }

    @Nullable
    @Override
    public String loadInBackground() {

        //URL where database is hosted
        /*try {
            URL url =new URL("Enter your URL here");
            HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
            httpURLConnection.setRequestMethod("GET");
            httpURLConnection.setDoInput(true);
            httpURLConnection.setDoOutput(true);
            OutputStream outputStream = httpURLConnection.getOutputStream();
            BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(outputStream));
            String post_data = URLEncoder.encode("Select Permission from Employee where EmployeeID is ","UTF-8");
            bufferedWriter.write(post_data);
            bufferedWriter.flush();
            bufferedWriter.close();
            outputStream.close();
            InputStream inputStream = httpURLConnection.getInputStream();
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
            String result = " ";
        }

        catch (MalformedURLException e) {
            e.printStackTrace();
        }

        catch (IOException e) {
            e.printStackTrace();
        }

         */

        //return NetworkLinks.Permissioninfo(EmpID);
        String IDJSONString = NetworkLinks.Permissioninfo(EmpID);
        try {
            String result = "Employee NOT found";
            JSONObject jsonObject = new JSONObject(IDJSONString);
            //JSONObject jsonObject2 = new JSONObject()
            JSONArray jsonArray = jsonObject.getJSONArray("data");
            //JSONObject jsonObject2 = new JSONObject(jsonObject.getString("data"));
            //JSONArray jsonArray = new JSONArray(jsonObject2);
            //JSONArray jsonArray = jsonObject2.getJSONArray("data");
            //JSONArray jsonArray = new JSONArray(IDJSONString);
            //JSONObject jsonObject2 = jsonObject.getJSONObject("data");
            //JSONArray jsonArray = new JSONArray(jsonObject2);
            //JSONArray jsonArray = jsonObject2.getJSONArray("data");
            int i = 0;
            while (i<jsonArray.length())
            {
                JSONObject jsonObject1 = jsonArray.getJSONObject(i);
                //JSONObject jsonObject2 = jsonObject1.getJSONObject("id");
                if(jsonObject1.getInt("id")== Integer.parseInt(EmpID))          //EmpID)
                {
                    result = jsonObject1.get("employee_name").toString();
                    /*AlertDialog dialog = new AlertDialog.Builder(this)
                            .setMessage("Employee not Found")
                            .setNegativeButton("Try Again", null).show();*/
                    //result =  jsonObject.getString("employee_name");
                    //result = "found";
                    //result = Integer.toString(jsonArray.length());
                    break;
                }
                else
                {
                    i++;
                    continue;
                }
            }
            //JSONObject jsonObject = new JSONObject(data);
            //JSONArray jsonArray = jsonObject.getJSONArray("Permission");
            //String result = jsonObject.toString();
            //Title.setText(result);
            return result;
            //return(Integer.toString(jsonArray.length()));
        }

        catch (JSONException e) {
            e.printStackTrace();
        }
       // return null;  // or return Employee Not found
        return ("Employee not found");
    }


}
