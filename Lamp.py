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
		# x0 = int(newCoords[0])
		# x1 = int(newCoords[1])
		# y0 = int(newCoords[2])
		# y1 = int(newCoords[3])
		# self.canvas.coords(self.lamp, newCoords[0], newCoords[1], newCoords[2], newCoords[3])
		# self.canvas.coords(self.lamp, x0, x1, y0, y1)

		self.canvas.coords(self.lamp, newCoords)

	def getNewCoords(self, coords, brightness):
		#diam = 120px

		# x0 = coords[0]
		# x1 = coords[1]
		# y0 = coords[2]
		# y1 = coords[3]

		diff = int((brightness * 120) / 2)
		'''
			UNTRIED CHANGES! 
			Done to perhaps solve the bug that only 
			makes the circle grow, and instead decrease
			in size when brightness is < 0.5
		'''
		if diff <= 0.5:
			diff = -diff
		# # print 'diff = ' + str(diff)
		v = []
		for x in range(0,4):
			if x == 0 or x == 1 :
				v.append(int(coords[x] - diff)) #bug here. Change size logix
			else :
				v.append(int(coords[x] + diff))


		print 'v = ' + str(tuple(v))
		return tuple(v)
		
		# tempstring =  ','.join(str(round(k, 2)) for k in v)



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