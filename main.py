from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

model = load_model("keras_model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

image = Image.open("test.jpg").convert("RGB")
image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)

image_array = np.asarray(image)
normalized = (image_array.astype(np.float32) / 127.5) - 1
data = np.expand_dims(normalized, axis=0)

prediction = model.predict(data)
index = np.argmax(prediction)

print("Class:", class_names[index].strip())
print("Confidence:", prediction[0][index])
