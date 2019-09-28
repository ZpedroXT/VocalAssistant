# -*-coding:Latin-1 -*

import pyttsx3
import speech_recognition as sr
import webbrowser as wb
from SpeechGeneration import SpeechGeneration
# engine = pyttsx3.init()
# engine.say("Bonjour monsieur. Cela fait un moment! il semblerait que les correcteurs holographique ne fonctionne pas.")
# engine.say("Que puis-je faire pour vous ?")
# engine.runAndWait()

# engine = pyttsx3.init()
# r1 = sr.Recognizer()
# r2 = sr.Recognizer()
# r3 = sr.Recognizer()

# with sr.Microphone() as source: 
#     print("search edureka")
#     audio = r3.listen(source)
#     print(r2.recognize_google(audio, language="fr-FR"))
# if 'Julius' in r2.recognize_google(audio):
#     r2 = sr.Recognizer()
#     url = ""
#     with sr.Microphone() as source: 
#         print("search query")
#         engine.say("Que puis-je faire pour vous ?")
#         engine.runAndWait()
#         audio = r2.listen(source)

#         try:
#             get = r2.recognize_google(audio)
#             print(get)
#             engine.say("Que puis-je faire pour vous ?"+get)
#             # wb.get().open_new(url+get)
#         except sr.UnknownValueError:
#             print("Error")
#         except sr.RequestError as e:
#             print("failed".format(e))

generation = SpeechGeneration()
generation.Listen()