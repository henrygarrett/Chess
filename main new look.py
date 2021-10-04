#stalemate
#castling- once per game
#pawn en passant
#remove link method- need to update king move method
#remove boardcall
from square import Square
from piece import Queen, King, Rook, Knight, Bishop, Pawn
#from castling import castling


#creating the board
board = {}
boardcall = []
for i, n in enumerate(range(8,0,-1)):
    for m in 'ABCDEFGH':
        board[m + str(n)] = Square(m + str(n),n,m)
        boardcall.append(m + str(n))
#links squares enabling king to move
for place, square in enumerate(boardcall):
    board[square].link(square, place, board, boardcall)


pieces = {}
#creating white pieces
whitebox = []#list of taken white pieces
pieces['kingw'] = King('kingw', board['E1'], True)
board['E1'].square_piece = pieces['kingw']
pieces['queenw'] = Queen('queenw', board['D1'], True)
board['D1'].square_piece = pieces['queenw']
pieces['bishopw1'] = Bishop('bishopw1', board['C1'],True)
board['C1'].square_piece = pieces['bishopw1']
pieces['bishopw2'] = Bishop('bishopw2', board['F1'],True)
board['F1'].square_piece = pieces['bishopw2']
pieces['knightw1'] = Knight('knightw1', board['B1'],True)
board['B1'].square_piece = pieces['knightw1']
pieces['knightw2'] = Knight('knightw2', board['G1'],True)
board['G1'].square_piece = pieces['knightw2']
pieces['rookw1'] = Rook('rookw1', board['A1'],True)
board['A1'].square_piece = pieces['rookw1']
pieces['rookw2'] = Rook('rookw2', board['H1'],True)
board['H1'].square_piece = pieces['rookw2']
for n in range(1,9):
    pieces['pawnw' + str(n)] = Pawn('pawnw' +str(n), board[chr(ord(str(n))+16)+'2'],True)
    board[chr(ord(str(n))+16)+'2'].square_piece = pieces['pawnw' + str(n)]


#creating black pieces
blackbox = []#list of taken black pieces
pieces['kingb'] = King('kingb', board['E8'], False)
board['E8'].square_piece = pieces['kingb']
pieces['queenb'] = Queen('queenb', board['D8'], False)
board['D8'].square_piece = pieces['queenb']
pieces['bishopb1'] = Bishop('bishopb1', board['C8'],False)
board['C8'].square_piece = pieces['bishopb1']
pieces['bishopb2'] = Bishop('bishopb2', board['F8'],False)
board['F8'].square_piece = pieces['bishopb2']
pieces['knightb1'] = Knight('knightb1', board['B8'],False)
board['B8'].square_piece = pieces['knightb1']
pieces['knightb2'] = Knight('knightb2', board['G8'],False)
board['G8'].square_piece = pieces['knightb2']
pieces['rookb1'] = Rook('rookb1', board['A8'],False)
board['A8'].square_piece = pieces['rookb1']
pieces['rookb2'] = Rook('rookb2', board['H8'],False)
board['H8'].square_piece = pieces['rookb1']
for n in range(1,9):
    pieces['pawnb' + str(n)] = Pawn('pawnb' +str(n), board[chr(ord(str(n))+16)+'7'],False)
    board[chr(ord(str(n))+16)+'7'].square_piece = pieces['pawnb' + str(n)]


