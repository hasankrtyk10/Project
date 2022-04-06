import time 


def EBOB(sayi1, sayi2):
	
	Kucuk_Sayi= min(sayi1, sayi2)
	
	liste = []
	
	for x in range(1, Kucuk_Sayi+1):
		
		if sayi1%x == 0 and sayi2%x == 0:
			liste.append(x)
			
	liste.sort(reverse = True)		
	return liste[0]

if __name__ == "__main__":
	S1 = int(input("ilk sayi:"))
	print("################")
	time.sleep(2)
	S2 = int(input("ikinci sayi:"))
	print("################")
	
	print("Sonuç", EBOB(S1, S2))
	
	
	