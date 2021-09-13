import turtle as t
import random as r
#https://repl.it/@AlexRose1/TicTacToe-1
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
  elif lboard[0][0] == 'O' and lboard[0][1] == 'O' and lboard[0][2] == 'O':
    win = 2
  elif lboard[1][0] == 'X' and lboard[1][1] == 'X' and lboard[1][2] == 'X':
    win = 1
  elif lboard[1][0] == 'O' and lboard[1][1] == 'O' and lboard[1][2] == 'O':
    win = 2
  elif lboard[2][0] == 'X' and lboard[2][1] == 'X' and lboard[2][2] == 'X':
    win = 1
  elif lboard[2][0] == 'O' and lboard[2][1] == 'O' and lboard[2][2] == 'O':
    win = 2
  elif lboard[0][0] == 'X' and lboard[1][0] == 'X' and lboard[2][0] == 'X':
    win = 1
  elif lboard[0][0] == 'O' and lboard[1][0] == 'O' and lboard[2][0] == 'O':
    win = 2
  elif lboard[0][1] == 'X' and lboard[1][1] == 'X' and lboard[2][1] == 'X':
    win = 1
  elif lboard[0][1] == 'O' and lboard[1][1] == 'O' and lboard[2][1] == 'O':
    win = 2
  elif lboard[0][2] == 'X' and lboard[1][2] == 'X' and lboard[2][2] == 'X':
    win = 1
  elif lboard[0][2] == 'O' and lboard[1][2] == 'O' and lboard[2][2] == 'O':
    win = 2
  elif lboard[0][0] == 'X' and lboard[1][1] == 'X' and lboard[2][2] == 'X':
    win = 1
  elif lboard[0][0] == 'O' and lboard[1][1] == 'O' and lboard[2][2] == 'O':
    win = 2
  elif lboard[2][0] == 'X' and lboard[1][1] == 'X' and lboard[0][2] == 'X':
    win = 1
  elif lboard[2][0] == 'O' and lboard[1][1] == 'O' and lboard[0][2] == 'O':
    win = 2
  else:
    win = 0
  
def click_board(x,y):
  global firstx, firsty, stepx, stepy, lboard, xmax, xmin, ymax, ymin, turn, freeze, first, win
  if freeze == False:
    if first == 'p' or first != 'p':
      for row in range(3):
        for col in  range(3):
          if lboard[row][col] == 'O' or lboard[row][col] == 'X':
            pass
          else:
            if (x > firstx + col* stepx) and (x < firstx + (col + 1)*stepx) and (y < firsty - row* stepy) and (y > firsty - (row + 1)*stepy) :
              convert_both('X', player, row, col)
              turn += 1   
              check_win()
              print turn
              print win
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
              # if freeze == True:
              #   wn.onclick(None)
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

