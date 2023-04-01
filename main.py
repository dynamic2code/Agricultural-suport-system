from flask import Flask
from apps_blueprint import app_blueprint

app = Flask(__name__)
app.register_blueprint(app_blueprint)

if __name__ == "__main__":
  app.run(debug=True)



    #crop recomendation dataset from kaggel https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset?resource=download
    # N - ratio of Nitrogen content in soil
    # P - ratio of Phosphorous content in soil
    # K - ratio of Potassium content in soil
    # temperature - temperature in degree Celsius
    # humidity - relative humidity in %
    # ph - ph value of the soil
    # rainfall - rainfall in mm


