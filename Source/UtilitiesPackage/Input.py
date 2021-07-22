import sys
sys.path.append('../')

import random

from UtilitiesPackage.Output import Output
from UtilitiesPackage.Validation import Validate

class Input:
		
	@staticmethod
	def getNextUserInput(self, board, isFirst, isMultiplayer, playerNumber) -> int:
	
		if isFirst == 1: 
			Output.clearBoard()
			print("============================")
			Output.printBoard(board)
			print("============================")
		userInput = input(("Your turn" if not isMultiplayer else ("Player " + str(playerNumber) + "'s turn")) + ", please select a valid square (0-8): ")
		
		if (not Validate.isValidInput(board, userInput)):
			print("============================")
			print("That is not a valid integer, please ty again")
			userInput = self.getNextUserInput(Input, board, 0, isMultiplayer, playerNumber)
		return int(userInput)
		
	@staticmethod
	def getNextComputerMoveEasy(board, playerCharacter, computerCharacter, Game, move) -> int:
		list = []
		board = board.ravel()
		
		# Otherwise lets try and take the center, it is always the best spot
		if Validate.isNumber(board[4]): return 4
		
		for x in board:
			if (Validate.isNumber(x)):
				list.append(x)
		return int(random.choice(list))
		
	@staticmethod
	def getNextComputerMoveHard(board, playerCharacter, computerCharacter, Game, move) -> int:
		list = []
		# Python lists/arrays are pass by reference
		raveledBoard = board.copy().ravel()
		
		# First we check if the computer has any spots it can instantly win
		for x in raveledBoard:
			copy = board.copy()
			# If it does we choose it
			if (Validate.isNumber(x) and Validate.hasWon(Validate, Game.updateBoard(copy, int(x), computerCharacter))):
				return int(x)
		
		# Second lets check if we can block the user from winning
		for x in raveledBoard:
			copy = board.copy()
			# If it does we choose it
			if (Validate.isNumber(x) and Validate.hasWon(Validate, Game.updateBoard(copy, int(x), playerCharacter))):
				return int(x)		
		
		# Otherwise lets try and take the center, it is always the best spot
		if Validate.isNumber(raveledBoard[4]) : return 4
		
		# Otherwise lets take a random spot
		for x in raveledBoard:
			if (Validate.isNumber(x)):
				list.append(x)
		return int(random.choice(list))	
		
	@staticmethod
	def getNextComputerMoveImpossible(board, playerCharacter, computerCharacter, Game, move) -> int:
		list = []
		# Python lists/arrays are pass by reference
		raveledBoard = board.copy().ravel()
		
		# First we check if the computer has any spots it can instantly win
		for x in raveledBoard:
			copy = board.copy()
			# If it does we choose it
			if (Validate.isNumber(x) and Validate.hasWon(Validate, Game.updateBoard(copy, int(x), computerCharacter))):
				#print("Found win... Moving!")
				return int(x)
		
		# Second lets check if we can block the user from winning
		for x in raveledBoard:
			copy = board.copy();
			# If it does we choose it
			if (Validate.isNumber(x) and Validate.hasWon(Validate, Game.updateBoard(copy, int(x), playerCharacter))):
				#print("Found block... Moving!")
				return int(x)		
		
		# Try a spot which allows the computer two ways to win next turn (It's a trap!)
		for x in raveledBoard:
			copy = board.copy()
			if (Validate.isNumber(x) and Validate.isTrap(Validate, Game.updateBoard(copy, int(x), computerCharacter), Game, computerCharacter)):
				#print("Found trap... Moving!")
				return int(x)	
		
		#Everything above will get passed in the early moves, but they need to happen first for the later turns
		
		# Undisputed best first move is a corner
		# Choose a random one because we don't want to be predicatable
		if move == 1:
			#print("Move 1 action")
			randomCorner = random.randrange(0, 4)
			if randomCorner == 0:
				return 0
			elif randomCorner == 1:
				return 2
			elif randomCorner == 2:
				return 6
			else:
				return 8
		elif move == 3:
			#print("Move 3 action")
			# we win if we go first and the user doesn't choose the center
			if Validate.isNumber(raveledBoard[4]): 
				#print("Move 3 action: take center or corner")
				return 4
				
			else:
				#print("Move 3 action: take opposite corner or edge")
				# if they choose the center we have two possible moves, both are equally good
				randomChoice = random.randrange(0,2)
				if randomChoice == 0:
					# Go to the opposite corner
					# First we must figure out which corner we went in the first move
					if Validate.isNumber(raveledBoard[0]):
						return 8
					elif Validate.isNumber(raveledBoard[2]):
						return 6
					elif Validate.isNumber(raveledBoard[6]):
						return 2
					else:
						return 8
				else:
					# Go to an edge square NOT touching our first move
					# First we must figure out which corner we went in the first move
					
					# No matter the corner we will have 2 moves, so..
					randomEdge = random.randrange(0, 2)
					
					if Validate.isNumber(raveledBoard[0]):
						if randomEdge == 0:
							return 5
						else:
							return 7
					elif Validate.isNumber(raveledBoard[2]):
						if randomEdge == 0:
							return 3
						else:
							return 7
					elif Validate.isNumber(raveledBoard[6]):
						if randomEdge == 0:
							return 1
						else:
							return 5
					else:
						if randomEdge == 0:
							return 3
						else:
							return 1
		elif move == 2:
			# These are the starting moves if we didn't go first
			
			# If they go into the center we can force a draw by going to a corner
			if not Validate.isNumber(raveledBoard[4]):
				#print("Move 2 action: take coner")
				randomCorner = random.randrange(0, 4)
				if randomCorner == 0:
					return 0
				elif randomCorner == 1:
					return 2
				elif randomCorner == 2:
					return 6
				else:
					#print("Move 2 action: take corner")
					return 8 
			else:
				# If they didn't choose the center we always will on the second move
				return 4;
		elif move == 4 and raveledBoard[4] == computerCharacter:
			#print("Move 4 action: try and take a corner if conditions meet")
			# If the user's first move isn't in the center lets continue to try and win
			# if the user's first move was the center then we are defending and will never get here
				
			if (raveledBoard[3] == playerCharacter and raveledBoard[5] == playerCharacter) or (raveledBoard[1] == playerCharacter and raveledBoard[7] == playerCharacter):
				# Choose a random corner cause I like to complicate things
				cornerList = [0,2,6,8]
				choiceList = []
				for x in cornerList:
					if Validate.isNumber(raveledBoard[x]):
						choiceList.append(x)
				return random.choice(choiceList)	
		
		
		# Final check to see if any rows are left un touched by the player, if so we will go in one of those spots
		# Random because I like to make things complicated
		randomSpotInRow = random.randrange(0, 3)
		possibleMoves = []
		# check each row
		#print("Calculate last check")
		for r in board:
			#print("Last check board row: ", r)
			if Validate.checkIfRowUnTouched(r, playerCharacter):
				if r[0] != computerCharacter: possibleMoves.append(int(r[0]))
				if r[1] != computerCharacter: possibleMoves.append(int(r[1]))
				if r[2] != computerCharacter: possibleMoves.append(int(r[2]))
		# check each col
		for r in board.transpose():
			#print("Last check transposed board row: ", r)
			if Validate.checkIfRowUnTouched(r, playerCharacter):
				if r[0] != computerCharacter: possibleMoves.append(int(r[0]))
				if r[1] != computerCharacter: possibleMoves.append(int(r[1]))
				if r[2] != computerCharacter: possibleMoves.append(int(r[2]))
				
		if len(possibleMoves) != 0: 
			#print("possibleMoves", possibleMoves)
			return random.choice(possibleMoves)	
		# Otherwise lets take a random spot
		for x in raveledBoard:
			if (Validate.isNumber(x)):
				list.append(x)
		#print("Random... moving!")
		return int(random.choice(list))	
		
	@staticmethod
	def getNeededWins() -> int:
		Output.clearBoard()
		return Validate.getIntegerFromInput(Validate, input("How many points should you need to win this match? "), 1)
		
	@staticmethod
	def getWhoGoesFirst() -> bool:
		Output.clearBoard()
		return Validate.getBooleanFromInput(input("Player 1 would you like to start first? "))
		
		
	@staticmethod
	def getDifficulty() -> int:
		Output.clearBoard()
		return Validate.checkDifficulty(Validate, input("Should the Computer's difficulty be easy, hard, or impossible? "), 1)
		
	@staticmethod
	def getIsItMultiplayer() -> bool:
		Output.clearBoard()
		return Validate.getBooleanFromInput(input("Are there two players? "))
		
	@staticmethod
	def getFirstUserCharacter() -> str:
		Output.clearBoard()
		return Validate.checkUserCharacter(Validate, input("Player 1 what character would you like to use? ")[0], 1, "")
	@staticmethod
	def getSecondUserCharacter(playerOneCharacter) -> str:
		Output.clearBoard()
		return Validate.checkUserCharacter(Validate, input("Player 2 what character would you like to use? ")[0], 1, playerOneCharacter)