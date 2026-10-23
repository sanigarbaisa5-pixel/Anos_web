from flask import Flask,render_template
import datetime
date_heur = datetime.datetime.now()

app = Flask("__name__")

@app.route('/')
def bonjour():
 
    return render_template("index.html")
    
    
if __name__=="__main__":
    app.run(debug=True)