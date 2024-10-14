# YUSUF DAG

import pyglet
import time
from gtts import gTTS
import os

filename = "textToSpeechSound.mp3"
print("Wait for Google API to respond.")

# tts = gTTS(text="Physical fitness refers to good body health, and is the result of regular exercise, proper diet and nutrition, and proper rest for physical recovery. A person who is physically fit will be able to walk or run without getting breathless and they will be able to carry out the activities of everyday living and not need help. How much each person can do will depend on their age and whether they are a man or woman. A physically fit person usually has a normal weight for their height. The relation between their height and weight is called their Body Mass Index. A taller person can be heavier and still be fit. If a person is too heavy or too thin for their height it may affect their health.", lang="en")
tts = gTTS(input("Enter the text you want to convert to audio.\n"), lang="en")

print("Save the response as an mp3 file.")
tts.save(filename)
if os.environ=='windows':
    pass
else:
    print("Set pyglet pre-values.")
    pyglet.options['audio'] = ('openal', 'pulse', 'silent') # This line is necessary for Linux, unnecessary for windows.

print("Read mp3 file.")
ses = pyglet.media.load(filename, streaming=False)

print("Perform the voiceover.")
ses.play()

print("Wait until playback of the audio file is complete.")
time.sleep(ses.duration)

print("The process is complete.")