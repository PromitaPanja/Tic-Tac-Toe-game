#TIC-TAC-TOE game using python
grid = [[1,2,3],
        [4,5,6],
        [7,8,9]]

def welcome(): #first - display
    print("!! Welcome !!")
    for i in range(3): #displaying the grid
        for j in range(3):
            print(grid[i][j],"| ",end="")
            grid[i][j]=" "
        print("\n- - - - - -")
    print("player-1 is 'x' and player-2 is '0'")

def check(i,j):
    if grid[i][j] == " ":
        return True
    return False

def convert(a):
    if(a==1):
        return 0,0
    elif a==2:
        return 0,1
    elif a==3:
        return 0,2
    elif a==4:
        return 1,0
    elif a==5:
        return 1,1
    elif a==6:
        return 1,2
    elif a==7:
        return 2,0
    elif a==8:
        return 2,1
    elif a==9:
        return 2,2

def turn(player): #make a turn
    while(True):
        a=int(input(f"Choose the cell {player}: "))
        i,j = convert(a)
        if not check(i,j):
            print("The cell is already filled, try another!")
        else:
            break
    entry(i,j,player) #enter the value in grid
    #checking for winner
    if(row_win(i,j,player) or cross_diag(i,j,player) or
       column_win(i,j,player) or diag_win(i,j,player)):
        return 0
    if player=="player-1":
        return "player-2"
    else:
        return "player-1"


def entry(i,j,player): #value is entered
    if player=="player-1":
        grid[i][j] = 'x'
    else:
        grid[i][j] = '0'
    for i in range(3):
        for j in range(3):
            print(grid[i][j],"| ",end="")
        print("\n- - - - - -")

def row_win(i,j,player):
    if player == 'player-1':
        sign = 'x'
    else:
        sign='0'
    for jj in range(3):#row-check
        if grid[i][jj]!=sign:
            return False
    print(f"Row-won by {player}")
    return True
def column_win(i,j,player):
    if player == 'player-1':
        sign = 'x'
    else:
        sign='0'
    for ii in range(3):#column-check
        if grid[ii][j]!=sign:
            return False
    print(f"Column-won by {player}")
    return True
def diag_win(i,j,player):
    if (i==1 and (j==0 or j==2))or(j==1 and(i==0 or i==2)):
        return 0
    if player == 'player-1':
        sign = 'x'
    else:
        sign='0'
    for ii in range(3):#diagonal-check
        if grid[ii][ii]!=sign:
            return False
    print(f"Diagonal-won by {player}")
    return True
def cross_diag(i,j,player):
    if (i==1 and (j==0 or j==2))or(j==1 and(i==0 or i==2)):
        return 0
    if player == 'player-1':
        sign = 'x'
    else:
        sign='0'
    for ii in range(3):
        if grid[ii][2-ii]!=sign:
            return 0
    print(f"cross diagonal win by {player}")
    return 1




#main
welcome()
count = 0
player = "player-1"
flag=0
while(count<9):
    player = turn(player)
    if(player==0):
        flag=1
        break
    count+=1
if flag==0:
    print("Game is Draw!")








