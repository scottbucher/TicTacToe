import sys
sys.path.append('../')

import numpy as np
	
TRUTH_VALUES = ["t", "y", "true", "yes", "1", "yea", "sure", "i guess", "definitely", "of course", "duh", "heck yea"]

class Validate:
	@staticmethod
	def isValidInput(board, userInput) -> bool:
		try:
			userInput = int(userInput)
			# check if the spot is an invalid spot or has already been used
			if (userInput < 0 or userInput > 8) or int(board[int(userInput / 3)][int(userInput % 3)]) != userInput:
				return False
		except ValueError:
			return False
		return True
	

	@staticmethod
	def checkUserCharacter(self, userInput, errorMessage, character) -> str:
		# Hybrid coupling for the win :)	
		if errorMessage == 0:
			userInput = input("Your character can't be a number! Please try again: ")
		elif errorMessage == 2:
			userInput = input("Player 1 already chose that character! Please try again: ")
		try:
			int(userInput)
			userInput = self.checkUserCharacter(Validate, userInput, 0, character)
		except ValueError:
			if (userInput == character):
				userInput = self.checkUserCharacter(Validate, userInput, 2, character)
			pass
		return userInput
		
	

	@staticmethod
	def checkDifficulty(self, userInput, isFirst) -> int:
		userInput = userInput.lower()
		if not isFirst:
			userInput = input("Invalid difficulty choice! Please try again: ")
			
		if userInput == "easy" or userInput == "e": return 1
		elif userInput == "hard" or userInput == "h": return 2
		elif userInput == "impossible" or userInput == "i": return 3
		else: return self.checkDifficulty(self, userInput, 0)		
		
	@staticmethod
	def isNumber(value):
		negative = False
		
		if(value[0] =='-'):
			negative = True
         
		if negative == True:
			value = value[1:]
		 
		# try to convert the string to int
		try:
			n = int(value)
			return True
		# catch exception if cannot be converted
		except ValueError:
			return False
		
	@staticmethod
	def checkIfRowUnTouched(row, playerCharacter) -> bool:
		# check each row
		for spot in row:
			if spot == playerCharacter:
				return False
		return True
		
	@staticmethod
	def checkRows(board) -> bool:
		# check each row
		for r in board:
			if len(set(r)) == 1:
				return True
		return False
		
	@staticmethod
	def checkDiagonals(board) -> bool:
		# check the left to right diagonal
		if len(set([board[i][i] for i in range(len(board))])) == 1:
			return True
		# check the right to left diagonal
		if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
			return True
		return False
		
	@staticmethod
	def hasWon(self, board) -> bool:
		# check left to right board and then flip the board to check up and down
		for newBoard in [board, np.transpose(board)]:
			if self.checkRows(newBoard):
				return True
		return self.checkDiagonals(board)
		
	@staticmethod
	def isTrap(self, board, Game, computerCharacter) -> bool:
		raveledBoard = board.copy().ravel()
		waysToWin = 0
		# check every move for the next turn if this current turn happens
		for x in raveledBoard:
			copy = board.copy()
			# If there is a win with this move increase ways to win
			if (Validate.isNumber(x) and Validate.hasWon(Validate, Game.updateBoard(copy, int(x), computerCharacter))):
				waysToWin += 1
		# if there is more than one way to win it is a trap!
		return waysToWin > 1
	
	@staticmethod
	def checkDiagonalsForTrap(board) -> int:
		waysToWin = 0
		print("checkDiagonalsForTrap!")
		# check the left to right diagonal
		if len(set([board[i][i] for i in range(len(board))])) == 1:
			waysToWin += 1
			print("found a diagonal way to win! Total: ", waysToWin)	
		# check the right to left diagonal
		if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
			waysToWin += 1
			print("found a diagonal way to win! Total: ", waysToWin)	
		return waysToWin
		
	@staticmethod
	def getBooleanFromInput(input) -> bool:
		return input.lower() in TRUTH_VALUES
		
	@staticmethod
	def getIntegerFromInput(self, userInput, isFirst) -> int:
		if not isFirst:
			userInput = input("That is an invalid number! Please try again: ")
		try:
			userInput = int(userInput)
		except ValueError:
			userInput = self.getBooleanFromInput(input, 0)
		return userInput
	