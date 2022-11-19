from PIL import Image
import PIL.ImageOps
import io

def invert_colors(img):
    
    inverted_image = PIL.ImageOps.invert(Image.open(io.BytesIO(img)))

    imgBuf = io.BytesIO()
    inverted_image.save(imgBuf, format='JPEG')
    imgBuf.seek(0)
    
    return imgBuf.seek(0)