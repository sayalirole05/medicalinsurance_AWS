import re
from flask import Flask, jsonify, render_template, request,redirect, url_for
import config
from project_app.utils import MedicalInsurence

app = Flask(__name__)

    
@app.route('/')
def main():
    return render_template('home.html',)

@app.route('/predict_charges',methods = ['POST','GET'])
def home():
    print("We are using POST method")
    data = request.form
    age = eval(data['a'])
    sex = data['b']
    bmi = eval(data['c'])
    children = eval(data['d'])
    smoker = data['e']
    region = data['f']

    print("age, sex, bmi,children,smoker, region",age, sex, bmi,children,smoker, region)
    med_ins = MedicalInsurence(age, sex, bmi,children,smoker, region)
    charges = med_ins.get_predicted_charges()
   
    return render_template('pred.html', data = charges)
    # return jsonify({"Result": f"Predicted Medical Insurence Charges are : {charges}"})


if __name__ == "__main__":
    app.run(host= '0.0.0.0', port = config.PORT_NUMBER,debug=False)
