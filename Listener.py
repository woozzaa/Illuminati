# -*- coding: utf-8 -*-
import sys, time, thread
sys.path.insert(0, '../../lib')
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class LeapListener(Leap.Listener):
	""" Listener for data from leapmotion """

	def setup(self, parent):
		self.parent = parent
		self.fingerNameList = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
		self.gestureType 	= 'no status available'
		self.handName 		= 'no hand'
		self.fingerNames 	= 'no fingers'
		self.thumbExtended = 'no'

		#Right hand variables
		self.handHeight = 0.5

		#Left hand variables
		self.leftHandFingers = 0

	'''def __init__(self):
					Leap.Listener.__init__(self)
					self.listener = self
					self.controller = Leap.Controller()
					self.controller.add_listener(self.listener)'''


	#when connecting Leap Motion
	def on_connect(self, controller):
		self.gestureType = 'connected'
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
		# print self.gestureType
		# self.getRefFrame(controller)

	#runs when frames available
	def on_frame(self, controller):

		frame = controller.frame()
		# print frame.current_frames_per_second

		if frame.hands.is_empty:
			self.handName 		= 'No hands'
			self.gestureType 	= 'No gesture'
			self.fingerNames 	= 'No fingers'
		else:
			for hand in frame.hands:
				if hand.is_valid:
					"""
					Right hand = illumination controller
					"""
					if hand.is_right:
						self.handHeight = self.normalizeHeight(hand.palm_position.y)
						
					'''
					Left hand = lamp controller
					'''
					if hand.is_left:
						fingers = hand.fingers
						self.leftHandFingers = len(fingers.extended())
						# print self.leftHandFingerss



	def normalizeHeight(self, height):	#highest = 450, lowest = 30
		normalizeFactor = 350
		normalizedVector = height / normalizeFactor

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