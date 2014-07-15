def diamond(width):
	i  =  width/2
	j = 0
	for dia in range(1, width, 2):
		print(i * '   ' +dia *' * ' )
		i -= 1
	for dia in range(width, 0,-2):
		print (j*'   '+dia*' * ')
		j += 1


diamond(9)