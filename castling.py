# this is to enable castling but is not quite finished yet
def castling(short,turn, whitebox, blackbox):
    if short:
        if turn%2 == 1:
            king = pieces['kingw']
            castle = pieces['rookw2']
            box = whitebox
        else:
            king = pieces['kingb']
            castle = pieces['rookb2']
            box = blackbox
    else:
        if turn%2 == 1:
            king = pieces['kingw']
            castle = pieces['rookw1']
            box = whitebox
        else:
            king = pieces['kingb']
            castle = pieces['rookb1']
            box = blackbox

    if castle in box:
        print('Your Rook has been taken so you cannot castle')
        return False
    elif not king.not_moved:
        print('You have moved your King so you cannot castle')
        return False
    elif not castle.not_moved:
        print('You have moved your Castle so you cannot castle')
        False
    elif short and board['F'+ king._position._name[1]]._piece != None:
        block = board['F'+ king._position._name[1]]._piece.__class__.__name__
        print('There is a ' + block +  ' on square F'+ king._position._name[1] + ' so you cannot castle')
        return False
    elif short and board['G'+ king._position._name[1]]._piece != None:
        block = board['G'+ king._position._name[1]]._piece.__class__.__name__
        print('There is a ' + block +  ' on square G'+ king._position._name[1] + ' so you cannot castle')
        return False

    elif not short and board['B'+ king._position._name[1]]._piece != None:
        block = board['B'+ king._position._name[1]]._piece.__class__.__name__
        print('There is a ' + block + ' on square B'+ king._position._name[1] + ' so you cannot castle')
        return False
    elif not short and board['C'+ king._position._name[1]]._piece != None:
        block = board['C'+ king._position._name[1]]._piece.__class__.__name__
        print('There is a ' + block + ' on square C'+ king._position._name[1] + ' so you cannot castle')
        return False
    elif not short and board['D'+ king._position._name[1]]._piece != None:
        block = board['D'+ king._position._name[1]]._piece.__class__.__name__
        print('There is a ' + block + ' on square D'+ king._position._name[1] + ' so you cannot castle')
        return False
    
