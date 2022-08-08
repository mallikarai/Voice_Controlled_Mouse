import speech_recognition
import gui_auto
import os
# The gui instance will be used to call GUI functions defined by us in 'gui_auto.py'
gui = gui_auto.gui_control()
recognizer = speech_recognition.Recognizer()
print("\n\nThreshold Value Before calibration:" + str(recognizer.energy_threshold))

with speech_recognition.Microphone() as src:
    
    while True:
        try:
            print("Enter one of the following commands: MOVE UP | MOVE DOWN | MOVE LEFT | MOVE RIGHT | OPEN CHROME | OPEN SPOTIFY | CLICK |RIGHT CLICK | DOUBLE CLICK | PLAY | STOP PLAYING")
            audio = recognizer.adjust_for_ambient_noise(src)
            print("\n\nThreshold Value After calibration:" + str(recognizer.energy_threshold))
            print("\nPlease speak:")
            audio = recognizer.listen(src)
            speech_to_txt = recognizer.recognize_google(audio).lower()
        except Exception as ex:
            print("Sorry. Could not understand Please try again.\n\n")
            continue
            
        print("I heard : " + speech_to_txt)
        
        #---------------------------------------------------------------------
        # The following if-else block is for the commands I have chosen and 
        # call their respective GUI action
        #---------------------------------------------------------------------
        if (speech_to_txt == "quit program") or (speech_to_txt == "exit program"):
            break
        elif speech_to_txt == "mouse up" or speech_to_txt == "move up":
            gui.mouse_up(recognizer, src)
        elif speech_to_txt == "mouse down" or speech_to_txt == "move down":
            gui.mouse_down(recognizer, src)
        elif speech_to_txt == "mouse left" or speech_to_txt == "move left":
            gui.mouse_left(recognizer, src)
        elif speech_to_txt == "mouse right" or speech_to_txt == "move right":
            gui.mouse_right(recognizer, src)
        elif speech_to_txt == "left click" or speech_to_txt == "click" or speech_to_txt == "left-click":
            gui.left_click()
        elif speech_to_txt == "right click" or speech_to_txt == "right-click":
            gui.right_click()
        elif speech_to_txt == "double click" or speech_to_txt == "double-click":
            gui.double_click()
        elif speech_to_txt == "open chrome":
            gui.open_chrome()
        elif speech_to_txt == "open spotify":
            gui.open_spotify()
        elif speech_to_txt == "play" or speech_to_txt=="stop playing":
            gui.play_pause()


