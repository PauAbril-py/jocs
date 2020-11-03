import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

nom=input("Quin es el teu nom?\n")
cls()

ppt="error","pedra","paper","tissores"

w=0
l=0
t=0

while True:
	a=int(input("Escull:\n\n\t1)pedra\n\t2)paper\n\t3)tisores\n"))
	b=random.randint(1,3)

	if a>3 or a<0:
		print("\nescull un nombre del 1 al 3")

# tie	
	elif a==b:
		print("\n"+nom,"ha tret",ppt[a],"i l'ordinador ha tret",ppt[b])
		print("Heu empatat")
		t=t+1

# win
	elif a==1 and b==3:
		print("\n"+nom,"ha tret",ppt[a],"i l'ordinador ha tret",ppt[b])
		print(nom,"ha guanyat")
		w=w+1
	elif a==2 and b==1:
		print("\n"+nom,"ha tret",ppt[a],"i l'ordinador ha tret",ppt[b])
		print(nom,"ha guanyat")
		w=w+1
	elif a==3 and b==2:
		print("\n"+nom,"ha tret",ppt[a],"i l'ordinador ha tret",ppt[b])
		print(nom,"ha guanyat")
		w=w+1

# lose
	elif a==1 and b==2:
		print("\n"+nom,"ha tret",ppt[a],"i l'ordinador ha tret",ppt[b])
		print(nom,"ha perdut")
		l=l+1
	elif a==2 and b==3:
		print("\n"+nom,"ha tret",ppt[a],"i l'ordinador ha tret",ppt[b])
		print(nom,"ha perdut")
		l=l+1
	elif a==3 and b==1:
		print("\n"+nom,"ha tret",ppt[a],"i l'ordinador ha tret",ppt[b])
		print(nom,"ha perdut")
		l=l+1
		
	if w==3:
		cls()
		print(nom,"ha guanyat")
		break
	elif l==3:
		cls()
		print("l'ordinador ha guanyat")
		break
	else:
		input("\nenter per continuar")
		cls()