# Hand_gesture_Recognition
Hand Gesture Recognition using MediaPipe Library

MediaPipe Hands utilizes an ML pipeline consisting of multiple models working together: 
A palm detection model that operates on the full image and returns an oriented hand bounding box. 
A hand landmark model that operates on the cropped image region defined by the palm detector and returns high-fidelity 3D hand keypoints.

WE NEED A MODEL TO DETECT THE HAND AND THE GESTURES FOR THAT THERE ARE MODEL BUNDLES AVAILABLE THAT CAN BE USED:

The Gesture Recognizer contains two pre-packaged model bundles: a hand landmark model bundle and a gesture classification model bundle. 
1.	The landmark model detects the presence of hands and hand geometry, and 
2.	The gesture recognition model recognizes gestures based on hand geometry.

Building a basic hand gesture recognizer, which is recognizing 4-5 hand gestures on the basis of change of landmarks for better classification by considering the wrist point as the origin and measuring distances to the finger points from there, which will identify if the finger is closed or open.
There are five conditions passed each for one finger and a thumb. The conditions will check if the finger is open or closed which will define a hand gesture , if a particular condition is satisfied,the model will identify it .

<img width="692" alt="Screen Shot 2023-10-30 at 3 23 09 PM" src="https://github.com/aditii02/Hand_gesture_Recognition/assets/38829128/e21499c7-ab80-4af3-bb3c-969c419260db">

<img width="692" alt="Screen Shot 2023-10-30 at 3 23 30 PM" src="https://github.com/aditii02/Hand_gesture_Recognition/assets/38829128/6bce3220-5038-49cd-9b9d-94dc2fe0e508">


PALM DETECTION IS TIME CONSUMING THEREFORE IT USES A BOUNDING BOX DEFINED BY THE DETECTED HAND LANDMARKS IN THE CURRENT FRAME TO LOCALIZE THE REGIONS OF THE HAND IN THE NEXT FRAME.

Do these steps to recognize the steps:
Step 1:Perform Hands Landmarks Detection
Step 2:Build the Fingers Counter
Step 3:Visualize the Counted Fingers
Step 4:Build the Hand Gesture Recognizer


Recognizing two hand gestures : victory and rock on:

<img width="568" alt="Screen Shot 2023-10-30 at 3 24 40 PM" src="https://github.com/aditii02/Hand_gesture_Recognition/assets/38829128/1d771eb1-087e-4a8f-90e8-3bd6a2417bc2">
<img width="568" alt="Screen Shot 2023-10-30 at 3 24 57 PM" src="https://github.com/aditii02/Hand_gesture_Recognition/assets/38829128/e091cb9f-e8e5-48cd-b477-40615eef7d73">

Returning the list of “recognized_gesture_list [3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, ]”


