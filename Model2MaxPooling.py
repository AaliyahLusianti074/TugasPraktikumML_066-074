"""**MODEL 2 MaxPooling**"""

from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, GlobalMaxPooling2D, Flatten, Dense

model2 = Sequential()
model2.add(Conv2D(filters = 32, kernel_size=(3, 3), input_shape = (32, 32, 3), activation = 'relu')),
model2.add(MaxPooling2D(pool_size=(2,2))),

model2.add(Flatten()),
model2.add(Dense(512, activation='relu')), 
model2.add(Dense(29,activation='sigmoid'))

from tensorflow.keras.optimizers import Adam

model2.compile(loss='binary_crossentropy',
              optimizer=Adam(lr=0.0001),
              metrics=['acc'])

H2 = model2.fit(x_train, y_train, batch_size=32, epochs=3, validation_data=(x_test, y_test))

plt.figure(figsize=(12, 12))
  plt.subplot(3, 2, 1)
  plt.plot(H2.history['acc'], label = 'train_accuracy')
  plt.plot(H2.history['val_acc'], label = 'val_accuracy')
  plt.xlabel('epoch')
  plt.ylabel('accuracy')
  plt.legend()
  plt.subplot(3, 2, 2)
  plt.plot(H2.history['loss'], label = 'train_loss')
  plt.plot(H2.history['val_loss'], label = 'val_loss')
  plt.xlabel('epoch')
  plt.ylabel('accuracy')
  plt.legend()
  plt.show()

test_loss, test_acc = model2.evaluate(x_test, y_test)

print('Test accuracy:', test_acc)
print('Test loss:', test_loss)

model2.save('sign_lang2.h5')