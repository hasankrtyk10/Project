#!/usr/bin/env python

import optparse

def control():
	optparser = optparse.OptionParser()
	optparser.add_option("-e",dest="encode",help="-e ilkvideo!")
	optparser.add_option("-s",dest="cipher",help="-s 5")

	(user_input,arguments) = optparser.parse_args()
	return user_input
	


def caesar(text,s):
	string = ""
	for x in range(len(text)):
		data = text[x]
		if data.isupper():
			string+= chr((ord(data)+ s-65)% 26+65)
		else:
			string+= chr((ord(data)+ s-97)% 26+97)

	print(string)


if __name__ == "__main__":
	ctrl = control()
	text = ctrl.encode
	s = int(ctrl.cipher)

	caesar(text,s)
















