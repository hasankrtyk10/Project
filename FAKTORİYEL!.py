#! /usr/bin/env python
import time
import pyfiglet

font = pyfiglet.figlet_format("Faktoriyel Hesaplama !")
print(font)
print("""
	[Directed by: hasanhuseyin9548, 
	Github: hasankrtyk10,
	]
""")
def fakt(value):
 	
 	try:
 		i = 1
 		
 		for x in range(value):
 			i = i * (x+1)
 		
 		print("=")
 		time.sleep(2)
 		print("==")
 		time.sleep(2)
 		print("==========")
 		print("Tebrikler başardıniz")
 		
 		
 		
 		return  i		
 		time.sleep(2)
 		
 	except:
 		pass
 		
 		
if __name__ == "__main__":
	
	Hesap_Sayisi = int(input("Faktoriyeli Gir:"))
	print(fakt(Hesap_Sayisi))
	
	
	