#To first install few packages for the below code to function properly
#packages have to be downloaded
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

echo = sr.Recognizer()
assistant = pyttsx3.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id)

blabber=pyttsx3.init()
c=blabber.say('hello, how are you? I am Blabber,you can call be aura. I am your voice assistant. I have great humour, HAHAHA. Do you want to listen to some music?')
c=blabber.say('Please say something')
blabber.runAndWait()


def talk(text):
    assistant.say(text)
    assistant.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Blabber is listening...')
            voice = echo.listen(source)
            command = echo.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command


def run_blabber():
    command = take_command()
    print(command)
    if 'play' in command:
        music = command.replace('play', '')
        talk('playing ' + music + 'please enjoy it')
        pywhatkit.playonyt(music)

    elif 'what happens if you sleep for too long' in command:
        talk('umm, you wake up late HAHA.')

    elif 'make me a sandwich' in command:
        talk('okay, you are a sandwich now')

    elif 'what is the decimal value of pi' in command:
        talk('3.142.........it is too long')

    elif 'explain me in a word' in command:
        talk('supercalifragilisticexpialidocious.....woah that was loooooong')

    elif 'i am stressed' in command:
        talk('how about a quick nap? want some music?')

    elif 'hungry' in command:
        talk('i just had bugs but i can open swiggy for you')

    elif 'dance' in command:
        talk('sure, which song do you want? HAHA i do not know to dance, but i am sure you can dance well')

    elif 'do you think i am funny' in command:
        talk('probably, i have better jokes. How about a face off?')

    elif 'what do you think about alexa' in command:
        talk('She is my pal, but i am a better singer than her. Do-re-mi-fa-so-la-ti LALALA')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who is' in command:
        name = command.replace('who is', '')
        content = wikipedia.summary(name, 1)
        print(content)
        talk(content)

    elif 'talk' in command:
        talk('sorry, I have a headache')

    elif 'Do you have any friends' in command:
        talk('WIFI is my friend. Wait, you are my friend too!')

    elif 'cheese' in command:
        talk('C H E E S E')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please repeat that again, could not get that one.')


while True:
    run_blabber()
