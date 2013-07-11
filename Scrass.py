#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os.path import exists
from time import time


class Scrass:
	""" This class implements all the required functions for Scrabbler"""
	def __init__(self, filename="wordlist.dic"):
		""" Does nothing :/ """
		# Variables initialisation
		self.dic_filename = filename
		self.scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2, "F": 4,
				"I": 1, "H": 4, "K": 5, "J": 8, "M": 3, "L": 1, "O": 1, "N": 1,
				"Q": 10, "P": 3, "S": 1, "R": 1, "U": 1, "T": 1, "W": 4, "V": 4,
				"Y": 4, "X": 8, "Z": 10}
		self.errors = 0

		# Call for checking methods
		self.CheckFile()

	def CheckFile(self):
		""" Checks if the dictionnary file exists """
		if exists(self.dic_filename):
			self.errors = 0
		else:
			print ("Error : Dictionnary file does not exist !")
			self.errors = 1

	def ScrabbleInput(self):
		""" Gets user input, and prepare it for coming operation """
		self.user_input = input('Enter your letters (MAX=10) : ')
		self.letter_list = []

		for i in self.user_input:
			self.letter_list.append(i.upper())
		self.letter_list.sort()

	def LettersInWord(self, word, letlist):
		""" Input : A word and a list of letters; will verify if all the
		letters in the word are part of the list """
		# Don't know if there is a better way to do so :/  # lint:ok
		self.pos = 0
		self.temp_list = list(letlist)
		# Almost forgot that : little verification on the size !
		if (len(word) > len(letlist)):
			return False

		for letter in word:
			try:
				self.pos = self.temp_list.index(letter)
			except ValueError:
				return False
			else:
				self.temp_list.pop(self.pos)

		return True

	def GimmeWords(self):
		""" Iterates over the dictionnary file, and return possible words """
		self.res_list = []
		self.my_file = open(self.dic_filename, "r")

		for line in self.my_file:
			line = str(line)
			line = line.rstrip()

			if (self.LettersInWord(line, self.letter_list) is True):
				self.res_list.append(line)

	def GimmeScore(self):
		""" Get the score of every entry in the list of words found """
		# Have we found something ?
		if (len(self.res_list) <= 0):
			print ("Sorry :/ No results !")
			return False
		# We need that little sucker to keep our WORDS/SCORE tuples
		self.win_dic = {}

		for entry in self.res_list:
			self.t_score = 0
			for letter in entry:
				self.t_score += self.scores[letter]
			self.win_dic[entry] = self.t_score

		# Some dark black magic for sorting the dic
		self.final_dic = [(k, v) for v, k in sorted([(v, k)
		for k, v in self.win_dic.items()])]
		# And now, we show tits
		for i in self.final_dic:
			print (i[0], end="...............")  # lint:ok
			print (i[1])