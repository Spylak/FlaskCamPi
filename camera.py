import cv2
from datetime import datetime

class VideoCamera(object):
    def __init__(self, flip = False, file_type  = ".jpg", photo_string= "stream_photo"):
        self.vs = cv2.VideoCapture(-1)
        self.vs.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
        self.vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
        
        self.flip = flip # Flip frame vertically
        self.file_type = file_type # image type i.e. .jpg
        self.photo_string = photo_string # Name to save the photo

    def __del__(self):
        self.vs.release()

    def get_frame(self):
        ret, image = self.vs.read()
        if not ret:
            return
        
        ret, jpeg = cv2.imencode(self.file_type,image, [cv2.IMWRITE_JPEG_QUALITY,30])
        return jpeg.tobytes()
