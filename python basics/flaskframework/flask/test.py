from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('aboutus.html')

@app.route("/form")
def form():
    return render_template('form.html')    #runs GET when forms open. as we using /sumbit route seperately for submmiting the values in form we dont need same code here as submit function below.


@app.route("/submit",methods=["POST"]) # this only runs when in form submit is pressed so the route changes to submit and always method will be post as form runs the get method
def submit():
    if request.method=="POST":
        name=request.form["name"]
        age=request.form["age"]
        return f"Hello {name}, Your Age is {age}"
    
@app.route("/successif/<int:score>")
def successif(score):
    return render_template('successif.html',result=score)

@app.route("/success")
def success():
    return render_template('success.html',result={"phy":56,"chem":60,"maths":40})

@app.route("/successres",methods=["POST","GET"]) # if dont write get its already understood
def successres():
    if request.method=="POST":
        maths=float(request.form["math"])       # form data sent by post is stored in request.form in flask
        chem=float(request.form["chem"])       
        phy=float(request.form["phy"])       
        isl=float(request.form["isl"])
        total_score=(maths+chem+phy+isl)/4
    else:
        return render_template('successres.html')
    return redirect(url_for('successif',score=total_score))

if __name__=="__main__":
    app.run(debug=True)