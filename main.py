import cv2
import mediapipe as mp
import cv2
import mediapipe as mp
import time
import collections
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


class HandDetector:
    def __init__(self, mode=False, maxHands=1, detectionCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        # formality you have to do to start using this module.
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.5, model_complexity=0, min_tracking_confidence =0.5)
        self.mpDraw = mp.solutions.drawing_utils
        print("intialize complete")

    def findHands(self, image):

        RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(RGB_image)  # detect the hands
        if self.results.multi_hand_landmarks: # if landmarks are detected then draw the landmarks
            for handLandmarks in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(image, handLandmarks, self.mp_hands.HAND_CONNECTIONS)
        return image

    def findPosition(self, img):
        landmarkList = []
        # if landmarks are being detected
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[0]
            for id, lm, in enumerate(myHand.landmark):
                h, w, c = img.shape
                # we need Width and height because our current x and y values are in decimal places and we
                # want to convert them into pixels.
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarkList.append([id, cx, cy])
        return landmarkList

    def gestureRecognizer(self, landmarkList, type):
        thumb_State = ""
        index_State = ""
        middle_State = ""
        ring_State = ""
        pinky_State = ""
        handGesture = ""

        if len(landmarkList) != 0:
            if landmarkList[2][1] > landmarkList[3][1] > landmarkList[4][1]:
                thumb_State = "CLOSE"
            elif landmarkList[2][1] < landmarkList[3][1] < landmarkList[4][1]:
                thumb_State = "OPEN"
            if landmarkList[0][2] + landmarkList[5][2] > landmarkList[7][2] + landmarkList[0][2] > landmarkList[8][2] + landmarkList[0][2]:
                index_State = "OPEN"

            elif landmarkList[0][2] + landmarkList[5][2] < landmarkList[7][2] + landmarkList[0][2] < landmarkList[8][
                2] + landmarkList[0][2]:
                index_State = "CLOSE"

            if landmarkList[0][2] + landmarkList[5][2] > landmarkList[7][2] + landmarkList[0][2] > landmarkList[8][2] + landmarkList[0][2]:
                middle_State = "OPEN"

            elif landmarkList[0][2] + landmarkList[9][2] < landmarkList[11][2] + landmarkList[0][2] < landmarkList[12][
                2] + landmarkList[0][2]:
                middle_State = "CLOSE"

            if landmarkList[0][2] + landmarkList[13][2] > landmarkList[15][2] + landmarkList[0][2] > landmarkList[16][2] + landmarkList[0][2]:
                ring_State = "OPEN"

            elif landmarkList[0][2] + landmarkList[13][2] < landmarkList[15][2] + landmarkList[0][2] < landmarkList[16][2] + landmarkList[0][2]:
                ring_State = "CLOSE"

            if landmarkList[0][2] + landmarkList[17][2] > landmarkList[19][2] + landmarkList[0][2] > landmarkList[20][2] + landmarkList[0][2]:
                pinky_State = "OPEN"
               # print("open")
            elif landmarkList[0][2] + landmarkList[17][2] < landmarkList[19][2] + landmarkList[0][2] < landmarkList[20][2] + landmarkList[0][2]:
                pinky_State = "CLOSE"
               # print("close")

        if type == "count":
            fingers = [thumb_State, index_State, middle_State, ring_State, pinky_State]
            openCount = 0
            for finger in fingers:
                if finger == "OPEN":
                    openCount += 1
            if openCount == 1:
                handGesture = "ONE"
            elif openCount == 2:
                handGesture = "TWO"
            elif openCount == 3:
                handGesture = "THREE"
            elif openCount == 4:
                handGesture = "FOUR"
            elif openCount == 5:
                handGesture = "FIVE"
        elif type == "sign":
            if thumb_State == "CLOSE" and index_State == "CLOSE" and middle_State == "OPEN" and ring_State == "OPEN" and pinky_State == "OPEN":
                handGesture = "OKAY"
            elif thumb_State == "CLOSE" and index_State == "OPEN" and middle_State == "CLOSE" and ring_State == "CLOSE" and pinky_State == "OPEN":
                handGesture = "ROCK ON"
            elif thumb_State == "CLOSE" and index_State == "OPEN" and middle_State == "OPEN" and ring_State == "CLOSE" and pinky_State == "CLOSE":
                handGesture = "VICTORY"
            elif thumb_State == "OPEN" and index_State == "OPEN" and middle_State == "OPEN" and ring_State == "OPEN" and pinky_State == "OPEN":
                handGesture = "START"
            else:
                handGesture = "NONE"

        print(handGesture)
        return handGesture

def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    hand_recognizer = {"ROCK ON" : 0, "VICTORY" : 1, "OKAY" : 2 , "START" :4, "NONE" : 3}
    recognized_gesture = ""
    recognized_gesture_list = []
    landmarkList = []
    while True:
        success, frame = cap.read()
        img = detector.findHands(frame)
        print("image detected",img)
        landmarkList = detector.findPosition(img)
        print("landmarklist",landmarkList)
        if len(landmarkList) != 0:
            recognized_gesture = detector.gestureRecognizer(landmarkList, "sign")
            recognized_gesture_list.append(hand_recognizer[recognized_gesture])
            cv2.putText(img, recognized_gesture, (landmarkList[0][1]-50, landmarkList[0][2]-320), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.imshow("Hand Tracking", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    cap.release()
    print("recognized_gesture_list",recognized_gesture_list)

if __name__ == "__main__":
    main()