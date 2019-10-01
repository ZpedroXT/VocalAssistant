#
# -*-coding:UTF-8 -*
import pyttsx3
import speech_recognition as sr
from google.cloud import texttospeech
from playsound import playsound
import time
import os
import random
class SpeechGeneration:

    def __init__(self):

        #Ici on initialise Les messages audio ainsi que le module de reconnaissance vocal

        self.r1 = sr.Recognizer()
        self.r2 = sr.Recognizer()
        self.r3 = sr.Recognizer()
        self.client = texttospeech.TextToSpeechClient()

        time.sleep(0.5)
        playsound("Eva/Bonjour.wav")



    def Listen(self):
        #on se met sur écoute
        with sr.Microphone() as source:
       
            print("Lancement")
            
            audio = self.r3.listen(source)
           
        #Si on a une entrée audio
        try:
            #On va utiliser le module Speech to text pour transformer notre voix en texte
            MyPhrase = self.r2.recognize_google(audio, language="fr-FR")
            print(MyPhrase)   
            #Si on detecte le hotWord Eva Elle nous repond puis attend l'ordre
            if 'Eva' in MyPhrase:

                ListeReponse = [
                    "Que puis-je faire pour vous ?",
                    "Oui, Monsieur?",
                    "Je suis là.",
                    "Monsieur?",
                    "Vous m'avez Appelé?",
                    "M'auriez vous appelé?"
                ]
                self.GetAudio(random.choice(ListeReponse))
                time.sleep(1)
                self.r2 = sr.Recognizer()
                with sr.Microphone() as source:



                    audio = self.r2.listen(source)

                try:
                    get = self.r2.recognize_google(audio, language="fr-FR")
                    print(get)
                    self.GetAudio("Je m'en occupe! ")


                except sr.UnknownValueError:
                    print('erreur')
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
 
    def GetAudio(self,phrase):




        # Set the text input to be synthesized
        synthesis_input = texttospeech.types.SynthesisInput(text=""+ phrase+"")

        # Build the voice request, select the language code ("fr-FR") and the ssml
        # voice gender ("female")
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='fr-FR',
            name="fr-FR-Wavenet-C",
            ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

        # Select the type of audio file you want returned
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = self.client.synthesize_speech(synthesis_input, voice, audio_config)

        # The response's audio_content is binary.
        with open('Eva/output.wav', 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "output.mp3"')

        playsound("Eva/output.wav")


