import cv2
class DeltaPrime:
def DeltaACT(self):
self.object = cv2.imread('image.jpg')
self.odject_resiz = cv2.resize(img, (500x, 500))
self.object_gray =  cv2.cvtColor(object_resize, cv2.COLOR_BGR2GRAY)
self.odject_blur =cv2.GaussianBlur(object_gray, (5, 5), 0)
self.object_canny = cv2.Canny(object_blur, 100, 300)
def DeltaShow(self):
  cv2.imshow('Original onject: ', object_resize)
  cv2.imshow('Gray style object: ', object_gray)
  cv2.imshow('Canny & Blur: ', object_canny \n object_blur)
  print("Enter the any symbol on the keyboard to close window..")
  cv2.waitKey(0)
  cv2.destroyALLWindows
Delta_object = DeltaPrime()
return DeltaACT('object')
return DeltaShow()
