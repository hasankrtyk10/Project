#! /usr/bin/env python

import time

def ustel_buyume(Time):
	
	a = int(input("Baslangic miktari:"))
	time.sleep(2)
	
	b = int(input("Buyume orani:"))
	print("{}/100".format(b))
	r = b/100
	time.sleep(2)
	
	formul = (a*(1+r)**Time)

		
	print("Formul: {}*(1+{})**{}".format(a, b, r))
	
	return formul
	
if __name__ == "__main__":
	dime = float(input("sure gir:"))
	print(ustel_buyume(dime))