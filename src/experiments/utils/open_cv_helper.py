import cv2

class OpenCVHelper:
    def __init__(self):
        pass
    
    def read_image(self, image_path):
        return cv2.imread(image_path)
    
    def show_image(self, image):
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
