import speech_recognition  as sr
print(sr.__version__)
r=sr.Recognizer()
mic=sr.Microphone(1)
a=sr.Microphone.list_microphone_names()
for i in a:
    print(i)
with mic as source:
   # r.adjust_for_ambient_noise(source)
    audio=r.listen(source,3,3)

print(r.recognize_google(audio))


