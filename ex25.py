#-*- coding:utf-8 -*-

def break_words(stuff):
	"""This function Will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Prints the first word after popping it off."""
	return sorted(words)

def print_frist_word(words):
	"""Print the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Print the last word after popping it off."""
	word = words.pop(-1)
	print word

def print_setence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	print_first_word(words)
	print_first_word(words)

def print_frist_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentenc(sentence)
	print_first_word(words)
	print_last_word(words)





