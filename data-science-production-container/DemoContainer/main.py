from ds_prod_api.apis.FlaskApi import FlaskApi

from predictive_models import baseline as baseline_model
from feature_extractors import baseline as baseline_extractor

model = baseline_model.BaselineModel()
model.load()
extractor = baseline_extractor.BaselineFeatureExtractor()

api = FlaskApi(model, extractor)
api.run()
