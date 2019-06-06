'''Trains a simple convnet on an OCR dataset and convert it to CoreML

'''

from __future__ import print_function
import sys
import os
import pdb
import keras
import gzip, pickle
import re
import numpy as np
import coremltools
import pandas as pd
from numpy import genfromtxt
from glob import glob
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Dropout, Activation, Flatten, Input
from keras.layers import Conv2D, MaxPooling2D, Lambda, Reshape
from keras.utils import np_utils
from keras.layers.recurrent import GRU
from keras.optimizers import SGD
from keras.models import Model
from keras.layers.merge import add, concatenate
from keras import backend as K
from keras import models
from PIL import Image
from scipy import ndimage
from sklearn.model_selection import train_test_split

np.random.seed(1337)  # for reproducibility
# FOR LOADING IMAGES AND LABELS
def dir_to_dataset(glob_files, loc_train_labels=""):
    print('\n')
    print("Gonna process:\t %s"%glob_files)
    dataset = []
    for file_count, file_name in enumerate(sorted(glob(glob_files))):
        if file_count % 100 == 0:
            sys.stdout.write(".")
            sys.stdout.flush()
        img = Image.open(file_name).convert('LA') #tograyscale
        pixels = [f[0] for f in list(img.getdata())]
        #print( file_name)
        dataset.append(pixels)

    print("\n TrainLabels ..")
    if len(loc_train_labels) > 0:
        df = pd.read_csv(loc_train_labels)
        print("\t Labels loaded  ..")
        return np.array(dataset), np.array(df["Class"])
    else:
        return np.array(dataset)

def dir_to_dataset_from_file(glob_files):
    print('\n')
    print("Gonna process:\t %s"%glob_files)
    dataset = []
    klasses = []
    pattern = r'\d+'
    for file_count, file_name in enumerate(sorted(glob(glob_files))):
        if file_count % 100 == 0:
            sys.stdout.write(".")
            sys.stdout.flush()
        match = re.search(pattern, file_name)
        img = Image.open(file_name).convert('LA') #tograyscale
        pixels = [f[0] for f in list(img.getdata())]
        #print( file_name)
        klasses.append(int(match.group(0)))
        dataset.append(pixels)

    print("\n TrainLabels ..")
    if len(klasses) > 0:
        print("\t Labels loaded  ..")
        return np.array(dataset), np.array(klasses)
    else:
        return np.array(dataset)


def ctc_lambda_func(args):
    y_pred, labels, input_length, label_length = args
    # the 2 is critical here since the first couple outputs of the RNN
    # tend to be garbage:
    y_pred = y_pred[:, 2:, :]
    return K.ctc_batch_cost(labels, y_pred, input_length, label_length)

# Training iterations
nb_epoch = 40
batch_size = 64 
# shape (image dimensions)
img_rows, img_cols = 28, 28

#
# Network parameters
#
# number of convolutional filters to use
nb_filters = 16
# convolution kernel size
kernel_size = (3, 3)
# size of pooling area for max pooling
p_size = 2
pool_size = (p_size, p_size)
time_dense_size = 32
rnn_size = 512
minibatch_size = 32


os.system('cls' if os.name == 'nt' else 'clear')
print('\n')
print('Loading images - Please wait ', end='')
#my images have the extension PNG not png !
# Data, y = dir_to_dataset('training_data/*.png','training_data/ocr.csv')
Data, y = dir_to_dataset_from_file('data/*.png')

nb_classes = y.max() - y.min() + 1


#random split and random shuffle the dataset 75% for train and 25% for test (= 0.25)
X_train, X_test, Y_train, Y_test = train_test_split(Data, y, test_size=0.30, random_state=42)

print('\n')
print('\n Dataset loaded')

if K.image_dim_ordering() == 'th':
    X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols)
    X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
    X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

print('\n')
print('\n')
print("%d Classes" % nb_classes)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')
print('\n')
print('\n')
print('\nBuilding the model')
# convert class vectors to binary class matrices
Y_train = np_utils.to_categorical(Y_train, nb_classes)
Y_test = np_utils.to_categorical(Y_test, nb_classes)

model = Sequential()
act = 'relu'
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(Conv2D(nb_filters, kernel_size, padding='same', activation=act, input_shape=input_shape))
model.add(Conv2D(nb_filters, kernel_size, padding='same',  activation=act))
model.add(MaxPooling2D(pool_size=pool_size))
model.add(Conv2D(nb_filters, kernel_size, padding='same',  activation=act))
model.add(MaxPooling2D(pool_size=pool_size))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128, activation=act))
model.add(Dropout(0.5))
model.add(Dense(nb_classes, activation='softmax'))
model.summary()

# sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
#compile the mlmodel
print('\n')
print('\nCompiling the model')
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer='adam',
              metrics=['accuracy'])


#start training
print('\n')
print('\nTrain the model')
print('\n')
print('\n')
model.fit(X_train, Y_train, batch_size=batch_size, epochs=nb_epoch,
          verbose=1, validation_data=(X_test, Y_test))


score = model.evaluate(X_test, Y_test, verbose=1)


models.save_model(model,'OCR_cnn.h5')
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)


print('\n')
print('Model trained and saved ..')
print('Convert the model to CoreML-Model ..')


#THIS SHOULD MATCH YOUR CLASSES !!!
#IT MEANS: Class 0 (in *.csv) is mapped as '0' and so on
numbers=[ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
uppercase=[ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
lowercase=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
# characters=[ "'", "," ]
test_characters = numbers + uppercase + lowercase
# output_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
output_labels = test_characters
scale = 1/255.
coreml_model = coremltools.converters.keras.convert('./OCR_cnn.h5',
                                                    input_names='image',
                                                    image_input_names='image',
                                                    output_names='output',
                                                    class_labels=output_labels,
                                                    image_scale=scale)

coreml_model.author = 'Nathaniel Bomberger'
coreml_model.license = 'MIT'
coreml_model.short_description = 'Model to classify characters for Magic the Gathering fonts'

coreml_model.input_description['image'] = 'Grayscale image'
coreml_model.output_description['output'] = 'Predicted character'

# SAVE THE COREML.model for using in Xcode
coreml_model.save('OCR.mlmodel')

print('\n')
print('\n')
print('CoreML-Model saved ! Accuracy = ', score[1])
print('Trained with Keras Version', keras.__version__)
print('\n')