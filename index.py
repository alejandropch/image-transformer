import cv2 as cv

import matplotlib.pyplot as plt

def rescaleFrame(frame, scale = 1.5):
  # [1] means the width of the image
  width = int(frame.shape[1]*scale)
  # [0] means the height of the image
  height = int(frame.shape[0]*scale)

  dimensions = (width, height)
  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def equalize():
  img = cv.imread('./photos/forest.jpg',0)
  # cv.imshow('my photo', img)
  eq = cv.equalizeHist(img)
  cv.imwrite('./photos/forest_equalizated.png',eq)

  img2 = cv.imread('./photos/forest_equalizated.png',0)


  cv.imshow("Foto por ecualizar",img)
  cv.calcHist(img,[0],None,[256],[0,256])
  plt.hist(img.ravel(),256,[0,256])
  plt.title("Histograma por ecualizar")
  plt.show()
  imgshow = cv.imread('./photos/forest_equalizated.png')
  cv.imshow("Foto por ecualizada",imgshow)

  cv.calcHist(img2,[0],None,[256],[0,256])
  plt.hist(img2.ravel(),256,[0,256])
  plt.title("Histograma ecualizado")
  plt.show()
  cv.waitKey(0)

 
 
def expand():
  img = cv.imread('./photos/photo.jpeg')
  cv.imshow('my photo', img)
  image_resized = rescaleFrame(img)
  cv.imshow('my photo resized', image_resized)
  # Calculing the histogram

  plt.figure()
  plt.title('Histograma')
  plt.xlabel('Rango de pixeles (r)')
  plt.ylabel('N° de pixeles')
  colors = ('r', 'g', 'b')
  for i, col in enumerate(colors):
    histogram = cv.calcHist([image_resized],[i], None, [256],[0,256])
    plt.plot(histogram, color = col)
    plt.xlim([0,256])
  plt.show()
  cv.waitKey(0)

print("Ingresa un valor\n1)Para expandir\n2)Para ecualizar")
value = input()

if( value == "1" ): 
  expand()
else:
  equalize()
