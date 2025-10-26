'''
This module will provide functions and classes that maintain the front end
display and user interaction.

We will need arcade here ... since that does front end stuff!
'''
import arcade
import engine
import random


'''
You will declare new View classes here! Each of these classes
will be used to switch views, as shown in the View tutorial:
https://api.arcade.academy/en/2.6.17/tutorials/views/index.html
'''

class WelcomeView(arcade.View):
    def __init__(self, window = None):
        super().__init__(window)
        arcade.set_background_color(arcade.color.GRAY)
        self.back_sprite = Character("La_Ratatouille_sign.png", 1, 1, 1, 1, 1, center_x= 150, center_y= 125, x = 0, y = 0, name = "x")
        self.back_list = arcade.SpriteList()
        self.back_list.append(self.back_sprite)
        '''
        We customize our classes with new initializers, attributes, and methods.
        Hint: one attribute will be your character! All views will need a reference to it.
        '''
    def on_draw(self):
        self.clear()
        arcade.draw_text("BONJOUR Chef", self.window.width/2, self.window.height/1.5, arcade.color.BLACK, 22, anchor_x= "center")
        arcade.draw_text("Welcome to Remy's Rat Rampage", self.window.width/2, self.window.height/2, arcade.color.BLACK, 18, anchor_x= "center" )
        self.back_list.draw()
        return super().on_draw()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            new_view = IntroAndSelection(self.window)

            self.window.show_view(new_view)


class IntroAndSelection(arcade.View):
    def __init__(self, window = None):
        super().__init__(window)
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        self._char_sprite_1 = Character("remy.png", 40, 10, 20, 15, 0, center_x = 150, center_y= 125, x = 0, y = 0, name = "Remy")
        self._char_sprite_2 = Character("emile.png", 10, 20, 30, 15, 0, center_x= 300, center_y= 125, x = 0, y = 0, name = "Emile")
        self._char_sprite_3 = Character("gitt.png", 40, 10, 20, 15, 0, center_x= 450, center_y= 125, x = 0, y = 0, name = "Gitt")
        self.character_list = arcade.SpriteList()
        self.character_list.append(self._char_sprite_1)
        self.character_list.append(self._char_sprite_2)
        self.character_list.append(self._char_sprite_3)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Time to choose your character!!", self.window.width/2, self.window.height/2, arcade.color.BLACK, 22, anchor_x= "center" )
        arcade.draw_text("A. Remy", self.window.width/2, self.window.height/2.25, arcade.color.BLACK, 15, anchor_x= "center" )
        arcade.draw_text("B. Emile", self.window.width/2, self.window.height/2.5, arcade.color.BLACK, 15, anchor_x= "center" )
        arcade.draw_text("C. Gitt", self.window.width/2, self.window.height/2.75, arcade.color.BLACK, 15, anchor_x= "center" )

        self.character_list.draw()
        


    def on_key_press(self, key, modifiers):

        if key == arcade.key.A:
            new_view = Navigation(self.window, self._char_sprite_1, reset_position = True, current_level = 1 )
            self.window.show_view(new_view)
        elif key == arcade.key.B:
            new_view = Navigation(self.window, self._char_sprite_2, reset_position = True, current_level = 1 )
            self.window.show_view(new_view)
        else:
            new_view = Navigation(self.window, self._char_sprite_3, reset_position = True, current_level = 1 )
            self.window.show_view(new_view)

