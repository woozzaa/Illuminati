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

		self.lamp1 = Lamp( self.canvas.create_oval(70,70,90,90)   , self.canvas) #top left
		self.lamp2 = Lamp( self.canvas.create_oval(320,70,340,90) , self.canvas) #top right
		self.lamp3 = Lamp( self.canvas.create_oval(70,320,90,340) , self.canvas) #bottom left
		self.lamp4 = Lamp( self.canvas.create_oval(320,320,340,340), self.canvas) #bottom right
		self.lamp5 = Lamp( self.canvas.create_oval(190,190,210,210), self.canvas) #center


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
		print 'left fingers = ' + str(leftHandFingers) + ' right hand = ' + str(handHeight)

		if (handHeight !=  None) and (leftHandFingers != None):

			if leftHandFingers == 1   : self.lamp1.changeBrightness(handHeight)

			elif leftHandFingers == 2 : self.lamp2.changeBrightness(handHeight)

			elif leftHandFingers == 3 : self.lamp3.changeBrightness(handHeight)

			elif leftHandFingers == 4 : self.lamp4.changeBrightness(handHeight); print 'lamp 4'

			elif leftHandFingers == 5 : self.lamp5.changeBrightness(handHeight); print 'lamp 5'

			else : print 'no fingers stretched out'

		else:
			print 'no valid finger'

		self.after(100, self.changeLamp)
		

	def quitApp(self):
		# self.controller.remove_listener(self.listener)
		self.destroy() 	#destroys root window
		self.quit() 	#quits mainloop

