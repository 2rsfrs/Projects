from tkinter import *
from tkinter import filedialog
import os

# browses files and deletes all empty directories
def browseFiles():
	foldername = os.path.abspath(filedialog.askdirectory())
	label_file_explorer.configure(text="Folder Selected: "+ foldername)
	os.chdir(foldername)
	for item in os.listdir(os.getcwd()):
		if os.path.isdir(item):
			if not os.listdir(item):
				print(os.path.join(os.getcwd(),item))
				os.removedirs(os.path.join(os.getcwd(),item))	


# creates window
window = Tk()

window.title('File Explorer')

# modifies size of the window
window.geometry("700x300")

# modifies background color of the window
window.config(background = "white")

# inserts title for program
label_file_explorer = Label(window,
			    text = "Empty Folder Deleter",
			    width = 100, height = 4,
			    fg = "green")

# button to browse directories and clear empty folders
button_explore = Button(window,
			text = "Browse and Delete Empty Folders",
			fg = "green",
			command = browseFiles)

# button to exit program 
button_exit = Button(window,
		     text = "Exit",
		     fg = "green",
		     command = window.destroy)

# aligning buttons and text
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row =2)

button_exit.grid(column = 1, row = 3)

window.mainloop()
