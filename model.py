import os
import json

import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost

from modelling_variables import Variables
from decision_tree_predict import predict



class decisionTree:
    def __init__(self):
        self.model = None
        self.params = {}
        self.n_estimators = None
        self.base_score = 0

class model:

    MODEL_TYPES = [ "decision tree", "neural net"]

    def __init__(self):
        self.decision_tree = None
        self.nn = None
        self.data_path = "data/"

        # Dataframes
        self.data = {"county_facts_dictionary12_16": None,
                    "county_facts12_16": None,
                    "US_County_Level_Presidential_Results_12-16": None,
                    "votes12_16": None}
                    
        self.data_main = None

        self.model_features = Variables.MODELLING_VAR

    @staticmethod
    def get_model_types():
        print("Available model types %s" % model.MODEL_TYPES)

    def init_model(self, model_type, **kwargs):
        """Check to see if there is model already 
        trained if not then train a model"""
        
        if model_type == "decision tree":
            if not self.decision_tree:
                """Train decision tree"""
                pass
                #self.decision_tree = self.train_decision_tree(kwargs)
        elif model_type == "neural net":
            if not self.nn:
                """Train nn"""
                pass
        else:
            raise NameError("Not valid model type")

    def load_data(self):
        for k in self.data.keys():
            if self.data[k] is None:
                self.data[k] = pd.read_csv(self.data_path+k+".csv")
            print("Load complete: %s" % k)

    def set_target(self):
        tbl = "US_County_Level_Presidential_Results_12-16"
        self.data[tbl]["target"] = self.data[tbl].apply(lambda x: 1 if x["per_dem_2012"] - x ["per_dem_2016"] >= (0.4*x["per_dem_2012"]) else 0, axis=1)
        print("Target set") 

    def preprocess_data(self):
        self.data_main = pd.merge(self.data["US_County_Level_Presidential_Results_12-16"], 
                                  self.data["county_facts12_16"], 
                                  how="inner", 
                                  left_on="FIPS", 
                                  right_on="fips")
        self.data_main.drop("Unnamed: 0", axis=1, inplace=True)
        
        # Cache data to hard disk
        self.data_main.to_csv(self.data_path+"data_main.csv")
        print("Data preprocessed")
    
    def test_train_split(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data_main[self.model_features], 
                                                                                self.data_main["target"], 
                                                                                test_size=0.33, 
                                                                                random_state=42)
        print("Data split")
        


    def train_decision_tree(self):
        self.decision_tree = decisionTree()
        self.decision_tree.model = xgboost.XGBRegressor()
        self.decision_tree.model.fit(self.X_train, self.y_train)
        self.decision_tree.model.get_booster().dump_model("params/dt_params.json", dump_format='json')
        
        self.decision_tree.n_estimators = self.decision_tree.model.n_estimators

    def _predict(self, input_vars={}):
        with open("params/dt_params.json") as k:
            params = json.load(k)

        return predict(input_vars, params, tree_limit=self.decision_tree.n_estimators, format_to_dictionary=False)
         
        

    
    def train_nn(self):
        return ""
    
    def retrain_model(self):
        pass

if __name__ == "__main__":
    m = model()
    m.load_data()
    m.set_target()
    m.preprocess_data()
    m.test_train_split()
    m.train_decision_tree()
    with open("test_json/test1.json") as k:
        input = json.load(k)
    p = m._predict(input_vars=input)
    print(p)


        