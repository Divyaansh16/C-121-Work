import cv2
import mediapipe as mp
video=cv2.VideoCapture(0)
width=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width,height)
hands=mp.solutions.hands
drawing=mp.solutions.drawing_utils
hand_obj=hands.Hands(min_detection_confidence=0.75,
                     min_tracking_confidence=0.75)
def countFingures(lst):
    count=0
    thresh=(lst.landmark[0].y*100-lst.landmark[9].y*100)/2
    #print("What is the thresh value:",thresh)
    if(lst.landmark[5].y*100-lst.landmark[8].y*100)>thresh:
        count+=1
    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        count += 1
    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        count += 1
    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        count += 1
    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) >6:
        count += 1
    return  count
while True:
    dummy,image=video.read()
    flipimage=cv2.flip(image,1)
    result=hand_obj.process(cv2.cvtColor(flipimage,cv2.COLOR_BGR2RGB))
    if result.multi_hand_landmarks:
        hand_keyPoints=result.multi_hand_landmarks[0]
        #print(hand_keyPoints)
        count=countFingures(hand_keyPoints)
        print("What is fingure count:",count)
        cv2.putText(flipimage, "Fingures " + str(count), (200, 100), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
        drawing.draw_landmarks(flipimage,hand_keyPoints,hands.HAND_CONNECTIONS)
    cv2.imshow("Hand Gestures:",flipimage)
    key=cv2.waitKey(1)
    if key==32:
        break
video.release()
cv2.destroyAllWindows()