#!/usr/bin/python
#-*- coding:utf-8 -*-

def contianer(Interge, Increment_Num):
	number = []
	i = 0
	while i < Interge:
		print "At the top i is %d" % i
		number.append(i)

		i += Increment_Num
		print "Numbers now: ", number
		print "At the bottom i is %d" % i 
	return number

print 'please input a number'
start_num = raw_input('> ')

print 'please increment value'
increment_num = raw_input('# ')

get_num = contianer(int(start_num), int(increment_num))

print "The numbers: "

for num in get_num:
	print num




