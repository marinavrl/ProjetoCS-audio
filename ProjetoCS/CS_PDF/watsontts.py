# Intall Dependencies

# Authenticate
import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url = ''
apikey = ''

# Setup Service
authenticator = IAMAuthenticator(apikey)
# New TTS Service
tts = TextToSpeechV1(authenticator=authenticator)
# Set Service URL
tts.set_service_url(url)

# Convert a String
"""with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize('Hello World!', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)"""

"""with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize('Bem vinda ao mundo da engenharia da computação!', accept='audio/mp3', voice='pt-BR_IsabelaV3Voice').get_result()
    audio_file.write(res.content)"""

# List Voices
"""voices = tts.list_voices().get_result()
print(json.dumps(voices, indent=2))"""

"""pt-BR_IsabelaVoice
pt-BR_IsabelaV3Voice """


# Convert from a File
"""for file in *.pdf; do pdftotext "$file" "$file.txt"; done"""
with open('C_FP23.txt', 'r') as f:
    text = f.readlines()

text = [line.replace('\n','') for line in text]

text = ' '.join(str(line) for line in text)

print(text)

with open('./C_FP23.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='pt-BR_IsabelaV3Voice').get_result()
    audio_file.write(res.content)

# Using New Language Models
