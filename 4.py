import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

w=0

while True:
	a=int(input("cuants xinos creus que hi hauran entre 0 i 6:\n"))
	if a<0 or a>6:
		print("escull un nombre entre 0 i 6\n")
	else:			
		while True:
			b=int(input("\nescull cuants xinos vols agafar entre 0 i 3:\n"))
			if b<0 or b>3:
				print("escull un nombre entre 0 i 3\n")
			else:
				if a>=0 and a<=6 and b>=0 and b<=3:
					c=random.randint(0,3)
					print("\nhas agafat",b,"xinos, i la maquina ha agafat",c,	"xinos.\nEn total hi han",c+b,"xinos")
					if c+b==a:
						w=w+1
						print("\nhas guanyat")
						print("\nhas guanyat",w,"vegaes")
						input("\n\nEnert to cumtinue")
						cls()
						break
					else:
						print("\nhas perdut")
						print("\nhas guanyat",w,"vegaes")
						input("\n\nEnert to cumtinue")
						cls()
						break
