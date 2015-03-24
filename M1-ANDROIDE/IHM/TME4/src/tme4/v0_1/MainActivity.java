package tme4.v0_1;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemSelectedListener;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.activity_main, menu);
        fillListeTauxSpinner();
        return true;
    }
    
    public void fillListeTauxSpinner(){
    	Spinner spinner = (Spinner) findViewById(R.id.spinner_taux);
    	// Create an ArrayAdapter using the string array and a default spinner layout
    	ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
    	        R.array.list_taux, android.R.layout.simple_spinner_item);
    	// Specify the layout to use when the list of choices appears
    	adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
    	// Apply the adapter to the spinner
    	spinner.setAdapter(adapter);
    	spinner.setOnItemSelectedListener(new SpinnerActivity(this));
    	
    }
    
    public void convert(View sender){
    	    	
    	((EditText)findViewById(R.id.edit_result)).setText(String.valueOf(Float.parseFloat(((EditText)findViewById(R.id.edit_euros)).getText().toString())*Float.parseFloat(((EditText)findViewById(R.id.edit_taux)).getText().toString())));
    }
    
    public class SpinnerActivity extends Activity implements OnItemSelectedListener {

    	private Activity activity;
    	
    	public SpinnerActivity(Activity activity){
    		super();
    		this.activity = activity;
    		
    	}
    	
		@Override
		public void onItemSelected(AdapterView<?> parent, View view, 
	            int pos, long id) {
			EditText editText = (EditText) activity.findViewById(R.id.edit_taux);
			switch(pos){
	    	case 0:
	    		editText.setText("1.02520");
	    		editText.setEnabled(false);

	    		break;
	    	case 1:
	    		editText.setText("130.988");
	    		editText.setEnabled(false);

	    		break;
	    	case 2:
	    		editText.setText("6.365");
	    		editText.setEnabled(false);

	    		break;
	    	case 3:
	    		editText.setText("0");
	    		editText.setClickable(true);
	    		editText.setEnabled(true);
	    		break;
	    	default:
	    		editText.setText("0");
	    		editText.setClickable(true);
	    		editText.setEnabled(true);
	    		
	    	}
			
		}

		@Override
		public void onNothingSelected(AdapterView arg0) {
			// TODO Auto-generated method stub
			
		}
    }
    
}
