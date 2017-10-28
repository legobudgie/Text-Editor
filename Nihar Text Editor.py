from tkinter import *
import tkinter.filedialog

class TextEditor:

    @staticmethod
    def quit_app(event=None):
        root.quit()

    def open_file(self, event=None):

        txt_file = tkinter.filedialog.askopenfilename(parent=root,
                    initialdir='C:\\Users\\Nihar Gaming\\Desktop\\Coding Stuff\\Saved Python Text Editor Files')
        if txt_file:
            self.text_area.delete(1.0, END)

            with open(txt_file) as _file:
                self.text_area.insert(1.0, _file.read())

                root.update_idletasks()

    def save_file(self, event=None):
        file = tkinter.filedialog.asksaveasfile(mode='w')

        if file != None:
            data = self.text_area.get(1.0, END + '-1c')
            file.write(data)
            file.close()

    def __init__(self, root):
 
        self.text_to_write = ""
 
        # Define title for the app
        root.title("Nihar's Text Editor")
 
        # Defines the width and height of the window
        root.geometry("600x500")
 
        frame = Frame(root, width=600, height=500)
 
        # Create the scrollbar
        scrollbar = Scrollbar(frame)
 
        # yscrollcommand connects the scroll bar to the text
        # area
        self.text_area = Text(frame, width=600, height=550,
                        yscrollcommand=scrollbar.set,
                        padx=10, pady=10)
 
        # Call yview when the scrollbar is moved
        scrollbar.config(command=self.text_area.yview)
 
        # Put scroll bar on the right and fill in the Y direction
        scrollbar.pack(side="right", fill="y")
 
        # Pack on the left and fill available space
        self.text_area.pack(side="left", fill="both", expand=False)
        frame.pack()
 
        # Create the menu object
        the_menu = Menu(root)
 
        # Create a pull down menu that can't be removed
        file_menu = Menu(the_menu, tearoff=0)
 
        # Add items to the menu that show when clicked
        # compound allows you to add an image
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
 
        # Add a horizontal bar to group similar commands
        file_menu.add_separator()
 
        # Call for the function to execute when clicked
        file_menu.add_command(label="Quit", command=self.quit_app)
 
        # Add the pull down menu to the menu bar
        the_menu.add_cascade(label="File", menu=file_menu)
 
        # Display the menu bar
        root.config(menu=the_menu)

root = Tk()

text_editor = TextEditor(root)

root.mainloop()
            

        
            
        
    
