from flask import Flask
from flask import jsonify
from flask import request

from config import Development as status


app = Flask(__name__)

@app.route("/", method=["POST"])
def predict():
    """
    Write the functional logic for recieving a county(FIPS)
    and returning a flip prediction probability
    """
    return_val = {"value_title": "value"}
    return jsonify(return_val)


if __name__ == "__main__":
    app.run(debug=status.DEBUG)