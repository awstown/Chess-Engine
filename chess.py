#!/usr/bin/python

# import modules used here -- sys is a very standard one


# Define the Board
class Board(object):
	"Defines the board"
	def __init__(self):
		self.pieces      = []
		self.history     = []
		self.whiteToMove = True

		## Set Up Board
		f = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
		#Pawns
		for i in f:
			self.pieces.append(Pawn('W',i,2))
			self.pieces.append(Pawn('B',i,7))
		#Rooks
		self.pieces.append(Rook('W','a',1))
		self.pieces.append(Rook('W','h',1))
		self.pieces.append(Rook('B','a',8))
		self.pieces.append(Rook('B','h',8))
		#Knights
		self.pieces.append(Knight('W','b',1))
		self.pieces.append(Knight('W','g',1))
		self.pieces.append(Knight('B','b',8))
		self.pieces.append(Knight('B','g',8))
		#Bishops
		self.pieces.append(Bishop('W','c',1))
		self.pieces.append(Bishop('W','f',1))
		self.pieces.append(Bishop('B','c',8))
		self.pieces.append(Bishop('B','f',8))
		#Queens
		self.pieces.append(Queen('W','d',1))
		self.pieces.append(Queen('B','d',8))
		#Kings
		self.pieces.append(Queen('W','e',1))
		self.pieces.append(Queen('B','e',8))

			
	def getPiecePositions(self):
		'''Returns a Dictionary?Tuple?List? of pieces and their positions on the board
			>>>a = Board()
			>>>a.getPiecePositions()
		'''
		li = []
		for piece in self.pieces:
			li.append(piece.getPosition)
		return li

	def prettyPrint(self):
		"Prints a pretty representation of the board"
		hr = '- - - - - - - -'
		print hr


class Position():
	""" Position class for 1) converting from characters to numbers 
						   2) making sure given Postions are valid
	"""
	def __init__(self, file, rank):
		class F(object):
			def __init__(self, char):
				self.file = char

			def __repr__(self):
				return str(self.file)

			def __call__(self):
				return self.file

			def __add__(self, other):
				return chr(ord(self.file) + other)

			def __sub__(self, other):
				return chr(ord(self.file) - other)

			def __eq__(self, other):
				if isinstance(other, self.__class__):
					return self.file == other.file
				else:
					return False


		# Makes that the position is on the board
		if file in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h') and rank in range(1,9):
			self.file = F(file)
			self.rank = rank
		else:
			raise NameError('Invalid Board Position')

	def __eq__(self, other):
		"Equals method for Pieces"
		if isinstance(other, self.__class__):
			return self.file() == other.file() and self.rank == other.rank
		else:
			return False
	
	def __repr__(self):
		"Represent this object as a tuple pair"
		return str((self.file, self.rank))



# Pieces
class Piece(object):
	"Generic Piece class that others will extend"
	def __init__(self, army, file, rank):
		self.army = army
		self.position = Position(file, rank)
		self.moves = []
		self.threats = []
		self.attackMoves = []
		self.history = self.position

	def __repr__(self):
		return self.army + '-' + self.name + ': ' + self.position.__repr__()

	def getPosition(self):
		return self.position

	def move(self, frm, to):
		"Makes moves the Piece updates postion, history, board"
		self.rankPos = to
		self.filePos = to

	def movePossible(self, move):
		if move in self.moves:
			return True



class King(Piece):
	"Define the kings possible moves"
	def __init__(self, army, file, rank):
		super(King,self).__init__(army, file, rank)
		self.name = 'King'

	def genMoves(self):
		"Returns a list of possible moves for the King(Positions type)"
		moves = []
		pos = self.position

		# Move left+right (changing files)
		moves.extend([
			Position(pos.file(),pos.rank+1),
			Position(pos.file(),pos.rank-1),
			Position(pos.file+1,pos.rank),
			Position(pos.file-1,pos.rank)
			]) 
		# TODO: Castling 
		# Check to see if King or Rook has moved
		return moves

class Queen(Piece):
	"Define the Queen's possible moves"
	def __init__(self, army, file, rank):
		super(Queen,self).__init__(army, file, rank)
		self.name = 'Queen'

	def genMoves(self):
		"Returns a list of possible moves for the Queen(Positions type)"
		pass

class Bishop(Piece):
	"Define the Bishop's possible moves"
	def __init__(self, army, file, rank):
		super(Bishop,self).__init__(army, file, rank)
		self.name = 'Bishop'

	def genMoves(self):
		"Returns a list of possible moves for the Bishop(Positions type)"
		pass

class Knight(Piece):
	"Define the Knight's possible moves"
	def __init__(self, army, file, rank):
		super(Knight,self).__init__(army, file, rank)
		self.name = 'Knight'

	def genMoves(self):
		"Returns a list of possible moves for the Knight(Positions type)"
		pass

class Rook(Piece):
	"Define the Rook's possible moves"
	def __init__(self, army, file, rank):
		super(Rook,self).__init__(army, file, rank)
		self.name = 'Rook'

	def genMoves(self):
		"Returns a list of possible moves for the Rook(Positions type)"
		pass

class Pawn(Piece):
	"Define the Pawns's possible moves"
	def __init__(self, army, file, rank):
		super(Pawn,self).__init__(army, file, rank)
		self.name = 'Pawn'

	def genMoves(self):
		"Returns a list of possible moves for the Pawn(Positions type)"
		pass



