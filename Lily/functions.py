from Lily.libraries import *

SkyClient = SkyQRemote('192.168.0.22')

def alarm(VoiceChoice, User, UIName):

    def WakeUp(current_time, User):
        LightOn(UIName)
        os.system(f'say -v {VoiceChoice} "Good morning, {User}, it is {current_time}."')
        Application = '"Spotify"'
        Command = (f"osascript -e 'tell application {Application} to play'")
        os.system(Command)

    while True:
        set_alarm = f"09:00:00"
        time.sleep(1)
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm:
            print("Is time.")
            WakeUp(current_time, User)
            WakeUp(current_time, User)
        else:
            print("Not time.")

def mute():
    os.system("osascript -e 'set Volume 0'")

def maxvol():
    os.system("osascript -e 'set Volume 10'")

def setvol(setting):
    os.system(f"osascript -e 'set Volume {setting}'")

def LightOn():
    USERNAME = ''
    PASSWORD = ''
    COUNTRY_CODE = ''
    api = TuyaApi()
    api.init(USERNAME, PASSWORD, COUNTRY_CODE)
    light_id = str("")
    api.get_device_by_id(light_id).turn_on()

def LightOff():
    USERNAME = ''
    PASSWORD = ''
    COUNTRY_CODE = ''
    api = TuyaApi()
    api.init(USERNAME, PASSWORD, COUNTRY_CODE)
    light_id = str("")
    api.get_device_by_id(light_id).turn_off()

def iPlayer():
    webbrowser.open("https://www.bbc.co.uk/iplayer")

def Amazon():
    webbrowser.open("https://www.amazon.co.uk/?ref_=nav_custrec_signin")

def Spotify():
    webbrowser.open("https://open.spotify.com/")

def DisneyPlus():
    webbrowser.open("https://www.disneyplus.com/en-gb/select-profile")

def PlayMusic():
    Application = '"Spotify"'
    Command = (f"osascript -e 'tell application {Application} to play'")
    os.system(Command)

def PauseMusic():
    Application = '"Spotify"'
    Command = (f"osascript -e 'tell application {Application} to pause'")
    os.system(Command)

def SkipMusic():
    Application = '"Spotify"'
    Command = (f"osascript -e 'tell application {Application} to next track'")
    os.system(Command)

def NewDocument():
    Application = '"Microsoft Word"'
    Command = (f"osascript -e 'tell application {Application} to create new document'")
    os.system(Command)

def NewCode():
    Application = '"Atom"'
    Command = (f"osascript -e 'tell application {Application} to create new document'")
    os.system(Command)

def Divider():
    print("  --=+=--  ")
    print("----=+=----")
    print("  --=+=--  ")

def ClearCache():
    files = glob.glob('__pycache__/*.pyc', recursive=True)
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

def StartUp(UIName, User, SAI_Version, Edition, VoiceChoice):
    Description = (f" {UIName} | {Edition} Edition | Powered by {Framework_Name}, Version: {SAI_Version} ")
    print("")
    print(Description)
    print("")
    print("---= [SETUP] =---")
    print(f"{Framework_Name}: Downloading 'punkt' from 'nltk' for '{UIName}'.")
    print("---= [SETUP] =---")
    nltk.download('punkt')
    print("---= [SETUP] =---")
    print(f"{Framework_Name}: Commencing the '{UIName}' startup procedure.")
    StartupGreeting = ["Hello, ", "Good day, ", "Hey there, ", "Hey, "]
    Divider()
    print(f"{User}: has activated this program.")
    print(f"{UIName} is thinking...")
    print(f"{UIName}: Program activated at {current_time}")
    try:
        os.system(f'say -v {VoiceChoice} "All systems online. {random.choice(StartupGreeting)}, {User}."')
    except:
        engine.say(f"All systems online. {random.choice(StartupGreeting)}, {User}.")


def Edit(UIName, Edition):
    Divider()
    ResponseOutput = ("Loading up IDE...")



    subprocess.Popen(["atom", "SAI.py"])
    subprocess.Popen(["atom", (Edition + " Chat.py")])

def SkyPlay(SkyClient):
    sequence = "play"
    SkyClient.press(sequence)

def SkyPower(SkyClient):
    sequence = "power"
    SkyClient.press(sequence)

def YouTubeSearch(secondarysentence, UIName):
    webbrowsersearch = secondarysentence
    webbrowsersearch = webbrowsersearch.replace("search YouTube for ", "")
    webbrowsersearch = webbrowsersearch.replace("search youtube for ", "")
    webbrowsersearch = webbrowsersearch.replace("search youtube ", "")
    webbrowsersearch = webbrowsersearch.replace("search YouTube ", "")
    webbrowsersearch = webbrowsersearch.replace("look up ", "")
    webbrowsersearch = webbrowsersearch.replace("Look up ", "")
    webbrowser.open("https://youtube.com/search?q=%s" % webbrowsersearch)
    Responses = ["Searching YouTube...", "Sure.", "YouTube search confirmed.", "Here you go."]
    ResponseOutput = random.choice(Responses)
    if "." not in ResponseOutput:
        ResponseOutput = (ResponseOutput + ".")

