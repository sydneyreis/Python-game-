def generate_character (char_type):
    '''
        This function generates the character the user will be playing as.

        Parameter: char_type
            This parameter holds a string (1-3)

        Return: character 
            Each string is linked to a character. The character with stats will be returned
            If a string not within 1-3 is entered an error message will be returned and the user will be reprompted to select a character
        
    '''
    if (char_type == '1'):
        # Attacking, running, defending, health
        char_stats = {'attacking' : 100,'running' : 60, 'defending' : -20, 'health' : 20,  'loot' : 0}
        return char_stats
    if (char_type == '2'):
        # Attacking, running, defending, health
        char_stats = {'attacking' : 0,'running' : -20, 'defending' : 100, 'health' : 25,  'loot' : 0}
        return char_stats
    if (char_type == '3'):
        # Attacking, running, defending, health
        char_stats = {'attacking' : -10,'running' : 50, 'defending' : 0, 'health' : 10,  'loot' : 0}
        return char_stats
    else:
        return None

def generate_enemy (number):
    '''
        This function will generate the enemy that a user faces in a battle 

        Parameter: num_battles_taken_place
            This parameter holds a string that correlates to the number of battles that a user has already participated in

        Returns: 
           if num_battles_taken_place is between 0 and 15 an enemy is generated
           if num_battles_taken_place is greater than 15 or less than 0 no enemy is generated and none is returned
    '''
    if (0):
        # Attacking, running, defending, health
        enemy_stats = {'attacking' : 30,'running' : 20, 'defending' : 10, 'health' : 50,}
        return enemy_stats
    if (1):
        # Attacking, running, defending, health
        enemy_stats = {'attacking' : 30,'running' : 0, 'defending' : 10, 'health' : 50,}
        return enemy_stats
    if (2):
        # Attacking, running, defending, health
        enemy_stats = {'attacking' : 40,'running' : 20, 'defending' : 30, 'health' : 50}
        return enemy_stats
    else:
        return None

        
    
def compute_level (total_points):
    '''
        This function will calculate the level a character is at.

        Parameter: total_points
            This parameter holds an integer that reflects the total number of points a character has from all its battles 

        Returns: compute_level
            Returned is the level a character is currently at 
            This is computed by taking total_points // 10
            The integer computed is the current level a character is at
    '''
    if (total_points >= 0):
        current_level = total_points // 10
        return current_level
    else: 
        return None
    
def battle(char_stats, enemy_stats):
    '''
    This function is where the battles within the game will take place, it will continue looping until the game is over or has been beat

    Parameter: char_stats
        This parameter holds a list, where each component of the list correlates to a different stat of the character

    Parameter: enemy_stats
        This parameter holds a list, where each component of the list correlates to a different stat of the enemy

    Return: battle_results 
        Using char_stats the user will be able to choose whether they want to attack, defend, or run. Using the random module
        it will randomly selected whether the enemy attacks, defends, or runs. Whoever has the higher value will be the one that
        wins the battle. A new list will be returned holding [True (or false if char lost battle), new health, points earned (xp), loot]
        The difference between the enemy and character's stats for a particular battle will be subtracting from the loser's health.
        So, for example is Remy has running = 15 and and original health of 20 and the health inspector has defending = 30 the health
        inspector will win the battle and Remy's health will decrease to 5.

        '''
    import random 
    while enemy_stats['health']>0 and char_stats['health'] >0:
        enemy_battle_choice = random.choice(['attacking', 'running', 'defending'])
        battle_choice_en = enemy_stats[enemy_battle_choice]
        user_selection = input(" How would you like to fight the enemy? Enter attacking, running, or defending")
        battle_choice_us = char_stats[user_selection]
        if battle_choice_us > battle_choice_en:
            calc = battle_choice_us - battle_choice_en
            char_stats['health']  += calc
            enemy_stats['health'] -= calc
        if battle_choice_us <= battle_choice_en:
            calc = battle_choice_en - battle_choice_us
            char_stats['health']  -= calc
            enemy_stats['health'] += calc
    if char_stats['health']<=0:
        return {'Battle Result' :False, 'loot' : 0,'points earned' :0}
    if enemy_stats['health']<=0:
        return {'Battle Result' : True, 'loot' : .5 * calc,'points earned' : .25 * calc}
    

def move_right(char_loc, game_world):
    char_x = char_loc[0]
    char_y = char_loc[1]
    if char_x +1 <= 6:
        return [char_x + 1,char_y] 
    else:
        return [char_x, char_y]
    
def move_left(char_loc, game_world):
    char_x = char_loc[0]
    char_y = char_loc[1]
    if char_x -1 >= 0:
        return [char_x - 1,char_y]
    else:
        return [char_x, char_y]

def move_up(char_loc, game_world):
    char_x = char_loc[0]
    char_y = char_loc[1]
    if char_y +1 <= 6:
        return [char_x,char_y +1]
    else:
        return [char_x, char_y]

def move_down(char_loc, game_world):
    char_x = char_loc[0]
    char_y = char_loc[1]
    if char_y -1 >= 0:
        return [char_x, char_y - 1]
    else:
        return [char_x, char_y]   
    
def navigate (game_world, char_loc, char_stats):
    '''
    This function allows users to walk across the game board and is where they will encounter the enemies they will battle

    Parameter: game_world
    Game_world is a dictionary that contains the 5 by 5 game board. The keys are sets of x and y coordinants that describe particular
    locations on the game board and the value stored in the keys is whether the user is facing an enemy, getting loot, or if nothing is happening 
    at the particular position on the game board.

    Parameter: char_loc
    Char_loc is a list that holds the characters position on the game board. It contains the coordinants of where the character is located 
    in the format (x, y).

    Parameter: char_stats
    These are the stats assigned to the character after initial character selection

    Return: updated char_loc and True or False:
    This function depends on user input as to where the character moves. If the user chooses to move the character into a space that 
    exists on the game board, before they can move they must face the enemy (if there is one) that exists on that section of the game
    board. If a battle takes place after the battle the health of the character is reviewed and if it is greater than 0 the character 
    can move into the next square of the board and the function will loop. After one iteration either True or False will be output (depending)
    on whether the character is alive or not and if true is outputted char_loc will update to the new square.

    '''
    

    user_dir = input("Pick a direction to go!")
    if user_dir == 'r':
        char_loc = move_right(char_loc, game_world)
    elif user_dir == 'l':
        char_loc = move_left(char_loc, game_world)
    elif user_dir == 'd':
        char_loc = move_down(char_loc, game_world)
    else:
        char_loc = move_up(char_loc, game_world)

    
    loc_key = tuple(char_loc)
    # print("here:", loc_key)
    event_value = game_world[loc_key]
    if event_value == 0:
        return [True, char_loc]
    elif event_value == 1:
        char_stats['loot'] += 30
        return [True, char_loc]
    elif event_value == 2:
        enemy_stats = generate_enemy(0)
        result = battle(char_stats, enemy_stats)
        print(result)
        key = result['Battle Result']
        if key == False:
            return [False, char_loc]
        else:
            return [True, char_loc]
    elif event_value == 3:
        enemy_stats = generate_enemy(1)
        result = battle(char_stats, enemy_stats)
        if result['Battle Result'] == False:
            return [False, char_loc]
        else:
            return [True, char_loc]
    elif event_value == 4:
        enemy_stats = generate_enemy(2)
        result = battle(char_stats, enemy_stats)
        if result['Battle Result'] == False:
            return [False, char_loc]
        else:
            return [False, char_loc]
        
