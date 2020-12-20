from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os, sys
import win32print
import win32api


root = Tk()
root.title('Brandon - TextPad!')
#root.iconbitmap('c:/texteditor/textedit.jpeg')
root.geometry("1200x680")

# Set variable for open file name
global open_status_name
open_status_name = False

global selected
selected = False

# Create New file Function
def new_file():
	# Delete previous text
	my_text.delete('1.0', END)
	# Update status bars
	root.title('New File  -  TextPad!')
	status_bar.config(text="New File        ")

	global open_status_name
	open_status_name = False

# Open File Function

def open_file():
 	# Delete previous text
 	my_text.delete('1.0', END)

 	# Grab Filename
 	text_file = filedialog.askopenfilename(initialdir="C:/Users/Brandon/Documents", title="Open File", filetypes=(("Text Files", "*.txt"), (".HTML Files", "*.HTML"), ("Python Files", "*.py"), ("All Files", "*.*")))
 	
 	# Check to see if there is a file name
 	if text_file:
 		# Make Filename global so we can access it later
	 	global open_status_name
	 	open_status_name = text_file


 	# Update Status Bars
 	name = text_file
 	status_bar.config(text=f'{name}        ')
 	name = name.replace("C:/Users/Brandon/Documents", "")
 	root.title(f'{name}  -  TextPad!')
 	# Open the File
 	text_file = open(text_file, 'r')
 	stuff = text_file.read()
 	# Add file to textbox
 	my_text.insert(END, stuff)
 	# Close the Open File
 	text_file.close()


# Save As Files
def save_as_file():
	text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Users/Brandon/Documents", title="Save File", filetypes=(("Text Files", "*.txt"), (".HTML Files", "*.HTML"), ("Python Files", "*.py"), ("All Files", "*.*")))
	if text_file:
		# Update Status Bar
		name = text_file
		status_bar.config(text=f'Saved: {name}        ')
		name = name.replace("C:/Users/Brandon/Documents", "")
		root.title(f'{name}  -  TextPad!')

		# Save the File
		text_file = open(text_file, 'w')
		text_file.write(my_text.get(1.0, END))
		# Close the file
		text_file.close()

# Save file
def save_file():
	global open_status_name
	if open_status_name:
		# Save the File
		text_file = open(open_status_name, 'w')
		text_file.write(my_text.get(1.0, END))
		# Close the file
		text_file.close()

		status_bar.config(text=f'Saved: {open_status_name}        ')
	else:
		save_as_file()

# Cut text
def cut_text(e):
	global selected
	# Check to see if keyboard shortcut used
	if e:
		selected = root.clipboard.get()
	else:
		if my_text.selections.get():
			# Grab selected text from text box
			selected = my_text.selections.get()
			# Delete selected text from text box
			my_text.delete("sel.first", "sel.last")
			# Clear the clipboard and append
			root.clipboard_clear()
			root.clipboard_append(selected)

# Copy text
def copy_text(e):
	global selected
	# Check to see if we used keyboard shortcuts
	if e:
		selected = root.clipboard.get()

	if my_text.selection_get():
		# Grab selected text from text box
		selected = my_text.selections.get()
		# Clear the clipboard and append
		root.clipboard_clear()
		root.clipboard_append(selected)

# Paste text
def paste_text(e):
	global selected
	# Check to see if keyboard shortcut used
	if e:
		selected = root.clipboard.get()
	else:
		if selected:
			position = my_text.index(INSERT)
			my_text.insert(position, selected)

# Bold Text
def bold_it():
	# Create our font
	bold_font = font.Font(my_text, my_text.cget("font"))
	bold_font.configure(weight="bold")

	# Configure a tag
	my_text.tag_configure("bold", font=bold_font)

	# define current tags
	current_tags = my_text.tag_names("sel.first")
	# if statement to see if tag has been set
	if "bold" in current_tags:
		my_text.tag_remove("bold", "sel.first", "sel.last")
	else:
		my_text.tag_add("bold", "sel.first", "sel.last")
# Italics text
def italics_it():
	# Create our font
	italics_font = font.Font(my_text, my_text.cget("font"))
	italics_font.configure(slant="italic")

	# Configure a tag
	my_text.tag_configure("italic", font=italics_font)

	# define current tags
	current_tags = my_text.tag_names("sel.first")
	# if statement to see if tag has been set
	if "italic" in current_tags:
		my_text.tag_remove("italic", "sel.first", "sel.last")
	else:
		my_text.tag_add("italic", "sel.first", "sel.last")

