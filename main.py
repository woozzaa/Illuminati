# -*- coding: utf-8 -*-
from Tkinter import * 
from Application import Application

"""
main file, starts up the whole shabang
"""
def main():
	root = Tk()
	root.title('Illumination Project')
	root.geometry('850x750') # Width x Height
	app = Application(root)
	try:
		root.mainloop()
	except KeyboardInterrupt:
		print 'exited'

if __name__ == "__main__":
	main()