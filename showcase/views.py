import io
from django.shortcuts import render
from .forms import ImageUploadForm
from PIL import Image
import numpy as np

from tensorflow.keras.applications.efficientnet import EfficientNetB0, preprocess_input, decode_predictions

# Load the pre-trained EfficientNetB0 model once when the server starts
model = EfficientNetB0(weights='imagenet')

def home(request):
    # Render your one-page home if needed
    return render(request, 'base.html')

def demo(request):
    prediction = None
    form = ImageUploadForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        # Open the uploaded image file
        image_file = form.cleaned_data['image']
        img = Image.open(image_file)

        # Convert image to RGB in case it is in a different format and resize to model expected size
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img = img.resize((224, 224))

        # Convert the image to a numpy array and add batch dimension
        x = np.array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)  # Preprocess the image data

        # Use the model to predict the class of the image
        preds = model.predict(x)
        decoded = decode_predictions(preds, top=1)[0][0]
        prediction = f"{' '.join(decoded[1].split('_')).title()} with a confidence of {decoded[2]*100:.2f}%"

    context = {
        'form': form,
        'prediction': prediction,
    }
    return render(request, 'demo.html', context)
