from flask import Flask

## this is the basic structure of flask frame work.
'''
we created an instance of flask class,
which will be our wsgi(web server gate way interface) application.
'''
## wsgi application # this will connect our webserver like web site page to our application.
app=Flask(__name__) ##instance of flask class 

## this piece of code should come before the initial condition __name__ vali.
## / means homepage. and this @ sign means decorator. so function below this decorator will be called in auto.
# when you run this program you see the msg welcome to homepage but thats not the home page put (/) in path of webpage running than press enter now you are on the home page.
# you can add as many route you want above initial condition. but sub function name should be different for each route.
#@app.route("/") → a decorator that defines a route (URL path).
#The function below it runs when that route is visited.

@app.route("/")  
def welcome():
    return "Welcome To Home Page, you just reload the page after any changes in the msg and changes will be visible only if debug is true server auto restart or else you have to restart the server"

@app.route("/index") 
def index(): # sub function
    return "Welcome To Index Page"

## initial condition for every application.
if __name__=="__main__":
    app.run(debug=True) 

# using debug = true will let the developer to not start the server again and again after doing any changes in data like welcome to homepage he just save the changes
# while running so server got auto restart and we can see changes after reloading the page so this debug is usefull there or else if have to restart by self.

