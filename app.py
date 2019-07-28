from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template

import xgboost
import shap
import sklearn
import joblib
import pandas as pd
import numpy as np
import redis

from modelling_variables import Variables
from config import Development as status

model_fname="modelling/predict_model.joblib"

app = Flask(__name__)

@app.route("/predict/<find>", methods=["GET"])
def predict(find):
    """
    Write the functional logic for recieving a county(FIPS)
    and returning a flip prediction probability
    """

    # Get data
    data = pd.read_csv("modelling/total_data.csv")
    
    # Find the input variable
    if try_int(find) == True:
        data = data.loc[data['fips']==int(find)][Variables.MODELLING_VAR]
    elif "county" in find.lower():
        data = data.loc[data['county_name']==find][Variables.MODELLING_VAR]
    else:
        data = data.loc[data['county_name']==find+" County"][Variables.MODELLING_VAR]

    data = np.array(data).reshape((1,-1))
    # Load model
    model = joblib.load(model_fname)
    result = model.predict(data, validate_features=False)[0]


    #return_val = {"value_title": fips}
    #return jsonify(return_val)
    return render_template('test_template.html', prediction=result, name=find)


def try_int(_str_):
    try:
        a = int(_str_)
        return True
    except:
        return False



if __name__ == "__main__":
    app.run(debug=status.DEBUG, port=status.PORT)