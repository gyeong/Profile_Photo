from random import randint

def random_player1():
	return randint(1,6)
def random_player2():
	return randint(1,6)

total_1=0
total_2=0
turn = 1

while(total_1 <= 100 or total_2 <= 100):
	print turn, "Turn : "

	num_1 = random_player1()
	total_1 += num_1
	print "Player1 : ", num_1
	print "Player1 Total : ", total_1

	num_2 = random_player2()
	total_2 += num_2
	print "Player2 : ", num_2
	print "Player2 Total : ", total_2

	if(total_1 >= 100 or total_2 >= 100):
		if(total_1 >= 100):
			print "Player1 WIN!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
			break
		else:
			print "Player2 WIN!!!!!!!!!!!!!!!!!!!!!!!!!!!"
			break
	else:
		turn = turn + 1

