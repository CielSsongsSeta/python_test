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

#ShowImage('person.jpg')

def ShowVideo(video_path):
    # 동영상 읽어오기
    vc = cv2.VideoCapture(video_path)
    # 무한반복(동영상 == 빠르게 여러 이미지를 출력)
    while True:
        # 변수 연달아 생성
        success, img = vc.read()

        # 동영상을 성공적으로 읽은 경우
        if success:
            cv2.imshow('title', img)
            # 무한대기
        cv2.waitKey(20)

#ShowVideo('person.mp4')

# webcam 실시간 가져오는 함수
def ShowCam():
    # 동영상 읽어오기
    vc = cv2.VideoCapture(0)
    # 화면 조정
    vc.set(3, 640)
    vc.set(4, 480)
    # 무한반복(동영상 == 빠르게 여러 이미지를 출력)
    while True:
        # 변수 연달아 생성
        success, img = vc.read()

        # 동영상을 성공적으로 읽은 경우
        if success:
            cv2.imshow('title', img)
            # 무한대기
        if cv2.waitKey(1) & 0xFF == 27 : # 27 == esc
            # ESC키를 눌러 종료
            break

ShowCam()    