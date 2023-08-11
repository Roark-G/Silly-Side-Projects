import keyboard
import random
from meowgenerator import accessRandMeow
import tkinter as tk
from PIL import Image, ImageTk

key2Listen4 = 'page down'

colorPallete = {'font':'#FFFFFF','bg':'#2D033B','accent':"#810CA8",'extra':'#C147E9'}

#3 possible = None: nothing happening, active: it's actively listening, inactive: waiting for user to save
recordingState = None

# Create the Tkinter window & configure
window = tk.Tk()
window.geometry("275x200")
window.configure(bg=colorPallete['bg'])
window.title("Meow Keyboard Settings")

#helpful
def destroyColRow(column, row):
    widget = window.grid_slaves(row=row, column=column)
    if widget:
        widget[0].destroy()
    
#occurs every key press
def onKeyPress(event):
    global recordedKey
    global recordingState
    
    #summoning of meow engine
    if event.name == key2Listen4:
        keyboard.write(accessRandMeow()+' ')

    #recording
    elif recordingState == 'active':

        recordingState = 'inactive'
        recordedKey = event.name

        destroyColRow(0,4)
        saveLabel = tk.Label(window, text=f"Are you sure you'd like to save {event.name}?", 
                 font=('Arial', 12, 'bold'),
                 foreground=colorPallete['font'],
                 background=colorPallete['bg'],
                 padx=10, pady=5)
        saveLabel.grid(column=0,row=4)

def doRecordingStuff():
    global recordingState
    
    if recordingState is None or recordingState == 'active':

        recordingState = 'active'

        destroyColRow(0,4)
        recordingLabel = tk.Label(window, text="Recording...", 
                 font=('Arial', 12, 'bold'),
                 foreground=colorPallete['font'],
                 background=colorPallete['bg'],
                 padx=10, pady=5)
        recordingLabel.grid(column=0,row=4)

def saveMeowKey():
    global recordingState

    if recordingState == 'inactive':
        global key2Listen4
        global recordedKey
        
        recordingState = None
        key2Listen4 = recordedKey

        destroyColRow(0,4)
        savedLabel = tk.Label(window, text="Saved!", 
                 font=('Arial', 12, 'bold'),
                 foreground=colorPallete['font'],
                 background=colorPallete['bg'],
                 padx=10, pady=5)
        savedLabel.grid(column=0,row=4)
        updateMeowBoardKeyDisplay()

# Display current key for meowBoard
def updateMeowBoardKeyDisplay():
    destroyColRow(0,0)
    label = tk.Label(window, text=f"Current Meowing key: {key2Listen4}", 
                    font=('Arial', 12, 'bold'),
                    foreground=colorPallete['font'],
                    background=colorPallete['accent'], 
                    padx=10, pady=5)
    label.grid(column=0,row=0)

updateMeowBoardKeyDisplay()

button = tk.Button(window, text="Record", 
                   command=doRecordingStuff, 
                   font=('Arial', 12, 'bold'), 
                   foreground=colorPallete['font'], 
                   background=colorPallete['extra'], 
                   padx=10, pady=5)
button.grid(column=0,row=1)

button1 = tk.Button(window, text="Save", 
                    command=saveMeowKey, 
                    font=('Arial', 12, 'bold'), 
                    foreground=colorPallete['font'], 
                    background=colorPallete['extra'], 
                    padx=10, pady=5)
button1.grid(column=0,row=2)

button1 = tk.Label(window, text="Tiramisukat on tumblr :3",  
                    font=('Arial', 10, ''), 
                    foreground=colorPallete['font'], 
                    background=colorPallete['bg'], 
                    padx=10, pady=5)
button1.grid(column=0,row=5)

keyboard.on_press(onKeyPress)

# Start the Tkinter event loop
window.mainloop()

