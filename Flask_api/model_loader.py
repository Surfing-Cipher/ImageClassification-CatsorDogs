# your_flask_app/model_loader.py

import tensorflow as tf
import numpy as np
import cv2
import albumentations as A
import os
from PIL import Image

# Define the model path relative to this script
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'your_model_files', 'efficientnetb0_cats_dogs_classifier.keras')

# Define your class names in the correct order
CLASS_NAMES = ['cat', 'dog'] # Make sure this matches the order from your training!

# Configuration for image size (must match your model's input)
IMG_SIZE = 224 

# Define the same normalization transform used during validation/prediction
# in your training notebook.
# This is crucial for consistent predictions.
preprocessing_transform = A.Compose([
    A.Resize(height=IMG_SIZE, width=IMG_SIZE),
    A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
])

# Load the model globally when the app starts
# This avoids loading the model on every request, which would be very slow.
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}")
except Exception as e:
    print(f"Error loading model from {MODEL_PATH}: {e}")
    model = None # Set to None if loading fails

def preprocess_image(image_path_or_bytes):
    """
    Loads and preprocesses an image for model prediction.
    Accepts either a file path (string) or image bytes (BytesIO object).
    """
    if isinstance(image_path_or_bytes, str):
        # If it's a path, use cv2.imread
        img = cv2.imread(image_path_or_bytes)
        if img is None:
            raise ValueError(f"Could not read image from path: {image_path_or_bytes}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert BGR to RGB
    else:
        # If it's bytes (e.g., from Flask request.files['file'].stream)
        img = Image.open(image_path_or_bytes)
        img = np.array(img) # Convert PIL Image to NumPy array
        if img.shape[2] == 4: # Handle RGBA images
            img = img[:, :, :3]
        elif len(img.shape) == 2: # Handle grayscale images
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)


    # Apply Albumentations transform
    augmented = preprocessing_transform(image=img)
    processed_img = augmented["image"]
    
    # Add batch dimension (model expects [batch_size, height, width, channels])
    processed_img = np.expand_dims(processed_img, axis=0)
    
    return processed_img

def predict_image(image_path_or_bytes):
    """
    Predicts the class of an image.
    Returns the predicted class name and confidence score.
    """
    if model is None:
        return "Error", "Model not loaded."

    try:
        processed_img = preprocess_image(image_path_or_bytes)
        predictions = model.predict(processed_img)
        
        # Get the predicted class index and confidence
        predicted_class_index = np.argmax(predictions, axis=1)[0]
        confidence = predictions[0][predicted_class_index] * 100 # Convert to percentage

        predicted_class_name = CLASS_NAMES[predicted_class_index]
        
        return predicted_class_name, f"{confidence:.2f}%"
    except Exception as e:
        return "Error during prediction", str(e)

if __name__ == '__main__':
    # Simple test if run directly
    print(f"Model path exists: {os.path.exists(MODEL_PATH)}")
    # If you have a local test image, you can test like this:
    # test_image_path = "path/to/your/test_image.jpg"
    # if os.path.exists(test_image_path):
    #     class_name, confidence = predict_image(test_image_path)
    #     print(f"Test prediction for {test_image_path}: {class_name} with {confidence} confidence")
    # else:
    #     print(f"Test image not found at {test_image_path}")