class Navigation(arcade.View):
    '''
    This class controls character movements throughout the game world. It generates sprites depending on the event located within the game world dictionary
    and recalculates the characters position based off of the user key presses. When the character collides with another sprite they either will get sent to a
    battle or recieve loot which will call the level up function.

    The parameters of the class is character (which the user selects in the prior window), reset_position (this allows the sprite location to not be reset after 
    battle is called), and current_level which allows the user and enemy to level up and for the level to not reset when windows are switched. 
    '''
    def __init__(self, window, character, reset_position, current_level):
        super().__init__(window)
        self._character = character
        self._reset_position = reset_position
        self._current_level = current_level

        #checking if character position should be set to 0, should only be when navigate is called from character selection not battle
        if self._reset_position == True:
            self._character.x = 0
            self._character.y = 0
            self._character.center_x = self.window._cell_size / 2
            self._character.center_y = self.window._cell_size / 2
      
        
        #creating sprite lists
        self._cheese_list = arcade.SpriteList()
        self._enemy_one_list = arcade.SpriteList()
        self._enemy_two_list = arcade.SpriteList()
        self._enemy_three_list = arcade.SpriteList()

        # for each even in the game world dictionary, add corresponding sprite to sprite list
        for key in self.window._game_world:
            if self.window._game_world[key] == 1:
                cheese_sprite = arcade.Sprite("cheesewheel.png", center_x = 0, center_y = 0)
                cheese_sprite.center_x = key[0] * self.window._cell_size + 50
                cheese_sprite.center_y = key[1] * self.window._cell_size + 50
                self._cheese_list.append(cheese_sprite)
            elif self.window._game_world[key] == 2:
                enemy_sprite_1 = Enemy("health inspector.png", 100, 60, -20, 20, center_x = 0, center_y = 0, name = "The Health Inspector")
                enemy_sprite_1.center_x = key[0] * self.window._cell_size + 50
                enemy_sprite_1.center_y = key[1] * self.window._cell_size + 50
                self._enemy_one_list.append(enemy_sprite_1)
            elif self.window._game_world[key] == 3:
                enemy_sprite_2 = Enemy ("boss.1.png", 0, -20, 100, 25, center_x = 0, center_y = 0, name = "Well known critic Anton Ego")
                enemy_sprite_2.center_x = key[0] * self.window._cell_size + 50
                enemy_sprite_2.center_y = key[1] * self.window._cell_size + 50
                self._enemy_two_list.append(enemy_sprite_2)
            elif self.window._game_world[key] == 4:
                enemy_sprite_3 = Enemy ("finalboss.png", 100, 100, 100, 100, center_x = 0, center_y = 0, name = "The evil little small chef")
                enemy_sprite_3.center_x = key[0] * self.window._cell_size + 50
                enemy_sprite_3.center_y = key[1] * self.window._cell_size + 50
                self._enemy_three_list.append(enemy_sprite_3)

    # drawing sprite lists (creating game world)
    def on_draw(self):
        self.clear()
        self._character.draw()
        self._cheese_list.draw()
        self._enemy_one_list.draw()
        self._enemy_two_list.draw()
        self._enemy_three_list.draw()
        output = f"Level: {self._current_level} "
        arcade.draw_text(output, 430, 475, arcade.color.BLACK, 12)

    # checking for position collision of character and sprite, if so remove that sprite!!
    def on_update(self, delta_time):
        self._cheese_list.update()
        cheese_hit_list = arcade.check_for_collision_with_list(self._character, self._cheese_list)
        enemy_one_hit_list = arcade.check_for_collision_with_list(self._character, self._enemy_one_list)
        enemy_two_hit_list = arcade.check_for_collision_with_list(self._character, self._enemy_two_list)
        enemy_three_hit_list = arcade.check_for_collision_with_list(self._character, self._enemy_three_list)
        for cheese in cheese_hit_list:
            cheese.remove_from_sprite_lists()

        for enemy in enemy_one_hit_list:
            enemy.remove_from_sprite_lists()

        for enemy in enemy_two_hit_list:
            enemy.remove_from_sprite_lists()
                
        for enemy in enemy_three_hit_list:
            enemy.remove_from_sprite_lists()

    event = None

    #Creating compute level function, take loot collected and integer divide it , then multiply it to character attack!
    def computing_lev(self):
        self._current_level += self._character.loot //50
        self._character.attacking += self._current_level
        return self._current_level, self._character.attacking
    
    

    
    def on_key_press(self, key, modifiers):
        
        #updating character location based off of user key press
        if key == arcade.key.UP:
            loc = engine.move_up((self._character.x, self._character.y), self.window._game_world)
            self._character.x = loc[0]
            self._character.y = loc[1]
            self._character.center_y = 50 + self._character.y * self.window._cell_size
        elif key == arcade.key.DOWN:
            loc = engine.move_down((self._character.x, self._character.y), self.window._game_world)
            self._character.x = loc[0]
            self._character.y = loc[1]
            self._character.center_y = 50 + self._character.y * self.window._cell_size
        elif key == arcade.key.LEFT:
            loc = engine.move_left((self._character.x, self._character.y), self.window._game_world)
            self._character.x = loc[0]
            self._character.y = loc[1]
            self._character.center_x = 50 + self._character.x * self.window._cell_size
        else:
            loc = engine.move_right((self._character.x, self._character.y), self.window._game_world)
            self._character.x = loc[0]
            self._character.y = loc[1]
            self._character.center_x = 50 + self._character.x * self.window._cell_size

        #adding loot or sending character to new window depending on event in game board
        event = self.window._game_world[tuple(loc)]
        if event == 1:
            self._character.loot += random.randint(5,15)
            self.computing_lev()
        elif event == 2:   
            enemy = Enemy("health inspector.png", 50, 60, -20, 20, center_x = 0, center_y = 0, name = "the Health Inspector")
            new_view = Battle(self.window, self._character, enemy, self._current_level)
            self.window.show_view(new_view)
        elif event == 3:   
            enemy = Enemy ("boss.1.png", 30, -20, 40, 25, center_x = 0, center_y = 0, name = "well known critic Anton Ego")
            new_view = Battle(self.window,  self._character, enemy, self._current_level)
            self.window.show_view(new_view)
        elif event == 4:   
            enemy =Enemy ("finalboss.png", 200, 200, 200, 200, center_x = 0, center_y = 0, name = "The evil, little, small chef")
            new_view = Battle(self.window,  self._character, enemy, self._current_level)
            self.window.show_view(new_view)


        # reseting game world to 0 once user has landed in a space
        if self.window._game_world[(self._character.x, self._character.y)] == 1:
            self.window._game_world[(self._character.x, self._character.y)] = 0
        if self.window._game_world[(self._character.x, self._character.y)] == 2:
            self.window._game_world[(self._character.x, self._character.y)] = 0
        if self.window._game_world[(self._character.x, self._character.y)] == 3:
            self.window._game_world[(self._character.x, self._character.y)] = 0
        if self.window._game_world[(self._character.x, self._character.y)] == 4:
            self.window._game_world[(self._character.x, self._character.y)] = 0




