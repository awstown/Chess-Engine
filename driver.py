#!/usr/bin/python

import chess

a = chess.Board()
b = a.getPiecePositions()

c = a.prettyPrint()

a.pieces[-2].genMoves(a)