
class Lamp:
	def __init__(self, lamp):
		self.lamp 			= lamp
		self.illumination 	= 0.5 #values from 0 to 1
		self.lit 			= True

	def changeBrightness(self, brightness):
		self.illumination = brightness

	def turnOn(self):
		if not self.lit:
			self.lit = True

	def turnOff(self):
		if self.lit:
			self.lit = False

	def changeColor(self, color):
		self.color = color
