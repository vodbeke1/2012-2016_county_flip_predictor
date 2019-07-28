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

from modelling_variables import Variables



from config import Development as status

model_fname="modelling/predict_model.joblib"

app = Flask(__name__)

@app.route("/predict/<fips>", methods=["GET"])
def predict(fips):
    """
    Write the functional logic for recieving a county(FIPS)
    and returning a flip prediction probability
    """

    # Get data
    data = pd.read_csv("modelling/total_data.csv")
    #data = data.loc[data['Fips']==int(fips)].to_dict()
    data = data.loc[data['fips']==int(fips)][Variables.MODELLING_VAR]

    data = np.array(data).reshape((1,-1))
    # Load model
    model = joblib.load(model_fname)
    result = model.predict(data, validate_features=False)


    #return_val = {"value_title": fips}
    #return jsonify(return_val)
    return render_template('test_template.html', prediction=result[0])


if __name__ == "__main__":
    app.run(debug=status.DEBUG, port=7898)