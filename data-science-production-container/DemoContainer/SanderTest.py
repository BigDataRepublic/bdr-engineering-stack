from ds_prod_api.apis.FlaskApi import FlaskApi

from predictive_models import demo as demo_model
from feature_extractors import demo as demo_extractor

model = demo_model.DemoModel()
extractor = demo_extractor.DemoFeatureExtractor()

api = FlaskApi(model, extractor)

api.run()