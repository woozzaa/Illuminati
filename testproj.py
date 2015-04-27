"""
Actual working document
Lab 3 in the makings

TODO
- instruktioner i Application.changeLamp()
"""
# import os, sys, inspect, thread, time
# src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
# import sys, time, thread
# sys.path.insert(0, '../../lib')
# import Leap
# from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

from Tkinter import * 
from Application import Application


def main():
	root = Tk()
	root.title('password')
	root.geometry('850x450') # Width x Height
	app = Application(root)
	root.mainloop()

if __name__ == "__main__":
	main()




#listener = LeapListener()
# controller = Leap.Controller()

# controller.add_listener(listener)

# # Keep this process running until Enter is pressed
# print "Press Enter to quit..."
# try:
#     sys.stdin.readline()
# except KeyboardInterrupt:
#     pass
# finally:
#     # Remove the sample listener when done
#     controller.remove_listener(listener)