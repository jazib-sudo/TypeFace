import cv2

im = cv2.imread('inp.png')
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
contours, hierarchy = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2:]

for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(im,(x,y),(x+w,y+h),(255,255,255),2)
    # cv2.drawContours(im,[cnt], 0, (36,255,12), 4)

cv2.imwrite('contours_cv.png', im)