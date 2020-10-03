import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:

    # 画像の読み込み
    ret, frame = cap.read()
    #frame = cv2.resize(frame, dsize=(640, 480))
    # BGRからHSVへの変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 赤色の上限値と下限値の設定
    lower_led = np.array([0,50,50])
    upper_led = np.array([10,255,255])

    # マスク処理の設定
    mask = cv2.inRange(hsv, lower_led, upper_led)

    # 実際にマスク処理
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
