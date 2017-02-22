from ds_prod_api.abstracts import Model

class DemoModel(Model):
    def load(self):
        print("hi")

    def predict(self, feature_vector):
        return "Result"

    def default(self):
        return "In case of problem return this"