from PIL import Image
import pytesseract

image = Image.open('files/text_2.png')
print(pytesseract.image_to_string(image))

