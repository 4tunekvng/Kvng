import random 

def print_board(game_data):
    print()
    print('', game_data[6], '|', game_data[7], '|', game_data[8], '       7 | 8 | 9 ')
    print('-'* 11, '    ', '-'* 11)
    print('', game_data[3], '|', game_data[4], '|', game_data[5], '       4 | 5 | 6 ')
    print('-'* 11, '    ', '-'* 11)
    print('', game_data[0], '|', game_data[1], '|', game_data[2], '       1 | 2 | 3 ')
    print()


game_data = [' '] * 9   # initialize game data to an empty array

whose_turn = 'player'   # TODO: alternate between computer and player (within the loop)

#choose your player symbol
choice_symbol=input("What would you like to be, x or o?:",)
if choice_symbol=="x":
    player_symbol="x"
    computer_symbol="o"
else:
    player_symbol="o"
    computer_symbol="x"
player_position=input("Do you want to go first, y or n:",)
if player_position=="y":
    whose_turn="player"
else:
    whose_turn="computer"
all_positions=[1,2,3,4,5,6,7,8,9]
used_positions=[]
# keep looping until there's a winner:
while True:
    print_board(game_data)
    # TODO: handle bad input:
    
    if game_data[0]==game_data[1]==game_data[2]== "x":
            print(game_data[0],"wins!")
            break
    elif game_data[3]==game_data[4]==game_data[5]== "x":
            print(game_data[3],"wins!")
            break
    elif game_data[6]==game_data[7]==game_data[8]== "x":
            print(game_data[6],"wins!")
            break
    elif game_data[2]==game_data[5]==game_data[8]== "x":
            print(game_data[2],"wins!")
            break
    elif game_data[1]==game_data[4]==game_data[7]== "x":
            print(game_data[1],"wins!")
            break
    elif game_data[0]==game_data[3]==game_data[6]== "x":
            print(game_data[0],"wins!")
            break
    elif game_data[2]==game_data[4]==game_data[6]== "x":
            print(game_data[2],"wins!")
            break
    elif game_data[0]==game_data[4]==game_data[8]== "x":
            print(game_data[0],"wins!")
            break
    

    if game_data[0]==game_data[1]==game_data[2]== "o":
            print(game_data[0],"wins!")
            break
    elif game_data[3]==game_data[4]==game_data[5]== "o":
            print(game_data[3],"wins!")
            break
    elif game_data[6]==game_data[7]==game_data[8]== "o":
            print(game_data[6],"wins!")
            break
    elif game_data[2]==game_data[5]==game_data[8]== "o":
            print(game_data[2],"wins!")
            break
    elif game_data[1]==game_data[4]==game_data[7]== "o":
            print(game_data[1],"wins!")
            break
    elif game_data[0]==game_data[3]==game_data[6]== "o":
            print(game_data[0],"wins!")
            break
    elif game_data[2]==game_data[4]==game_data[6]== "o":
            print(game_data[2],"wins!")
            break
    elif game_data[0]==game_data[4]==game_data[8]== "o":
            print(game_data[0],"wins!")
            break
    elif used_positions==all_positions:
            print("tie!")
            break
  
    
    
    
    if whose_turn == 'player':
        selection = input('Where would you like to go (1-9)? ')
        try:
            if int(selection) in used_positions:
                print("This position has been taken")
                continue
            elif 1<=int(selection)<=9:
                game_data[int(selection) - 1] = player_symbol
                used_positions.append(int(selection))
                whose_turn="computer"
                continue
            else:
                print("That is not a possible move")
                continue 
        except ValueError:
            print("Please enter a number")
            continue   
      
        
       
    elif whose_turn == "computer":
        choice= random.choice(all_positions)
        if choice in used_positions:
            continue 
        else:
            game_data[choice-1]= computer_symbol
            used_positions.append(choice)
            whose_turn="player"
            continue

    # TODO: handle computer's turn:
    # TODO: check if someone won or if there's a tie