# Change selected text color
def text_color():
	# Pick a color
	my_color = colorchooser.askcolor()[1]
	if my_color:
		# Create our font
		color_font = font.Font(my_text, my_text.cget("font"))

		# Configure a tag
		my_text.tag_configure("colored", font=color_font, foreground=my_color)

		# define current tags
		current_tags = my_text.tag_names("sel.first")
		# if statement to see if tag has been set
		if "colored" in current_tags:
			my_text.tag_remove("colored", "sel.first", "sel.last")
		else:
			my_text.tag_add("colored", "sel.first", "sel.last")

#Change Background color

def bg_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(bg=my_color)

# Change all text color

def all_text_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(fg=my_color)	

# Print File function

def print_file():
	# Check default printer name in status bar
	#printer_name = win32print.GetDefaultPrinter()
	#status_bar.config(text=printer_name)

	file_to_print = filedialog.askopenfilename(initialdir="C:/Users/Brandon/Documents", title="Open File", filetypes=(("Text Files", "*.txt"), (".HTML Files", "*.HTML"), ("Python Files", "*.py"), ("All Files", "*.*")))

	if file_to_print:
		win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)

# Select all text
def select_all(e):
	# Add sel tag to select all text
	my_text.tag_add('sel', '1.0', 'end')

# Clear all text
def clear_all(e):
	my_text.delete(1.0, END)

# Turn on Night Mode
def night_on():
	main_color = "#000000"
	secondary_color = "#373737"
	text_color = "green"
	root.config(bg=main_color)
	status_bar.config(bg=main_color, fg=text_color)
	my_text.config(bg=secondary_color)
	toolbar_frame.config(bg=main_color)
	# Toolbar button colors
	bold_button.config(bg=secondary_color)
	italics_button.config(bg=secondary_color)
	redo_button.config(bg=secondary_color)
	undo_button.config(bg=secondary_color)
	color_text_button.config(bg=secondary_color)
	# File menu colors
	file_menu.config(bg=main_color, fg=text_color)
	edit_menu.config(bg=main_color, fg=text_color)
	color_menu.config(bg=main_color, fg=text_color)
	options_menu.config(bg=main_color, fg=text_color)

# Turn Off Night Mode
def night_off():
	main_color = "SystemButtonFace"
	secondary_color = "SystemButtonFace"
	text_color = "Black"
	root.config(bg=main_color)
	status_bar.config(bg=main_color, fg=text_color)
	my_text.config(bg="white")
	toolbar_frame.config(bg=main_color)
	# Toolbar button colors
	bold_button.config(bg=secondary_color)
	italics_button.config(bg=secondary_color)
	redo_button.config(bg=secondary_color)
	undo_button.config(bg=secondary_color)
	color_text_button.config(bg=secondary_color)
	# File menu colors
	file_menu.config(bg=main_color, fg=text_color)
	edit_menu.config(bg=main_color, fg=text_color)
	color_menu.config(bg=main_color, fg=text_color)
	options_menu.config(bg=main_color, fg=text_color)



# Create a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)


# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)


#Create our Scrollbar from the Text Box

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Horizontal Scrollbar
hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

#Create Text Box

my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand= hor_scroll.set)
my_text.pack()


#Configure our Scrollbars

text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print File", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command = root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="Ctrl+Y")
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=lambda: select_all(True), accelerator="Ctrl+Shift+A")
edit_menu.add_command(label="Clear All", command=lambda: clear_all(True), accelerator="Ctrl+a")

# Add Color Menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Change Selected Text", command=text_color)
color_menu.add_command(label="All Text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)

# Add options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Night Mode On", command=night_on)
options_menu.add_command(label="Night Mode Off", command=night_off)


# Add Status Bar to Bottom of App
status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)


# Edit Bindings
root.bind('<Control-x>', cut_text)
root.bind('<Control-c>', copy_text)
root.bind('<Control-v>', paste_text)
# Select Bindings
root.bind('<Control-A>', select_all)
root.bind('<Control-a>', clear_all)


# Create Buttons

# Bold Buttons
bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx=5)
italics_button = Button(toolbar_frame, text="Italics", command=italics_it)
italics_button.grid(row=0, column=1, padx=5)

# Undo/Redo Buttons
undo_button = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5)
redo_button = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5)

# Text Color
color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=4, padx=5)

root.mainloop()