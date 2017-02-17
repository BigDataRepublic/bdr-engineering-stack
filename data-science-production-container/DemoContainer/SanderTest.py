from ds_prod_api.ds_prod_api.abstracts import Model, FeatureExtractor
from ds_prod_api.ds_prod_api.apis.FlaskApi import FlaskApi


class DemoModel(Model):
    def load(self):
        print("hi")

    def predict(self, feature_vector):
        return "Result"

    def default(self):
        return "In case of problem return this"


class DemoFeatureExtractor(FeatureExtractor):
    def get_features(self, id):
        return None


model = DemoModel()
extractor = DemoFeatureExtractor()

api = FlaskApi(model, extractor)

api.run()