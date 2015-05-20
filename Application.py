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

		self.canvas = Canvas(self, width=500, height=500, bg='#ededed')
		self.canvas.grid(row=1, column=0, sticky=W)

		self.scale1 = Scale(self, from_=0, to=100); self.scale1.grid(row=2, column=0, sticky=W)
		self.scale2 = Scale(self, from_=0, to=100); self.scale2.grid(row=2, column=0, sticky=W, padx=110)
		self.scale3 = Scale(self, from_=0, to=100); self.scale3.grid(row=2, column=0, sticky=W, padx=220)
		self.scale4 = Scale(self, from_=0, to=100); self.scale4.grid(row=2, column=0, sticky=W, padx=330)
		self.scale5 = Scale(self, from_=0, to=100); self.scale5.grid(row=2, column=0, sticky=W, padx=440)

		self.lamp1 = Lamp(self.scale1, self.canvas, self.canvas.create_polygon(90,90, 110,90, 110,110, 90,110)) #top left
		self.lamp2 = Lamp(self.scale2, self.canvas, self.canvas.create_polygon(400,90, 420,90, 420,110, 400,110)) #top right
		self.lamp3 = Lamp(self.scale3, self.canvas, self.canvas.create_polygon(90,400, 110,400, 110,420, 90,420)) #bottom left
		self.lamp4 = Lamp(self.scale4, self.canvas, self.canvas.create_polygon(400,400, 420,400, 420,420, 400,420)) #bottom right
		self.lamp5 = Lamp(self.scale5, self.canvas, self.canvas.create_polygon(240,240, 260,240, 260,260, 240,260)) #center

		self.allLamps = [self.lamp1, self.lamp2, self.lamp3, self.lamp4, self.lamp5]
		# print str(self.allLamps)

		# """ Wrap = tells what value will be displayed in the box """
		self.text = Text(self, width = 50, height = 2, wrap = WORD)
		self.text.grid(row = 0, column = 1, sticky = W)

		# """ creates quit-button """
		self.quitButton = Button (self, text = 'quit', command = self.quitApp)
		self.quitButton.grid(row = 1, column = 1, sticky = S)

	def reveal(self):
		""" Display message based on password typed in """
		#0.0 is position (row, column)

		textContent = 'handheight : %s \nextended fingers: %s' % (self.leap.listener.handHeight, self.leap.listener.rightHandFingers)
		self.text.delete(0.0, END)
		self.text.insert(1.0, textContent) 

		self.after(100, self.reveal)

	def changeLamp(self):
		
		handHeight 			= self.leap.listener.handHeight
		rightHandFingers 	= self.leap.listener.rightHandFingers
		rightHandRoll 		= self.leap.listener.rightHandRoll

		if (handHeight !=  None) and (rightHandFingers != None):

			if rightHandFingers == 1   : self.changeColor(self.lamp1); self.lamp1.changeLampAttributes(handHeight, rightHandRoll)

			elif rightHandFingers == 2 : self.changeColor(self.lamp2); self.lamp2.changeLampAttributes(handHeight, rightHandRoll)

			elif rightHandFingers == 3 : self.changeColor(self.lamp3); self.lamp3.changeLampAttributes(handHeight, rightHandRoll)

			elif rightHandFingers == 4 : self.changeColor(self.lamp4); self.lamp4.changeLampAttributes(handHeight, rightHandRoll)

			elif rightHandFingers == 5 : self.changeColor(self.lamp5); self.lamp5.changeLampAttributes(handHeight, rightHandRoll)

			else : print 'no fingers stretched out'

		else:
			print 'no valid finger'
			self.changeColor(None)

		self.after(100, self.changeLamp)

	def changeColor(self, activeLamp):
		for lamp in self.allLamps:
			if lamp is not activeLamp:
				lamp.changeColor('darkgray')
			else:
				lamp.changeColor('green')

	def quitApp(self):
		# self.controller.remove_listener(self.listener)
		self.destroy() 	#destroys root window
		self.quit() 	#quits mainloop

