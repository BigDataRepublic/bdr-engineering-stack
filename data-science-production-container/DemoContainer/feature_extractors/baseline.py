from ds_prod_api.abstracts import FeatureExtractor

class BaselineFeatureExtractor(FeatureExtractor):
    def get_features(self, json_features_dict):
        return json_features_dict['text']