# PA-Alpha with GUI (speech recognition to be added soon)
# since voice support is not added, mic button does the same thing as the send button
from tkinter import *
import tkinter as tk                # tkinter should be installed
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
import threading

# works on google chrome for now
driver = webdriver.Chrome()         # chromedriver should be installed

########## GUI ##########

window = tk.Tk()
window.title("Personal Assistant | Alpha")
window.geometry('700x900')
window.minsize(700,900)

def saveChats():
        text_area_text = chatwindow.get('1.0', 'end-1c')
        save_text = open("chat_history1.txt", 'w')
        save_text.write(text_area_text)
        save_text.close()

def exitWindow():
        driver.close()
        exit()

def Help():
        helpframe=Toplevel(bg='white')
        helpframe.geometry('400x400')
        helpframe.minsize(400,400)
        helpcontent = """ 
Features ---------
1) auto login into insta,fb,twitter
2) auto wp reply
3) search location
4) get time
5) get date
6) find files in computer
7) search on google and youtube
8) roll a dice or toss a coin
9) calculator
10) screenshot
11) search wikipedia for def
12) input user name
13) tell jokes 
        """
        hlp=Label(master=helpframe,text=helpcontent,justify=LEFT,bg='white',padx=15,pady=15).pack()
        helpframe.mainloop()

# toolbar menu
main_menu=Menu(window,bg="#cedbff",tearoff=0)

file_menu=Menu(main_menu,tearoff=0)
file_menu.add_command(label='Help',command=Help)
file_menu.add_command(label='Save chat',command=saveChats)
file_menu.add_command(label='Exit',command=exitWindow)

main_menu.add_cascade(label='Options', menu = file_menu)
main_menu.add_command(label='About')
main_menu.add_command(label='Exit',command=exitWindow)
window.config(menu=main_menu,bg='#cedbff')

# hero frame
frame1 = tk.Frame(master=window, bg="#cedbff",width=400, height=400)
frame1.pack(fill=tk.BOTH,side=tk.TOP,expand=True,padx=16,pady=16)
# scroll bar
scroll_bar = Scrollbar(master=frame1,width=20)  
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
# chat window for all chats
chatwindow=Text(master=frame1,relief = FLAT, bg="#fff", fg="#000",yscrollcommand = scroll_bar.set, padx=10,pady=10)
chatwindow.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
chatwindow.config(state='disabled')

# button frame
frame3 = tk.Frame(master=window, height=40, bg="#cedbff")
frame3.pack(fill=tk.X,side=tk.BOTTOM, padx=16,pady=10)
# direct msg btn
send_btn=Button(master=frame3,text="SEND", bg='#8761FD', fg='white', relief=FLAT , activebackground='#4476ff', width=8, height=2, font=('Arial',10),command = lambda:Take_input())    #EC4176
send_btn.pack(side=RIGHT, padx=5)
# mic btn
mic_btn=Button(master=frame3,text="MIC", bg='#ff5151', fg='white', relief=FLAT , activebackground='red', width=8, height=2, font=('Arial',10),command = lambda:Take_input())    #EC4176
mic_btn.pack(side=LEFT, padx=5)

# message frame
frame2 = tk.Frame(master=window, bg="yellow")
frame2.pack(fill=tk.X,side=tk.BOTTOM,padx=16)
msgwindow=Text(master=frame2,relief = GROOVE, bg="#fff", fg="#000",height=3)
msgwindow.pack(fill=tk.X)

############# Features #############

def CoinToss(): # coin toss
    moves=["head", "tails"]   
    move=random.choice(moves)
    ttsp("It's a " + move)
    
def RollDice(): # roll a dice
    moves=["1","2","3","4","5","6"]   
    move=random.choice(moves)
    ttsp("It's a " + move)

def Calc(INPUT):     # a simple calculator
    search_term = INPUT.split("calculate")[-1]
    search_term=search_term.replace("plus", "+")
    search_term=search_term.replace("minus", "-")
    search_term=search_term.replace("multiplied by", "*")
    search_term=search_term.replace("divided by", "/")
    search_term=search_term.replace("into", "*")
    search_term=search_term.replace("by", "/")
    calc = eval(str(search_term))
    ttsp("The result is "+str(calc))

def ctime():    # for time
    current_time = datetime.datetime.now() 
    # print ("Current Time is : ", current_time.hour,":",current_time.minute,":",current_time.second) 
    ttsp ("Current Time is : "+ str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)) 

def cdate():    # for date
    current_date = datetime.datetime.now() 
    # print ("Current Date is : ", current_date.day,"/",current_date.month,"/",current_date.year)
    ttsp ("Current Date is : "+ str(current_date.day)+"/"+str(current_date.month)+"/"+str(current_date.year))

def TellJokes():    # tell jokes
    jokes = pyjokes.get_joke()
    ttsp(jokes)

def FindOnGoogle(INPUT): # find on google
    search_term = INPUT.split("for")[-1]
    url = f"https://google.com/search?q={search_term}"
    webbrowser.get().open(url)
    ttsp('Here is what I found for '+search_term+' on google')
    
