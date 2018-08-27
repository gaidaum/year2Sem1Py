#!/usr/bin/env python

def get():
	s = raw_input()
	output = []
	while s != "end":
		output.append(s)
		s = raw_input()

	return output