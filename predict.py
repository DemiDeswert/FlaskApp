from fastai import *
from fastai.vision import *
import pickle
def predict(image):
    model = pickle.load(open('model.pkl', 'rb'))
    prediction = model.predict(image).save("./static/prediction.jpg")
    return 