import cv2

image = cv2.imread("solar-system.jpg")
cv2.putText(image, "Sun", (35, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 255, 0))
cv2.putText(image, "Mercury", (100, 190), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 255, 0))
cv2.putText(image, "Venus", (200, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 255, 0))
cv2.putText(image, "Earth", (280, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 255, 0))
cv2.putText(image, "Mars", (380, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 255, 0))
cv2.putText(image, "Jupiter", (590, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 255, 0))
cv2.putText(image, "Saturn", (780, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 255, 0))
cv2.putText(image, "Uranus", (950, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 255, 0))
cv2.putText(image, "Neptune", (1100, 300), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 255, 0))

cv2.imshow("Planets", image)
cv2.waitKey(0)
