from Lily.AI import *

PERSONAL_DISCORD_API = os.getenv('PERSONAL_DISCORD_API')
UIName = os.getenv('UIName')
VoiceChoice = os.getenv('VoiceChoice')
User = os.getenv('User')

while True:
    try:
        VoiceCommand(UIName, User, VoiceChoice)
        with open('ResponseOutput.txt') as f:
            ResponseOutput = f.read()

        os.system(f'say -v {VoiceChoice} "{ResponseOutput}"')
    except:
        pass
