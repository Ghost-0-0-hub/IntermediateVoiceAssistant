import random
import time
import speech_recognition as sr
import os
import webbrowser
import pyautogui

def listen_for_audio():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        audio = listener.listen(source)
    
    try:
        return listener.recognize_google(audio).lower()
    except sr.UnknownValueError:
        print("I didn't catch that.")
        return None
    except sr.RequestError:
        print('API is unavailable')
        return None
    
def web_searching():
    while True:
        print('What would you like to browse?')
        query = listen_for_audio()
        if query is None:
            print("sorry I didn't catch that.")
            continue
        query = query.strip()
        if 'stop' in query.lower():
            print('Exiting Search..')
            break
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(search_url)
        print(f"Searching for: {query}")

def opening_applications():
    Apps = {
    'google':r"C:\Users\Harris\OneDrive\Desktop\Softwares\Google Chrome.lnk",
    'vs': r"C:\Users\Harris\OneDrive\Desktop\Softwares\Visual Studio Code.lnk",
    'file':r"C:\Users\Harris\OneDrive\Desktop\Softwares\This PC - Shortcut.lnk",
    'code': r"C:\Users\Harris\OneDrive\Desktop\Code"
    }
    Tabs = {
    'netflix': "https://www.netflix.com/browse",
    'video': "https://www.youtube.com/",
    'mail' : "https://mail.google.com/mail/u/0/#inbox",
    'google meet' : "https://meet.google.com/landing"
    }
    while True:
        print('What would you like to open?')
        choice = listen_for_audio()
        
        if choice:
            choice = choice.lower()
            if choice in ['stop','quit']:
                print('Exiting Task Opener..')
                break
            elif choice in Apps:
                os.startfile(Apps[choice])
            elif choice in Tabs:
                webbrowser.open(Tabs[choice])
                time.sleep(3)
                if choice == 'google meet':
                    pyautogui.click(800,400,duration=1)
                    pyautogui.click(800,435,duration=1)
            else:
                print('Sorry I cant find that')
        
def time_telling():
    x = time.strftime('%I:%M')    
    print(x)

def joking():
        jokes = ("Why did the scarecrow win an award?Because he was outstanding in his field!","What do you call fake spaghetti? An impasta!","Why did the bicycle fall over? Because it was two-tired!",
                "What do you call cheese that isn't yours? Nacho Cheese!", "Why don't skeletons fight eachother? they don't have the guts!", "What did one wall say to the other? I'll meet you at the corner")
        random_joke = random.choice(jokes)
        print(random_joke)

def help():
    print('''
          
I see you are confused, I can assist you with the following:
          
1. Web searching; E.g: "I want to search something"
2. Telling the Time; E.g: "Tell me the time"
3. Telling a Joke; E.g: "Tell me a joke"
4. Executing files; E.g: "Open something for me"
5. Play Music; E.g: "Play music"
6. Take a Screenshot; E.g: "Take a screenshot"
7. Sending Messages on Whatsapp; E.g: "I want to send a message"
8. Ask for help; E.g: "Assist me"

''')
    
def music():
    print('Opening Spotify..')
    music = "https://open.spotify.com/playlist/71Sh4WqH5OMOeRYE4M0mky"
    webbrowser.open(music)

def screenshot():
    pyautogui.hotkey('win','Shift','s')
    pyautogui.click(980,30, duration=1)
    pyautogui.click(980,100, duration=1)

def message_send():
        print('Who would you like to message?')
        msg_option = listen_for_audio()
        time.sleep(5)
        pyautogui.click(1200,1060,duration=0.5)
        if 'friends' in msg_option:
            pyautogui.click(300,200,duration=0.5)
            pyautogui.click(1200,1010,duration=0.5)
            message = listen_for_audio()
            pyautogui.write(message)
            pyautogui.press('Enter')
            print('Exiting message bot..')
        elif 'sir' in msg_option:
            pyautogui.click(300,500,duration=0.5)
            pyautogui.click(1200,1010,duration=0.5)
            message = listen_for_audio()
            pyautogui.write(message)
            pyautogui.press('Enter')
            print('Exiting message bot..')

def main_assistant():
    print('Hello! What can I help you with?')
    while True:
        task = listen_for_audio()
        
        if task:
            if 'search' in task:
                web_searching()
            elif 'open' in task:
                opening_applications()
            elif 'time' in task:
                time_telling()
            elif 'screenshot' in task:
                screenshot()
            elif 'joke' in task:
                joking()
            elif 'assist' in task:
                help()
            elif 'music' in task:
                music()
            elif 'message' in task:
                message_send()
            elif 'exit' in task:
                print('Goodbye!')
                break
        else:
            print("I didn't understand that command.")
main_assistant()