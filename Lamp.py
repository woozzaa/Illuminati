import time

class Lamp:
	def __init__(self, lamp, canvas):
		self.lamp = lamp
		self.canvas = canvas
		# , fill='grey', width=1
		self.canvas.itemconfig(self.lamp, outline='green', fill='green', width='1')
		# self.changeOpacity()

	def changeBrightness(self, brightness):
		#mappa om brightness
		#diameter = 120px
		self.canvas.coords(self.lamp, 280,20,380,120)

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