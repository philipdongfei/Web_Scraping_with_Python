from PIL import Image
import subprocess

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    #Set a threshold value for the image, and save
    image = image.point(lambda x: 0 if x<135 else 255)
    image.save(newFilePath)

    #call tesseract to do OCR on the newly created image
    subprocess.call(['tesseract', newFilePath, 'output'])

    #Open and read the resulting data file
    outputFile = open('output.txt', 'r')
    print(outputFile.read())
    outputFile.close()

if __name__ == '__main__':
    cleanFile('files/textOriginal.png', 'text_2.png')

