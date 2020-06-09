from PIL import Image
import pytesseract
from pytesseract import Output

image = Image.open('files/textOriginal.png')
#image = Image.open('captchaExample.png')
data = pytesseract.image_to_data(image,output_type=Output.DICT)
print(data)
#print(data['conf'])

print()
print(pytesseract.image_to_string(image, output_type=Output.BYTES))
print()
print(pytesseract.image_to_boxes(image))
print()
print(pytesseract.image_to_osd(image))


