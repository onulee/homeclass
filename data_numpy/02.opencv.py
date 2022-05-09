import cv2

img_basic = cv2.imread('a1.jpg',cv2.IMREAD_COLOR)
cv2.imshow('Image Basic',img_basic)
cv2.waitKey(0)
cv2.imwrite('result1.png',img_basic)

