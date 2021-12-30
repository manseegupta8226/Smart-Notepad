from NotepadFileModel import *
import speech_recognition as s


class File_Controller:

    def __init__(self):
       self.file_model=File_Model()

    def save_file(self,msg):
        self.file_model.save_file(msg)

    def save_as(self,msg):
        self.file_model.save_as(msg)

    def read_file(self,url):
       #result=self.file_model.read_file(url)
      # return result[0],result[1]
        self.msg,self.base= self.file_model.read_file(url)
        return self.msg,self.base

    def new_file(self):
        self.file_model.new_file()

    def take_query(self):
        sr = s.Recognizer()
        print("listening....")
        with s.Microphone() as m:
            print('24')
            s.pause_threshold=1
            sr.adjust_for_ambient_noise(m)
            audio = sr.listen(m)
            print("26")
            text = sr.recognize_google(audio, language="en-in")
            print("28")
            return text


