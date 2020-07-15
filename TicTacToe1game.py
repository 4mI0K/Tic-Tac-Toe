board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

playing = 1
turns = 0
gl, gs, gd, s, sl, sd, dl, ds, dd = False, False, False, False, False, False, False, False, False


while playing:
    xo = input()
    if  xo.lower() == 'xgd':
        if gd == False:
            gd = True
            board[0][2] = 1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'xgs':
        if gs == False:
            gs = True
            board[0][1] = 1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'xgl':
        if gl == False:
            gl = True
            board[0][0] = 1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'xsd':
        if sd == False:
            sd = True
            board[1][2] = 1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'xs':
        if s == False:
            s = True
            board[1][1] = 1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'xsl':
        if sl == False:
            sl = True
            board[1][0] = 1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'xdl':
        if dl == False:
            dl = True
            board[2][0] = 1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'xds':
        if ds == False:
            ds = True
            board[2][1] = 1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'xdd':
        if dd == False:
            dd = True
            board[2][2] = 1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'ogl':
        if gl == False:
            gl = True
            board[0][0] = -1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'ogd':
        if gd == False:
            gd = True
            board[0][2] = -1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'ogs':
        if gs == False:
            gs = True
            board[0][1] = -1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'os':
        if s == False:
            s = True
            board[1][1] = -1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'ods':
        if ds == False:
            ds = True
            board[2][1] = -1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'osl':
        if sl == False:
            sl = True
            board[1][0] = -1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'osd':
        if sd == False:
            sd = True
            board[1][2] = -1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'odl':
        if dl == False:
            dl = True
            board[2][0] = -1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'odd':
        if dd == False:
            dd = True
            board[2][2] = -1
            turns += 1
        else:
            print("It's already taken")
    elif xo.lower() == 'reset':
        board[0] = [0, 0, 0]
        board[1] = [0, 0, 0]
        board[2] = [0, 0, 0]
        turns -= turns 
        gl, gs, gd, s, sl, sd, dl, ds, dd = False, False, False, False, False, False, False, False, False
    elif xo.lower() == 'exit':
        exit()
    else:
        print('i dont understand you')

    for cell in board:
        if board[0][0] == 1 and board[0][0] == board[0][1] and board[0][0] == board[0][2] or board[1][0] == 1 and board[1][0] == board[1][1] and board[1][0] == board[1][2] or board[2][0] == 1 and board[2][0] == board[2][1] and board[2][0] == board[2][2]:
            for cell in board:
                print(cell)
            print('iks je pobedio')
            exit()
        elif board[0][0] == 1 and board[0][0] == board[1][0] and board[0][0] == board[2][0] or board[0][1] == 1 and board[0][1] == board[1][1] and board[0][1] == board[2][1] or board[0][2] == 1 and board[0][2] == board[1][2] and board[0][2] == board[2][2]:
            for cell in board:
                print(cell)
            print('iks je pobedio')
            exit()
        elif board[0][0] == 1 and board[0][0] == board[1][1] and board[0][0] == board[2][2] or board[0][2] == 1 and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
            for cell in board:
                print(cell)
            print('iks je pobedio')
            exit()
        elif board[0][0] == -1 and board[0][0] == board[0][1] and board[0][0] == board[0][2] or board[1][0] == -1 and board[1][0] == board[1][1] and board[1][0] == board[1][2] or board[2][0] == -1 and board[2][0] == board[2][1] and board[2][0] == board[2][2]:
            for cell in board:
                print(cell)
            print('oks je pobedio')
            exit()
        elif board[0][0] == -1 and board[0][0] == board[1][0] and board[0][0] == board[2][0] or board[0][1] == -1 and board[0][1] == board[1][1] and board[0][1] == board[2][1] or board[0][2] == -1 and board[0][2] == board[1][2] and board[0][2] == board[2][2]:
            for cell in board:
                print(cell)
            print('oks je pobedio')
            exit()
        elif board[0][0] == -1 and board[0][0] == board[1][1] and board[0][0] == board[2][2] or board[0][2] == -1 and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
            for cell in board:
                print(cell)
            print('oks je pobedio')
            exit()
        elif turns == 9:
            for cell in board:
                print(cell)
            exit()
        print(cell)
        
