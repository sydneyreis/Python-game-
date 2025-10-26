import arcade

SCREEN_WIDTH = 800
# making the screen taller!
SCREEN_HEIGHT = 700


def draw_grass():
    """ Draw the ground """
    #drawing the grass, does not need to be centered with x, y coordinants
    # changed background color
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.BLUE_BELL)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    # drawing the bodies of the snow men, just using the draw function within arcade to make and fill in circles 
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    # drawing the yes, using the drae function w/in arcade, but positioning them using x and y coordinants
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)

    # Creating a nose... it is like a carrot but from a front view
    arcade.draw_circle_filled(x - 7.5, 203 + y, 5, arcade.color.ORANGE)



def main():
    #setting the window to prepare for drawing
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    #calling the draw grass function
    draw_grass()
    #calling the snowman functions and passing in their respective x and y coordinants
    draw_snow_person(150, 140)
    draw_snow_person(450, 180)
    #added another snowman... he is lurking half on and half off the screen
    draw_snow_person(0, 220)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()