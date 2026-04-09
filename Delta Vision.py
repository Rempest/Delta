import cv2
import numpy as np
class Delta_vision:
  #analyze a photo
   def DeltaACT(self):
     self.object = cv2.imread('image.jpg')
     if (self.object is None):
       print("Image not found!")
       return False
      #edit a photo
     self.object_resize = cv2.resize(self.object, (500, 500))
     self.object_gray =  cv2.cvtColor(self.object_resize, cv2.COLOR_BGR2GRAY)
     self.object_blur =cv2.GaussianBlur(self.object_gray, (5, 5), 0)
     self.object_canny = cv2.Canny(self.object_blur, 100, 300)
     return True
     ##imshow a photo
   def DeltaShow(self):
    cv2.imshow('Original object: ', self.object_resize)
    cv2.imshow('Gray style object: ', self.object_gray)
    cv2.imshow('Canny: ', self.object_canny) 
    cv2.imshow('Blur: ', self.object_blur)
    print("Enter the any symbol on the keyboard to close window..")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

