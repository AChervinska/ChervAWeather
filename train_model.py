import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist

# Завантаження датасету
(train_images, train_labels), (test_images,
                               test_labels) = fashion_mnist.load_data()

# Нормалізація зображень (масштабування пікселів у діапазон [0, 1])
train_images = train_images / 255.0
test_images = test_images / 255.0

# Переконаємось, що дані є
print("Train images shape:", train_images.shape)
print("Test images shape:", test_images.shape)

# Далі йде створення моделі
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Навчання моделі
model.fit(train_images, train_labels, epochs=10,
          validation_data=(test_images, test_labels))

# Збереження моделі
model.save("model.h5")
print("Модель збережено як model.h5")
