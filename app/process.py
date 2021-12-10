# load_model_sample.py
from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import os
from app import APP_ROOT


def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(150, 150))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

    return img_tensor


def predict_img(path):
    # load model
    print(APP_ROOT)
    target = os.path.join('/app/', 'static/')
    model = load_model(target+"ModelMLCNN.h5")
    labels = ["cat", "dog"]
    # image path
    target = os.path.join('/app/', 'temp/')
    img_path = (target+path)    # dog
    #img_path = '/media/data/dogscats/test1/19.jpg'      # cat
    # load a single image
    new_image = load_image(img_path)

    # check prediction
    pred = model.predict(new_image)
    label = np.argmax(pred)
    #os.remove(img_path)
    return labels[label]