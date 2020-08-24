import numpy as np

class Player:
	"""docstring for Player"""
	def __init__(self, symbol):
		self.symbol = symbol
		
class Board:
	"""docstring for Board"""
	def __init__(self,size):
		self.num_rows = size
		self.num_cols = size
		self.board = [ [' ' for _ in range(self.num_rows)] for _ in range(self.num_cols)]

	def draw(self):
		for row_idx, row in enumerate(self.board):
			for col_idx,col in enumerate(row):
				if col_idx < self.num_cols-1:
					print(f" {col} |",end='')
				else:
					print(f" {col} ",end='')
			print("")
			if row_idx < self.num_rows-1:
				print("-" * (self.num_cols * 4))

	def check_row_win(self):
		for row in self.board:
			if row[0] != ' ' and row.count(row[0]) == len(row):
				return True
		return False

	def check_col_win(self):
		for col_ind in range(self.num_cols):
			count = 0
			for row in self.board:
				#print(f"col ind {col_ind} and {row[col_ind]} and {self.board}")
				if row[col_ind] != ' ' and row[0]  == row[col_ind]:
					count += 1
			#print(f"Count_Value: {count} and {self.num_cols}")
			if count == self.num_cols:
				return True
		return False

	def check_diagonal(self):
		count_dia1 = 0
		count_dia2 = 0

		for row_idx in range(self.num_rows):
			if self.board[row_idx][row_idx] != ' ' and self.board[0][0] == self.board[row_idx][row_idx]:
					count_dia1 += 1
		print(f"Count {count_dia1} and colum : {self.num_cols}")
		if count_dia1 == self.num_rows:
			return True

		for col_idx in range(self.num_cols-1, -1, -1):
			if self.board[abs(col_idx-2)][col_idx] != ' ' and self.board[0][2] == self.board[abs(col_idx-2)][col_idx]:
				count_dia2 += 1
		print(f"Count {count_dia2} and colum : {self.num_cols}")
		if count_dia2 == self.num_rows:
			return True

		return False	


class GameState:
	# Class of the Game State
	def __init__(self, size):
		self.player_1 = Player('X')
		self.player_2 = Player('O')
		self.board = Board(size)
		self.turn = True # When turn is true its Player_1's turn and visversa

	def check(self):
		# Check all Rows
		if self.board.check_row_win():
			return True

		# Check all Columns
		if self.board.check_col_win():
			return True

		# Check all Diagonals
		if self.board.check_diagonal():
			return True

		return False


	def check_draw(self):
		for row in self.board.board:
			for val in row:
				if val == ' ':
					return False
		return True



	def run(self):
		self.board.draw()
		while True:
			if self.turn:
				print("Turn : Player 1")
			else:
				print("Turn : Player 2")
			row, col = input("Enter Row and Column :").split(' ')
			row = int(row)
			col = int(col)
			if self.board.board[row][col] == ' ':
				if self.turn:
					self.board.board[row][col] = self.player_1.symbol
				else:
					self.board.board[row][col] = self.player_2.symbol

				self.board.draw()

				if self.check():
					if self.turn:
						print("Player 1 WON")
					else:
						print("Player 2 WON")
					return
				else:
					if self.check_draw():
						print("Its a Draw!!!")
						return
				self.turn = not self.turn
			else:
				print("Position Not Empty!!")

print("Welcome To Tic Tac Toe")
game = GameState(3)
game.run()





