from ds_prod_api.abstracts import Model
import os
import pickle
import sys
import nltk

import src.models

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

sys.path.append(path)

class BaselineModel(Model):
    def load(self):
        nltk.download("stopwords")
        nltk.download("punkt")
        self.estimator = pickle.load(open(path + '/../models/PartyClassifier.pkl', "rb"), encoding="UTF-8")

    def predict(self, feature_vector):
        return str(self.estimator.predict(feature_vector))

    def default(self):
        return "In case of problem return this"