package com.benjdragocreations.trialapplication2;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.loader.app.LoaderManager;
import androidx.loader.content.Loader;
//import android.support.v4.app.loadermanager;
//import android.support.v4.content.Loader;
//import android.support.v4.app.AppCompatActivity;
import android.net.ConnectivityManager;
import android.os.Bundle;
import android.telephony.AvailableNetworkInfo;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity implements View.OnClickListener, LoaderManager.LoaderCallbacks<String> {

    private Button Permissionbtn;
    private Button Searchagainbtn;
    private EditText Inputfield;
    private TextView Title;
    private  Button Exit;
    private String EmpID;
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Permissionbtn = (Button) this.findViewById(R.id.Permission);
        Searchagainbtn = (Button) this.findViewById(R.id.Search_Again);
        Inputfield = (EditText) this.findViewById(R.id.Input_Unique_ID);
        Title = (TextView) this.findViewById(R.id.Message);
        Exit = (Button) this.findViewById(R.id.Exit);

        Permissionbtn.setOnClickListener(this);
        Searchagainbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Permissionbtn.setVisibility(View.VISIBLE);
                Title.setVisibility(View.VISIBLE);
                Searchagainbtn.setVisibility(View.GONE);
                Exit.setVisibility(View.GONE);

            }
        });

        Exit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });
        Searchagainbtn.setVisibility(View.GONE);
        Exit.setVisibility(View.GONE);

        }

    public  void onClick(View v) {

        //String ID = "abc123";
        EmpID = Inputfield.getText().toString();
        //BackgroundTask backgroundTask =new BackgroundTask(this,EmpID);

        //BackgroundTask.execute(EmpID);
        //AlertDialog.Builder dialog = new AlertDialog.Builder(this)
                //.setMessage("Employee not Found");
        /*AlertDialog dialog = new AlertDialog.Builder(this)
                .setMessage("Employee not Found")
                .setNegativeButton("Try Again", null).show();*/
        InputMethodManager inputMethodManager = (InputMethodManager) getSystemService(INPUT_METHOD_SERVICE);

        //Keyboard hiding
        if(inputMethodManager != null)
        {
            inputMethodManager.hideSoftInputFromWindow(v.getWindowToken(),InputMethodManager.HIDE_NOT_ALWAYS);
        }
        /*
        //Network Status
        ConnectivityManager connectivityManager = (ConnectivityManager) getSystemService(CONNECTIVITY_SERVICE);
        AvailableNetworkInfo networkInfo = null;
        if(connectivityManager != null)
        {
            networkInfo = connectivityManager.getActiveNetwork();
        }

        // if network is available and connected
        if(networkInfo != null && networkInfo.isConnected() && EmpID.length() != 0)
        {
            Bundle bundle = new Bundle();
            bundle.putString("EmpID",EmpID);
            getSupportLoaderManager().restartLoader(0,bundle,this);
        }

        // otherwise if no connection tell the user
        */
        Bundle bundle = new Bundle();
        bundle.putString("queryString",EmpID);
        //LoaderManager loaderManager = new
        LoaderManager.getInstance(this).initLoader(0,bundle,  this);
        //getSupportLoaderManager().initLoader(0,bundle,this);
       //Searchagain();

        }

    //public void KeepTalking(final String s) { }
    
    //public void Searchagain(){ }

    @NonNull
    @Override
    public Loader<String> onCreateLoader(int id, @Nullable Bundle args) {

        String querystring ;
        if(args != null)
        {
            querystring = args.getString("queryString");
        }
        else
        {
            querystring = EmpID;
        }
        AlertDialog.Builder dialog = new AlertDialog.Builder(this)
                .setMessage("Employee not Found");
        return new BackgroundTask(this,querystring);
        //return null;
    }

    @Override
    public void onLoadFinished(@NonNull Loader<String> loader, String data) {

        // JSON response conversion
        /*
        try {
            String result = "Employee not found";
            JSONObject jsonObject = new JSONObject(data);
            JSONArray jsonArray = new JSONArray("data");
            int i = 0;
            while (i<jsonArray.length())
            {
                JSONObject jsonObject1 = jsonArray.getJSONObject(i);
                if(jsonObject1.getString("id")==EmpID)
                {
                    //result = jsonObject.get("employee_name").toString();
                    /*AlertDialog dialog = new AlertDialog.Builder(this)
                            .setMessage("Employee not Found")
                            .setNegativeButton("Try Again", null).show();
                    //result =  jsonObject.getString("employee_name");
                    result = "found";
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
            Title.setText(result);
        }

        catch (JSONException e) {
            e.printStackTrace();
        }
        */
        if(data == "Employee not found")
        //if(data == "found")
        {AlertDialog dialog = new AlertDialog.Builder(this)
                .setMessage(data)
                .setNegativeButton("Try Again", null).show();}
        else
        {
            AlertDialog dialog = new AlertDialog.Builder(this)
                    .setMessage(data)
                    .setNegativeButton("Try Again", null).show();
        }
        //Title.setText(data);
        Searchagain();
    }

    @Override
    public void onLoaderReset(@NonNull Loader<String> loader) {


    }
    public void Searchagain()
    {
        Permissionbtn.setVisibility(View.GONE);
        Title.setVisibility(View.GONE);
        Searchagainbtn.setVisibility(View.VISIBLE);
        Exit.setVisibility(View.VISIBLE);
    }
}