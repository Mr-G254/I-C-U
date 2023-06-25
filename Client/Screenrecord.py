from PIL import ImageGrab
import pyautogui
import cv2
import numpy as np

class Screenrecord():
    def __init__(self):
        self.on = False

    def start(self):
        self.on  = True
        while True:
            self.image = pyautogui.screenshot()
            self.frame = np.array(self.image)
            self.frame = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)
            self.send_stream(self.frame)
            cv2.imshow("Live",self.frame)

            if cv2.waitKey(1) == ord('q'):
                self.stop()
            
            if not self.on:
                break

    def stop(self):
        self.on = False

    def send_stream(self,frame):
        return frame

record = Screenrecord()
record.start()