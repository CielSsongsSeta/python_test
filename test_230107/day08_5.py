import cv2
import mediapipe as mp

# 비디오 읽기
cap = cv2.VideoCapture('person.mp4') # 0으로 입력하면 웹캠ㅇ
# 구글이 제공하는 mp_fd
mp_fd = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
# 50% 얼굴이면 얼굴로 인식
fd = mp_fd.FaceDetection(0.5) # 정확도 조정

# 읽은 비디오를 여러개의 이미지로
success, img = cap.read()
# 색보정(정확도)
from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 얼굴 찾아달라
result = fd.process(from_bgr_to_rgb)

def ShowImage(img_path):
    img = cv2.imread('person.jpg')
    cv2.imshow('title', img)
    cv2.waitKey(0)

#ShowImage('person.jpg')

def ShowVideo(video_path):
    vc = cv2.VideoCapture(video_path)
    while True:
        success, img = vc.read()

        if success:
            cv2.imshow('title', img)
        cv2.waitKey(20)

#ShowVideo('person.mp4')

# webcam
def ShowCam():
    vc = cv2.VideoCapture(0)
    # 화면 조정
    vc.set(3, 640)
    vc.set(4, 480)
    while True:
            # 변수 연달아 생성
        success, img = cap.read()

        # 동영상을 성공적으로 읽은 경우
        # 보여주기 전에 face, 얼굴을 찾는다
        if success:
            from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #opencv는 블루그린레드가 기본이어서 바꿔준다. 
            face = fd.process(from_bgr_to_rgb)

            if face.detections:
                # 얼굴을 찾은 경우 하고 싶은 동작
                for id, detection in enumerate(face.detections):
                    #mp_draw.draw_detection(img,detection)   # 찾은 얼굴을 사각 표시
                    fd_box= detection.location_data.relative_bounding_box
                    box= int(fd_box.xmin*img.shape[1]), int(fd_box.ymin*img.shape[0]),\
                        int(fd_box.width*img.shape[1]), int(fd_box.height*img.shape[0])
                cv2.rectangle(img, box, (255,0,255),2)
                cv2.putText(img,f'{round(detection.score[0]*100,1)}%',(box[0], box[1]),cv2.FONT_ITALIC,1,(255,0,255),2)
                #cv2.putText(img,f'hello',(0,50),cv2.FONT_ITALIC,1,(255,0,255),2)

            cv2.imshow('title', img)
            # 무한대기
        if cv2.waitKey(1) & 0xFF == 27 : # 27 == esc
            # ESC키를 눌러 종료
            break

ShowCam()    