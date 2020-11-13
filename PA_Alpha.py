from selenium import webdriver      # selenium should be installed
from selenium.webdriver.common.keys import Keys
import os
import time
import random
import datetime
import pyttsx3                      # pyttx3 should be installed
import speech_recognition as sr     # speech recognition should be installed
import pyaudio                      # pyaudio should be installed
import webbrowser
import wikipedia                    # wikipedia should be installed
import pyautogui                    # pyautogui should be installed
import pyjokes                      # pyjokes should be installed
from UserData import *              # imports user data from UserData.py
import requests

print ("""

 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |      __      | || |   _____      | || |   ______     | || |  ____  ____  | || |      __      | |
| |     /  \     | || |  |_   _|     | || |  |_   __ \   | || | |_   ||   _| | || |     /  \     | |
| |    / /\ \    | || |    | |       | || |    | |__) |  | || |   | |__| |   | || |    / /\ \    | |
| |   / ____ \   | || |    | |   _   | || |    |  ___/   | || |   |  __  |   | || |   / ____ \   | |
| | _/ /    \ \_ | || |   _| |__/ |  | || |   _| |_      | || |  _| |  | |_  | || | _/ /    \ \_ | |
| ||____|  |____|| || |  |________|  | || |  |_____|     | || | |____||____| | || ||____|  |____|| |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 


""")

# works on google chrome for now
driver = webdriver.Chrome()         # chromedriver should be installed

r = sr.Recognizer()

YourName = "Ronik"

