import turtle as t
import random as r
wn = t.Screen()
wn.setup(800,800)
wn.addshape("circle.png")
wn.addshape("x2.png")
wn.bgpic("tictactoe2.png")
opponent = t.Turtle()
opponent.penup()
opponent.shape("circle.png")
opponent.speed(0)
opponent.goto(1000,1000)
player = t.Turtle()
player.penup()
player.shape("x2.png")
player.speed(0)
player.goto(1000,1000)
t.color('red')
t.penup()
t.ht()
t.goto(-170,150)
xmin = -t.window_width()/2
xmax = t.window_width()/2
ymin = -t.window_height()/2
ymax = t.window_height()/2
firstx = xmin + 10
firsty = ymax - 10
stepx = 190
stepy = 200
lboard = []
turn = 0
win = 0
freeze = False
for row in range(3):
  lboard.append([" "]*3)
  print lboard[row]
def convert(row,col):
  global firstx, firsty, stepx, stepy, lboard, xmax, xmin, ymax, ymin
  b_x = (firstx +  (stepx / 2) + col * stepx)
  b_y = (firsty -  (stepy / 2) - row * stepy)
  return b_x, b_y
def check_win():
  global firstx, firsty, stepx, stepy, lboard, xmax, xmin, ymax, ymin, turn, win
  if lboard[0][0] == 'X' and lboard[0][1] == 'X' and lboard[0][2] == 'X':
    win = 1
  if lboard[0][0] == 'O' and lboard[0][1] == 'O' and lboard[0][2] == 'O':
    win = 2
  if lboard[1][0] == 'X' and lboard[1][1] == 'X' and lboard[1][2] == 'X':
    win = 1
  if lboard[1][0] == 'O' and lboard[1][1] == 'O' and lboard[1][2] == 'O':
    win = 2
  if lboard[2][0] == 'X' and lboard[2][1] == 'X' and lboard[2][2] == 'X':
    win = 1
  if lboard[2][0] == 'O' and lboard[2][1] == 'O' and lboard[2][2] == 'O':
    win = 2
  if lboard[0][0] == 'X' and lboard[1][0] == 'X' and lboard[2][0] == 'X':
    win = 1
  if lboard[0][0] == 'O' and lboard[1][0] == 'O' and lboard[2][0] == 'O':
    win = 2
  if lboard[0][1] == 'X' and lboard[1][1] == 'X' and lboard[2][1] == 'X':
    win = 1
  if lboard[0][1] == 'O' and lboard[1][1] == 'O' and lboard[2][1] == 'O':
    win = 2
  if lboard[0][2] == 'X' and lboard[1][2] == 'X' and lboard[2][2] == 'X':
    win = 1
  if lboard[0][2] == 'O' and lboard[1][2] == 'O' and lboard[2][2] == 'O':
    win = 2
  if lboard[0][0] == 'X' and lboard[1][1] == 'X' and lboard[2][2] == 'X':
    win = 1
  if lboard[0][0] == 'O' and lboard[1][1] == 'O' and lboard[2][2] == 'O':
    win = 2
  if lboard[2][0] == 'X' and lboard[1][1] == 'X' and lboard[0][2] == 'X':
    win = 1
  if lboard[2][0] == 'O' and lboard[1][1] == 'O' and lboard[0][2] == 'O':
    win = 2
  
def click_board(x,y):
  global firstx, firsty, stepx, stepy, lboard, xmax, xmin, ymax, ymin, turn, freeze, first
  if freeze == False:
    if first == 'p':
      for row in range(3):
        for col in  range(3):
          if lboard[row][col] == 'O' or lboard[row][col] == 'X':
            pass
          else:
            if (x > firstx + col* stepx) and (x < firstx + (col + 1)*stepx) and (y < firsty - row* stepy) and (y > firsty - (row + 1)*stepy) :
              convert_both('X', player, row, col)
              turn += 1   
              win = check_win()
              print turn
              if win == 0 and turn >= 9:
                print "Draw"
                t.clear()
                t.write("Draw", font = ("arial",40,"bold"))
                freeze = True
              if win == 1:
                print "Win"
                t.clear()
                t.write("Win", font = ("arial",40,"bold"))
                freeze =  True
              if win == 2:
                print "Loss"
                t.clear()
                t.write("Loss", font = ("arial",40,"bold"))
                freeze = True
              first ='c'
              if freeze == True:
                wn.onclick(None)
              #   return None
    for row in range(3):
      print (lboard[row])

