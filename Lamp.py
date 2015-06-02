import time

'''
Initiates lamp object
'''
class Lamp:
	def __init__(self, scale, canvas, lamp, warningTextField):
		self.scale 	= scale
		self.lamp 	= lamp
		self.canvas = canvas
		self.roll 	= None
		self.startVar = False
		self.warningTextField = warningTextField
		
		self.originalCoords = self.canvas.coords(self.lamp)
		self.scale.config(orient='horizontal', sliderlength=10)
		self.scale.set(50)
		self.changeColor('gray')



	'''
	changes lamp attributes, such as brightness and angle
	'''
	def changeLampAttributes(self, brightness, roll):
		brightness = int(brightness*100)

		if self.startVar is False:
			self.changeBrightness(brightness)
			self.changeDirection(roll)
			self.startVar = True

		print 'brightness = ' + str(brightness)
		scaleVal = self.scale.get()
		if (brightness > (scaleVal - 5) and brightness < (scaleVal + 5)):
			if (roll > (self.roll - 0.5) and roll < (self.roll + 0.5)):
				self.changeBrightness(brightness)
				self.changeDirection(roll)
			else : print 'hand in height range, not in roll range'
		else : print 'hand not in height range'
		

		
	# THIS FUNCTION IS NOT WORKING; THEREFORE INACTIVE
	# def changeWarningtext(self, warningText):
	# 	warningText = 'Message : %s' % (warningText) 
	# 	self.warningTextField.delete(0.0, END)
	# 	self.warningTextField.insert(1.0, warningText)



	'''
	Changes the brightness. 
	Value depends on scale
	'''
	def changeBrightness(self, brightness):
		self.scale.set(brightness)
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
		self.roll = roll

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