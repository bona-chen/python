import random
answer=random.randint(1,10)
times=3
admit=input("Lst's play a game!\nWhat about guessing which number(1-10)I am thinking?\nOK! Let's do it ! You have three chance.\nnumber:")
while admit.isdigit()==0:
	print("Illegal input")
	admit=input("Please input again:")
	guess=int(admit)
guess=int(admit)
while times!=0:
	if guess==answer:
		print("You're right!")
		print("Congratuations!")
		break
	else:
		times=times-1
		if times!=0:
			if times==2:
				print("You have two more chance!")
				if guess >answer:
					print("Tip:\nYour number is too big.")
				else:
					print("Tip:\nYour number is too small.")
				admit=input("Again:")
				while admit.isdigit()==0:
					print("Illegal input")
					admit=input("Please input again:")
				guess=int(admit)
			else:
				print("You have only one more chance!")
				if guess >answer:
					print("Tip:\nYour number is too big.")
				else:
					print("Tip:\nYour number is too small.")
				admit=input("Last chance:")
				while admit.isdigit()==0:
					print("Illegal input")
					admit=input("Please input again:")
				guess=int(admit)
		else:
			print("You have no chance!")
if times==0:
	print("You don't have chances any more!")
	print("The right answer is "+str(answer))
print("Game over!")
