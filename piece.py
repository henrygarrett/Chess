class Piece():
    #sets up generic Piece class
    def __init__(self, name, square, white):
        self._name = name
        self._position = square
        self._white = white
    @property
    def white(self):
        return self._white
    @white.setter
    def white(self,colour):
        self._white = colour
    @property
    def piece_name(self):
        return self._name
    @piece_name.setter
    def piece_name(self, name):
        self._name = name
    @property
    def piece_position(self):
        return self._position
    @piece_position.setter
    def piece_position(self, position):
        self._position = position
    #checks if space is free of pieces of the same colour for a piece to move into it
    def end_blocker(self, board, command):
        if (board[command].square_piece != None) and (board[command].square_piece.white == self.white):
            return True  
        else:
            return False
    #main method for moving pieces
    def move(self, board, whitebox, blackbox, pieces):
        while True:
            #general
            command = input('\nWhere would you like to move your ' + self.__class__.__name__ + '?: ')
            #the following if and elifs check if all conditions are satisfied in order to move a piece
            if command not in board:
                print('That is not a square on the board. give coordinates. e.g. A4')
            elif command == self.piece_position._name:
                print('You are already on that square')
            #specific
            elif self.cannot_move(command):
                pass
            elif self.middle_blocker(board, command) != None:
                print('You can\'t move there. There is a ' + self.middle_blocker(board, command).__class__.__name__ + ' in the way.')
            #general
            elif self.end_blocker(board, command):
                print('You can\'t move there. There is a piece in the way.')
            #the following moves the piece
            elif board[command].square_piece == None:
                print('Moved ' + self._name + ' to ' + command) 
                self.piece_position.square_piece = None  
                self.piece_position = board[command]
                self.piece_position.square_piece = pieces[self._name]
                if isinstance(self,Rook) or isinstance(self,King):
                    self.not_moved = False
                break
            # if the target square is occupied checks if player wants to take piece, if not the players go starts from the begining
            elif board[command].square_piece != None:
                while True:
                    take = input('Do you want to take the ' + board[command].square_piece.__class__.__name__ + ' with your ' + self.__class__.__name__ + '?: ')
                    if take.upper() == ('YES' or 'NO' or 'Y' or 'N' or 'YEAH' or 'NAH' or 'YEP' or 'NOPE'):
                        break
                    else:
                        print('Please type YES or NO')


                if take.upper() == ('YES' or 'Y' or 'YEAH' or 'YEP'):
                    if board[command].square_piece.white:
                        whitebox.append(board[command].square_piece)
                    else:
                        blackbox.append(board[command].square_piece)
                    print('Moved your ' + self.__class__.__name__ + ' to ' + command + ' and taken their ' + board[command].square_piece.__class__.__name__)
                    self.piece_position.square_piece = None  
                    self.piece_position = board[command]
                    self.piece_position.square_piece = pieces[self._name]
                    if isinstance(self,Rook) or isinstance(self,King):
                        self.not_moved = False
                    break
                else:
                    print('I don\'t know how you got here. Try again')
    #this is used to check in the castling move to check if the king can move and will also be used to check if the king is in stalemate
    def attack(self, board, whitebox, blackbox, pieces, command):
        if self.cannot_move(command):
            return False
        elif self.middle_blocker(board, command) != None:
            return False
        elif self.end_blocker(board, command):
            return False
        elif board[command].square_piece != None:
            return False
        elif board[command].square_piece == None:
            return True
        else:
            print('I don\'t know how you got here. Try again')
# each of these extend the Piece class to allow for checking if the piece can move in a certain way and if there are pieces
#between the piece's starting square and its target square
class Rook(Piece):
    def __init__(self, name, square, white):
        super().__init__(name, square, white)
        self.not_moved = True
    def cannot_move(self, command):
        if (command[0] != self.piece_position._name[0]) and (command[1] != self.piece_position._name[1]):
            print('Rooks can only move up, down, left, and right')
            return True
        else:
            return False
    def middle_blocker(self, board, command):
        if command[0] == self.piece_position._name[0]:
            for n in range(int(self.piece_position._name[1])+1,int(command[1])):
                if board[command[0]+str(n)].square_piece != None:
                    return board[command[0] + str(n)].square_piece.__class__.__name__
        else:
            for n in range(ord(self.piece_position._name[0])+1,ord(command[0])):
                if board[chr(n)+ command[1]].square_piece != None:
                    return board[chr(n) + command[1]].square_piece.__class__.__name__
        return None
