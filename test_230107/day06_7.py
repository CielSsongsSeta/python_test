import cv2

#image = cv2.imread('img1.png')
#cv2.imshow('title',image)
#cv2.waitKey(0)


def cv_img(path):
    img = cv2.imread(path)
    cv2.imshow('title',img)
    cv2.waitKey(0)

cv_img('smiley-ge2d8ce210_640.jpg')