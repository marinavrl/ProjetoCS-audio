"""import pyttsx
engine = pyttsx.init()
engine.say("I will speak this text")
engine.runAndWait()"""

import pyttsx
engine = pyttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].id)

