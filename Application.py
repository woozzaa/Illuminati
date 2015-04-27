import sys, time, thread
# sys.path.insert(0, '../../lib')
# import Leap
# from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

from Tkinter 	import *
from Listener 	import *
from Lamp 		import *


class Application(Frame):
	""" Handles UI """

	#initiates UI
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
		self.leap = LeapMotion()

		self.reveal()

		#ends app on window close
		master.protocol('WM_DELETE_WINDOW', self.quitApp) 


	def create_widgets(self):

		self.instruction = Label(self, text='Lamps :')
		self.instruction.grid(row=0, column=0, columnspan=2, sticky=W)

		self.canvas = Canvas(self, width=400, height=400, bg='#ededed')
		self.canvas.grid(row=1, column=0)

		lamp1 = Lamp(self.canvas.create_oval(20,20,120,120, outline='darkgrey', fill='grey', width=1))
		# lamp2 = Lamp()
		# lamp3 = Lamp()
		# lamp4 = Lamp()
		# lamp5 = Lamp()

		# lamp1 = 
		# lamp2 = self.canvas.create_oval(280,20,380,120, outline='darkgrey', fill='grey', width=1)
		# lamp3 = self.canvas.create_oval(20,280,120,380, outline='darkgrey', fill='grey', width=1)
		# lamp4 = self.canvas.create_oval(280,280,380,380, outline='darkgrey', fill='grey', width=1)
		# lamp5 = self.canvas.create_oval(150,150,250,250, outline='darkgrey', fill='grey', width=1)



		# """ create button, text and entry widget """
		# self.instruction = Label(self, text = 'Status')
		
		# """ Sets row, column and span. Sticky = west, ie left side """
		# self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)

		# """ Wrap = tells what value will be displayed in the box """
		self.text = Text(self, width = 50, height = 2, wrap = WORD)
		self.text.grid(row = 0, column = 1, sticky = W)

		# """ creates quit-button """
		self.quitButton = Button (self, text = 'quit', command = self.quitApp)
		self.quitButton.grid(row = 1, column = 1, sticky = S)

	def reveal(self):
		""" Display message based on password typed in """
		#0.0 is position (row, column)

		textContent = 'handheight : %s \nextended fingers: %s' % (self.leap.listener.handHeight, self.leap.listener.leftHandFingers)
		self.text.delete(0.0, END)
		self.text.insert(1.0, textContent) 

		self.after(100, self.reveal)
		

	def quitApp(self):
		# self.controller.remove_listener(self.listener)
		self.destroy() 	#destroys root window
		self.quit() 	#quits mainloop

