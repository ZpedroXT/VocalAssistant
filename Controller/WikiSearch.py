# -*-coding:UTF-8 -*
import speech_recognition as sr
import wikipedia
from google.cloud import texttospeech
from playsound import playsound
import time
import os
import random
class WikiSearch:
    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()
        self.r2 = sr.Recognizer()



    def getSearchWikipedia(self):
        self.GetAudio("Que souhaitez-vous rechercher?")
        time.sleep(1)
        self.r2 = sr.Recognizer()
        with sr.Microphone() as source:
            # audio = self.r2.adjust_for_ambient_noise(source)
            audio = self.r2.listen(source)

        try:
            getSequence = self.r2.recognize_google(audio, language="fr-FR")
            print("my sequence " + getSequence)
            # self.GetAudio(random.choice(self.ListeLoad))
            wikipedia.set_lang("fr")
            wikiText = wikipedia.summary(getSequence, sentences=1)
            print(wikiText)
            self.GetAudio(wikiText)
            return ""
        except:
            self.GetAudio("Monsieur, pourriez-vous parler plus fort je vous prie, je ne vous entends pas très bien.")

            return self.getSearchWikipedia()


    def GetAudio(self,phrase):




        # Set the text input to be synthesized
        synthesis_input = texttospeech.types.SynthesisInput(text=""+phrase+"")

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


