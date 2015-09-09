#!/usr/bin/python
#-*- coding:utf-8 -*-

from sys import argv

script, filename = argv

def all_file(f):
	print f.read()

def rewind(f):
	f.seek(10)

def read_one_lin(line_num, f):
	print line_num, f.readline(),

current_file = open(filename)

print "Frist let's print the whole file:\n"

all_file(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
read_one_lin(current_line, current_file)

current_line += 1
read_one_lin(current_line, current_file)

current_line += 1
read_one_lin(current_line, current_file)

