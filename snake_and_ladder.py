#Author: Anuraj R
player_name=dict()
snake={17:4,19:7,27:1,54:34,62:18,64:60,87:24,93:73,95:75,99:51}
ladder={3:22,5:8,11:26,20:29,27:84,36:44,51:67,71:91,80:98}
    
#function for dice rolling 
def roll():
    import random 
    return random.randint(1,6)
    
#function for change score value 
def move_player(pman):
    if(pman == "bot"):
        dice=roll()
    else:
        input(f"{pman}, your turn. Please press Enter to roll the dice.")
        dice=roll()
    position=player_name[pman]    
    new=position+dice

    if(new>100):
        return position
    print(f"{pman} rolled a {dice} and moved from {position} to {new}.")
    if(new in snake):
        print(f"Oh no! {pman} was bitten by a snake and moved down to {snake[new]}.")
        return snake[new]
    elif(new in ladder):
        print(f"{pman} climbed a ladder and moved to {ladder[new]}.")
        return ladder[new]

    return new
        
    
#function for multi-player 
def multiplayer():
    print("multi-player:\n")
    print("Maximum player for multi-player game is 4 \n")
    print("please enter how many player are attending now to play this game \n ")
    while True:
        player=int(input("enter the value in numeric "))
        if 2 <= player <= 4:
                print("You are entered to the game")
                break
        else:
            print(" enter the valuable data read the instruction above ") 
    nm=input("do have change the default names of the player.then enter yes .otherwise no.   ").lower()
    while True:
        if(nm=="yes"):
            print(f"enter {player} names.")
            print("enter the unique name.if the names are same add last name.otherwise player didn't  play the game ")
            for i in range(player):
                name=input(f"enter {i+1} name ")
                player_name[name]=0
            break   
        elif(nm=="no"):
            for i in range(player):
                name=f"player{i+1}"
                player_name[name]=0
            break    
        else:
            print("enter the vaild data. read the instruction above carefully")
            
    while True:
        for player in player_name:
            player_name[player]=move_player(player)
            if(player_name[player]==100):
                print(f"Congratulations {player}.you are wins the game")
                break 
        else:
            continue
        break    
        
        
            
#function for bot
def bot_player():
    nm=input("do have change the default names of the player.then enter yes .otherwise no.   ").lower()
    if(nm=="yes"):
        name=input("enter a name for player ")
        player_name[name]=0
        player_name["bot"]=0
    elif(nm=="no"):
        player_name["player"]=0
        player_name["bot"]=0
    while True:
        for player in player_name:
            player_name[player]=move_player(player)
            if(player_name[player]==100):
                print(f"Congratulations {player}.you are wins the game")
                break 
        else:
            continue
        break    
    
    
    
    
#main function    
print("welcome to snake and ladder game\n")
print("are you play with bot then enter yes or not please enter no for activating multi-player position \n")
while True:
    bot=input("enter the answer in yes or no  ").lower()
    if(bot == "no"):
        print("multi-player is activated \n")
        multiplayer()
        break
    elif(bot == "yes"):
        print("bot is activated ")
        bot_player()
        break
    else: 
        print("enter the valid input .read the instruction above carefully.\n")
        
