import getpass
from flask import Flask, render_template, jsonify
import os
import subprocess
from datetime import datetime
from pytz import timezone 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/htop")
def htop():
    # Capture output of 'top' command (as an alternative to 'htop')
    try:
        top_output = subprocess.check_output(["top", "-bn1"], universal_newlines=True)
    except subprocess.CalledProcessError as e:
        top_output = f"Error running top: {str(e)}"
    
    # Get the current logged-in user
    username = "ashish"
    username = getpass.getuser()

    # Get the current time in IST
    ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    

    # Return the results as plain text or json
    return "<div> Name: sample_name<br>user: "+ username + "<br>Server Time (IST): " + str(ind_time) + "<br>TOP output:<pre>"+  top_output +"<pre></div>"
        # "username": username,
        # "top_output": top_output,
        # 'server_time_ist': ind_time
    

if __name__ == "__main__":
    app.run(debug=True)
