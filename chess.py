#!/usr/bin/python

# import modules used here -- sys is a very standard one


# Define the Board
class Board:
	"Defines the board"
	
	# Instance Varibles
	ranks = []

	def __init__():
		pass

	def prettyPrint():
		"Prints a pretty representation of the board"
		leBorder = '- - - - - - - -'
		heBorder = '|'


# Pieces
class Piece(object):
	"Generic Piece class that others will extend"
	def __init__(self):
		self.rankPos = 1
		self.filePos = 'a'
		self.moves = []
		self.threats = []
		self.attackMoves = []

	def possibleMoves(self):
		"Generates a tuple of possible moves"
		print 'Hello, World'



class King(Piece):
	"Define the kings possible moves"
	def __init__(self):
		super(King,self).__init__()
		self.rankPos = 1
		self.filePos = 'e'
		self.moves = []

class Queen(Piece):
	pass

class Bishop:
	pass

class Knight:
	pass

class Rook:
	pass

class Pawn:
	pass

