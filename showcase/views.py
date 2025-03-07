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
        image_file = form.cleaned_data['image']
        # Use a context manager to open and process the image,
        # ensuring the image file is closed after processing.
        with Image.open(image_file) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img = img.resize((224, 224))
            x = np.array(img)
        
        # Add batch dimension and preprocess the image
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        
        # Predict and decode results
        preds = model.predict(x)
        decoded = decode_predictions(preds, top=1)[0][0]
        prediction = f"{' '.join(decoded[1].split('_')).title()} with a confidence of {decoded[2]*100:.2f}%"
    
    context = {
        'form': form,
        'prediction': prediction,
    }
    return render(request, 'demo.html', context)
