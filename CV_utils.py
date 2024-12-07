import os
import numpy as np
from PIL import Image

def image_preprocessing(data, class_names, path):

    images = []
    labels = []

    for class_name in class_names:
        class_folder = os.path.join(path, class_name)

        for filename in os.listdir(class_folder):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                img_path = os.path.join(class_folder, filename)

                img = Image.open(img_path)
                img = img.convert('RGB')
                img = img.resize((128, 128))
                img_array = np.array(img)

                images.append(img_array)
                labels.append(class_name)

    images_array = np.array(images)
    labels_array = np.array(labels)
    
    return images_array, labels_array