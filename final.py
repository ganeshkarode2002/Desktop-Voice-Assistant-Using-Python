import speech_recognition as sr    
import pyttsx3                     
import datetime                    
import wikipedia                   
import webbrowser                  
import os                          
from tkinter import *              
import pyjokes                     
import keyboard                    
from googletrans import Translator
from PIL import Image , ImageTk


def gkEglish():
    
    name_file = open("Assistant_name", "r")
    name_assistant = name_file.read()
    
    engine = pyttsx3.init('sapi5')  
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[1].id)
        
    def speak1(text):
        engine.say(text)
        print( "Assistant : "  +  text)
        engine.runAndWait() 
    
    
    def wishMe1():
    
    
      hour=datetime.datetime.now().hour
    
      if hour >= 0 and hour < 12:
    
          speak1("Hello,Good Morning !!")
     
      elif hour >= 12 and hour < 18:
    
          speak1("Hello,Good Afternoon !!")
    
      else:
    
          speak1("Hello,Good Evening !!")
    
      speak1("I am your assistant Sir. Please tell me how may I help you ?")       
    
    def takecommand1(): 
    
        r = sr.Recognizer() 
        audio = '' 
    
        with sr.Microphone() as source: 
    
            print("Listening") 
            audio = r.listen(source, phrase_time_limit = 3) 
                    
        try: 
            print("Recognizing...")
            text = r.recognize_google(audio, language ='en-in') 
            print('You: ' + ': ' + text)
            return text
    
    
        except:
    
            return "None"
    
    
    
    wishMe1()
    
    def Process_audio1():
    
        run = 1
        if __name__=='__main__':
            while run==1:
    
                
                statement = takecommand1().lower()
                results = ''
                run +=1
    
                if 'wikipedia' in statement:
                    speak1('Searching Wikipedia...')
                    statement = statement.replace("wikipedia", "")
                    results = wikipedia.summary(statement,sentences=2)
                    speak1("According to Wikipedia")
                    speak1(results)
    
                elif ('open youtube' in statement )or ('youtube' in statement):
                    speak1("What do you want to search for ?")
                    search = takecommand1()
                    url = 'https://www.youtube.com/results?search_query=' + search
                    result = webbrowser.get().open(url)
                    speak1("Here is what i found")
                    speak1(search)
    
                elif 'search' in statement:
                    speak1("What do you want to search for ?")
                    search = takecommand1()
                    url = 'https://google.com/search?q=' + search
                    result = webbrowser.get().open(url)
                    speak1("Here is what i found")
                    speak1(search)
                
                
                elif 'find location' in statement or 'location' in statement:
                    speak1("What is the location")
                    location = takecommand1()
                    url = 'https://www.google.nl/maps/place/' + location + '/?amp;'
                    result = webbrowser.get().open(url)
                    speak1("Here is location")
                    speak1(location)
                
                elif 'news' in statement or 'todays news' in statement:
                    speak1("which city news do you want to search for ?")
                    search = takecommand1()
                    url = 'https://timesofindia.indiatimes.com/city/' + search
                    result = webbrowser.get().open(url)
                    speak1("Here are some headlines from the Times of India, Happy reading")
                    speak1(search)
                
                elif 'open google' in statement:
                    webbrowser.open("google.com")
    
                elif 'open college website' in statement or 'college website' in statement:
                    webbrowser.open("https://learner.vierp.in")
    
                elif 'open virtual classroom' in statement or 'classroom' in statement:
                    webbrowser.open("https://classroom.volp.in/login")
    
                elif 'play music' in statement or 'music' in statement:
                    music_dir = 'D:\\songs'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))
    
                elif 'the time' in statement:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak1(f"Sir, the time is {strTime}")
            
                elif 'open code' in statement or 'code' in statement :
                    codePath = "C:\\Users\\ganes\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
            
                elif 'open gmail' in statement or 'gmail' in statement:
                    webbrowser.open_new_tab("mail.google.com")
                    speak1("Google Mail open now")
                       
                elif 'cricket' in statement or 'live score' in statement:
                    news = webbrowser.open_new_tab("cricbuzz.com")
                    speak1('This is live news and score from cricbuzz')
                
                elif 'joke' in statement:
                  result = pyjokes.get_joke()
                  speak1(result)
                  
                elif 'corona' in statement or 'covid cases' in statement:
                    speak1("which country covid cases do you want to search for ?")
                    search = takecommand1()
                    url = 'https://www.worldometers.info/coronavirus/country/' + search
                    result = webbrowser.get().open(url)
                    speak1("Here are the latest covid-19 numbers")
                    speak1(search)
            
                else:
                    url = 'https://google.com/search?q=' + statement
                    result = webbrowser.get().open(url)
                    speak1("Here is what i found")
                    speak1(statement)
    
    
    
    def change_name1():
    
      name_info = name.get()
    
      file=open("Assistant_name", "w")
    
      file.write(name_info)
    
      file.close()
    
      settings_screen1.destroy()
    
      screen1.destroy()
    
    
    def change_name_window1():
        
          global settings_screen1
          global name
    
    
          settings_screen1 = Toplevel(screen1)
          settings_screen1.title("Settings")
          settings_screen1.geometry("500x500")
          settings_screen1.iconbitmap('app_icon.ico')
    
          
          name = StringVar()
    
          current_label1 = Label(settings_screen1, text = "Current name: gk")
          current_label1.pack()
    
          enter_label1 = Label(settings_screen1, text = "Please enter your Virtual Assistant's name below") 
          enter_label1.pack(pady=10)   
          
    
          Name_label1 = Label(settings_screen1, text = "Name")
          Name_label1.pack(pady=10)
         
          name_entry1 = Entry(settings_screen1, textvariable = name)
          name_entry1.pack()
    
    
          change_name_button1 = Button(settings_screen1, text = "Ok", width = 10, height = 1, command = change_name1)
          change_name_button1.pack(pady=10)
    
    
    def info1():
    
      info_screen1 = Toplevel(screen1)
      info_screen1.title("Info")
      info_screen1.iconbitmap('app_icon.ico')
    
      creator_label1 = Label(info_screen1,text = "Created by Ganesh karode")
      creator_label1.pack()
    
      Age_label1 = Label(info_screen1, text= " Guide Name:prof. Amol bhosale")
      Age_label1.pack()
    
      for_label1 = Label(info_screen1, text = "For SDP project")
      for_label1.pack()
    
    keyboard.add_hotkey("F4", Process_audio1)
    
    
    def main_screen1():
    
          global screen1
          screen1 = Tk()
          screen1.title(name_assistant)
          screen1.geometry("300x350")
          screen1.iconbitmap('app_icon.ico')
    
    
          name_label1 = Label(screen1,text = name_assistant,width = 300, bg = "black", fg="white", font = ("Calibri", 13))
          name_label1.pack()
    
    
          '''microphone_photo1 = PhotoImage(file = "logo.png" ,height=100,width=100)
          microphone_button1 = Button(image=microphone_photo1, command = Process_audio1)
          microphone_button1.pack(pady=10)'''
          '''image2 = Image.open("logo.png")
          photo2 = ImageTk.PhotoImage(image2)

          pass1_label2 = Label(screen1 , image=photo2)
          pass1_label2.pack(pady=10)
        '''
          
          microphone_button1 = Button(screen1,text = "Ask", command = Process_audio1)
          microphone_button1.pack(pady=10)
    
          settings_button1 = Button(screen1,text = "Edit Name", command = change_name_window1)
          settings_button1.pack(pady=10)
           
          info_button1= Button(screen1,text ="Info", command = info1)
          info_button1.pack(pady=10)
    
          screen1.mainloop()    
    main_screen1()


