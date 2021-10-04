class Square():
    def __init__(self, name, row, column):
        self._name = name
        self.linked_squares = {}
        self.row = row
        self.column = column
        self._piece = None
    def __str__(self):
        return self.name

    @property
    def named(self):
        return self._name
    @named.setter
    def named(self, name):
        self._name = name

    @property
    def square_piece(self):
        return self._piece
    @square_piece.setter
    def square_piece(self, piece):
        self._piece = piece
    #this was for the original way I was planning to move pieces but I found an easier way and now this is only used by King pieces
    def link(self, name, position, board, boardcall):
        if '8' not in name:
            self.linked_squares['N'] = board[boardcall[position - 8]]

        if ('8' and 'H') not in name:
           self.linked_squares['NE'] = board[boardcall[position - 7]]

        if 'H' not in name:
            self.linked_squares['E'] = board[boardcall[position + 1]]

        if ('1' not in name) and ('H' not in name):
            
            self.linked_squares['SE'] = board[boardcall[position + 9]]

        if '1' not in name:
           self.linked_squares['S'] = board[boardcall[position + 8]]

        if ('1' not in name) and ('A' not in name):
            self.linked_squares['SW'] = board[boardcall[position + 7]]

        if 'A' not in name:
            self.linked_squares['W'] = board[boardcall[position - 1]]

        if ('8' and 'A') not in name:
           self.linked_squares['NW'] = board[boardcall[position - 9]]