class Battle(arcade.View):
    def __init__(self, window, character, enemy, current_level):
        '''
        This class takes in the parameter self, window, character (the users selected character), enemy (the enemy the user has 
        encountered in the navigate window), and current level, calculated in navigate

        The enemy class handles battles once the user has entered a space with an enemy. The enemy and users stats as well
        as sprites are printed on the screen. From there the on key press function is called. On key press handles whether the
        user wants to attack defend or run. This function then calls the handle battle function which is where the nuts and bolts
        of the battle is handled. The parameters are the user battle choice (from on key press)and self. The enemy battle choice is
        randomly generated from the random module and then the user battle and enemy battle choices values are compared. Whoever has 
        the greater value wins the battle. The difference between these two values is added to the winners health and subtracted from
        the loser's health. The winner also gets 10 added to their defense value. Once their is a winner in the battle the user is either
        sent back to navigate, or arcade is exited, or if the final boss is defeated a victory screen is generated
        '''
        super().__init__(window)
        self._character = character
        self._enemy = enemy
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        self._current_level = current_level

        #creating temp variables to hold where x and y were in navigate, so they can return
        self._original_x = character.center_x
        self._original_y = character.center_y

        #moving character and enemy sprites to better location !
        self._character.center_x = self.window.width * 0.25 
        self._character.center_y = self.window.height * 0.35
        self._enemy.center_x = self.window.width * 0.75
        self._enemy.center_y = self.window.height * 0.35

        # enemy attack being edited to account for user leveling up
        self._enemy.attacking += self._current_level

    

    def on_draw(self):
        # drawing character and enemy sprites and their stats
        self.clear()
        arcade.draw_text(f"Time for {self._character.name} to fight {self._enemy.name}", self.window.width/2, self.window.height/1.1, arcade.color.BLACK, 13, anchor_x= "center" )
        arcade.draw_text(f"health = {self._character.health}", self.window.width * .25, self.window.height * .65, arcade.color.BLACK, 13, anchor_x= "center" )
        arcade.draw_text(f"health = {self._enemy.health}", self.window.width * .75, self.window.height * .65, arcade.color.BLACK, 13, anchor_x= "center" )
        arcade.draw_text(f"How would you like to fight this enemy", self.window.width * .5, self.window.height * .85, arcade.color.BLACK, 13, anchor_x= "center" )
        arcade.draw_text(f"Select A to attack, B to defend, C to run", self.window.width * .5, self.window.height * .75, arcade.color.BLACK, 13, anchor_x= "center" )
        arcade.draw_text(f"attack = {self._character.attacking}", self.window.width * .25, self.window.height * .60, arcade.color.BLACK, 13, anchor_x= "center" )
        arcade.draw_text(f"defend = {self._character.defending}", self.window.width * .25, self.window.height * .55, arcade.color.BLACK, 13, anchor_x= "center" )
        arcade.draw_text(f"running = {self._character.running}", self.window.width * .25, self.window.height * .50, arcade.color.BLACK, 13, anchor_x= "center" )
        arcade.draw_text(f"attack = {self._enemy.attacking}", self.window.width * .75, self.window.height * .60, arcade.color.BLACK, 13, anchor_x= "center" )
        arcade.draw_text(f"defend = {self._enemy.defending}", self.window.width * .75, self.window.height * .55, arcade.color.BLACK, 13, anchor_x= "center" )
        arcade.draw_text(f"running = {self._enemy.running}", self.window.width * .75, self.window.height * .50, arcade.color.BLACK, 13, anchor_x= "center" )


        self._character.draw()
        self._enemy.draw()
        return super().on_draw()
    
    
    # getting key press for user battle selection
    def on_key_press (self, key, mofiers):
        if self._character.health >= 0 and self._enemy.health <= 0:
            return

        if key == arcade.key.A:
            battle_choice_user = self._character.attacking
        elif key == arcade.key.B:
            battle_choice_user = self._character.defending
        else:
            battle_choice_user = self._character.running

        self.handle_battle(battle_choice_user) 
    
    #battle itself is being handled
    def handle_battle(self, battle_choice_user):
        enemy_battle_choice = random.choice(['attacking', 'running', 'defending'])
        battle_choice_en = getattr(self._enemy, enemy_battle_choice)


        if battle_choice_user > battle_choice_en:
            calc = battle_choice_user - battle_choice_en
            self._character.health  += calc
            self._enemy.health -= calc
            self._character.loot += random.randint(5, 15)
            self._character.defending += 10
        elif battle_choice_user <= battle_choice_en:
            calc = battle_choice_en - battle_choice_user
            self._character.health  -= calc
            self._enemy.health += calc
            self._enemy.defending += 10

        #the user has won and defeated the final boss - the game is over
        if self._character.health > 0 and self._enemy.health <= 0:
            if self._enemy.name == "The evil, little, small chef":
                new_view = Victory()
                self.window.show_view(new_view)
        #the user won the battle... but there are more battles to be had, back to navigate
            else:
                self._character.center_x = self._original_x
                self._character.center_y = self._original_y
                new_view = Navigation(self.window, self._character, reset_position = False, current_level = self._current_level)
                self.window.show_view(new_view)
        #the user has lost
        elif self._character.health <= 0: 
            new_view = LoserNation()
            self.window.show_view(new_view)


