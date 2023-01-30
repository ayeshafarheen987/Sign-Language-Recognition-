import cv2
from sklearn.utils import resample
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
model = load_model('capstone_keras_model.h5')



#labels = ["A", "B", "C"]


cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, image = cap.read()
    image = cv2.flip(image, 1)
    roi = image[0 : 205, 390 : 627]
    cv2.rectangle(image,pt1=(400,0), pt2=(620,200), color=(255,0,0), thickness=2)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    Gaussain_blur = cv2.GaussianBlur(gray, (5, 5), 4)
    #cv2.imshow('Gaussain_blur',Gaussain_blur)
    th3 = cv2.adaptiveThreshold(Gaussain_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    ret, res = cv2.threshold(th3, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #kernel = np.ones((3, 3), np.uint8)
    #closing = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel, iterations=1)
    test_image = res / 255
    test_images = cv2.resize(test_image, (224, 224), 1)
    test_images = np.expand_dims(test_images, 0)
    pred_img = model.predict(np.array(test_images))
    print(pred_img)
    pred_result = np.argmax(pred_img, axis=1)
    #print(pred_result)
    
    if pred_result==0:
        preds="A"
    elif pred_result==1:
        preds="B"
    else:
        preds="C"
    print(preds)
    cv2.putText(image,preds,(75,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("image",image)
    if cv2.waitKey(20) & 0xFF == ("q"):
        break

cv2.destroyAllWindows()
cap.release()