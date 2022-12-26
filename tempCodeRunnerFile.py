


def gkEglish():
    
    name_file = open("Assistant_name", "r")
    name_assistant = name_file.read()
    
    engine = pyttsx3.init('sapi5')  
    voices = engine.getProperty('voices')  