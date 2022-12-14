#!/usr/bin/env python

#----------------------------------------------------------------------------
# Created By  : Julie Pivin-Bachler
# Created Date: 03/2022 - 08/2022
# ---------------------------------------------------------------------------
""" Class built to make a button for ungrasping in the handover task """ 
# ---------------------------------------------------------------------------
#                                  IMPORTS
# ---------------------------------------------------------------------------
from Tkinter import *
import tkFont as font
# ---------------------------------------------------------------------------


class UngraspButton(object):
	"""UngraspButton"""

	def __init__(self, command):
		super(UngraspButton,self).__init__()
		# create a tkinter window
		self.root = Tk()             
		 
		# Open window having dimension 100x100
		self.root.geometry('300x120')
		 
		myFont = font.Font(family='Helvetica', size=30, weight='bold')

		# Create a Button
		self.btn = Button(self.root, text = 'Ungrasp', bd = '5', command = command, height = 280, width = 110, fg="#ff0000")
		self.btn['font'] = myFont

		# Set the position of button on the top of window.  
		self.btn.pack(side = 'top')

	def launch(self):
		self.root.mainloop()

	def kill(self):
		self.root.destroy()

