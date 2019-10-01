# -*-coding:Latin-1 -*

from Controller.SpeechGeneration import SpeechGeneration
import os

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/bousaidi/Bureau/Credential/MyProject-37091e95e1fa.json'


# os.system("export GOOGLE_APPLICATION_CREDENTIALS='/home/bousaidi/Téléchargements/MyProject-37091e95e1fa.json'")
generation = SpeechGeneration()
generation.Listen()