class Victory(arcade.View):
    def __init__(self, window = None):
        super().__init__(window)
        arcade.set_background_color(arcade.color.LIGHT_YELLOW)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Congratulations chef, you have won!", self.window.width/2, self.window.height/2, arcade.color.BLACK, 18, anchor_x= "center" )
        return super().on_draw()

class LoserNation(arcade.View):
    def __init__(self, window = None):
        super().__init__(window)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Oh no! You lost!", self.window.width/2, self.window.height/2, arcade.color.WHITE, 18, anchor_x= "center" )
        arcade.draw_text("Press A to quit and B to try again", self.window.width/2, self.window.height/4, arcade.color.WHITE, 18, anchor_x= "center" )

        return super().on_draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            arcade.close_window()
        else:
            game_world = {"width" : 7, "height" :7, (0,0): 0, (1,0): 1, (2,0): 1, (3,0): random.randint(0,3), (4,0): 1, (5, 0): random.randint(0,3), (6,0):random.randint(0,3),
                  (0,1): 1, (1,1): random.randint(0,3), (2,1):random.randint(0,3), (3,1): random.randint(0,3), (4,1):random.randint(0,3), (5, 1): random.randint(0,3), (6,1):random.randint(0,3),
                  (0,2): random.randint(0,3), (1,2): random.randint(0,3), (2,2): random.randint(0,3), (3,2): random.randint(0,3), (4,2): random.randint(0,3), (5, 2): random.randint(0,3), (6,2):random.randint(0,3),
                  (0,3): 1, (1,3): random.randint(0,3), (2,3): 1, (3,3): 0, (4,3): random.randint(0,3),(5, 3): random.randint(0,3), (6,3):random.randint(0,3),
                  (0,4): random.randint(0,3), (1,4): random.randint(0,3), (2,4): random.randint(0,3), (3,4): random.randint(0,3), (4,4): random.randint(0,3), (5, 4): random.randint(0,3), (6,4):random.randint(0,3), 
                  (0,5): 0, (1,5): random.randint(0,3), (2,5): random.randint(0,3), (3,5): 1, (4,5): random.randint(0,3), (5, 5): 0, (6,5):random.randint(0,3),
                  (0,6): random.randint(0,3), (1,6): random.randint(0,3), (2,6): 1, (3, 6): random.randint(0,3), (4,6): random.randint(0,3), (5, 6): random.randint(0,3), (6,6):4 }
            cell_size = 100
            window = MyGame(game_world, cell_size)
            window_view = WelcomeView(window)
            window.show_view(window_view)
       



