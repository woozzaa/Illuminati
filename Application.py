# -*- coding: utf-8 -*-
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
		self.changeLamp()

		#ends app on window close
		master.protocol('WM_DELETE_WINDOW', self.quitApp) 


	def create_widgets(self):

		self.instruction = Label(self, text='Lamps :')
		self.instruction.grid(row=0, column=0, columnspan=2, sticky=W)

		self.canvas = Canvas(self, width=400, height=400, bg='#ededed')
		self.canvas.grid(row=1, column=0)

		self.lamp1 = Lamp(self.canvas.create_oval(20,20,140,140)  , self.canvas) #top left
		self.lamp2 = Lamp(self.canvas.create_oval(270,20,390,140) , self.canvas) #top right
		self.lamp3 = Lamp(self.canvas.create_oval(20,270,140,390) , self.canvas) #bottom left
		self.lamp4 = Lamp(self.canvas.create_oval(270,270,390,390), self.canvas) #bottom right
		self.lamp5 = Lamp(self.canvas.create_oval(140,140,260,260), self.canvas) #center


		# """ create button, text and entry widget """
		# self.instruction = Label(self, text = 'Status')
		
		# """ Sets row, column and span. Sticky = west, ie left side """
		# self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)
		
		self.changeButton = Button(self, text = 'change', command = self.lamp1.changeOpacity)
		self.changeButton.grid(row=1, column=1, sticky=W)

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

	def changeLamp(self):
		
		handHeight 		= self.leap.listener.handHeight
		leftHandFingers = self.leap.listener.leftHandFingers

		if leftHandFingers == 1   : self.lamp1.changeBrightness(handHeight)

		elif leftHandFingers == 2 : self.lamp2.changeBrightness(handHeight)

		elif leftHandFingers == 3 : self.lamp3.changeBrightness(handHeight)

		elif leftHandFingers == 4 : self.lamp4.changeBrightness(handHeight)

		elif leftHandFingers == 5 : self.lamp5.changeBrightness(handHeight)

		else:
			pass

		self.after(100, self.changeLamp)
		

	def quitApp(self):
		# self.controller.remove_listener(self.listener)
		self.destroy() 	#destroys root window
		self.quit() 	#quits mainloop

