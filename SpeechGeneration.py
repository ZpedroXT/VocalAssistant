import pyttsx3
import speech_recognition as sr
from playsound import playsound
import time
import os
class SpeechGeneration:

    def __init__(self):
        self.engine = pyttsx3.init()  
        self.r1 = sr.Recognizer()
        self.r2 = sr.Recognizer()
        self.r3 = sr.Recognizer()
        # self.Listen(self)
        
        playsound('SFX/Open.wav')
       
        self.engine.say("Initialisation terminé.")
        self.engine.runAndWait()
        playsound('SFX/ItsOK.wav')

    def Listen(self):
        
        with sr.Microphone() as source:
       
            print("Lancement")
            
            audio = self.r3.listen(source)
           
        
        try:
            MyPhrase = self.r2.recognize_google(audio, language="fr-FR")
            print(MyPhrase)   
        
            if 'Eva' in MyPhrase:
                self.r2 = sr.Recognizer()
                with sr.Microphone() as source:

                    self.engine.say("Oui monsieur ?")
                    self.engine.runAndWait()
                    audio = self.r2.listen(source)

                try:
                    get = self.r2.recognize_google(audio, language="fr-FR")
                    print(get)
                    self.engine.say("Que puis-je faire pour vous ?")
                    self.engine.runAndWait()
                    # wb.get().open_new(url+get)
                except sr.UnknownValueError:
                     self.Listen()
                except sr.RequestError as e:
                    self.Listen()
                    print("failed".format(e))
            else:
                self.Listen()
        except sr.UnknownValueError:
           self.Listen()
        except sr.RequestError as e:
            self.Listen()
            print("failed".format(e))
 
