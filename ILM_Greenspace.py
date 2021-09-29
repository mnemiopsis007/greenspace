import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

os.chdir('/Users/mnemiopsis/Desktop/ILMGreenSpace/AzyImages')

filename = 'j14.png'

img = cv2.imread(filename, cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# for gray pixels
lower_concrete = np.array([0,0,50], np.uint8)
upper_concrete = np.array([179,35,255], np.uint8)

lower_total = np.array([0,0,0],np.uint8)
upper_total = np.array([179,255,255],np.uint8)

mask = cv2.inRange(hsv, lower_concrete, upper_concrete)
maskall = cv2.inRange(hsv, lower_total, upper_total)

# Smoothing data
res = cv2.bitwise_and(img, img, mask=mask)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(mask, kernel, iterations = 1)

# Determination of gray space
countTruea = cv2.countNonZero(mask)
countTrueErosion = cv2.countNonZero(erosion)
countTotal = cv2.countNonZero(maskall)

upper_est = (countTruea/countTotal)*100
lower_est = (countTrueErosion/countTotal)*100

print(upper_est)
print(lower_est)

cv2.imwrite('Mask_' + filename, mask)
cv2.imwrite('Smoothed_' + filename, erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()







# grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# for green pixels
# lower_concrete = np.array([20,30,10], np.uint8)
# upper_concrete = np.array([90,255,255], np.uint8)

# dilation = cv2.dilate(mask, kernel, iterations = 1)

# smoothing
# kernel = np.ones((15,15), np.float32)/255
# smoothed = cv2.filter2D(res, -1, kernel)
# blur = cv2.GaussianBlur(res, (15,15), 0)
# median = cv2.medianBlur(res, 15)

# cv2.imshow('HW HSV', hsv)
# cv2.imshow('dilate', dilation)

# print(img.size)

# print(countTruea, countTrueb, maskall)

# cv2.imwrite('HWb.jpg', hsv)
# cv2.imwrite('HWd.jpg', res)

#res2 = cv2.imread('HWd.jpg')
#res2 = cv2.cvtColor(res2, cv2.COLOR_BGR2RGB)
#plt.imshow(res2)
#plt.show()

# cv2.imshow('HW Original', img)
# cv2.imshow('HW Mask', mask)
# cv2.imshow('erosion', erosion)
