# pip install speechrecognition
# pip install pyaudio
# sudo apt-get install python3-pyaudio
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
   print("Speak Anything :")
   audio = r.listen(source,timeout=5,phrase_time_limit=25)
   print("Done, Please wait while we are processing what you said...")
   try:
     text=r.recognize_google(audio)
     print("you said: {}".format(text))
   except:
     print("Sorry, we could not recognize what you said. You can try again")