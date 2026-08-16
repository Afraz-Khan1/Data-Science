from flask import Flask,request,render_template,jsonify # jsonify to return result in json. and render_template to run html file.
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

application=Flask(__name__)
app=application

ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict_data",methods=['GET','POST'])
def predict_data():
     if request.method=="POST":
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))

        scaled_data=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]]) #we used only transform as fit_transform is
        #already applied to our training data so we use transform only on our form data.

        result=ridge_model.predict(scaled_data)

        return render_template('home.html',results=result[0])  # we give result in form of list.

     else:
         return render_template('home.html') # we run home to html where our form is present.


if __name__ =="__main__":
    app.run(host="0.0.0.0",debug=True) #hose 0.0.0.0 is running on your local machine.