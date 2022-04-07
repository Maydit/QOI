import cv2
import numpy as np
import sys

def main(imagepath):
  img = cv2.imread(imagepath, -1) #alpha

  previous = {r: 0, g: 0, b: 0, a: 255}

  hash_table = np.zeros(64)

  for i in numpy.ndindex(image.shape[:2]):
    r, g, b, a = *image[i]
    index_position = (r * 3 + g * 5 + b * 7 + a * 11) % 64
    print(index_position)

if __name__ == __main__():
  main(sys.argv[1])