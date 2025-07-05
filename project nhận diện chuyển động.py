import cv2 
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
for i in range(3):
    xx,flame=cap.read()
    flame=cv2.resize(flame,(640,480))
    gray = cv2.cvtColor(flame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (25, 25), 0)
    last_flame=gray 
while 1:
    xx,flame=cap.read()
    gray=cv2.cvtColor(flame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(25,25),10) 
    abs_img = cv2.absdiff(last_flame, gray)
    last_flame=gray 
    _, img_mask = cv2.threshold(abs_img, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 900:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(flame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow("Window", img_mask)
    cv2.imshow('window',flame)


    if cv2.waitKey(10) & 0xff==27:   
        break 