def hasSomeoneWon():
  if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
    return True
  if board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
    return True
  if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
    return True
  if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
    return True
  if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
    return True
  if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
    return True
  if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
    return True
  if board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
    return True
  if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
    return True
  if board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
    return True
  if board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
    return True
  if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
    return True
  if board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
    return True
  if board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
    return True
  if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
    return True
  if board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
    return True
  return False


def noMoreEmptySpaces():
  if board[0][0] != "-" and board[0][1] != "-" and board[0][2] != "-" and board[1][0] != "-" and board[1][1] != "-" and board[1][2] != "-" and board[2][0] != "-" and board[2][1] != "-" and board[2][2] != "-":
    return True 
  return False 

def isGameOver():
  return hasSomeoneWon() or noMoreEmptySpaces()
def shouldPlayHorizontally(row):
  if board[row][0] != "-" and board[row][1] != "-" and board[row][2] != "-" : 
    return False
  if board[row][0] == "X" or board[row][1] == "X" or board[row][2] == "X" :
    return False
  else: 
    return True
def shouldPlayVertically(column):
  if board[0][column] != "-" and board[1][column] != "-" and board[2][column] != "-" : 
    return False
  if board[0][column] == "X" or board[1][column] == "X" or board[2][column] == "X" :
    return False
  else: 
    return True
  return
def playAnywhere():
  if board[0][0] == "-":
    board[0][0] = "X"
  elif board[0][1] == "-":
    board[0][1] = "X" 
  elif board[0][2] == "-":
    board[0][2] = "X"
  elif board[1][0] == "-":
    board[1][0] = "X"
  elif board[1][1] == "-":
    board[1][1] = "X"
  elif board[1][2] == "-":
    board[1][2] = "X"
  elif board[2][0] == "-":
    board[2][0] = "X"
  elif board[2][1] == "-":
    board[2][1] = "X"
  elif board[2][2] == "-":
    board[2][2] = "X" 
  return

def playHorizontally(row):
  if board[row][0] == "-":
    board[row][0] = "X"
  elif board[row][1] == "-":
   board[row][1] = "X"
  elif board[row][2] == "-":
   board[row][2] = "X"

def playVertically(column):
  if board[0][column] == "-":
    board[0][column] = "X"
  elif board[1][column] == "-":
    board[1][column] = "X"
  elif board[2][column] == "-":
     board[2][column] = "X"

def mustPlayHorizontally(row):
  if board[row][0] != "-" and board[row][1] != "-" and board[row][2] != "-" : 
    return False
  if (board[row][0] == 'O' and board[row][1] == 'O') or (board[row][0] == 'O' and board[row][2] == 'O') or (board[row][1] == 'O' and board[row][2] == 'O'):
    return True
  return False

def mustPlayVertically(column):
  if board[0][column] != "-" and board[1][column] != "-" and board[2][column] != "-" : 
    return False
  if (board[0][column] == 'O' and board[1][column] == 'O') or (board[0][column] == 'O' and board[2][column] == 'O') or (board[1][column] == 'O' and board[2][column] == 'O'):
    return True
  return False

board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]
board[1][1] = "X"
print(board)
while not isGameOver() :
  opponentCell = [int(x) for x in input("enter your cell: ").split(",")]
  row = opponentCell[0]
  column = opponentCell[1]
  if board[row][column] != "-":
    print("already occupied, pick again ")
    print(board)
    continue
  board[row][column] = "O"
  if mustPlayHorizontally(row):
    playHorizontally(row)
  elif mustPlayVertically(column):
    playVertically(column)
  elif shouldPlayHorizontally(row):
    playHorizontally(row)
  elif shouldPlayVertically(column):
    playVertically(column)
  else:
    playAnywhere()
  print(board)
print("Game Over ")
