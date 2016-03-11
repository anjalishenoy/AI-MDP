# /bin/python
class team57:
	def __init__(self):
		self.reward=-0.05*16
		self.board = [[0,   0,   0,   0,   0,   0],	#Top row Padding
					  [0,   0,   0,  16,   0,   0],
					  [0,   0, -16,   0,   0,   0], 
					  [0,   0,   0,   0,   0,   0],
					  [0,   0,   0,   0,   0,   0]] #Bottom row padding

	def displayBoard(self):
		for row in [1,2,3]:
			print ""
			for col in [1,2,3,4]:
				if row == 2 and col == 3:
					print '%10s' % "Wall",
				else:
					print '{:10.5f}'.format(self.board[row][col]),

		print "\n----------------------------------------------------------"

	def calculateMEU(self, N):
		iteration=N
		if iteration>10:
			return
		else:
			print "\nFor iteration: "+str(iteration)
			for col in [4,3,2,1]:
				for row in [1,2,3]:
					N=S=E=W=0
					if ( row == 1 and col ==3 ) or ( row == 2 and col == 2) or ( row == 2 and col == 3): #Ignore for terminal states/walls
						continue
					N=0.8*self.board[row-1][col]+0.1*self.board[row][col+1]+0.1*self.board[row][col-1]
					S=0.8*self.board[row+1][col]+0.1*self.board[row][col+1]+0.1*self.board[row][col-1]
					E=0.8*self.board[row][col+1]+0.1*self.board[row-1][col]+0.1*self.board[row+1][col]
					W=0.8*self.board[row][col-1]+0.1*self.board[row-1][col]+0.1*self.board[row+1][col]
					'''if row == 2 and col == 4:	
						print self.board[row][col-1]
					elif row == 1 and col == 1:
						print self.board[row][col+1]'''

					self.board[row][col] = self.reward + max(N,S,E,W)

		self.displayBoard()
		self.calculateMEU(iteration+1)



if __name__ == '__main__':
	B=team57()
	x=1
	B.calculateMEU(x)