def convert_both(turnholder, player_t, row, col):
  global lboard
  lboard[row][col] = turnholder
  opponent1 = player_t.clone()
  opponent1.penup()
  opponent1.st()
  b_x, b_y = convert(row, col)
  opponent1.goto(b_x, b_y)


count = 0
human = 'X'
computer = 'O'

def winning(board, player):
  jump = 0
  for row in range(3):
    if board[row + jump] == player and board[row + 1 + jump] == player and  board[row + 2 + jump] == player:
      return True
    jump += 2
  for col in range(3):
    if board[col] == player and board[col + 3] == player and board[col + 6] == player:
      return True
  if board[0] == player and board[4] == player and board[8] == player:
    return True
  if board[6] == player and board[4] == player and board[2] == player:
    return True
  return False
#win = winning(originalboard, human)
#print win

def emptyindexes(board):
  emptyindex = []
  for i in range(len(board)):
    if board[i] != 'X' and board[i] != 'O':
      emptyindex.append(board[i])
  return emptyindex
  
def minimax(newboard, player):
  global human, computer, count
  count += 1
  availspots = emptyindexes(newboard)
  
  if winning(newboard, human):
    result = {"index": None, "score": -10}
    return result
  elif winning(newboard, computer):
    result = {"index": None, "score": 10}
    return result
  elif (len(availspots) == 0):
    result = {"index": None, "score": 0}
    return result
  moves = []
  for i in range(len(availspots)):
    move = {}
    move["index"] = newboard[availspots[i]]
    newboard[availspots[i]] = player
    if player == computer:
      result = minimax(newboard, human)
      move["score"] = result["score"]
    elif player == human:
      result = minimax(newboard, computer)
      move["score"] = result["score"]
    newboard[availspots[i]] = move["index"]
    moves.append(move)
  if player == computer:
    bestscore = -10000
    for i in range(len(moves)):
      if moves[i]["score"] > bestscore:
        bestscore = moves[i]["score"]
        bestmove = i
  else:
    bestscore = 10000
    for i in range(len(moves)):
      if moves[i]["score"] < bestscore:
        bestscore = moves[i]["score"]
        bestmove = i
  return moves[bestmove]
  
def ai_play():
  global lboard, count, human, computer
  originalboard = []
  for row in range(3):
    for col in range(3):
      if lboard[row][col] == " ":
        originalboard.append((row * 3) + col)
      else:
        originalboard.append(lboard[row][col])
  print originalboard
  bestmove = minimax(originalboard, computer)
  return bestmove
  

  
      
first = input("Who goes first? Enter 'p' for the player or 'c' for the computer").lower()
wn.onclick(click_board)
#wn.onkey(ai_play,"space")
#wn.listen()
wn.mainloop()
while True:
  if first == 'c':
    bestmove = ai_play()
    print bestmove
    if bestmove["index"] != None:
      row = int(bestmove["index"] / 3)
      col = int(bestmove["index"] % 3)
      print 'r',row,col
      lboard[row][col] = "O"
      convert_both("O", opponent, row, col)
    turn += 1
    check_win()
    print turn
    if win == 0 and turn >= 9:
      print "Draw"
      t.clear()
      t.write("Draw", font = ("arial",40,"bold"))
      freeze = True
    if win == 1:
      print "Win"
      t.clear()
      t.write("Win", font = ("arial",40,"bold"))
      freeze =  True
    if win == 2:
      print "Loss"
      t.clear()
      t.write("Loss", font = ("arial",40,"bold"))
      freeze = True
    first = 'p'
    if freeze == True:
      break
    
