import cv2 as cv
import matplotlib.pyplot as plt


def rescaleFrame(frame, scale = 1.5):
  # [1] means the width of the image
  width = int(frame.shape[1]*scale)
  # [0] means the height of the image
  height = int(frame.shape[0]*scale)

  dimensions = (width, height)
  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('./photos/forest.jpg')
cv.imshow('my photo bitch', img)
image_resized = rescaleFrame(img)
cv.imshow('my photo resized motherfucka', image_resized)

# Calculing the histogram

plt.figure()
plt.title('Histograma')
plt.xlabel('Rango de pixeles (r)')
plt.ylabel('N° de pixeles')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
  histogram = cv.calcHist([img],[i], None, [256],[0,256])
  plt.plot(histogram, color = col)
  plt.xlim([0,256])

plt.show()
cv.waitKey(0)

