import tensorflow as tf
from keras.saving import register_keras_serializable
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from PIL import Image
import io
import base64

app = FastAPI()

# Allow frontend requests (CORS settings)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend domain for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register 'mae' (Mean Absolute Error) as a custom function
@register_keras_serializable()
def mae(y_true, y_pred):
    return tf.reduce_mean(tf.abs(y_true - y_pred))

# Load the pre-trained model with custom objects
custom_objects = {"mae": mae}
model = tf.keras.models.load_model("test_gan_1.h5", custom_objects=custom_objects)

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read and process the uploaded image
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")  # Convert to RGB
    image = image.resize((256, 256))  # Resize to model input size
    image_array = np.array(image) / 255.0  # Normalize
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Generate the colorized image
    prediction = model.predict(image_array)[0]  # Remove batch dimension
    prediction = (prediction * 255).astype(np.uint8)  # Convert back to image format

    # Convert NumPy array to image
    colorized_image = Image.fromarray(prediction)

    # Save image to buffer and encode in Base64
    img_io = io.BytesIO()
    colorized_image.save(img_io, format="PNG")
    img_io.seek(0)
    base64_image = base64.b64encode(img_io.getvalue()).decode("utf-8")

    return {"message": "Prediction completed", "image": base64_image}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
