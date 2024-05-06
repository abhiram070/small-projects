
"""
Original file is located at
    https://colab.research.google.com/drive/1ru-IohsqmTK0y6vcvgdW1-EwRr8m75IK

TIC TAC TOE
"""

def printboard(board):
    for i in range(0, 9):
        if (i % 3) == 0:
            print("\n")
        if board[i] == 0:
            print("_ ", end="")
        elif board[i] == 1:
            print("O ", end="")
        else:
            print("X ", end="")
    print("\n")

def analyzeboard(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == 1:
            return -1

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == 1:
            return -1

    # Check diagonals
    if board[0] == board[4] == board[8] == 1:
        return -1
    if board[2] == board[4] == board[6] == 1:
        return -1

    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == 2:
            return 1

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == 2:
            return 1

    # Check diagonals
    if board[0] == board[4] == board[8] == 2:
        return 1
    if board[2] == board[4] == board[6] == 2:
        return 1

    # If no winner is found, return 0
    return 0

def markonboard_plr(board):
  printboard(board);
  print("select corresponding number to mark on board");
  for i in range(0,9):
    if(i % 3 == 0):
      print("");
    print(i+1,end=" ")
  print("");
  while (True):
    select = int(input());
    if (select > 9 or board[select-1] != 0):
      print("WRONG MOVE..!!!")
    else:
      board[select-1] = 1;
      break;


def minmax(board,player):
  x = analyzeboard(board);
  if(x != 0):
    return x*player;
  best_score = -2
  best_move = -1
  for i in range(0, 9):
    if(player == -1):
      plr = 1;
    else:
      plr = 2
    if board[i] == 0:
      board[i] = plr
      score = -minmax(board, player*-1)
      board[i] = 0
      if score > best_score:
        best_score = score
        best_move = i
  if(best_move == -1):
    return 0;
  return best_score;

def markonboard_comp(board):
  best_score = -2
  best_move = -1
  for i in range(0, 9):
    if board[i] == 0:
      board[i] = 2
      score = -minmax(board, -1)
      board[i] = 0
      if score > best_score:
        best_score = score
        best_move = i
  if best_move != -1:
    board[best_move] = 2

def main():
  board = [0,0,0,0,0,0,0,0,0];
  while True:
    print("you want to play 1st or 2nd");
    choice = int(input());
    if(choice==1 or choice==2):
      break;
    else:
      print("wrong input..!!")
  n = 0;

  for i in range(0,9):
    if(choice == 1):
      if(analyzeboard(board) == 0):
        if i%2 == 0:
          markonboard_plr(board);
        else:
          markonboard_comp(board);
      else:
        break;
    elif(choice == 2):
      if(n == 0):
        board[4] = 2;
        n = 1;
      elif(analyzeboard(board) == 0):
        if i%2 == 1:
          markonboard_plr(board);
        else:
            markonboard_comp(board);
      else:
        break;
    else:
      print("oops something happened :(");

  if(analyzeboard(board) == -1):
    printboard(board);
    print("YOU won :-)");
  elif(analyzeboard(board) == 1):
    printboard(board);
    print("COMPUTER won :-(");
  else:
    printboard(board);
    print("MATCH IS DRAW...!!!!!!")

main()

