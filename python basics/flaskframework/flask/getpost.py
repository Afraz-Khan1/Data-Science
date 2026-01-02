from flask import Flask,render_template,request   #request is a library that can be used to capture the i.e(form fill) information on page.

app=Flask(__name__)

@app.route("/") 
def welcome():
    return render_template('home.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about us")
def about():
    return render_template('aboutus.html')

@app.route("/form",methods=["GET","POST"])
def form():
    if(request.method=="POST"): # this runs when submit pressed means post request generated. but if we remove action=/submit from html everything works same just on same form route "/form". but if we inlucde action=/submit then it hits other submit route where it shows value.
        name=request.form["name"] # retriving name information from form stored in "name" and storing it in varibale here.
        age=request.form["age"]   
        return f"Hello {name}\n Your Age is {age} !"
    
    return render_template('form.html') # this will run on GET. Yes, it runs first — when you open the form page (GET) before submitting it. when submitting values than post return runs inside if.
#if we dont write GET in methods flask auto consider it. GET method means the request of page we are on. or viewing a page is GET method so its on auto from flask even if we dont write

@app.route("/submit",methods=["GET","POST"])
def submit():
    if(request.method=="POST"):
        name=request.form["name"]
        age=request.form["age"]
        return f"Hello {name}\n Your Age is {age} !"
    
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)
