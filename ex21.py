#!/usr/bin/python
#-*- coding:utf-8 -*-

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtrcat(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLY %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d * %d" % (a, b)
	return a / b


print "Let's do some math with just functions!"

age = add(30, 3)
height = subtrcat(200, 30)
weight = multiply(35, 2)
iq = divide(180, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

what = add(age, subtrcat(height, multiply(weight, divide(iq, 3))))

print "That becomes: ", what, "Can you do it by hand?"

