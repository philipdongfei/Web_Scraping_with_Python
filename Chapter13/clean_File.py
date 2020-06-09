from PIL import Image
import pytesseract

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    #Set a threshold value for the image, and save
    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(newFilePath)
    return image

if __name__ == '__main__':
    image = cleanFile('files/textBad.png', 'textCleaned.png')

    #call tesseract to do OCR on the newly created image
    print(pytesseract.image_to_string(image))

