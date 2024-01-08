from tkinter import *

# widgets = GUI elements: buttoms, textboxes, labels, images
# windows = serves as a contaianer to hold or contian these widgets

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Frank Code first GUI program")

icon = PhotoImage(file='Frank.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop() #place window on computer screen, listen for events