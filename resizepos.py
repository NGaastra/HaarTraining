import imutils
import cv2

im = cv2.imread('forklift.jpg')
im = imutils.resize(im, height=min(50, im.shape[1]), width=min(50, im.shape[1]))
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imwrite('forklift5050.jpg', im)