import pytesseract
from pytesseract import Output
from PIL import Image
import numpy as np

def cleanFile(filePath, threshold):
    image = Image.open(filePath)
    #Set a threshold value for the image, save
    image = image.point(lambda x: 0 if x<threshold else 255)
    return image

def getConfidence(image):
    data = pytesseract.image_to_data(image, output_type=Output.DICT)
    text = data['text']
    confidences = []
    numChars = []

    for i in range(len(text)):
        #print(data['conf'][i])
        #print(type(data['conf'][i]))
        if int(data['conf'][i]) > -1:
            confidences.append(data['conf'][i])
            numChars.append(len(text[i]))
    print(confidences)
    print()
    print(numChars)
    print()
    return np.average(confidences, weights=numChars), sum(numChars)

if __name__ == '__main__':
    filePath = 'files/textBad.png'

    start = 130 #80
    step = 5
    end = 180 #200

    for threshold in range(start, end, step):
        image = cleanFile(filePath, threshold)
        scores = getConfidence(image)
        print('threshold: {}, confidences: {}, numChars {}'.format(str(threshold), str(scores[0]), str(scores[1])))