def gkHindi():
    name_file = open("Assistant_name", "r")
    name_assistant = name_file.read()
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    #print (voices[0].id)
    engine.setProperty('voice',voices[2].id)
    
    def speak3(text):
        engine.say(text)
        print("सहायक : "  +  text)
        engine.runAndWait() 
    
    def Translate3(Text):
        translate = Translator()
        result = translate.translate(Text,dest='hi')
        Text_res = result.text
        return Text_res
    
    
    def wishMe3():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak3("शुभ प्रभात!")
    
        elif hour>=12 and hour<18:
            speak3("शुभ दोपहर")   
    
        else:
            speak3("नमस्ते!")  
    
        speak3("मैं आपका सहायक हूं सर। कृपया मुझे बताएं कि मैं आपकी कैसे मदद कर सकता हूं")       
    
    def takecommand3():
        #It takes microphone input from the user and returns string output
        r = sr.Recognizer() 
        audio = '' 
    
        with sr.Microphone() as source: 
    
            print("सहायक सुन रहा है ...") 
            audio = r.listen(source, phrase_time_limit = 3) 
                    
        try: 
            print("सहायक पहचान रहा है ...")
            text = r.recognize_google(audio, language ='hi-in') 
            print('उपयोगकर्ता ने कहा: ' + ': ' + text)
            return text
    
    
        except:
    
            return "None"
    
    wishMe3()
    
    def Process_audio3():
    
        run = 1
        if __name__=='__main__':
            while run==1:
    
                
                statement = takecommand3().lower()
                results = ''
                run +=1
    
            # Logic for executing tasks based on statement
                
                if ('खोज करो' in statement )or ('सर्च करो' in statement):
                    speak3("आप क्या खोजना चाहते है ?")
                    search = takecommand3()
                    url = 'https://google.com/search?q=' + search
                    result = webbrowser.get().open(url)
                    speak3("जो मुझे मिला वह यहां है !!")
                    speak3(search)
    
                elif ('यूट्यूब' in statement )or ('यूट्यूब सर्च ' in statement):
                    speak3("आप क्या खोजना चाहते है ?")
                    search = takecommand3()
                    url = 'https://www.youtube.com/results?search_query=' + search
                    result = webbrowser.get().open(url)
                    speak3("जो मुझे मिला वह यहां है !!")
                    speak3(search)
    
    
                elif 'जगह सर्च करो' in statement or 'जगह खोज करो' in statement:
                    speak3("आप कौन सी जगह ढूंढ़ना चाहते हैं")
                    location = takecommand3()
                    url = 'https://www.google.nl/maps/place/' + location + '/?amp;'
                    result = webbrowser.get().open(url)
                    speak3("यहाँ स्थान है")
                    speak3(location)
            
                elif ('गूगल खोलो' in statement) or ('गूगल' in statement):
                    webbrowser.open("google.com")
    
                elif ('कॉलेज की  वेबसाइट खोलो' in statement) or ('कॉलेज वेबसाइट' in statement):
                    webbrowser.open("https://learner.vierp.in")
    
                elif ('क्लासरूम खोलो' in statement) or ('आभासी कक्षा' in statement):
                    webbrowser.open("https://classroom.volp.in/login")
    
                elif 'गाना बजाओ' in statement:
                    music_dir = 'D:\\songs'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))
    
                elif ('समय' in statement) or ('समय बताओ' in statement):
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak3(f"सर, समय हो गया है {strTime}")
            
                elif 'कोड खोलो' in statement:
                    codePath = "C:\\Users\\ganes\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
                else:
                    url = 'https://google.com/search?q=' + statement
                    result = webbrowser.get().open(url)
                    speak3("जो मुझे मिला वह यहां है !!")
                    speak3(statement)
    
    
    def change_name3():
    
      name_info = name.get()
    
      file=open("Assistant_name", "w")
    
      file.write(name_info)
    
      file.close()
    
      settings_screen3.destroy()
    
      screen3.destroy()
    
    
    def change_name_window3():
        
          global settings_screen3
          global name
    
    
          settings_screen3 = Toplevel(screen3)
          settings_screen3.title("Settings")
          settings_screen3.geometry("500x500")
          settings_screen3.iconbitmap('app_icon.ico')
    
          
          name = StringVar()
    
          current_label3 = Label(settings_screen3, text = "वर्तमान नाम: gk ")
          current_label3.pack()
    
          enter_label3 = Label(settings_screen3, text = "कृपया अपने वर्चुअल असिस्टेंट का नाम नीचे दर्ज करें.") 
          enter_label3.pack(pady=10)   
          
    
          Name_label3 = Label(settings_screen3, text = "नाम")
          Name_label3.pack(pady=10)
         
          name_entry3 = Entry(settings_screen3, textvariable = name)
          name_entry3.pack()
    
    
          change_name_button3 = Button(settings_screen3, text = "नाम जोड़ें", width = 10, height = 1, command = change_name3)
          change_name_button3.pack(pady=10)
    
    
    def info3():
    
      info_screen3 = Toplevel(screen3)
      info_screen3.title("जानकारी")
      info_screen3.iconbitmap('app_icon.ico')
    
      creator_label3 = Label(info_screen3,text = "गणेश द्वारा बनाया गया.")
      creator_label3.pack()
    
      Age_labe3 = Label(info_screen3, text= "मार्गदर्शक का नाम: प्रोफेसर अमोल भोसले ")
      Age_labe3.pack()
    
      for_label3 = Label(info_screen3, text = "एसडीपी परियोजना के लिए.")
      for_label3.pack()
    
    keyboard.add_hotkey("F4", Process_audio3)
    
    
    def main_screen3():
          global screen3
          screen3 = Tk()
          screen3.title(name_assistant)
          screen3.geometry("300x350")
          screen3.iconbitmap('app_icon.ico')
    
    
          name_label = Label(screen3 ,text = name_assistant,width = 300, bg = "black", fg="white", font = ("Calibri", 13))
          name_label.pack()
    
    
          '''microphone_photo3 = PhotoImage(file = "logo.png" ,height=100,width=100)
          microphone_button3 = Button(image=microphone_photo3, command = Process_audio3)
          microphone_button3.pack(pady=10)'''
          '''image1 = Image.open("logo.png")
          photo1 = ImageTk.PhotoImage(image1)

          pass1_label1 = Label(image=photo1)
          pass1_label1.pack(pady=10)
         '''
          
          microphone_button3 = Button(screen3,text = "पूछना", command = Process_audio3)
          microphone_button3.pack(pady=10)
    
          settings_button3 = Button(screen3,text = "नाम संपादित करें", command = change_name_window3)
          settings_button3.pack(pady=10)
           
          info_button3 = Button(screen3,text ="जानकारी", command = info3)
          info_button3.pack(pady=10)
    
          screen3.mainloop()
    main_screen3()

    
    

def main_screen2():

      screen2 = Tk()
      screen2.title("gk")
      screen2.geometry("300x350")
      screen2.iconbitmap('app_icon.ico')

      image = Image.open("logo.png")
      photo = ImageTk.PhotoImage(image)

      pass1_label = Label(image=photo)
      pass1_label.pack(pady=10)

      settings_button2 = Button(screen2 ,text = "English", command = gkEglish)
      settings_button2.pack(pady=10)

      settings_button2 = Button(screen2 ,text = "Hindi", command = gkHindi)
      settings_button2.pack(pady=10)
       
      
      screen2.mainloop()

main_screen2()
