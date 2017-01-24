#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pythag.py
#  
#  Copyright 2017 Jesse Rominske
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA. 

#  This program finds arbitrarily many Pythagorean Multiples within the given Upper Bound and Dimensionality
# 	Upper Bound: all variables on LHS less than/equal to Upper Bound
#	Dimensionality: number of variables  whose squares are summed (number of dimensions to which the multiple applies)

#  Assumptions:
#	1. If a,b are integers, then a,b,c are a Pythagorean Multiple IFF a^2 + b^2 = c^2 AND c is an integer. (definition)
#	2. a^2 + b^2 = c^2 AND c^2 + d^2 = e^2 IF a^2 + b^2 + d^2 = e^2. (a,b,d,e are a Pythagorean Quadruple; inductively the Pythagorean Theorem generalizes for any number of dimensions)
#	3. If x is an integer, ceil(x) = x.
#	4. Pythagorean Multiples involving zero are trivial and can be ignored.

import math # because we want math

def isInteger(x): # determines if x is an integer by ensuring it is equal to its own ceiling
	if math.ceil(x) == x:
		return True
	else:
		return False
		
def Triples(ubnd): # checks Pythagorean Triples up to ubnd
	triples = []
	if ubnd < 4: return triples # kills instantly if nothing to check - nothing smaller than 3,4,5
	
	for a in range(1, ubnd): # for each positive integer within the upper bound
		for b in range(a, ubnd): # for each positive integer between the first and the upper bound
			c = math.sqrt(a*a + b*b)
			if isInteger(c):
				c = int(c) # make c an int in real life
				triples.append((a, b, c)) # add the new multiple to the list
				print("Found triple: " + str((a,b,c)))
	return triples
	
def DimUp(currentDim, trips): # returns the multiples from the range the next level up
	upDimmed = [] # the list we plan to return

	for t in currentDim: # for each multiple
		for s in trips: # check every triple
			if t[-1] == s[0]: # to see if the sum of the multiple is the beginning of the triple, and if so,
				new = t[:-1] + s[1:] # combine them, removing the sum of the multiple from each
				upDimmed.append(new) # then update list of multiples
				print("Found "  + str(len(new)) + "-multiple: " + str(new)) # alert the user for shock and awe
				break # and stop checking every other triple for the multiple because that new one will be unique
	return upDimmed	
			
def Multiples(dims, trips): # general case for higher dimensions 
	if dims == 2: return trips # no extra work to be done if in 2 dimensions
	
	mults = [] # the list we plan to return
	currentMults = trips # the list we are currently checking with the triples
	
	for d in range(2, dims+1):
		if d == dims: # if we have finished
			return currentMults
		else:
			print
			mults = DimUp(currentMults, trips) # raise the dimensionality by one
			currentMults = mults # shift the current mults up a dimension
			mults = [] # reset the list we plan to return

while True: # main program loop
	arg1 = raw_input("Enter upper bound for Pythagorean Multiple search: ")
	argInt1 = int(arg1, 10)
	arg2 = raw_input("Enter number of dimensions for Pythagorean Multiple search: ")
	argInt2 = int(arg2, 10)
	
	triples = Triples(argInt1)
	if len(triples) == 0:
		print("No Pythagorean Triples found within range")
		continue

	multiples = Multiples(argInt2, triples)
	if len(multiples) == 0:
		print("No Pythagorean Multiples of given dimensionality found within range")
		continue
	
	arg3 = raw_input("Name of output file: ")
	resultFile = open(arg3 + ".txt", "w")
	print("Creating output file " + resultFile.name)
	for m in multiples:
		resultFile.write("%s\n" % str(m))
	resultFile.close()
	print("Output file created")
	
