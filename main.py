def print_ttt(values):
  print("\n")
  print("\t     |     |")
  print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
  print('\t_____|_____|_____')
  print("\t     |     |")
  print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
  print('\t_____|_____|_____')
  print("\t     |     |")
  print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
  print("\t     |     |")
  print("\n")
 
def print_scores(scores):
  print("Scores")
  players = list(scores.keys())
  print(players[0], "\t", scores[players[0]])
  print(players[1], "\t", scores[players[1]])

def win_check(player_position, current_player):
  win_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
  for x in win_combos:
    if all(y in player_position[current_player] for y in x):
      return True      
  return False       

def draw_check(player_position):
  if len(player_position['X']) + len(player_position['O']) == 9:
    return True
  return False       

def print_choices(current_player):
  print(f"{current_player}'s turn")
  print("Enter 1 for X")
  print("Enter 2 for O")
  print("Enter 3 to Quit")

def single_game(current_player):
  values = [' ' for x in range(9)]
  player_position = {'X':[], 'O':[]}
  game_over = win_check(player_position, current_player) or draw_check(player_position)
  while not game_over:
    print_ttt(values)
    try:
      print(f"{current_player}'s turn Choose a space (1 top left, 9 bottom right): ", end="")
      move = int(input()) 
    except ValueError:
      print("Wrong Input!!! Try Again")
      continue

    if move < 1 or move > 9:
      print("Wrong Input!!! Try Again")
      continue
 
    if values[move-1] != ' ':
      print("That space is already filled. Please try again!!")
      continue
 
    values[move-1] = current_player
    player_position[current_player].append(move)
 
    if win_check(player_position, current_player):
      print_ttt(values)
      print(f"{current_player} won!") 
      return current_player

    if draw_check(player_position):
      print_ttt(values)
      print("That's a draw!")
      print("\n")
      return 'Draw'
 
    if current_player == 'X':
      current_player = 'O'
    else:
      current_player = 'X'
 
if __name__ == "__main__":
  print('Welcome to Tic Tac Toe!')
  player_1 = input("Player 1 enter your name : ")
  player_2 = input("Player 2 enter your name : ")

  while True:
    if player_2 == player_1:
      print(f"The name {player_2} is already taken. Please choose a new name for Player 2")
      player_2 = input("Enter your name : ")
    else:
      break
     
  current_player = player_1
  player_choice = {'X' : "", 'O' : ""}
  options = ['X', 'O']

  scores = {player_1: 0, player_2: 0}
  print_scores(scores)

  while True:
    print_choices(current_player)
    try:
      choice = int(input())   
    except ValueError:
      print("Wrong input! Please try again!\n")
      continue

    if choice == 1:
      player_choice['X'] = current_player
      if current_player == player_1:
        player_choice['O'] = player_2
      else:
        player_choice['O'] = player_1
    elif choice == 2:
      player_choice['O'] = current_player
      if current_player == player_1:
        player_choice['X'] = player_2
      else:
        player_choice['X'] = player_1  
    elif choice == 3:
      print("Here are the final scores:")
      print_scores(scores)
      print("Thank you for playing!")
      break
    else:
      print("Wrong input! Please try again!")

    winner = single_game(options[choice-1]) 
    if winner != 'Draw':
      player_won = player_choice[winner]
      scores[player_won] = scores[player_won] + 1

    print_scores(scores)
    if current_player == player_1:
      cur_player = player_2
    else:
      cur_player = player_1