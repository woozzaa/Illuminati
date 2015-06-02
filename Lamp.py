import time

'''
Inits lamp object
'''
class Lamp:
	def __init__(self, scale, canvas, lamp):
		self.scale 	= scale
		self.lamp 	= lamp
		self.canvas = canvas
		
		self.originalCoords = self.canvas.coords(self.lamp)
		self.scale.config(orient='horizontal', sliderlength=10)
		self.scale.set(50)
		self.changeColor('gray')


	'''
	changes lamp attributes, such as brightness and angle
	'''
	def changeLampAttributes(self, brightness, roll):
		self.changeBrightness(brightness)
		self.changeDirection(roll)



	'''
	Changes the brightness. 
	Value depends on scale
	'''
	def changeBrightness(self, brightness):
		val = round(brightness*50, 0)
		self.scale.set(int(brightness*100))
		self.changeIllumination()



	'''
	Calculates and sets new size 
	to the rectangles
	'''
	def changeIllumination(self):
		v = []
		scaleVal = self.scale.get() * 0.8
		sizeConstant = 0.25

		# print 'scaleVal = ' + str(scaleVal)
		
		for x in range(0,8):
			if x == 0 or x == 6:   v.append(self.originalCoords[x] - (scaleVal * sizeConstant))
			elif x == 1 or x == 3: v.append(self.originalCoords[x] - scaleVal)
			elif x == 4 or x == 2: v.append(self.originalCoords[x] + (scaleVal * sizeConstant))
			elif x == 7 or x == 5: v.append(self.originalCoords[x] + scaleVal)

		self.canvas.coords(self.lamp, tuple(v))



	'''
	changes color of active lamp
	'''
	def changeColor(self, color):
		self.canvas.itemconfig(self.lamp, fill=color)



	'''
	Changes direction of the lamp
	'''
	def changeDirection(self, roll):
		v = []
		
		if roll > 1 : roll = 1
		if roll < -1 : roll = -1

		roll = -round(roll*50, 0)
		activeCoords = self.canvas.coords(self.lamp)

		# print 'roll = ' + str(roll)

		if roll > 0.2:
			for x in range(0,8):
				if x == 0 or x == 2 : v.append(activeCoords[x] + roll)
				elif x == 6 or x == 4 : v.append(activeCoords[x] - roll)
				elif x == 5 or x == 3 : v.append(activeCoords[x] + roll*0.5)
				else : v.append(activeCoords[x] - roll*0.5)
		
		elif roll < -0.2:
			for x in range(0,8):
				if x == 0 or x == 2 : v.append(activeCoords[x] + roll)
				elif x == 6 or x == 4 : v.append(activeCoords[x] - roll)
				elif x == 5 or x == 3 : v.append(activeCoords[x] + roll*0.5)
				else : v.append(activeCoords[x] - roll*0.5)
		
		else : v = activeCoords

		self.canvas.coords(self.lamp, tuple(v))



# For the old, circular lamp GUI
# 	if x == 0 or x == 1:
# 		v.append(self.originalCoords[x] - scaleVal)
# 	else:
# 		v.append(self.originalCoords[x] + scaleVal)


