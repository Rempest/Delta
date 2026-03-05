import cv2
import numpy as np
class DeltaPrime:
  #analyze a photo
   def DeltaACT(self):
     self.object = cv2.imread('image.jpg')
     if (self.object = None):
       print("Image not found!")
       return
      #edit a photo
     self.odject_resiz = cv2.resize(object, (500, 500))
     self.object_gray =  cv2.cvtColor(object_resize, cv2.COLOR_BGR2GRAY)
     self.odject_blur =cv2.GaussianBlur(object_gray, (5, 5), 0)
     self.object_canny = cv2.Canny(object_blur, 100, 300)
     ##imshow a photo
   def DeltaShow(self):
    cv2.imshow('Original onject: ', self.object_resize)
    cv2.imshow('Gray style object: ', self.object_gray)
    cv2.imshow('Canny & Blur: ', self.object_canny \n self.object_blur)
    print("Enter the any symbol on the keyboard to close window..")
    cv2.waitKey(0)
    cv2.destroyALLWindows()
     #main
Delta_object = DeltaPrime()
Delta_object.DeltaACT()
DeltaACT.DeltaShow()
