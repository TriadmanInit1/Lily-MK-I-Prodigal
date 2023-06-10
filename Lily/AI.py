from Lily.libraries import *
from Lily.nltk_utils import *
from Lily.model import *
from Lily.functions import *

intents = {"intents": [
{"tag": "greeting", "patterns": ["Hello", "hi", "hey", "hello", "what's up", "hey"], "responses": ["Hey there, how can I help you today?", "Hello, how can I assist you?"]},
{"tag": "goodbye", "patterns": ["bye", "see you later", "see you in a bit", "later", "bye bye", "goodbye"], "responses": ["Goodbye for now. I'll be online should you require me again.", "Farewell, I shall remain online until you need me next."]},
{"tag": "username", "patterns": ["what is my name?", "what's my name", "who am I?", "do you know me?", "am I known to you?", "do you recognise me?"], "responses": [" ", " "]},
{"tag": "open-amazon", "patterns": ["Open Amazon.", "Load up Amazon.", "Bring up Amazon", "Go onto Amazon"], "responses": ["Sure thing, opening Amazon now. Is there anything specific you're looking for?", "Sure thing.", "As you wish."]},
{"tag": "open-iplayer", "patterns": ["Open BBC iPlayer", "Open iPlayer", "Load iPlayer", "BBC iPlayer", "Bring up BBC iPlayer"], "responses": ["As you wish.", "Sure thing.", "Absolutely, opening BBC iPlayer for you now."]},
{"tag": "open-disney+", "patterns": ["Open Disney Plus", "Open Disney+", "Load up Disney", "Disney Plus", "Bring up Disney Plus", "Load up Disney Plus", "Disney+", "Open Disney"], "responses": ["As you wish.", "Sure thing.", "Of course, opening Disney Plus for you now."]},
{"tag": "clear-cache", "patterns": ["clear cash", "clear up the cash", "Clear cache", "Start clearing", "Clear out the cache", "empty cache", "Empty cache"], "responses": ["Clearing cache.", "One moment.", "Yes."]},
{"tag": "light-on", "patterns": ["turn light on", "turn my light on", "light on", "turn on light", "let there be light", "on light"], "responses": ["Light activated", "Sure.", "Lighting on."]},
{"tag": "light-off", "patterns": ["turn light off", "light off", "turn my light off", "kill the light", "lights out", "turn off the light", "let there be darkness", "it's too bright in here", "off light", "kill the light", "kill power"], "responses": ["Light deactivated", "Sure.", "Lighting off.", "Electric bill saved."]},
{"tag": "sky-pause-play", "patterns": ["Pause the TV.", "TV Pause", "pause tv", "pause the tv", "Play the TV.", "TV Play", "play tv", "play the tv", "resume tv", "resume the tv"], "responses": ["Command sent.", "I have sent the command."]},
{"tag": "sky-power", "patterns": ["Turn off the TV.", "TV off", "turn off tv", "turn off the tv", "turn on the tv", "turn the tv on", "Turn the TV on", "Switch the TV on", "power on the tv"], "responses": ["Command sent.", "I have sent the command."]},
{"tag": "search-google", "patterns": ["search Google for ", "search google for this", "look up for me", "look up this for me", "search google for this"], "responses": ["Done.", "No problem.", "Google search completed.", "Affirmative.", "Task completed."]},
{"tag": "are-you-up", "patterns": ["are you up?", "are you online?", "are you ready?", "are you up and running?"], "responses": ["For you, always", "Yes, for you, always."]},
{"tag": "gracious", "patterns": ["thank you", "thanks", "cheers", "thanking you", "great, thank you", "awesome, thank you"], "responses": ["You are welcome.", "You're welcome.", "Just doing my job.", "No problem", "De nada."]},
{"tag": "incapable", "patterns": ["I am lonely", "I feel lonely", "I feel sad", "I am upset", "I am not happy", "I feel pain", "I hate my life"], "responses": ["My apologies, I'm afraid I cannot help with that. I suggest you contact another human.", "I am sorry, but I can't help you with that. Try talking to a fellow human."]},
{"tag": "time", "patterns": ["What is the time?", "what's the time", "what's the current time?", "the time", "tell me the time", "timing"], "responses": ["The time is ", "It is currently ", "It is "]},
{"tag": "word-doc", "patterns": ["Open a new word document.", "I want a new document.", "New word document.", "Create a new word document.", "New project file."], "responses": ["Certainly.", "One moment.", "As you wish."]},
{"tag": "play-music", "patterns": ["Play music", "play music", "resume music", "drop my needle"], "responses": ["Music playing.", "As you wish."]},
{"tag": "pause-music", "patterns": ["pause music", "stop music", "stop the music"], "responses": ["Music now paused.", "As you wish."]},
{"tag": "atom", "patterns": ["new atom file", "new code", "new code script"], "responses": ["As you wish.", "Sure thing."]},
{"tag": "skip-music", "patterns": ["skip music", "Skip music", "skip song", "next song", "new song"], "responses": ["Music skipping.", "As you wish."]},
{"tag": "morning-routine", "patterns": ["good morning, ", "morning", "I'm awake", "wake Jack up", "wake up Jack"], "responses": [f"Good morning. It is ", "Good morning, it is currently "]},
{"tag": "mute", "patterns": ["mute", "silence", "mute"], "responses": ["As you wish.", "Muted."]}
]}

