# -*- coding: utf-8 -*-
import time

class Lamp:
	def __init__(self, lamp, canvas, outline):
		self.lamp 		= lamp
		self.canvas 	= canvas
		self.outlineOval = outline
		self.canvas.itemconfig(self.lamp, outline='green', fill='green', width='1')
		self.originalCoords = self.canvas.coords(self.lamp)

	def changeBrightness(self, brightness):
		newCoords = self.getNewCoords(self.lamp, brightness)
		self.canvas.coords(self.lamp, newCoords)

	def getNewCoords(self, lamp, brightness):

		originalCoords = self.canvas.coords(self.lamp)

		diff = round((brightness * 10), 0)
		if diff <= 5 : diff = -(5-diff) # range 0 -> -5
		elif diff > 5: diff = diff - 5  # range 0 -> 5
		
		coordinates = self.calculateCoords(diff, self.canvas.coords(self.lamp))

		return tuple(coordinates)


	def calculateCoords(self, diff, coords):
		v = []
		for x in range(0,4):
			if x == 0 or x == 1 :
				if (coords[x]-diff) > self.originalCoords[x]:
					v.append(int(coords[x] - diff))
				else:
					v.append(int(coords[x] - (self.originalCoords[x]-coords[x])))
			else :
				if (coords[x]+diff) < self.originalCoords[x]:
					v.append(int(coords[x] + diff))
				else:
					v.append(int(coords[x] + (self.originalCoords[x]-coords[x])))
		
		coordsDiffAfter = v[3] - v[1]
		print 'coordsDiffAfter = ' + str(coordsDiffAfter)
		
		
		return tuple(v)

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