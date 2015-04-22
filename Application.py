import sys, time, thread
# sys.path.insert(0, '../../lib')
# import Leap
# from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

from Tkinter import *
from Listener import *


class Application(Frame):
	""" Handles UI """

	#initiates UI
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
		self.leap = LeapMotion()

		#creates Leap Motion Listener
		# self.listener = LeapListener()
		# self.controller = Leap.Controller()
		# self.controller.add_listener(self.listener)
		
		#starts listener (change name?)
		self.reveal()

		#ends app on close windows
		master.protocol('WM_DELETE_WINDOW', self.quitApp) 


	def create_widgets(self):
		""" create button, text and entry widget """
		self.instruction = Label(self, text = 'Status')
		
		""" Sets row, column and span. Sticky = west, ie left side """
		self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)

		""" Wrap = tells what value will be displayed in the box """
		self.text = Text(self, width = 35, height = 8, wrap = WORD)
		self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W)
		self.text.insert(0.0, 'tjoho')

		""" creates quit-button """
		self.quitButton = Button (self, text = 'quit', command = self.quitApp)
		self.quitButton.grid(row = 4, column = 0, sticky = W)

	def reveal(self):
		""" Display message based on password typed in """
		#0.0 is position (row, column)

		textContent = 'gesture type : %s\nhand : %s \nextended fingers: %s \nfingers pointing : %s\n' % (self.leap.listener.gestureType, self.leap.listener.handName, self.leap.listener.noOfFingers, self.leap.listener.fingerNames)
		self.text.delete(0.0, END)
		self.text.insert(1.0, textContent) 

		self.after(100, self.reveal)
		

	def quitApp(self):
		# self.controller.remove_listener(self.listener)
		self.destroy() 	#destroys root window
		self.quit() 	#quits mainloop