def FindOnYT(INPUT): # find on youtube
    search_term = INPUT.split("for")[-1]
    url = f"https://www.youtube.com/results?search_query={search_term}"
    webbrowser.get().open(url)
    ttsp('Here is what I found for '+search_term+' on youtube')

def ScreenShot():   # for screenshot
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(screenshot_savedir)
    ttsp("Screenshot saved in "+screenshot_savedir)

def FindFiles(INPUT):   # for finding files
    filename = INPUT.split("named")[-1]
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    # print("\nFile is present in the following location/s : \n",result)
    ttsp ("File is present in  "+result)

def FindWiki(INPUT):     # find definition on wikipedia
    search_term = INPUT.split("for")[-1]
    try:
        ttsp(wikipedia.summary(search_term, sentences=2))
    except wikipedia.exceptions.DisambiguationError as e:
        ttsp("Can you be a bit more specific ?  There are many results based on your search. I am printing a list of those below\n")
        print (e.options)
        chatwindow.config(state='normal')
        chatwindow.insert(END, '\n'+List+': '+e.options+'\n')
        chatwindow.config(state='disabled')

def FindLocation(INPUT): # find location
    location = INPUT.split("for")[-1]
    driver.get('https://www.google.com/maps')
    time.sleep(2)
    searchbox = driver.find_element_by_id("searchboxinput")
    searchbox.send_keys(location)
    ttsp('Here is what I found for '+location+' on google maps')
    time.sleep(1)
    searchbox.send_keys(Keys.ENTER)

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



############ Inputs ##########

YourName = "Ronik"

def Take_input(): 
        INPUT = msgwindow.get("1.0", "end-1c") 
        print(INPUT)
        chatwindow.config(state='normal')
        chatwindow.insert(END, '\n'+YourName+': '+INPUT+'\n')
        chatwindow.config(state='disabled')
        msgwindow.delete("1.0", END)

        if there_exists(["hello","hi"],INPUT):
                ttsp("Hello, hope you are doing well")

        # if there_exists(["change my name to"],INPUT):
        #         search_term = INPUT.split("to ")[-1]
        #         global YourName
        #         YourName = search_term
        #         ttsp("Username changed to "+YourName)

        if there_exists(["good morning"],INPUT):
                ttsp("Good Morning. Rise and shine and be on your own way")

        if there_exists(["good night"],INPUT):
                ttsp("Good night. May the most pleasant dreams greet you")

        if there_exists(["good afternoon"],INPUT):
                ttsp("Good Afternoon")

        if there_exists(["what is your name","what's your name","tell me your name"],INPUT):
                ttsp("My name is Alpha")

        if there_exists(["what's the time","tell me the time","what time is it"],INPUT):
                ctime()
                
        if there_exists(["what's the date","tell me the date","what's today's date"],INPUT):
                cdate()

        if there_exists(["find on maps for","find on map for"],INPUT):
                FindLocation(INPUT)
        
        if there_exists(["find the file named"],INPUT):
                FindFiles(INPUT)

        if there_exists(["take screenshot"],INPUT):
                ScreenShot()

        if there_exists(["find on google for","find for"],INPUT):
                FindOnGoogle(INPUT)

        if there_exists(["find on youtube for"],INPUT):
                FindOnYT(INPUT)

        if there_exists(["calculate"],INPUT):
                Calc(INPUT)
                
        if there_exists(["login to instagram","log into instagram"],INPUT):
                instalogin(insta_username,insta_password)
                
        if there_exists(["login to twitter","log into twitter"],INPUT):
                twitterlogin(twitter_username,twitter_password)
                
        if there_exists(["login to facebook","log into facebook"],INPUT):
                fblogin(fb_username,fb_password)
                
        if there_exists(["perform whatsapp automation"],INPUT):
                autoWPReply()
                
        if there_exists(["roll a dice"],INPUT):
                RollDice()
                
        if there_exists(["toss a coin"],INPUT):
                CoinToss()

        if there_exists(["tell a joke","tell me a joke"],INPUT):
                TellJokes()

        if there_exists(["wikipedia for"],INPUT):
                FindWiki(INPUT)

        if there_exists(["exit", "bye bye", "quit", "goodbye"],INPUT):
                ttsp("going offline")
                driver.close()
                exit()


        

def there_exists(terms,INPUT):        # for checking existence of certain terms or phrases in voice
    for term in terms:
        if term in INPUT:
            return True

def ttsp(ttspeech):     # text to speech
        chatwindow.config(state='normal')
        chatwindow.insert(END, 'Alpha: '+ttspeech+'\n')
        chatwindow.config(state='disabled')
        t1=threading.Thread(target=V_out(ttspeech)).start()
        
def V_out(ttspeech):
        engine = pyttsx3.init()
        engine.say(ttspeech)
        engine.runAndWait()

scroll_bar.config( command = chatwindow.yview )
window.mainloop()