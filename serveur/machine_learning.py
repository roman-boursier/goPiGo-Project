from keras.applications.mobilenet import MobileNet, decode_predictions
from keras.models import load_model

import numpy as np
from PIL import Image
from matplotlib.pyplot import imshow
from skimage.transform import resize
from tabulate import tabulate

def predictImageClasse():

    model = MobileNet()

    img = np.asarray(Image.open('./image.jpg'))
    img = resize(img, [224, 224])
    imshow(img)
    X = np.reshape(img, [1, 224, 224, 3])

    preds = model.predict(X)

    #The 5 most likely between 1000 image net classes
    print(tabulate(decode_predictions(preds, top=5)[0], headers=['Name', 'Probability']))

    return decode_predictions(preds, top=5)[0]