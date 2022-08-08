import pyautogui
import os

FASTER=150
SLOWER=18

class gui_control:
    def __init__(self):
        pyautogui.PAUSE = 1
        pyautogui.FAILSAFE = True
        pyautogui.size()

    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer UP from it's current position, until user says STOP.
    #------------------------------------------------------------------------------------
    def mouse_up(self,recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(0, -1*SLOWER, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse up :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(0, -1*FASTER, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(0, -1*SLOWER, duration=0.25)
            
    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer DOWN from it's current position, until user says STOP.
    #------------------------------------------------------------------------------------        
    def mouse_down(self,recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(0, 1*SLOWER, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse down :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(0, 1*FASTER, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(0, 1*SLOWER, duration=0.25)

    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer LEFTWARD from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------ 
    def mouse_left(self,recognizer, src):
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(-1*SLOWER, 0, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse left :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(-1*FASTER, 0, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(-1*SLOWER, 0, duration=0.25)

    #------------------------------------------------------------------------------------
    # Moves the Mouse pointer RIGHTWARD from it's current position, 
    # until 'STOP' keyword is heard. 
    #------------------------------------------------------------------------------------ 
    def mouse_right(self,recognizer, src):
        pyautogui.moveRel(100, 0, duration=0.25)
        while True:
            speech_to_txt = ""
            pyautogui.moveRel(1*SLOWER, 0, duration=0.25)
            try:
                audio = recognizer.listen(src)
                speech_to_txt = recognizer.recognize_google(audio).lower()
            except:
                pass
            print("Inside mouse right :" + speech_to_txt)
            if speech_to_txt == "stop":
                break
            elif speech_to_txt == "faster":
                pyautogui.moveRel(1*FASTER, 0, duration=0.25)
            elif speech_to_txt == "slower":
                pyautogui.moveRel(1*SLOWER, 0, duration=0.25)
    
    #------------------------------------------------------------------------------------
    # CLICKS the LEFT Mouse button it's current position 
    #------------------------------------------------------------------------------------    
    def left_click(self):
        pyautogui.click()
 
    #------------------------------------------------------------------------------------
    # CLICKS the RIGHT Mouse button it's current position 
    #------------------------------------------------------------------------------------  
    def right_click(self):
        print("Right Clicking")
        pyautogui.click(button='right', clicks=2, interval=0.25)
 
    #------------------------------------------------------------------------------------
    # DOUBLE CLICKS the LEFT Mouse button it's current position 
    #------------------------------------------------------------------------------------  
    def double_click(self):
        print("Double Clicking")
        pyautogui.click(button='left', clicks=2, interval=0.25)

    #------------------------------------------------------------------------------------
    # CLICKS the CHROME icon (if present in taskbar)
    # A screenshot needs to be captured and stored in 'screenshots' folder, before the 
    # program is run.
    #------------------------------------------------------------------------------------       
    def open_chrome(self):
        print("Opening Chrome")
        try:
            d = '/Applications'
            apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
            app = 'Google Chrome'
            os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))
        except Exception as ex:
            print("Exception occurred while opening chrome: "+ str(ex))

    def open_spotify(self):
        print("Opening Spotify")
        try:
            d = '/Applications'
            apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
            app = 'Spotify'
            os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))
        except Exception as ex:
            print("Exception occurred while opening Spotify: "+ str(ex))

    #------------------------------------------------------------------------------------
    # Simulates the SPACE key press
    #------------------------------------------------------------------------------------ 
    def play_pause(self):
        print("Pressing SPACE Key")
        pyautogui.typewrite(['space'])

