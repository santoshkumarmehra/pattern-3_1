n=7
for i in range(1,n+1):
	x=i
	print(" "*(i-1),end='')
	for j in range(1,n-i+2):
		print(x," ",end='')
		x=x+1
	print()
for i in range(n-1,0,-1):
	x=i
	print(" "*(i-1),end='')
	for j in range(1,n-i+2):
		print(x," ",end='')
		x=x+1
	print()