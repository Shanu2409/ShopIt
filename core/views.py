from django.shortcuts import render

from item.models import Catagory, Item

from PIL import Image

import os
# Create your views here.

def index(req):
    items = Item.objects.filter(is_sold = False)[0:6]
    catagories = Catagory.objects.all()

    # This code will resize all the images and overwrite the old images
    for item in items:
        
        path = os.getcwd() + item.image.url
        with Image.open(path) as img:
            # Resize the image to the desired dimensions
            resized_img = img.resize((5536, 4160))

            # Overwrite the original image with the resized image
            resized_img.save(path)

    return render(req, 'core/index.html', {
        "catagories": catagories,
        "items": items,
    })

    

def contact(req):
    return render(req, 'core/contact.html')