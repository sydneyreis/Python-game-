'''
Wecome to the Dungeon!

This is the primary python script file that will launch your game.
It will evolve over the entire semester until you have a working application!
'''

import engine

def main():
    '''
    This is a *function* that starts up your game. You will create variables,
    build logic, and perform basic inputs and outputs.
    '''

    user_name = input("Enter    your     name")
    print(f"Hello, {user_name} welcome to Remy's Rat Rampage!")
    char_num = input("Select a character!\n 1. Remy \n 2. Gitt \n 3. Emile")
    char_stats = engine.generate_character(char_num)
    '''
    enemy_stats = engine.generate_enemy(0)
    result = engine.battle(char_stats, enemy_stats)
    print(f"{result}")
    if result['Battle Result'] == False:
        print("You have lost the battle")
    else:
        print("You have won the battle")
        print(f"You have reached level {engine.compute_level(result['points earned'])}")
    print(f"new character health is {char_stats['health']}")
    print(f"new enemy health is {enemy_stats['health']}")
    '''

    ## nothing=0, loot=1, battle=2, battle =3, final boss = 4
    game_world = {(0,0): 0, (1,0): 2, (2,0): 1, (3,0): 3, (4,0): 1,
                  (0,1): 1, (1,1): 3, (2,1):2, (3,1): 1, (4,1):0,
                  (0,2): 0, (1,2): 2, (2,2): 0, (3,2): 1, (4,2): 0,
                  (0,3): 0, (1,3): 1, (2,3): 0, (3,3): 1, (4,3): 0,
                  (0,4): 0, (1,4): 3, (2,4): 1, (3,4): 0, (4,4): 4 }
    char_loc = [0,0]
    thing = True

    ##while char_stats['health'] > 0:

    while thing == True:
        result = engine.navigate(game_world, char_loc, char_stats)
        char_loc = result[1]
        thing = result[0]
        print(char_loc)

    if char_stats['health'] <= 0:
        print(" Oh no you have lost the game :(")
    else:
        print("You have won the game!! Yay!! WoHoo!!")

    
    # print(char_loc)
  


    
    

    # char_loc = engine.move_right(char_loc, game_world)
    # print(f"New character location: {char_loc}")

    
    





'''
This code down here tells the Python interpreter that this
file is a main program to lauch.
'''
if __name__ == '__main__':
    main()