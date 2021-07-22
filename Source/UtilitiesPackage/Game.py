import sys
sys.path.append('../')
import numpy as np

from UtilitiesPackage.Input import Input
from UtilitiesPackage.Validation import Validate

class Game:

	@staticmethod
	def updateBoard(b, spot, character) -> any:
		b[int(spot / 3)][int(spot % 3)] = character
		return b
		
	@staticmethod
	def processTurn(self, board, isUserTurn, userCharacter, computerCharacter, isMultiplayer, move, difficulty) -> any:
		if isUserTurn:
			# process user turn
			choice = Input.getNextUserInput(Input, board, 1, isMultiplayer, 1)
			board = Game.updateBoard(board, choice, userCharacter)
		else:
			#process computer turn
			if isMultiplayer:
				choice = Input.getNextUserInput(Input, board, 1, isMultiplayer, 2)
			else:
				if difficulty == 3:
					choice = Input.getNextComputerMoveImpossible(board, userCharacter, computerCharacter, Game, move)
				elif difficulty == 2:
					choice = Input.getNextComputerMoveHard(board, userCharacter, computerCharacter, Game, move)
				else:
					choice = Input.getNextComputerMoveEasy(board, userCharacter, computerCharacter, Game, move)
			board = Game.updateBoard(board, choice, computerCharacter)
			
		return board