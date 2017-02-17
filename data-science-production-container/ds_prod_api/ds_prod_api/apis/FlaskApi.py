from flask import Flask


class FlaskApi(object):


    def __init__(self, model, feature_extractor):
        self.model = model
        self.feature_extractor = feature_extractor
        self.app = Flask(__name__)
        self.app.add_url_rule('/predict/<string:predict_id>', 'predict', self.predict)

    def predict(self, predict_id):
        try:
            features = self.feature_extractor.get_features(predict_id)
            result = self.model.predict(features)

        except Exception:
            result = self.model.default()

        return result

    def run(self):
        self.app.run(host='0.0.0.0')

