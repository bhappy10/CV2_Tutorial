import cv2
import numpy as np

img = cv2.imread('imgData/messi5.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (150, 150), (255, 0, 0), 15)              # point1, point2, line_color, line_width
cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 15)       # point1, point2, line_color, line_width
cv2.circle(img, (100, 63), 55, (0, 0, 255), -1)                 # if fill there, input: -1 at thickness=

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1, 1, 2))
# print pts
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tuts', (0, 130), font, 1, (255, 255, 255), 3, cv2.LINE_AA)


# print img.shape           # get image size(height, width, channel)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
