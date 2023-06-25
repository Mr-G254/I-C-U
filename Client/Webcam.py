import cv2

class WebCam():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.on = False

    def get_feed(self):
        self.on = True
        while(self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret==True:
                self.send_stream(frame)
                cv2.imshow("Live",frame)

                if cv2.waitKey(1) == ord('q'):
                    self.stop_feed()

                if not self.on:
                    break
            else:
                break

        self.cap.release()
    
    def stop_feed(self):
        self.on = False

    def send_stream(self,frame):
        return frame

cam = WebCam()
cam.get_feed()