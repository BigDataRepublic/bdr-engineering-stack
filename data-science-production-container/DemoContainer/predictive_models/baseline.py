from ds_prod_api.abstracts import Model
import os
import pickle
import sys

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

sys.path.append(path)

from models import *

class BaselineModel(Model):
    def load(self):
        self.estimator = PartyClassifier()
        self.estimator = pickle.load(open(path + '/../models/PartyClassifier.pkl', "rb"), encoding="UTF-8")

    def predict(self, feature_vector):
        self.estimator.predict_proba(feature_vector)

    def default(self):
        return "In case of problem return this"