#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import system
from Scrass import Scrass

MyScrabbler = Scrass()
print("Welcome to Scrabbler, Alpha 0.1")

while True:
	MyScrabbler.ScrabbleInput()
	if (MyScrabbler.user_input == ""):
		break
	system("clear")
	print ("Your letters : ", end=" ")  # lint:ok
	for i in MyScrabbler.letter_list:
		print (i, end="")
	print (" ")
	print ("Results :")
	MyScrabbler.GimmeWords()
	MyScrabbler.GimmeScore()

print ("Have a nice day !")