import sys
sys.path.append('../')
import numpy as np
from UtilitiesPackage.Input import Input
from UtilitiesPackage.Output import Output
from UtilitiesPackage.Validation import Validate
from UtilitiesPackage.Game import Game

def main():
	keepPlaying = True
	
	playerOneCharacter = Input.getFirstUserCharacter()
	
	isMultiplayer = Input.getIsItMultiplayer()
	difficulty = 1;
	
	if isMultiplayer:
		secondPlayerCharacter = Input.getSecondUserCharacter(playerOneCharacter)
	else:
		secondPlayerCharacter = "o" if playerOneCharacter != "o" else "x"
		difficulty = Input.getDifficulty()
	
	
	isPlayerOneTurn = Input.getWhoGoesFirst()
	
	while keepPlaying:
		neededWins = Input.getNeededWins()
		
		if neededWins == 0: neededWins = 1
	
		playerOneWins = 0
		playerTwoWins = 0
		
		while playerOneWins < neededWins and playerTwoWins < neededWins:
			board = np.array([['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']])
			
			isTie = True
			
			Output.displayWhoIsFirst(isPlayerOneTurn, isMultiplayer, playerOneWins, playerTwoWins)
			
			for x in range(9):
				board = Game.processTurn(Game, board, isPlayerOneTurn, playerOneCharacter, secondPlayerCharacter, isMultiplayer, x+1, difficulty)
				if Validate.hasWon(Validate, board):
					if isPlayerOneTurn:
						isTie = False
						print("============================")
						Output.printBoard(board)
						print("============================")
						print("You managed to beat a computer... congratulations?" if not isMultiplayer else "Player 1 won!")
						input("Press Enter to continue")
						playerOneWins += 1
						isPlayerOneTurn = False
						break
					else:
						isTie = False
						print("============================")
						Output.printBoard(board)
						print("============================")
						print("You got beat by a computer..." if not isMultiplayer else "Player 2 won!")
						playerTwoWins += 1
						isPlayerOneTurn = True
						input("Press Enter to continue")
						break
				if isPlayerOneTurn and x != 8 and not isMultiplayer: 
					Output.confirmComputerTurn(board)
				isPlayerOneTurn = not isPlayerOneTurn
			
			if isTie:
				print("============================")
				Output.printBoard(board)
				print("============================")
				print("Tie.")
				input("Press Enter to continue")
		
		if playerOneWins > playerTwoWins:
			print("============================")
			print("You won the match! (But it was only against a computer lol)" if not isMultiplayer else "Player 1 won the match!")
		else:
			print("============================")
			print("The computer won the match! How did you lose to a computer???" if not isMultiplayer else "Player 2 won the match!")
		
		input("Press Enter to continue")
		
		print("============================")
		keepPlaying = Validate.getBooleanFromInput(input("Would you like to play again? "))
		print("============================")
		
if __name__ == '__main__':
	main()