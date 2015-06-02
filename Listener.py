# -*- coding: utf-8 -*-
import sys, time, thread
sys.path.insert(0, '../../lib')
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class LeapListener(Leap.Listener):
	""" Listener for data from leapmotion """

	def setup(self, parent):
		#General variables
		self.parent 			= parent
		self.fingerNameList 	= ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
		self.gestureType 		= 'no status available'
		self.handName 			= 'no hand'
		self.fingerNames 		= 'no fingers'
		self.thumbExtended 		= 'no'
		self.framerate 			= 0

		#Right hand variables
		self.rightHandHeight 	= None
		self.rightHandFingers 	= None
		self.rightHandRoll		= None
		self.rightHandPitch		= None
		self.rightHandYaw		= None

		#Left hand variables
		self.leftHandLampNumber = 1
		self.leftHandHeight 	= None
		self.leftHandRoll		= None
		self.leftHandFingers 	= None
		self.lampChangeBool 	= True

	#when connecting Leap Motion
	def on_connect(self, controller):
		self.gestureType = 'connected'
		'''
		Following is for allowing and using gestures 
		'''
		# controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
		# controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
		# controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
		# controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)	
		
	#runs when frames available
	def on_frame(self, controller):

		frame = controller.frame()
		self.framerate = frame.current_frames_per_second

		if frame.hands.is_empty:
			self.handName 		= 'No hands'
			self.gestureType 	= 'No gesture'
			self.fingerNames 	= 'No fingers'

			#right hand variables
			self.rightHandHeight 	= None
			self.rightHandFingers 	= None
			self.rightHandRoll		= None
			self.rightHandYaw		= None
			self.rightHandPitch		= None

			#left hand variables
			self.leftHandLampNumber = 1
			self.leftHandHeight 	= None
			self.leftHandRoll		= None

		else:
			for hand in frame.hands:
				if hand.is_valid:
					"""
					Right hand = illumination controller
					"""
					if hand.is_right:
						self.rightHandHeight 	= self.normalizeHeight(hand.palm_position.y)
						self.rightHandFingers 	= len(hand.fingers.extended())
						self.rightHandRoll 		= hand.palm_normal.roll
						self.rightHandYaw 		= hand.direction.yaw
						self.rightHandPitch 	= hand.direction.pitch

						if self.rightHandFingers < 1:
							self.rightHandFingers = None
						
					'''
					Left hand = lamp controller
					'''
					if hand.is_left:
						self.leftHandFingers 	= len(hand.fingers.extended())
						self.leftHandHeight 	= self.normalizeHeight(hand.palm_position.y)
						self.leftHandRoll 		= hand.palm_normal.roll

						'''
						Built-in gesture types changes lamp
						'''
						# for gesture in frame.gestures():
						# 	if gesture.type is Leap.Gesture.TYPE_SCREEN_TAP:
						# 		self.leftHandLampNumber += 1
						# 		if self.leftHandLampNumber == 6 : self.leftHandLampNumber = 1
						# 		print 'number = ' + str(self.leftHandLampNumber)

						'''
						Closing hand changes lamp
						'''
						if self.leftHandFingers < 1:
							if self.lampChangeBool:
								self.leftHandLampNumber += 1
								if self.leftHandLampNumber == 6 : self.leftHandLampNumber = 1
								# print 'number = ' + str(self.leftHandLampNumber)
								self.lampChangeBool = False
							self.leftHandFingers = None
						else:
							self.lampChangeBool = True



	def normalizeHeight(self, height):	#highest = 450, lowest = 30
		normalizeFactor = 300
		normalizedVector = (height-50) / normalizeFactor

		if height > 400 or normalizedVector > 1:
			normalizedVector = 1
		elif height < 50 or normalizedVector < 0:
			normalizedVector = 0
		return normalizedVector



	#runs on application shutdown
	def on_exit(self, controller):
		self.controller.remove_listener(self.listener)
		print 'exited'





'''
Initiates LeapMotion listener and sets up a controller
'''
class LeapMotion:
	def __init__(self):
		self.listener = LeapListener()
		self.listener.setup(self)
		self.controller = Leap.Controller()
		self.controller.add_listener(self.listener)