class Character(arcade.Sprite):
    def __init__ (self, filename, attacking, running, defending, health, loot, center_x , center_y, x, y, name):
        '''
        PARAMETERS:

        filename- the file holding the character's sprite
        attacking- the value the character has for attacking
        running- the value the character has for running
        defending- the value the character has for defending
        health- the characters health level throughout the game (will change after battles)
        loot- the loot the character has, starts at 0 builds its way up as battles and cheese wheels are collected
        center_y - y coordinant position
        center_x - x coordinant position
        name - characters name !

        This class is used to create the characters that the user will be able to use as they walk through the 
        game ! It also contains the add xp function
        '''
        super().__init__(filename, center_x = center_x, center_y = center_y)
        self.attacking = attacking
        self.running = running
        self.defending = defending
        self.health = health
        self.loot = loot
        self.x = x
        self.y = y
        self.name = name
    

    def add_xp(self, xp_amt):
        self.xp_amt += xp_amt
        engine.compute_level(xp_amt)

    
class Enemy(arcade.Sprite):
    def __init__ (self, filename, attacking, running, defending, health, center_x , center_y, name ):
        '''
        PARAMETERS:

        filename- the file holding the enemy's sprite
        attacking- the value the enemy has for attacking
        running- the value the enemy has for running
        defending- the value the enemy has for defending
        health- the enemy's health level throughout the game (will change during battles)
        center_y - y coordinant position
        center_x - x coordinant position
        name - enemy's name !

        This class is used to create the enemies that the user will battle throughout the course of the game
        '''
        super().__init__(filename, center_x = center_x, center_y = center_y)
        self.attacking = attacking
        self.running = running
        self.defending = defending
        self.health = health
        self.name = name

class MyGame(arcade.Window):
    def __init__(self, game_world, cell_size):
        self._game_world = game_world
        self._cell_size = cell_size
        super().__init__(game_world["width"]*cell_size, game_world["height"]*cell_size)

def main():
    title = "My Awesome Dungeon Crawler!"
    # The following starts up the arcade system and starts handling your inputs.
    game_world = {"width" : 7, "height" :7, (0,0): 0, (1,0): 1, (2,0): 1, (3,0): random.randint(0,3), (4,0): 1, (5, 0): random.randint(0,3), (6,0):random.randint(0,3),
                  (0,1): 1, (1,1): random.randint(0,3), (2,1):random.randint(0,3), (3,1): random.randint(0,3), (4,1):random.randint(0,3), (5, 1): random.randint(0,3), (6,1):random.randint(0,3),
                  (0,2): random.randint(0,3), (1,2): random.randint(0,3), (2,2): random.randint(0,3), (3,2): random.randint(0,3), (4,2): random.randint(0,3), (5, 2): random.randint(0,3), (6,2):random.randint(0,3),
                  (0,3): 1, (1,3): random.randint(0,3), (2,3): 1, (3,3): 0, (4,3): random.randint(0,3),(5, 3): random.randint(0,3), (6,3):random.randint(0,3),
                  (0,4): random.randint(0,3), (1,4): random.randint(0,3), (2,4): random.randint(0,3), (3,4): random.randint(0,3), (4,4): random.randint(0,3), (5, 4): random.randint(0,3), (6,4):random.randint(0,3), 
                  (0,5): 0, (1,5): random.randint(0,3), (2,5): random.randint(0,3), (3,5): 1, (4,5): random.randint(0,3), (5, 5): 0, (6,5):random.randint(0,3),
                  (0,6): random.randint(0,3), (1,6): random.randint(0,3), (2,6): 1, (3, 6): random.randint(0,3), (4,6): random.randint(0,3), (5, 6): random.randint(0,3), (6,6):4 }
    cell_size = 100
    window = MyGame(game_world, cell_size)
    window_view = WelcomeView(window)
    window.show_view(window_view)
    arcade.run()

'''
Do not edit below!
'''
if __name__ == '__main__':
    main()