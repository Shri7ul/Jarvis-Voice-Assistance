import speech_recognition as sr
mic_list = sr.Microphone.list_microphone_names()
print(mic_list)