def LilyAI(sentence, intents):

    system_times = os.times()
    current_time = system_times[4]
    current_time_str = time.ctime(current_time)
    print("Current time: ", current_time_str)

    sentence = str(sentence)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    FILE = "data.pth"
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    UIName = os.getenv("UIName")

    while True:

        if sentence == "quit":
            break

        type(sentence)

        if type(sentence) == str:
            sentence = tokenize(sentence)
        else:
            return

        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        ConfidenceRate = prob.item()

        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    AIFunctions(User, UIName, intent, sentence)
        else:
            ResponseOutput = (f"I do not understand...")
            ConfidenceRate = prob.item()

        f = open("Confidence.txt", "w+")
        f.write(f"Confidence: {ConfidenceRate}")
        f.close()

        with open("ResponseOutput.txt") as f:
            ResponseOutput = f.read()
            f.close()

        print(f"{UIName}: {ResponseOutput} | Confidence Rate: {ConfidenceRate}")

def CarterSentry(sentence, User):
    response = requests.post("https://api.carterlabs.ai/chat", headers={
        "Content-Type": "application/json"
    }, data=json.dumps({
        "text": f"{sentence}",
        "key": f"{CARTER_ULTRON_API}",
        "playerId": f"{User}"
    }))

    RawResponse = response.json()
    Response = RawResponse["output"]
    FullResponse = Response["text"]
    ResponseOutput = FullResponse
    User = str(User)

    ResponseOutput = ResponseOutput.replace("Unknown person", User)
    ResponseOutput = ResponseOutput.replace("Unknown Person", User)
    ResponseOutput = ResponseOutput.replace("unknown person", User)

    f = open("ResponseOutput.txt", "w")
    f.write(f"{ResponseOutput}")
    f.close()

def CarterGriot(sentence, User):
    response = requests.post("https://api.carterlabs.ai/chat", headers={
        "Content-Type": "application/json"
    }, data=json.dumps({
        "text": f"{sentence}",
        "key": f"{CARTER_GRIOT_API}",
        "playerId": f"{User}"
    }))

    RawResponse = response.json()
    Response = RawResponse["output"]
    FullResponse = Response["text"]
    ResponseOutput = FullResponse
    User = str(User)

    ResponseOutput = ResponseOutput.replace("Unknown person", User)
    ResponseOutput = ResponseOutput.replace("Unknown Person", User)
    ResponseOutput = ResponseOutput.replace("unknown person", User)

    f = open("ResponseOutput.txt", "w")
    f.write(f"{ResponseOutput}")
    f.close()

