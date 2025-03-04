from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(
        label='Upload an image for classification',
        help_text='Select an image file and let our model tell you what it sees!'
    )
