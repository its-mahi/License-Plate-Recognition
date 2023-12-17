import matplotlib.pyplot as plt
import cv2
import easyocr
from IPython.display import Image

Image("/plates/scaned_img_0.jpg")

reader = easyocr.Reader(['en'])

output = reader.readtext('plates/scaned_img_0.jpg')

# output
print(output)

# cord = output[-1][0]