class King(Piece):
    def __init__(self, name, square, white):
        super().__init__(name, square, white)
        self.not_moved = True
    def cannot_move(self, command):
        if command not in self.piece_position.linked_squares:
            print('Kings can only move to a free adjacent square')
            return True
        else:
            return False
    def middle_blocker(self, board, command):
        return None
class Bishop(Piece):
    def cannot_move(self, command):
        if abs(ord(command[0]) - ord(self.piece_position._name[0])) != abs(ord(command[1]) - ord(self.piece_position._name[1])):
            print('Bishops can only move along diagionals(Must stay on the same colour)')
            return True
        else:
            return False
    def middle_blocker(self, board, command):
        if ord(command[0]) - ord(self.piece_position._name[0]) > 0:
            if ord(command[1]) - ord(self.piece_position._name[1]) > 0:
                for n in range(1,abs(ord(command[0]) - ord(self.piece_position._name[0]))):
                    if board[chr(ord(self.piece_position._name[0]) + n) + str(int(self.piece_position._name[1]) + n)].square_piece != None:
                        return board[chr(ord(self.piece_position._name[0]) + n) + str(int(self.piece_position._name[1]) + n)].square_piece
            else:
                for n in range(1,abs(ord(command[0]) - ord(self.piece_position._name[0]))):
                    if board[chr(ord(self.piece_position._name[0]) + n) + str(int(self.piece_position._name[1]) - n)].square_piece != None:
                        return board[chr(ord(self.piece_position._name[0]) + n) + str(int(self.piece_position._name[1]) - n)].square_piece
                
        else:
            if ord(command[1]) - ord(self.piece_position._name[1]) > 0:
                for n in range(1,abs(ord(command[0]) - ord(self.piece_position._name[0]))):
                    if board[chr(ord(self.piece_position._name[0]) - n) + str(int(self.piece_position._name[1]) + n)].square_piece != None:
                        return board[chr(ord(self.piece_position._name[0]) - n) + str(int(self.piece_position._name[1]) + n)].square_piece
            else:
                for n in range(1,abs(ord(command[0]) - ord(self.piece_position._name[0]))):
                    if board[chr(ord(self.piece_position._name[0]) - n) + str(int(command[1]) - n)].square_piece != None:
                        return board[chr(ord(self.piece_position._name[0]) - n) + str(int(self.piece_position._name[1]) - n)].square_piece
        return None
class Queen(Piece):
    def cannot_move(self, command):
        if (command[0] == self.piece_position._name[0]) or (command[1] == self.piece_position._name[1]):
            return False
        elif abs(ord(command[0]) - ord(self.piece_position._name[0])) == abs(ord(command[1]) - ord(self.piece_position._name[1])):
            return False
        else:
            print('Queens can move in any direction but only in straight lines')
            return True
    def middle_blocker(self, board, command):
        if command[0] == self.piece_position._name[0]:
            for n in range(int(self.piece_position._name[1])+1,int(command[1])):
                if board[command[0]+str(n)].square_piece != None:
                    return board[command[0] + str(n)].square_piece.__class__.__name__
        elif command[1] == self.piece_position._name[1]:
            for n in range(ord(self.piece_position._name[0])+1,ord(command[0])):
                if board[chr(n)+ command[1]].square_piece != None:
                    return board[chr(n) + command[1]].square_piece.__class__.__name__
        elif ord(command[0]) - ord(self.piece_position._name[0]) > 0:
            if ord(command[1]) - ord(self.piece_position._name[1]) > 0:
                for n in range(1,abs(ord(command[0]) - ord(self.piece_position._name[0]))):
                    if board[chr(ord(self.piece_position._name[0]) + n) + str(int(self.piece_position._name[1]) + n)].square_piece != None:
                        return board[chr(ord(self.piece_position._name[0]) + n) + str(int(self.piece_position._name[1]) + n)].square_piece
            else:
                for n in range(1,abs(ord(command[0]) - ord(self.piece_position._name[0]))):
                    if board[chr(ord(self.piece_position._name[0]) + n) + str(int(self.piece_position._name[1]) - n)].square_piece != None:
                        return board[chr(ord(self.piece_position._name[0]) + n) + str(int(self.piece_position._name[1]) - n)].square_piece
                
        else:
            if ord(command[1]) - ord(self.piece_position._name[1]) > 0:
                for n in range(1,abs(ord(command[0]) - ord(self.piece_position._name[0]))):
                    if board[chr(ord(self.piece_position._name[0]) - n) + str(int(self.piece_position._name[1]) + n)].square_piece != None:
                        return board[chr(ord(self.piece_position._name[0]) - n) + str(int(self.piece_position._name[1]) + n)].square_piece
            else:
                for n in range(1,abs(ord(command[0]) - ord(self.piece_position._name[0]))):
                    if board[chr(ord(self.piece_position._name[0]) - n) + str(int(command[1]) - n)].square_piece != None:
                        return board[chr(ord(self.piece_position._name[0]) - n) + str(int(self.piece_position._name[1]) - n)].square_piece
        return None