#game loop
turn = 1
while True:
    #printing the board
    for place, square in enumerate(boardcall):
        #prints checkers squares for empty spaces on the board
        if place%8 == 0:
            print(str(square[1]) + ' ',end = '')
        if board[square].square_piece == None:
            if place%2 == 0 and (place//8)%2 == 0:
                print('X ',end = '')
            elif place%2 == 0 and (place//8)%2 == 1:
                print('X ', end = '')
            elif place%2 == 1 and (place//8)%2 == 0:
                print('X ',end = '')
            elif place%2 == 1 and (place//8)%2 == 1:
                print('X ', end = '')
        #prints the chess pieces
        elif isinstance(board[square].square_piece, Pawn):
            if board[square].square_piece._white:
                print('P ', end = '')
            else:
                print('p ', end = '')
        elif isinstance(board[square].square_piece, Rook):
            if board[square].square_piece._white:
                print('R ',end = '')
            else:
                print('r ',end = '')
        elif isinstance(board[square].square_piece, Knight):
            if board[square].square_piece._white:
                print('N ',end = '')
            else:
                print('n ',end = '')
        elif isinstance(board[square].square_piece, King):
            if board[square].square_piece._white:
                print('K ',end = '')
            else:
                print('k ',end = '')
        elif isinstance(board[square].square_piece, Queen):
            if board[square].square_piece._white:
                print('Q ',end = '')
            else:
                print('q ',end = '')
        elif isinstance(board[square].square_piece, Bishop):
            if board[square].square_piece._white:
                print('B ',end = '')
            else:
                print('b ',end = '')
        
        #prints all the pieces black has lost
        if square == 'H6':
            print(' Black Losses:',end = '')
        if square == 'H5':
            for n in blackbox:
                print(' ' + n.piece_name + ' ',end = '')
        #prints all the pieces white has lost
        if square == 'H4':
            print(' White Losses:',end = '')
        if square == 'H3':
            for n in whitebox:
                print(' ' + n.piece_name + ' ',end = '')
        if place%8 == 7 and place != 0:
            print('')
    print('  A B C D E F G H')


    if turn%2 == 0:
        print('Black\'s turn')
        white = False
    else:
        print('White\'s turn')
        white = True
    while True:
        chosen_piece = input('Which piece would you like to move? (Type the square it\'s on in capitals.e.g. A3): ')

        #these calls don't work yet as I haven't finished the methods for them
##        if chosen_piece == 'CS':
##            if castling(True, turn, whitebox, blackbox):
##                break
##        if chosen_piece == 'CL':
##            if castling(False, turn, whitebox, blackbox):
##                break

        #redefines chosen_piece from the users input to an instant of the required object piece
        if chosen_piece in board:
            if board[chosen_piece].square_piece != None:
                if white and board[chosen_piece].square_piece._white:
                    chosen_piece = board[chosen_piece].square_piece
                    break
                elif not white and not board[chosen_piece].square_piece._white:
                    chosen_piece = board[chosen_piece].square_piece
                    break
                elif white and not board[chosen_piece].square_piece._white:
                    print('That piece is not white. Please pick a white piece.')
                elif not white and board[chosen_piece].square_piece._white:
                    print('That piece is not black. Please pick a black piece.')  
            else:
                print('Sorry there is no piece on that square')
        else:
            print('Sorry that is not a square on the board')
    #moves the chosen piece if it is possible to
    chosen_piece.move(board, whitebox, blackbox, pieces)
    if pieces['kingw'] in whitebox:
        print('Black Wins')
        break
    if pieces['kingb'] in blackbox:
        print('White Wins')
        break
    for piece in pieces:
        breaker = False
        #below code allows for pawn promotion when it reaches the other end of the board
        if isinstance(pieces[piece],Pawn) and ((pieces[piece]._position._name[1] == '1') or (pieces[piece]._position._name[1] == '8')):
            while True:
                new_piece = input('What would you like to promote your Pawn to? ')
                if new_piece.capitalize() not in ['Queen','Bishop','Knight','Rook']:
                    print('Please choose one of: Queen, Bishop, Knight, or Rook')
                else:
                    if chosen_piece._white:
                        name = new_piece.lower() + 'w' + str(turn)
                    else:
                        name = new_piece.lower() + 'b' + str(turn)
                    if new_piece.capitalize() == 'Queen':
                        pieces[name] = Queen(name, board[chosen_piece._position._name], chosen_piece._white)
                        board[chosen_piece._position._name].square_piece = pieces[name]
                        breaker = True
                        break
                    elif new_piece.capitalize() == 'Bishop':
                        pieces[name] = Bishop(name, board[chosen_piece._position._name], chosen_piece._white)
                        board[chosen_piece._position._name].square_piece = pieces[name]
                        breaker = True
                        break
                    elif new_piece.capitalize() == 'Knight':
                        pieces[name] = Knight(name, board[chosen_piece._position._name], chosen_piece._white)
                        board[chosen_piece._position._name].square_piece = pieces[name]
                        breaker = True
                        break
                    elif new_piece.capitalize() == 'Rook':
                        pieces[name] = Rook(name, board[chosen_piece._position._name], chosen_piece._white)
                        board[chosen_piece._position._name].square_piece = pieces[name]
                        breaker = True
                        break
        if breaker:
            break
                        
    turn +=1
