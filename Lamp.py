import time

class Lamp:
	def __init__(self, scale, canvas, lamp):
		self.scale 	= scale
		self.lamp 	= lamp
		self.canvas = canvas
		
		self.originalCoords = self.canvas.coords(self.lamp)
		self.scale.config(orient='horizontal', sliderlength=10)
		self.scale.set(50)

	def changeBrightness(self, brightness):
		val = round(brightness*100, 0)
		print 'val = ' + str(val)
		self.scale.set(int(brightness*100))
		# self.canvas.itemconfig(self.lamp, fill='green')
		self.changeIllumination()

	def changeIllumination(self):
		v = []
		scaleVal = self.scale.get()
		
		print 'scaleval = ' + str(scaleVal)
		
		for x in range(0,4):
			if x == 0 or x == 1:
				v.append(self.originalCoords[x] - scaleVal)
			else:
				v.append(self.originalCoords[x] + scaleVal)

		self.canvas.coords(self.lamp, tuple(v))

	def changeColor(self, color):
		self.canvas.itemconfig(self.lamp, fill=color)
