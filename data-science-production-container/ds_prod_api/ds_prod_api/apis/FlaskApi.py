from flask import Flask, request


class FlaskApi(object):


    def __init__(self, model, feature_extractor):
        self.model = model
        self.feature_extractor = feature_extractor
        self.app = Flask(__name__)
        self.app.add_url_rule('/predict', 'predictFromBody', self.predict, methods=['POST'])


    @app.route('/users/')
    def predictFromBody(self):
        try:
            content = request.get_json()
            features = self.feature_extractor.get_features(content)
            result = self.model.predict(features)

        except Exception:
            result = self.model.default()

        return result

    def run(self):
        self.app.run(host='0.0.0.0')

