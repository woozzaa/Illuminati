# -*- coding: utf-8 -*-
import sys, time, thread

from Tkinter 	import *
from Listener 	import *
from Lamp 		import *


class Application(Frame):
	""" Handles UI """

	'''
	Initiates the Application
	'''
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
		self.leap = LeapMotion()

		self.reveal()
		self.changeLamp()

		#ends app on window close
		master.protocol('WM_DELETE_WINDOW', self.quitApp) 


	'''
	Creates the GUI as well as creates all the Lamp objects
	'''
	def create_widgets(self):

		self.instruction = Label(self, text='Lamps :')
		self.instruction.grid(row=0, column=0, columnspan=2, sticky=W)

		# """ Wrap = tells what value will be displayed in the box """
		self.text = Text(self, width = 70, height = 2, wrap = WORD)
		self.text.grid(row = 0, column = 0, sticky = W)

		self.text2 = Text(self, width = 70, height = 2, wrap = WORD)
		self.text2.grid(row=1, column = 0, sticky = W)

		self.warningText = Text(self, width = 70, height = 2, wrap = WORD)
		self.warningText.grid(row = 2, column = 0, sticky = W)

		self.canvas = Canvas(self, width=500, height=500, bg='#ededed')
		self.canvas.grid(row=3, column=0, sticky=W)

		self.scale1 = Scale(self, from_=0, to=100); self.scale1.grid(row=4, column=0, sticky=W)
		self.scale2 = Scale(self, from_=0, to=100); self.scale2.grid(row=4, column=0, sticky=W, padx=110)
		self.scale3 = Scale(self, from_=0, to=100); self.scale3.grid(row=4, column=0, sticky=W, padx=220)
		self.scale4 = Scale(self, from_=0, to=100); self.scale4.grid(row=4, column=0, sticky=W, padx=330)
		self.scale5 = Scale(self, from_=0, to=100); self.scale5.grid(row=4, column=0, sticky=W, padx=440)

		self.lamp1 = Lamp(self.scale1, self.canvas, self.canvas.create_polygon(90,90, 110,90, 110,110, 90,110), self.warningText) #top left
		self.lamp2 = Lamp(self.scale2, self.canvas, self.canvas.create_polygon(400,90, 420,90, 420,110, 400,110), self.warningText) #top right
		self.lamp3 = Lamp(self.scale3, self.canvas, self.canvas.create_polygon(90,400, 110,400, 110,420, 90,420), self.warningText) #bottom left
		self.lamp4 = Lamp(self.scale4, self.canvas, self.canvas.create_polygon(400,400, 420,400, 420,420, 400,420), self.warningText) #bottom right
		self.lamp5 = Lamp(self.scale5, self.canvas, self.canvas.create_polygon(240,240, 260,240, 260,260, 240,260), self.warningText) #center

		self.allLamps = [self.lamp1, self.lamp2, self.lamp3, self.lamp4, self.lamp5]

		# """ creates quit-button """
		self.quitButton = Button (self, text = 'quit', command = self.quitApp)
		self.quitButton.grid(row = 1, column = 1, sticky = S)


	'''
	Updates informative text in GUI
	'''
	def reveal(self):
		""" Display message based on password typed in """
		#0.0 is position (row, column)
		rightPitch 	= self.leap.listener.rightHandPitch
		rightYaw 	= self.leap.listener.rightHandYaw
		rightRoll 	= self.leap.listener.rightHandRoll
		rightHandHeight 	= self.leap.listener.rightHandHeight
		rightFingers= self.leap.listener.rightHandFingers
		framerate 	= round(self.leap.listener.framerate, 4)

		if rightHandHeight != None : 
			handHeight 	= round(handHeight, 4)
			rightPitch 	= round(rightPitch, 3)
			rightYaw 	= round(rightYaw, 3)
			rightRoll 	= round(rightRoll, 3)

		textContent = 'handheight : %s extended fingers: %s\n pitch : %s yaw : %s roll : %s' % (rightHandHeight, rightFingers, rightPitch, rightYaw, rightRoll)
		dataContent = 'framerate : %s' % (framerate)

		self.text.delete(0.0, END)
		self.text2.delete(0.0, END)
		self.text.insert(1.0, textContent)
		self.text2.insert(1.0, dataContent)

		self.after(100, self.reveal)


	'''
	Function ran to switch or change attributes of a Lamp object
	'''
	def changeLamp(self):
		
		rightHandHeight 	= self.leap.listener.rightHandHeight
		rightHandFingers 	= self.leap.listener.rightHandFingers
		rightHandRoll 		= self.leap.listener.rightHandRoll
		
		leftHandLamp		= self.leap.listener.leftHandLampNumber
		leftHandHeight		= self.leap.listener.leftHandHeight
		leftHandRoll		= self.leap.listener.leftHandRoll
		leftHandFingers		= self.leap.listener.leftHandFingers

		if (rightHandHeight !=  None) and (rightHandFingers != None):
			print 'right hand visible'

			if rightHandFingers == 1   : self.changeColor(self.lamp1); self.lamp1.changeLampAttributes(rightHandHeight, rightHandRoll)
			elif rightHandFingers == 2 : self.changeColor(self.lamp2); self.lamp2.changeLampAttributes(rightHandHeight, rightHandRoll)
			elif rightHandFingers == 3 : self.changeColor(self.lamp3); self.lamp3.changeLampAttributes(rightHandHeight, rightHandRoll)
			elif rightHandFingers == 4 : self.changeColor(self.lamp4); self.lamp4.changeLampAttributes(rightHandHeight, rightHandRoll)
			elif rightHandFingers == 5 : self.changeColor(self.lamp5); self.lamp5.changeLampAttributes(rightHandHeight, rightHandRoll)
			else : pass #nothing to be done

		elif (leftHandHeight != None) and (leftHandFingers != None):
			print 'left hand visible'

			if leftHandLamp == 1   : self.changeColor(self.lamp1); self.lamp1.changeLampAttributes(leftHandHeight, leftHandRoll)
			elif leftHandLamp == 2 : self.changeColor(self.lamp2); self.lamp2.changeLampAttributes(leftHandHeight, leftHandRoll)
			elif leftHandLamp == 3 : self.changeColor(self.lamp3); self.lamp3.changeLampAttributes(leftHandHeight, leftHandRoll)
			elif leftHandLamp == 4 : self.changeColor(self.lamp4); self.lamp4.changeLampAttributes(leftHandHeight, leftHandRoll)
			elif leftHandLamp == 5 : self.changeColor(self.lamp5); self.lamp5.changeLampAttributes(leftHandHeight, leftHandRoll)
			else : pass #nothing to be done

		else:
			print 'no visible hands'
			self.changeColor(None)

		self.after(25, self.changeLamp)


	'''
	Changes color of the lamp representations in the GUI
	'''
	def changeColor(self, activeLamp):
		for lamp in self.allLamps:
			if lamp is not activeLamp:
				lamp.changeColor('darkgray')
			else:
				lamp.changeColor('green')


	'''
	Takes care of the Application on quit / window shutdown
	'''
	def quitApp(self):
		# self.controller.remove_listener(self.listener)
		self.destroy() 	#destroys root window
		self.quit() 	#quits mainloop

