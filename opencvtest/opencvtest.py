from cv2 import CascadeClassifier
from cv2 import imread
from cv2 import rectangle
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
# 이미지 받아옴
pixels = imread('front2.jpg')

# 학습 모델 읽어옴 정면에 있는 얼굴
classifier = CascadeClassifier('haarcascade_frontalface_default.xml')

# defalt 는 1.1 , 3 인데
bboxes = classifier.detectMultiScale(pixels, 1.1, 8)
# 분류기가 감지한 경계상자를 출력
for box in bboxes:
    x, y, width, height = box
    x2, y2 = x + width, y + height
    rectangle(pixels, (x, y), (x2, y2), (0, 0, 255), 1)

# 이미지 출력
imshow('face detection', pixels)

# 키가 눌리면 창닫기
waitKey(0)
destroyAllWindows()