class Knight(Piece): 
    def cannot_move(self, command):
        if abs((ord(command[0]) - ord(self.piece_position._name[0]))*(ord(command[1]) - ord(self.piece_position._name[1]))) == 2:
            return False
        else:
            print('Knights can only move one square up, down, left, or right, then one square diagionally away')
            return True

    def middle_blocker(self, board, command):
        return None
class Pawn(Piece):
    #rewrote the move and attack method completely for pawns as their movement is very different to other pieces
    def move(self, board, whitebox, blackbox, pieces):
            while True:
                #general
                command = input('\nWhere would you like to move your Pawn?: ')
                if command not in board:
                    print('That is not a square on the board. give coordinates. e.g. A4')
                elif command == self.piece_position._name:
                    print('You are already on that square')
                elif int(command[1]) not in [int(self.piece_position._name[1])+2*self.white-1,int(self.piece_position._name[1])+ 2*(2*self.white-1)] or ord(command[0]) not in [ord(self.piece_position._name[0]), ord(self.piece_position._name[0])+1, ord(self.piece_position._name[0])-1]:
                    print('Pawns can only move forward one space or attack diagonally foward one space. Exception on their first turn they can move foward two spaces')
                elif self.end_blocker(board, command):
                    print('You can\'t move there. There is a piece in the way.')

                elif (command[0] == self.piece_position._name[0]) and (int(command[1]) == int(self.piece_position._name[1])+2*self.white-1) and board[command].square_piece == None:
                    print('Moved ' + self._name + ' to ' + command) 
                    self.piece_position.square_piece = None  
                    self.piece_position = board[command]
                    self.piece_position.square_piece = pieces[self._name]
                    break
                elif (self.piece_position._name[1] == '2' or '7') and (command[0] == self.piece_position._name[0]) and (int(command[1]) == int(self.piece_position._name[1])+2*(2*self.white-1)) and board[command].square_piece == None:
                    print('Moved ' + self._name + ' to ' + command) 
                    self.piece_position.square_piece = None  
                    self.piece_position = board[command]
                    self.piece_position.square_piece = pieces[self._name]
                    break
                elif (int(command[1]) != int(self.piece_position._name[1])+2*(2*self.white-1)):
                    while True:
                        take = input('Do you want to take the ' + board[command].square_piece.__class__.__name__ + ' with your ' + self.__class__.__name__ + '?: ')
                        if take.upper() == ('YES' or 'NO' or 'Y' or 'N' or 'YEAH' or 'NAH' or 'YEP' or 'NOPE'):
                            break
                        else:
                            print('Please type YES or NO')


                    if take.upper() == ('YES' or 'Y' or 'YEAH' or 'YEP'):
                        if board[command].square_piece.white:
                            whitebox.append(board[command].square_piece)
                        else:
                            blackbox.append(board[command].square_piece)
                        print('Moved ' + self._name + ' to ' + command)
                        self.piece_position.square_piece = None  
                        self.piece_position = board[command]
                        self.piece_position.square_piece = pieces[self._name]
                        break
                    else:
                        print('No move')
                else:
                    print('I don\'t know how you got here. Try again')
                    
    def attack(self, board, whitebox, blackbox, pieces, command):
        if int(command[1]) not in [int(self.piece_position._name[1])+2*self.white-1,int(self.piece_position._name[1])+ 2*(2*self.white-1)] or ord(command[0]) not in [ord(self.piece_position._name[0]), ord(self.piece_position._name[0])+1, ord(self.piece_position._name[0])-1]:
            return False
        elif self.end_blocker(board, command):
            return False
        elif (command[0] == self.piece_position._name[0]) and (int(command[1]) == int(self.piece_position._name[1])+2*self.white-1) and board[command].square_piece == None:
            return True
        elif (self.piece_position._name[1] == '2' or '7') and (command[0] == self.piece_position._name[0]) and (int(command[1]) == int(self.piece_position._name[1])+2*(2*self.white-1)) and board[command].square_piece == None:
            return True
        elif (int(command[1]) != int(self.piece_position._name[1])+2*(2*self.white-1)):
            return True
        else:
            print('I don\'t know how you got here. Try again')

















