import cv2

#my image
img_file = 'cars.jpg'
#video = cv2.VideoCapture("C://Users//rozer//Videos//tesla.mp4")
video = cv2.VideoCapture("C://Users//rozer//Videos//bike_tour.mp4")

#pre-trained car and pedestrians classifier
car_tracker_file = 'car_dedector.xml'
pedestrian_tracker_file = 'haarcascade_fullbody.xml'
img = cv2.imread(r"C://Users//rozer//OneDrive//Resimler//cars.jpg")


#create car and pedestrianclassifier
car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)


while True:
    #read the current frame
    (read_successful, frame) = video.read()

    if read_successful:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    
    
    
    #detect cars and pedestrian
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    #draw rectangles around the cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    #draw rectangles around the pedestrians
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)



    #display the img
    cv2.imshow('Clever Programmer Car Detector', frame)

    #wait and listen for a key press
    key = cv2.waitKey(1)

    #stop if Q key is pressed Ascii
    if key == 81 or key == 113:
        break
video.release()
"""

# create opencv img
img = cv2.imread(r"C://Users//rozer//OneDrive//Resimler//cars.jpg")

#convert to grayscale
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#create car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

#detect cars
cars = car_tracker.detectMultiScale(black_n_white)

#draw rectangles around the cars
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#print(cars)
#display the img
cv2.imshow('Clever Programmer Car Detector', img)

#wait and listen for a key press
cv2.waitKey()
"""
print("Code Completed")