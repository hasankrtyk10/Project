#!/usr/bin/env python

# s = chr((ord(data)+ cipher-65)% 26+65)
# s = chr((ord(data)+ cipher-97)% 26+97)


import time
import optparse

def option():

	optparser = optparse.OptionParser()

	optparser.add_option("-e","--encode",dest="encode",help="-e <'_'> **** --encode <'__'> ")

	optparser.add_option("-s","--cipher",dest="cipher",help="-s 3 **** --encode 3")
	
	optparser.add_option("-d","--decode",dest="decode",help="-d <'_'> **** --decode <'__'> ")	

	(user_input,arguments) = optparser.parse_args()
	
	return user_input

def cipher(text,s):
	string = ""
	for x in range(len(text)):
		data = text[x]
		
		if data.isupper():
		
			string+= chr((ord(data)+ s-65)% 26+65)
		
		else:
		
			string+= chr((ord(data)+ s-97)% 26+97)

	print(string)

def cipher_decode(cipher,s):
	string = ""
	for y in range(len(cipher)):
		data = text[y]
		if data.isupper():
			string+= chr((ord(data)- s-65)% 26+65)
		else:
			string+= chr((ord(data)- s-97)%26+97)
	print(string)

if __name__ == "__main__":
	inputer = option()

	text = inputer.encode
	s = int(inputer.cipher)
	decode = inputer.decode
	
	cipher(text,s)
	
	cipher_decode(decode,s)