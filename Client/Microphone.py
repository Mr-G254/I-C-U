import sounddevice

class Microphone():
    def __init__(self):
        self.on = False
        self.sound = sounddevice.InputStream(latency='low')

    def get_audio(self):
        self.sound.start()
        self.on = True

    def stop_audio(self):
        self.sound.stop()

    def send_stream(self,indata,frames,time,status):
        return indata