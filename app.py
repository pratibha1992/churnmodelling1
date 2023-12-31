import pickle
from flask import Flask,request,app,jsonify,render_template,url_for

import numpy as np
import pandas as pd

app=Flask(__name__)
#load the model
model=pickle.load(open('rscvmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    output=rscv.predict(data)
    print(output[0])
    return jsonify(output[0])

if __name__="__main__":
    app.run(debug=True)