def ai_play():
  global lboard
  count_o_row = 0
  count_s_row = 0
  count_o_col = 0
  count_s_col = 0
  count_o_d1 = 0
  count_s_d1 = 0
  count_o_d2 = 0
  count_s_d2 = 0
  flag = False
  for row in range(3):
    for col in range(3):
      if lboard[row][col] == 'O':
        count_o_row += 1
      if lboard[row][col] == ' ':
        count_s_row += 1
        row_s_r = row
        col_s_r = col
      if lboard[col][row] == 'O':
        count_o_col += 1
      if lboard[col][row] == ' ':
        count_s_col += 1
        row_s_c = col
        col_s_c = row
      if lboard[col][col] == "O":
        count_o_d1 += 1
      if lboard[col][col] == " ":
        count_s_d1 += 1
        row_s_d1 = col
      if lboard[col][2 - col] == "O":
        count_o_d2 += 1
      if lboard[col][2 - col] == " ":
        count_s_d2 += 1
        row_s_d2 = col
        col_s_d2 = 2 - col
    # print "1",flag, " ", "o_r =", count_o_row, "s_r=", count_s_row
    if flag == False and count_o_row == 2 and count_s_row == 1:
      flag = True
      convert_both("O",opponent,row_s_r, col_s_r)
    # print flag, " ", "o_c =", count_o_col, "s_c=", count_s_col 
    if flag == False and count_o_col == 2 and count_s_col == 1:
      flag = True
      convert_both("O",opponent,row_s_c, col_s_c)
      
    if flag == False and count_o_d1 == 2 and count_s_d1 == 1:
      flag = True
      convert_both("O",opponent,row_s_d1, row_s_d1)
      
    if flag == False and count_o_d2 == 2 and count_s_d2 == 1:
      flag = True
      convert_both("O",opponent,row_s_d2, col_s_d2)
    

    count_o_row = 0
    count_s_row = 0
    count_o_col = 0
    count_s_col = 0
    count_o_d1 = 0
    count_s_d1 = 0
    count_o_d2 = 0
    count_s_d2 = 0
  # AI stopping the player from winning
  count_x_row = 0
  count_s_row = 0
  count_x_col = 0
  count_s_col = 0
  count_x_d1 = 0
  count_s_d1 = 0
  count_x_d2 = 0
  count_s_d2 = 0
  for row in range(3):
    for col in range(3):
      if lboard[row][col] == 'X':
        count_x_row += 1
      if lboard[row][col] == ' ':
        count_s_row += 1
        row_s_r = row
        col_s_r = col
      if lboard[col][row] == 'X':
        count_x_col += 1
      if lboard[col][row] == ' ':
        count_s_col += 1
        row_s_c = col
        col_s_c = row
      if lboard[col][col] == "X":
        count_x_d1 += 1
      if lboard[col][col] == " ":
        count_s_d1 += 1
        row_s_d1 = col
      if lboard[col][2 - col] == "X":
        count_x_d2 += 1
      if lboard[col][2 - col] == " ":
        count_s_d2 += 1
        row_s_d2 = col
        col_s_d2 = 2 - col
    # print "1",flag, " ", "o_r =", count_o_row, "s_r=", count_s_row
    if flag == False and count_x_row == 2 and count_s_row == 1:
      flag = True
      convert_both("O",opponent,row_s_r, col_s_r)
    # print flag, " ", "o_c =", count_o_col, "s_c=", count_s_col 
    if flag == False and count_x_col == 2 and count_s_col == 1:
      flag = True
      convert_both("O",opponent,row_s_c, col_s_c)
      
    if flag == False and count_x_d1 == 2 and count_s_d1 == 1:
      flag = True
      convert_both("O",opponent,row_s_d1, row_s_d1)
      
    if flag == False and count_x_d2 == 2 and count_s_d2 == 1:
      flag = True
      convert_both("O",opponent,row_s_d2, col_s_d2)
    

    count_x_row = 0
    count_s_row = 0
    count_x_col = 0
    count_s_col = 0
    count_x_d1 = 0
    count_s_d1 = 0
    count_x_d2 = 0
    count_s_d2 = 0
  if lboard[1][1] == ' ' and flag == False:
      flag = True
      convert_both("O",opponent,1, 1)
  corners = []
  for row in range(3):
    for col in range(3):
      if row != 1 and col != 1 and lboard[row][col] == ' ':
        corners.append([row,col])
  
  semis = []
  for row in range(3):
    for col in range(3):
      if (col == (row + 1) or col == (row - 1)) and lboard[row][col] == ' ':
        semis.append([row,col])
  if flag == False and len(semis) != 0:
    if (lboard[0][0] == 'X' and lboard [2][2] == 'X') or (lboard[0][2] == 'X' and lboard[2][0] == 'X'): 
      empty2 = r.choice(semis)
      flag = True
      convert_both("O",opponent,empty2[0], empty2[1])
      
      #Take the corner at the intersection of a row and column which each contain only one x
  if flag == False and len(corners) != 0:
    for corner in corners:
      flag1 = False
      flag2 = False
      row1 = corner[0]
      col1 = corner[1]
      c_x = 0
      c_s = 0
      for col in range(3):
        if lboard[row1][col] == 'X':
          c_x += 1
        elif lboard[row1][col] == ' ':
          c_s += 1
      if c_x == 1 and c_s == 2:
        flag1 = True
      c_x = 0
      c_s = 0  
      for row in range(3):
        if lboard[row][col1] == 'X':
          c_x += 1
        elif lboard[row][col1] == ' ':
          c_s += 1
      if c_x == 1 and c_s == 2:
        flag2 = True
      if flag1 == True and flag2 == True:
        convert_both("O",opponent,row1,col1)
        flag = True
        break   
        
  if flag == False and len(corners) != 0:
    empty = r.choice(corners)
    flag = True
    convert_both("O",opponent,empty[0], empty[1])
  
  if flag == False:
    ai_row = r.randint(0,2)
    ai_col = r.randint(0,2)
    while lboard[ai_row][ai_col] != ' ':
      ai_row = r.randint(0,2)
      ai_col = r.randint(0,2)
    
    flag = True  
    convert_both("O",opponent,ai_row, ai_col)     
  for row in range(3):
    print (lboard[row])
      
first = input("Who goes first? Enter 'p' for the player or 'c' for the computer").lower()
wn.onclick(click_board)
wn.onkey(ai_play,"space")
wn.listen()
wn.mainloop()
while True:
  if first == 'c':
    ai_play()
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
    