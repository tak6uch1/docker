import keras
from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from IPython import get_ipython
import matplotlib.pyplot as plt
import numpy as np
import copy

#%matplotlib inline
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')

np.random.seed(0)

batch_size = 128
num_classes = 10
epochs = 20

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_test_org = copy.deepcopy(x_test)

# show a part of training images
label_name = ('T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ancle boot')

n_rows = 5
n_cols = 5
fig, axs = plt.subplots(n_rows, n_cols, figsize=(28,28))
plt.subplots_adjust(wspace=0.0, hspace=0.6)
i = 0
for ax, pixels, label in zip(axs.flat, x_train, y_train):
    ax.imshow(pixels, cmap="gray")
    ax.set_title('{}: {}'.format(i, label_name[label]), fontsize=20)
    ax.set_xticks([])
    ax.set_yticks([])
    i+=1
plt.show()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# pick wrong choices
prex = model.predict(x_test)
wrong = []
title = []
i = 0
while True:
    yi = y_test[i:i+1]
    prei = prex[i:i+1]
    if prei.argmax() != yi.argmax():
        wrong.append(i)
        title.append('{}: {} -> {}'.format(i, label_name[yi.argmax()], label_name[prei.argmax()]))
    if len(wrong) == n_rows * n_cols or i == len(y_test):
        break
    i+=1

print('wrong choice: {}'.format(title))

fig, axs = plt.subplots(n_rows, n_cols, figsize=(28,28))
plt.subplots_adjust(wspace=0.0, hspace=0.6)
for ax, num, label in zip(axs.flat, wrong, title):
    ax.imshow(x_test_org[num], cmap="gray")
    ax.set_title(label, fontsize=20)
    ax.set_xticks([])
    ax.set_yticks([])
plt.show()
