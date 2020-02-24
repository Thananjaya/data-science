import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

data = keras.datasets.fashion_mnist

(train_data, train_labels), (test_data, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print(train_data.shape)

print(test_data.shape)

# plt.imshow(train_data[1], cmap=plt.cm.binary)
# plt.show()
train_data = train_data/255.0
test_data = test_data/255.0

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_data[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_data, train_labels, epochs=10)

loss, acc = model.evaluate(test_data, test_labels, verbose=2)
print(loss, acc)

# Add the image to a batch where it's the only member.
img = (np.expand_dims(test_data[9],0))
print(img.shape)

predictions = model.predict(img)

print(class_names[np.argmax(predictions)])
plt.imshow(test_data[9], cmap=plt.cm.binary)
plt.show()