from flask import Flask,render_template ## this render_template used to redirect to html code file . but all these files should in in template name folder

## now we use Html tags/templates . templates are html tags(<html></html>) where flask puts the real value on execution.
app=Flask(__name__)

# decorators are used here.
@app.route("/") ## this is home page dont write /home or it will start every time from not found. / is home
def welcome():
    ##return "<html><H1>Welcome To The Home Page<H1/><html/>" ## but this is not good practice as we need lot of html code we make another file for template(meaning html code which will be repalced will value on execution) and redirect it to that html file.
    return render_template('home.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about us")
def about():
    return render_template('aboutus.html')

if __name__=="__main__":
    app.run(debug=True)
