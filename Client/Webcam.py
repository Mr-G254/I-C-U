import cv2


class WebCam():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.output = cv2.VideoWriter('output.mp4',self.fourcc, 25.0, (640,480))
        self.disabled = False

    def start_recording(self):
        while(self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret==True:
                print(frame)
                print()
                self.output.write(frame)

                # cv2.imshow('frame',frame)
                # if cv2.waitKey(1) & 0xFF == ord('q'):
                if self.disabled:
                    break
            else:
                break

        # Release everything if job is finished
        self.cap.release()
        self.output.release()
        # cv2.destroyAllWindows()
    
    def stop_recording(self):
        self.disabled = True

