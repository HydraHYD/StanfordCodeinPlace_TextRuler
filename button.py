from graphics import Canvas

#Button object class to make creating objects easier (creates a rectangular button with optional text and click detection)
class Button:
    def __init__(self, origin, width, height, canvas, margin, value):
        #Initialize properties
        self.origin = origin
        self.width = width
        self.height = height
        self.canvas = canvas
        self.margin = margin
        #Return value if button detects interaction
        self.value = value
        #Starting neutral color
        self.color = "White"
        
    #Creates a rectangle
    def draw_button(self):
        self.button = self.canvas.create_rectangle(self.origin[0] - self.margin, 
        self.origin[1] - self.margin, 
        self.origin[0] + self.width + self.margin, 
        self.origin[1] + self.height + self.margin,
        self.color,
        'black')

    #Draws text
    def draw_text(self, text, font, font_size):
        self.string = text
        self.font = font
        self.font_size = font_size
        self.text = self.canvas.create_text(self.origin[0], 
        self.origin[1], 
        text,
        font, 
        font_size)

    #Changes the color of the button after already being instantialized (drawn)
    def change_color(self, color):
        self.color = color
        self.delete_button()
        self.draw_button()
        self.draw_text(self.string, self.font, self.font_size)

    #Redraws both the button and text without deleting either
    def update_button(self, text, font, font_size):
        self.draw_button()
        try:
            self.draw_text(text, font, font_size)
        except:
            pass

    #Detect a click within the boundaries of the button
    def detect_click(self, mouse_x, mouse_y):
        if mouse_x > self.origin[0] - self.margin and mouse_x < self.origin[0] + self.width + self.margin:
            if mouse_y > self.origin[1] - self.margin and mouse_y < self.origin[1] + self.height + self.margin:
                return True
        return False

    #Destroys this object
    def delete_button(self):
        self.canvas.delete(self.button)
        self.canvas.delete(self.text)