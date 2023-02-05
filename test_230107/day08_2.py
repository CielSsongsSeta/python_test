import cv2

#pip install python-opencv
#pip install opencv-python

def ShowImage(img_path):
    # 이미지 읽어오기
    img = cv2.imread('person.jpg')
    # 이미지 보여주기
    cv2.imshow('title', img)
    # 무한대기
    cv2.waitKey(0)

ShowImage('person.jpg')