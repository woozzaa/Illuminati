# -*- coding: utf-8 -*-
import time

class Lamp:
	def __init__(self, lamp, canvas):
		self.lamp = lamp
		self.canvas = canvas
		# , fill='grey', width=1
		self.canvas.itemconfig(self.lamp, outline='green', fill='green', width='1')
		# self.changeOpacity()

	def changeBrightness(self, brightness):
		newCoords = self.getNewCoords(self.canvas.coords(self.lamp), brightness)
		self.canvas.coords(self.lamp, newCoords[0], newCoords[1], newCoords[2], newCoords[3])

	def getNewCoords(self, coords, brightness):
		#diam = 120px

		v1 = coords[0] #x0
		v2 = coords[1] #x1
		v3 = coords[2] #y0
		v4 = coords[3] #y1

		diff = (brightness * 120) / 2
		for x in range(0,3):
			v[x] = coords[x] + diff


	def turnOn(self):
		if not self.lit:
			self.lit = True

	def turnOff(self):
		if self.lit:
			self.lit = False

	def changeColor(self, color):
		self.color = color





	'''
	Functions pending implementation
	'''
	def itemConfig(self, attri, changeValue):
		#waiting function
		# self.canvas.itemconfig(self.lamp, command.mkarg(attri) = changeValue)
		pass

	def changeOpacity(self):
		#waiting function
		# self.canvas.itemconfig(self.lamp, '-alpha', '0.5')
		pass