import glob
import os
from PIL import Image

for img_path in sorted(glob.glob('static/tga/*.tga')):
    print(img_path)
    img = Image.open(img_path)  # PIL image
    file_name = os.path.basename(img_path)
    file_name, file_ext = os.path.splitext(file_name)
    img_path = "static/img/" + file_name + ".jpg"
    print(img_path)
    img = img.convert("RGB")
    img.save(img_path)