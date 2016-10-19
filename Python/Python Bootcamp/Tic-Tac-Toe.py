import sys, time, random
from subprocess import call

def _Clear():
  if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    call('cls', shell=True)
  elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    call('clear', shell=True)

def _Replace(s, r, i):
  return s[:i] + r + s[i + 1:]

def _PlayersName():
  global player_1
  global player_2
  player_1 = input('Player 1: What is your name? ')
  player_2 = input('Player 2: What is your name? ')
  if player_1[0].islower() or player_2[0].islower():
    player_1 = _Replace(player_1, player_1[0].upper(), 0)
    player_2 = _Replace(player_2, player_2[0].upper(), 0)

def _PrintBoard(board):
  _Clear()
  one = board[0]
  two = board[1]
  three = board[2]
  four = board[3]
  five = board[4]
  six = board[5]
  seven = board[6]
  eight = board[7]
  nine = board[8]
  if one == ' ':
    one = 1
  if two == ' ':
    two = 2
  if three == ' ':
    three = 3
  if four == ' ':
    four = 4
  if five == ' ':
    five = 5
  if six == ' ':
    six = 6
  if seven == ' ':
    seven = 7
  if eight == ' ':
    eight = 8
  if nine == ' ':
    nine = 9

  print('''
---|---|---
 {one} | {two} | {three}
---|---|---
 {four} | {five} | {six}
---|---|---
 {seven} | {eight} | {nine}
---|---|---
  '''.format(
    one = one, 
    two = two, 
    three = three,
    four = four,
    five = five,
    six = six,
    seven = seven,
    eight = eight,
    nine = nine))

def _PlayerInput():
  marker = ''
  goesfirst = ''
  marker_op = ''
  while not (marker == 'X' or marker == 'O'):
    if _GoesFirst(1, 2) == 1:
      goesfirst = 1
      marker = input('{player}: Do you want to be "X" or "O"? '.format(player = player_1)).upper()
    elif _GoesFirst(1, 2) == 2:
      goesfirst = 2
      marker = input('{player}: Do you want to be "X" or "O"? '.format(player = player_2)).upper()
    if goesfirst == 1:
      if marker == 'X':
        marker_op = 'O'
      elif marker == 'O':
        marker_op = 'X'
      else:
        print('Please make sure that you enter either an "X" or "O"')
      return [marker, marker_op]
    else:
      if marker == 'X':
        marker_op = 'O'
      elif marker == 'O':
        marker_op = 'X'
      else:
        print('Please make sure that you enter either an "X" or "O"')
      return [marker_op, marker]


    if marker == 'X':
      return ['X', 'O']
    elif marker == 'O':
      return ['O', 'X']
    else:
      print('Please make sure that you enter either an "X" or "O"')

def _PlaceMarker(board, marker, position):
  board[position - 1] = marker

def _CheckWin(board, mark):
  return (
  (board[0] == mark and board[1] == mark and board[2] == mark) or # First Row
  (board[3] == mark and board[4] == mark and board[5] == mark) or # Second Row
  (board[6] == mark and board[7] == mark and board[8] == mark) or # Third Row
  (board[0] == mark and board[3] == mark and board[6] == mark) or # First Column
  (board[1] == mark and board[4] == mark and board[7] == mark) or # Second Column
  (board[2] == mark and board[5] == mark and board[8] == mark) or # Third Column
  (board[0] == mark and board[4] == mark and board[8] == mark) or # Diagonal
  (board[2] == mark and board[4] == mark and board[6] == mark)) # Diagonal

def _GoesFirst(first, second):
  while random.randint(0, 1) == 0:
    return first
  else:
    return second


def _SpaceEmpty(board, position):
  return board[position - 1] == ' '

def _BoardFull(board):
  for x in range(1, 10):
    if _SpaceEmpty(board, x):
      return False
  return True

def _NextMove(board):
  position  = ''
  while position not in '1 2 3 4 5 6 7 8 9'.split() or not _SpaceEmpty(board, int(position)):
    print("It is {player}'s Turn".format(player = whose_turn))
    position = input('Choose your next move (1-9) ')
    if position not in '1 2 3 4 5 6 7 8 9':
      print('Please make sure you enter a number (1-9)')
  return int(position)

def _Replay():
  while True:
    x = input('Do you want to play again (Yes or No)?: ').lower()
    _Clear()
    if x == 'yes':
      return True
    elif x == 'no':
      return False
    else:
      print('Please make sure that you enter either "Yes" or "No"')
      continue

_PlayersName()
while True:
  listBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
  player1_m, player2_m = _PlayerInput()
  whose_turn = _GoesFirst(player_1, player_2)
  # print(whose_turn, 'will go first')
  # time.sleep(5)
  game = True

  while game:
    if whose_turn == player_1:
      whose_turn = player_1
      _PrintBoard(listBoard)
      position = _NextMove(listBoard)
      _PlaceMarker(listBoard, player1_m, position)
      if _CheckWin(listBoard, player1_m):
        _PrintBoard(listBoard)
        print('{player} has won the game'.format(player = player_1))
        game = False
      else:
        if _BoardFull(listBoard):
          _PrintBoard(listBoard)
          print('You and {player} tied'.format(player = player_2))
          break
        else:
          whose_turn =  player_2
    else:
      whose_turn ==  player_2
      _PrintBoard(listBoard)
      position = _NextMove(listBoard)
      _PlaceMarker(listBoard, player2_m, position)

      if _CheckWin(listBoard, player2_m):
        _PrintBoard(listBoard)
        print('{player} has won the game'.format(player = player_2))
        game = False
      else:
        if _BoardFull(listBoard):
          _PrintBoard(listBoard)
          print('You and {player} tied'.format(player = player_1))
          break
        else:
          whose_turn = player_1

  if _Replay() == False:
    break