def record_audio(ask=False):    # speech to text
    with sr.Microphone() as source: # microphone as source
        if ask:
            ttsp(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert speech to text
        except sr.UnknownValueError: # speech recognizer does not understand
            ttsp("I didn't get that")
        except sr.RequestError:
            ttsp('Sorry, the service is down') # speech recognizer is disconnected
        print("\n"+YourName+":  "+voice_data.lower()) # print what user said
        return voice_data.lower()


def respond(voice_data):   # conditions

    if there_exists(["change my name to"]):
        search_term = voice_data.split("to ")[-1]
        global YourName
        YourName = search_term
        ttsp("Username changed to "+YourName)

    if there_exists(["hello","hi"]):
        ttsp("Hello, hope you are doing well")

    if there_exists(["good morning"]):
        ttsp("Good Morning. Rise and shine and be on your own way")

    if there_exists(["good night"]):
        ttsp("Good night. May the most pleasant dreams greet you")

    if there_exists(["good afternoon"]):
        ttsp("Good Afternoon")

    if there_exists(["what is your name","what's your name","tell me your name"]):
        ttsp("My name is Alpha")

    if there_exists(["what's the time","tell me the time","what time is it"]):
        ctime()
        
    if there_exists(["what's the date","tell me the date","what's today's date"]):
        cdate()

    if there_exists(["find on maps for","find on map for"]):
        FindLocation()

    if there_exists(["tell the weather","tell me today's weather","tell me the weather"]):
        getWeather()
    
    if there_exists(["find the file named"]):
        FindFiles()

    if there_exists(["take screenshot"]):
        ScreenShot()

    if there_exists(["find on google for","find for"]):
        FindOnGoogle()

    if there_exists(["find on youtube for"]):
        FindOnYT()

    if there_exists(["calculate"]):
        Calc()
        
    if there_exists(["login to instagram","log into instagram"]):
        instalogin(insta_username,insta_password)
        
    if there_exists(["login to twitter","log into twitter"]):
        twitterlogin(twitter_username,twitter_password)
        
    if there_exists(["login to facebook","log into facebook"]):
        fblogin(fb_username,fb_password)
        
    if there_exists(["perform whatsapp automation"]):
        autoWPReply()
        
    if there_exists(["roll a dice"]):
        RollDice()
        
    if there_exists(["toss a coin"]):
        CoinToss()

    if there_exists(["tell a joke","tell me a joke"]):
        TellJokes()

    if there_exists(["wikipedia for"]):
        FindWiki()

    if there_exists(["exit", "bye bye", "quit", "goodbye"]):
        ttsp("going offline")
        driver.close()
        exit()
        

def there_exists(terms):        # for checking existence of certain terms or phrases in voice
    for term in terms:
        if term in voice_data:
            return True

def ttsp(ttspeech):     # text to speech
    engine = pyttsx3.init()
    engine.say(ttspeech)
    print("Alpha: "+ttspeech) 
    engine.runAndWait()

def instalogin(username,password):  # instagram login
    driver.get('https://www.instagram.com/')
    time.sleep(2)
    instaUsername = driver.find_element_by_name("username").send_keys(username)
    instaPwd = driver.find_element_by_name("password").send_keys(password)
    instaLogin = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
    ttsp("Succesfully logged into instagram")

def fblogin(username,password): # facebook login
    driver.get('https://www.facebook.com/')
    time.sleep(2)
    fbUsername = driver.find_element_by_id("email").send_keys(username)
    fbPwd = driver.find_element_by_id("pass").send_keys(password)
    fbLogin = driver.find_element_by_name("login").click()
    ttsp("Succesfully logged into facebook")

def twitterlogin(username,password):    # twitter login
    driver.get('https://twitter.com/login')
    time.sleep(2)
    twitterUsername = driver.find_element_by_name("session[username_or_email]").send_keys(username)
    twitterPwd = driver.find_element_by_name("session[password]").send_keys(password)
    twitterLogin = driver.find_element_by_xpath("//div[@data-testid='LoginForm_Login_Button']").click()
    ttsp("Succesfully logged into twitter") 

def autoWPReply():     # automated reply to people on whatsapp
    driver.get("https://web.whatsapp.com/")
    input("After QR code scan, press anything to proceed")
    time.sleep(10)              # pauseeeee
    for name in names:
        targetprsn = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
        targetprsn.click()

        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        recieved = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
        msg = [message.text for message in recieved]

        if msg[-1] == WPmsg:   # search for this specific text
            myreply = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            myreply.clear()
            myreply.send_keys(WPif)    # send this text if condition is satisfied
            myreply.send_keys(Keys.RETURN)
        else :
            myreply = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            myreply.clear()
            myreply.send_keys(WPelse)  # send this text if condition fails
            myreply.send_keys(Keys.RETURN)
    ttsp("Task is completed")

def FindLocation(): # find location
    location = voice_data.split("for")[-1]
    driver.get('https://www.google.com/maps')
    time.sleep(2)
    searchbox = driver.find_element_by_id("searchboxinput")
    searchbox.send_keys(location)
    ttsp('Here is what I found for '+location+' on google maps')
    time.sleep(1)
    searchbox.send_keys(Keys.ENTER)

def FindOnGoogle(): # find on google
    search_term = voice_data.split("for")[-1]
    url = f"https://google.com/search?q={search_term}"
    webbrowser.get().open(url)
    ttsp('Here is what I found for '+search_term+' on google')
    
def FindOnYT(): # find on youtube
    search_term = voice_data.split("for")[-1]
    url = f"https://www.youtube.com/results?search_query={search_term}"
    webbrowser.get().open(url)
    ttsp('Here is what I found for '+search_term+' on youtube')

def CoinToss(): # coin toss
    moves=["head", "tails"]   
    move=random.choice(moves)
    ttsp("It's a " + move)
    
def RollDice(): # roll a dice
    moves=["1","2","3","4","5","6"]   
    move=random.choice(moves)
    ttsp("It's a " + move)

def ScreenShot():   # for screenshot
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(screenshot_savedir)
    ttsp("Screenshot saved in "+screenshot_savedir)

def getWeather():
    URL1 = 'https://wttr.in/?1AF'
    URL2 = 'https://wttr.in/?0AF&format=4'
    ERR_MSG = 'Error: could not reach the service. Status code: {}.'
    CONN_ERR = 'Error: connection not available.'

    try:
        response1 = requests.get(URL1)
        response2 = requests.get(URL2)
        if response1.ok and response2.ok:
            ttsp(response2.text)
            print(response1.text)
        else:
            ttsp(ERR_MSG.format(response2.status_code))
    except requests.exceptions.ConnectionError:
        ttsp(CONN_ERR)

def Calc():     # a simple calculator
    search_term = voice_data.split("calculate")[-1]
    search_term=search_term.replace("plus", "+")
    search_term=search_term.replace("minus", "-")
    search_term=search_term.replace("multiplied by", "*")
    search_term=search_term.replace("divided by", "/")
    search_term=search_term.replace("into", "*")
    search_term=search_term.replace("by", "/")
    calc = eval(str(search_term))
    ttsp("The result is "+str(calc))

def FindWiki():     # find definition on wikipedia
    search_term = voice_data.split("for")[-1]
    try:
        ttsp(wikipedia.summary(search_term, sentences=2))
    except wikipedia.exceptions.DisambiguationError as e:
        ttsp("Can you be a bit more specific ?  There are many results based on your search. I am printing a list of those below\n")
        print (e.options)

def ctime():    # for time
    current_time = datetime.datetime.now() 
    # print ("Current Time is : ", current_time.hour,":",current_time.minute,":",current_time.second) 
    ttsp ("Current Time is : "+ str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)) 

def cdate():    # for date
    current_date = datetime.datetime.now() 
    # print ("Current Date is : ", current_date.day,"/",current_date.month,"/",current_date.year)
    ttsp ("Current Date is : "+ str(current_date.day)+"/"+str(current_date.month)+"/"+str(current_date.year))

def FindFiles():   # for finding files
    filename = voice_data.split("named")[-1]
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    # print("\nFile is present in the following location/s : \n",result)
    ttsp ("File is present in  "+result)

def TellJokes():    # tell jokes
    jokes = pyjokes.get_joke()
    ttsp(jokes)


while(1):
    voice_data = record_audio() # for voice input
    respond(voice_data) # for reply