def AIFunctions(User, UIName, intent, sentence):
    system_times = os.times()
    current_time = system_times[4]
    current_time_str = time.ctime(current_time)
    AlreadyDone = 0
    if "youtube-download" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            try:
                YouTubeDownload(User, UIName)
            except:
                print(f"{UIName}: A fatal error occured in the process...")

    elif "morning-routine" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}{current_time_str}. I will now play your spotify music and run the morning routine.")
            LightOn()
            PlayMusic()
            maxvol()

    elif "mute" == intent["tag"]:
            ResponseOutput = (random.choice(intent['responses']))
            mute()

    elif "open-amazon" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            Amazon()
            webbrowser.open("https://www.amazon.co.uk/", new=2)
            if "." not in ResponseOutput:
                ResponseOutput = (ResponseOutput + ".")


    elif "open-iplayer" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            iPlayer()
            webbrowser.open("https://www.bbc.co.uk/iplayer", new=2)
            if "." not in ResponseOutput:
                ResponseOutput = (ResponseOutput + ".")


    elif "open-disney+" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            DisneyPlus()
            webbrowser.open("https://www.disneyplus.com/en-gb/home", new=2)
            if "." not in ResponseOutput:
                ResponseOutput = (ResponseOutput + ".")

    elif "weather" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            Weather()

    elif "light-on" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            LightOn()

    elif "light-off" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            LightOff()

    elif "sky-pause-play" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            SkyPlay(SkyClient)

    elif "sky-power" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            SkyPower(SkyClient)

    elif "clear-cache" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            ClearCache()

    elif "time" == intent["tag"]:
            current_time = now.strftime("%H:%M")
            ResponseOutput = (f"{random.choice(intent['responses'])}{current_time_str}")

    elif "spotify" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            Spotify()

    elif "pause-music" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            PauseMusic()

    elif "play-music" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            PlayMusic()

    elif "word-doc" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            NewDocument()

    elif "skip-music" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            SkipMusic()

    elif "atom" == intent["tag"]:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            NewCode()
    else:
        try:
            CarterGriot(sentence, User)
            AlreadyDone = 1
        except:
            ResponseOutput = (f"{random.choice(intent['responses'])}")
            AlreadyDone = 0

    if AlreadyDone == 1:
        AlreadyDone = 0
        return
    else:
        f = open("ResponseOutput.txt", "w")
        f.write(f"{ResponseOutput}")
        f.close()

def VoiceCommand(UIName, User, VoiceChoice):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100
    seconds = 3.8
    filename = "audio.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

        # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print(f'{UIName}: I have finished recording.')

        # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    speech(UIName, User, VoiceChoice)

def speech(UIName, User, VoiceChoice):

    rate, data = wavfile.read("audio.wav")
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    wavfile.write("cleaned_audio.wav", rate, reduced_noise)

    model = whisper.load_model("base.en")
    result = model.transcribe("cleaned_audio.wav")
    sentence = result["text"]
    print(f"{User}: {sentence}")

    f = open("Memory.txt", "a")
    current_time = datetime.now()
    f.write(f" | {current_time}:")
    Memory = (f" {sentence} ")
    f.write(Memory)
    f.close()
    sentence = str(sentence)

    LilyAI(sentence, intents)

PERSONAL_DISCORD_API = os.getenv('PERSONAL_DISCORD_API')
UIName = os.getenv('UIName')
VoiceChoice = os.getenv('VoiceChoice')
User = os.getenv('User')
AuthorisedUsers = os.getenv('AuthorisedUsers')
JURISDICTIONSERVERS = os.getenv('JURISDICTIONSERVERS')

CARTER_GRIOT_API = os.getenv('CARTER_GRIOT_API')
CARTER_ULTRON_API = os.getenv('CARTER_ULTRON_API')
