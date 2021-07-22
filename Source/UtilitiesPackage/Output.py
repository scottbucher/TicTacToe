import sys
import numpy as np

class Output:
			
	def clearBoard():
		for x in range(0, 70):
			print()
			
	@staticmethod
	def printBoard(board):
		Output.clearBoard()
		print("Board:")
		print("============================")
		print()
		print(" ", board[0][0], "|", board[0][1], "|", board[0][2]);
		print(" -----------")
		print(" ", board[1][0], "|", board[1][1], "|", board[1][2]);
		print(" -----------")
		print(" ", board[2][0], "|", board[2][1], "|", board[2][2]);
		print()
			
	@staticmethod
	def confirmComputerTurn(board):
		Output.clearBoard()
		print("============================")
		Output.printBoard(board)
		print("============================")
		input("Press Enter to continue to the computer's turn.")
		
	
	@staticmethod
	def displayWhoIsFirst(isPlayerOneTurn, isMultiplayer, playerOneWins, playerTwoWins):
		Output.clearBoard()
		if not isMultiplayer:
			print(("The user will go first." if isPlayerOneTurn else "The computer will go first.") + " The score is " + str(playerOneWins) + "-" + str(playerTwoWins))
		else:
			print(("Player 1 will got first." if isPlayerOneTurn else "Player 2 will go first.") + " The score is " + str(playerOneWins) + "-" + str(playerTwoWins))
		input("Press Enter to begin.")
