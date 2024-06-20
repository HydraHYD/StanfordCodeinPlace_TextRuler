from graphics import Canvas
from button import *


#Global variables [current object placements are based on a (400, 400) canvas]
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def main():
    #Initiate canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    #Local variables for main
        #Booleans as switches
    running = True
    recording = False
        #Starting values for functions
    input_text = ""
    target_change = 0
    text = "Your text here"
    font = "Arial Black"
    font_size = 24
    width = 100
    height = 100

    #Initate objects
        #Buttons
    buttons_w, buttons_h = draw_scale_buttons(canvas)
    button_text, button_font, button_size = draw_change_buttons(canvas)
    draw_input_button(canvas, input_text)
        #Static text
    width_text, height_text = update_scale_text(canvas, width, height)
        #Adjustable text/rectangle object
    box = draw_objects(canvas, width, height, text, font, font_size)
        #Input display text
    canvas.create_text(75, 380, "Press Enter to Confirm Input", "Arial Black", 16)

    #Program loop
    while running == True:
        #Get mouse and keyboard data
        click = canvas.get_last_click()
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        key = canvas.get_last_key_press()

        #Loop for user inputs (records every keyboard character besides the Enter key)
        if recording == True:
            if key != None:
                if key == "Enter":
                    #On successful user input
                    clear_button_colors(button_text, button_font, button_size, "white")
                    try:
                        if target_change == 1:
                            text = input_text
                        elif target_change == 2:
                            font = input_text
                        elif target_change == 3:
                            font_size = int(input_text)
                    except:
                        pass
                    
                    #Reset for future inputs
                    recording = False
                    target_change = 0
                    input_text = ""

                    box.delete_button()
                    box = draw_objects(canvas, width, height, text, font, font_size)
                    draw_input_button(canvas, input_text)

                else:
                    input_text = input_text + key
                    draw_input_button(canvas, input_text)

        #Check for button interactions if a click has been made
        if click != None:
            #Check width and height buttons
            for i in buttons_w:
                if i.detect_click(mouse_x, mouse_y):
                    width += i.value
                    box.delete_button()
                    box = draw_objects(canvas, width, height, text, font, font_size)
                    canvas.delete(width_text)
                    canvas.delete(height_text)
                    width_text, height_text = update_scale_text(canvas, width, height)
            for i in buttons_h:
                if i.detect_click(mouse_x, mouse_y):
                    height += i.value
                    box.delete_button()
                    box = draw_objects(canvas, width, height, text, font, font_size)
                    canvas.delete(width_text)
                    canvas.delete(height_text)
                    width_text, height_text = update_scale_text(canvas, width, height)
            
            #Check user input buttons
            if button_text.detect_click(mouse_x, mouse_y):
                recording = True
                clear_button_colors(button_text, button_font, button_size, "white")
                button_text.change_color('orange')
                target_change = 1
            if button_font.detect_click(mouse_x, mouse_y):
                recording = True
                clear_button_colors(button_text, button_font, button_size, "white")
                button_font.change_color('orange')
                target_change = 2
            if button_size.detect_click(mouse_x, mouse_y):
                recording = True
                clear_button_colors(button_text, button_font, button_size, "white")
                button_size.change_color('orange')
                target_change = 3


#Draws the adjustable text and rectangle objects
def draw_objects(canvas, width, height, text, font, font_size):
    box = Button((0, 0), width, height, canvas, 0, 0)
    box.update_button(text, font, font_size)
    return box


#Draws 12 buttons to adjust rectangle scale
def draw_scale_buttons(canvas):
    #Empty lists to hold buttons
    buttons_w = []
    buttons_h = []

    #Base origin, objects are placed in reference to this point
    origins = (22, CANVAS_HEIGHT/2)

    #Width and height of all buttons
    width = 53
    height = 16

    #Displayed text
    texts = ['-100', ' -10', '  -1', '  +1', ' +10', '+100']

    #Button object return value
    values = [-100, -10, -1, 1, 10, 100]

    #Font parameters
    font = "Arial Black"
    font_size = 20

    #Loops to create and add buttons to each list
    for i in range(len(texts)):
        button = Button((origins[0] + i*60, origins[1] - 20), width, height, canvas, 5, values[i])
        button.update_button(texts[i], font, font_size)
        buttons_w.append(button)
    for i in range(len(texts)):
        button = Button((origins[0] + i*60, origins[1] + 40), width, height, canvas, 5, values[i])
        button.update_button(texts[i], font, font_size)
        buttons_h.append(button)

    return buttons_w, buttons_h


#Draws all three user input buttons
def draw_change_buttons(canvas):
    font = "Arial Black"
    font_size = 14
    change_text = Button((15, 300), 97, 13, canvas, 5, "Change Text")
    change_font = Button((150, 300), 97, 13, canvas, 5, "Change Font")
    change_size = Button((285, 300), 96, 13, canvas, 5, "Change Size")
    change_text.update_button("Change Text", font, font_size)
    change_font.update_button("Change Font", font, font_size)
    change_size.update_button("Change Size", font, font_size)
    return change_text, change_font, change_size


#Resets all three user input buttons back to a neutral color (white)
def clear_button_colors(button_text, button_font, button_size, color):
    button_text.change_color(color)
    button_font.change_color(color)
    button_size.change_color(color)


#Draws the input display bar
def draw_input_button(canvas, text):
    font = "Arial Black"
    font_size = 14
    change_input = Button((15, 350), CANVAS_WIDTH-30, 13, canvas, 5, text)
    change_input.update_button(text, font, font_size)


#Updates the width and height display
def update_scale_text(canvas, width, height):
    font = "Arial Black"
    font_size = 20
    origins = (22, CANVAS_HEIGHT/2)
    width_text = canvas.create_text(origins[0], origins[1] - 50, f"Width: {width}", font, font_size)
    height_text = canvas.create_text(origins[0], origins[1] + 10, f"Height: {height}", font, font_size)
    return width_text, height_text

if __name__ == '__main__':
    main()