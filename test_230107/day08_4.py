import cv2
import mediapipe as mp

'''
만약에 웹캠이면 VideoCapture에 0을 넣고, 맨 밑 WaitKey에 1을 넣는다
'''

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

# 얼굴 찾으면
if result.detections:
    #각 얼굴별로
    for id, detection in enumerate(result.detections):
        mp_draw.draw_detection(img, detection)

# 보여주기
cv2.imshow('title',img)
# 대기
cv2.waitKey(0)