#########################################
#
#         85pt - Add a cancel button
#
#########################################

from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myParent = parent
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="OK", background= "green")
		self.button1.pack(side=LEFT)	
		self.button1.bind("<Button-1>", self.button1Click)
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Cancel", background= "red")
		self.button2.pack(side=RIGHT)	
		self.button2.bind("<Button-2>", self.button2Click) 
	def button1Click(self, event): 
		if self.button1["background"] == "green":
			self.button1["background"] = "yellow"
		else:
			self.button1["background"] = "green"
	def button2Click(self, event): 
		if self.button2["background"] == "red": 
			self.button2["background"] = "blue"
		else:
			self.button2["background"] = "red"
root = Tk()
myapp = MyApp(root)
root.mainloop()