def WikiSearch(sentence, UIName):
    query = sentence
    query = query.replace("what is", "")
    query = query.replace("who is", "")
    query = query.replace("what's a", "")
    query = query.replace("What is", "")
    query = query.replace("Who is", "")
    query = query.replace("What's a", "")
    query = query.replace(" ", "_")
    webbrowser.open("https://en.wikipedia.org/wiki/" + query)
    Responses = ["Let's find out...", "Here's the wikipedia", "I found this on the web."]
    ResponseOutput = random.choice(Responses)
    if "." not in ResponseOutput:
        ResponseOutput = (ResponseOutput + ".")

def GoogleSearch(secondarysentence, UIName):
    webbrowsersearch = secondarysentence
    webbrowsersearch = webbrowsersearch.replace("search Google for ", "")
    webbrowsersearch = webbrowsersearch.replace("search google for ", "")
    webbrowsersearch = webbrowsersearch.replace("google", "")
    webbrowsersearch = webbrowsersearch.replace("search Google", "")
    webbrowser.open("https://google.com/search?q=%s" % webbrowsersearch)
    Responses = ["Searching Google...", "Sure.", "Google search confirmed.", "Here you go."]
    ResponseOutput = random.choice(Responses)
    if "." not in ResponseOutput:
        ResponseOutput = (ResponseOutput + ".")


def AmazonSearch(secondarysentence, UIName):
    webbrowsersearch = secondarysentence.replace(" ", "+")
    webbrowser.open(f"https://www.amazon.co.uk/s?k={webbrowsersearch}&ref=nb_sb_noss_2+")
    Responses = ["Searching Amazon...", "Sure.", "Amazon shopping search confirmed.", "Here you go."]
    ResponseOutput = random.choice(Responses)
    if "." not in ResponseOutput:
        ResponseOutput = (ResponseOutput + ".")

def Weather():
    webbrowser.open("https://www.bbc.co.uk/weather/2641157")

def YouTubeDownload(User, UIName):
    StarterResponses = ["Alright, enter the URl to the video in the terminal interface.", "I need a direct link to the video, paste it into the terminal.", "I'll need a link to it. Paste it into the terminal please."]
    ResponseOutput = (random.choice(StarterResponses))
    if "." not in ResponseOutput:
        ResponseOutput = (ResponseOutput + ".")
    os.system(f'say -v {VoiceChoice} "{ResponseOutput}"')

    VideoURL = input(f"{User}: The URL is... ")
    YTLink = YouTube(VideoURL)
    Videos = YTLink.streams.all()
    Audio = list(enumerate(Videos))
    Video = list(enumerate(Videos))
    for i in Audio:
        print(f"{UIName}: {i}")
    VideoFormat = int(input(f"{User}: Video Format is... "))
    AudioFormat = int(input(f"{User}: With the Audio Format being... "))
    DN_Option = VideoFormat
    DN_OptionAudio = AudioFormat
    DN_Video = Videos[DN_Option]
    DN_Audio = Videos[DN_OptionAudio]
    DownloadedVideo = DN_Video.download()
    ResponseOutput = ("MP4 download attempted. Now attempting to download MP3.")
    if "." not in ResponseOutput:
        ResponseOutput = (ResponseOutput + ".")

    try:
        os.system(f'say -v {VoiceChoice} "{ResponseOutput}"')
    except:
        return


    os.rename(DownloadedVideo, "Download.mp4")
    DownloadedAudio = DN_Audio.download()
    ResponseOutput = ("MP3 download attempted. Now merging MP4 and MP3 files into one file.")
    if "." not in ResponseOutput:
        ResponseOutput = (ResponseOutput + ".")

    try:
        os.system(f'say -v {VoiceChoice} "{ResponseOutput}"')
    except:
        return


    os.rename(DownloadedAudio, "Download.mp3")
    video_stream = ffmpeg.input('Download.mp4')
    audio_stream = ffmpeg.input('Download.mp3')
    ffmpeg.output(audio_stream, video_stream, 'FullDownload.mp4').run()
    ResponseOutput = ("Download attempt completed. MP4 & MP3 files merged successfully...")
    if "." not in ResponseOutput:
        ResponseOutput = (ResponseOutput + ".")

    try:
        os.system(f'say -v {VoiceChoice} "{ResponseOutput}"')
    except:
        return


    print(f"{Framework_Name}: Clearing up...")
    os.remove("Download.mp3")
    os.remove("Download.mp4")
