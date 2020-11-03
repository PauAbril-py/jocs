import random

while True:
	a=int(input("cuants xinos creus que hi hauran entre 0 i 6:"))
	if a<0 or a>6:
		print("escull un nombre entre 0 i 6")
	else:
		while True:
			b=int(input("escull cuants xinos vols agafar entre 0 i 3:"))
			if b<0 or b>3:
				print("escull un nombre entre 0 i 3")
			else:
				if a>=0 and a<=6 and b>=0 and b<=3:
					c=random.randint(0,3)
					print("has agafat",b,"xinos, i la maquina ha agafat",c,"xinos.\nEn total hi han",c+b,"xinos")
					if c+b==a:
						print("has guanyat")
					else:
						print("has perdut")