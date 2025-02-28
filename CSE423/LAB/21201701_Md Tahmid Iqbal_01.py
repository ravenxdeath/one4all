##### Name: Tahmid Iqbal 
##### ID: 21201701
##### Assignment 01 
##### github: https://github.com/TahmidRaven 
##### itch.io: https://ravendeath.itch.io/rougeknight  # my 2d platformer game 



# # # # # #  Press Ctrl + U twice to undo comment for Task 01. Task 02 is after Task 01 at line 235


# ### TASK 01 ###

# # INSTRUCTIONS :-

# # keep pressing 'D'= Day or 'N'= Night to change the skin 
# # keep pressing up or down arrow keys to change rain density
# # keep pressing left or right arrowkeys to change rain direction 
# # Esc key to exit


# # from OpenGL.GL import *
# # from OpenGL.GLUT import *
# # from OpenGL.GLU import *
# # import math
# # import random


# # rain_direction_angle = 0.0
# # bg_color = 0.5  # Mid-gray start for dusk
# # raindrops = []
# # rain_density = 250  
# # is_daytime = True  # keeping tyack day/night for rain color

 
# # def init_raindrops():
# #     global raindrops
# #     raindrops = [(random.uniform(-50, 50), random.uniform(-50, 50)) for i in range(rain_density)]

# # def display():
# #     global bg_color
# #     glClearColor(bg_color, bg_color, bg_color, 1.0)  # Background color changes for day/night
# #     glClear(GL_COLOR_BUFFER_BIT)

# #     # roof
# #     glColor3f(0.75, 0.58, 0.89)  
# #     glBegin(GL_TRIANGLES)
# #     glVertex2f(-10, -10)   
# #     glVertex2f(0, 10)     
# #     glVertex2f(10, -10)
# #     glEnd()
    
# #     glColor3f(0.1, 0.7, 1.0)  # custom lavender of my choice
# #     glBegin(GL_LINES)
# #     glVertex2f(-10, -10)  # Left  roof
# #     glVertex2f(0,10)
# #     glVertex2f(10, -10)  # Left  root
# #     glVertex2f(0,10)
    
# #     glVertex2f(10, -10)
# #     glVertex2f(-10, -10)   
# #     glEnd()

# #     # house walls
# #     glColor3f(0.1, 0.7, 1.0)     
# #     glLineWidth(3)            
      
# #     glBegin(GL_LINES)
    
# #     glVertex2f(-10, -30)  # Left  
# #     glVertex2f(-10, -10)
# #     glVertex2f(10, -30)   # Right 
# #     glVertex2f(10, -10)
    
# #     glVertex2f(-10, -30)  # Bottom 
# #     glVertex2f(10, -30)
# #     glEnd()

# #     # # door knob
# #     glColor3f(0.1, 0.0, 1.0)   
# #     glPointSize(3.5)            
# #     glBegin(GL_POINTS)
    
# #     glVertex2f(1, -26)         
# #     glEnd()

# #     # door
# #     glColor3f(0.5, 0.35, 0.2)  
# #     glBegin(GL_LINES)
# #     glVertex2f(-2, -30)  # Left  
# #     glVertex2f(-2, -20)
    
# #     glVertex2f(2, -30)   # Right 
# #     glVertex2f(2, -20)
# #     glVertex2f(-2, -20)  # Top 
# #     glVertex2f(2, -20)
# #     glEnd()
    
# #     # window
# #     glColor3f(0.5, 1.0, 0.2)  
# #     glBegin(GL_LINES)
# #     glVertex2f(4, -15)   
# #     glVertex2f(7, -15)
# #     glVertex2f(4, -18)   
# #     glVertex2f(7, -18)
# #     glVertex2f(4, -15)   
# #     glVertex2f(4, -18)   

# #     glVertex2f(7, -15)
# #     glVertex2f(7, -18)  
    
    
# #     glVertex2f(4, -15)
# #     glVertex2f(7, -18)   
    
# #     glVertex2f(7, -15)
# #     glVertex2f(4, -18)
    
    
       
    
      
# #     glEnd()
    

 
 

# #     # Rain color changes based on day/night
# #     if is_daytime:
# #         glColor3f(0.0, 0.0, 0.0)  # Dark blue for daytime  
# #     else:
# #         glColor3f(1.0, 1.0, 0.0)  # Yellow for nighttime  

# #     glPointSize(1.5)

# #     glBegin(GL_POINTS)
# #     for drop in raindrops:
# #         glVertex2f(drop[0], drop[1])
# #     glEnd()

# #     glutSwapBuffers()

 
# # def rain_ani(value):
# #     global raindrops, rain_direction_angle
# #     new_drops = []
# #     for (x, y) in raindrops:
       
# #         x += math.sin(rain_direction_angle) * 0.5   
# #         y -= 0.7   

        
# #         if y < -50:
# #             y = 50
# #             x = random.uniform(-50, 50)  

# #         new_drops.append((x, y))

# #     raindrops = new_drops
# #     glutPostRedisplay()
# #     glutTimerFunc(16, rain_ani, 0)  # 60 FPS

 

# # def keyboard(key, x, y):
# #     global rain_direction_angle, bg_color, is_daytime

# #     if key == b'\x1b':  # Escape key to exit
# #         print("ESC pressed: Exiting program.")
# #         glutLeaveMainLoop()

# #     elif key == b'd':  # Daytime mode
# #         bg_color = min(1.0, bg_color + 0.01)
# #         is_daytime = True
# #         print("Switching to daytime mode.")

# #     elif key == b'n':  # Nighttime mode
# #         bg_color = max(0.0, bg_color - 0.01)
# #         is_daytime = False
# #         print("Switching to nighttime mode.")


# # def special_input(key, x, y):
# #     global rain_direction_angle, raindrops, rain_density

# #     if key == GLUT_KEY_LEFT:  # left
# #         rain_direction_angle -= 0.05
# #         print("Rotating rain to the left.")

# #     elif key == GLUT_KEY_RIGHT:  # right
# #         rain_direction_angle += 0.05
# #         print("Rotating rain to the right.")

# #     elif key == GLUT_KEY_UP:   
# #         if rain_density < 300:
# #             rain_density += 10
# #             init_raindrops()
# #             print(f"Increasing rain density to {rain_density}.")
# #         else:
# #             print("Rain density is already at maximum.")

# #     elif key == GLUT_KEY_DOWN:  
# #         if rain_density > 10:
# #             rain_density -= 10
# #             init_raindrops()
# #             print(f"Decreasing rain density to {rain_density}.")
# #         else:
# #             print("Rain density is already at minimum.")


 
# # def main():
# #     glutInit()
# #     glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
# #     glutInitWindowSize(800, 600)
# #     glutCreateWindow(b"Raven's house on a rainy day")
# #     gluOrtho2D(-50, 50, -50, 50)

# #     init_raindrops()
# #     glutDisplayFunc(display)
# #     glutTimerFunc(0, rain_ani, 0)
# #     glutKeyboardFunc(keyboard)
# #     glutSpecialFunc(special_input)
# #     glutMainLoop()

# # if __name__ == "__main__":
# #     main()


 



### TASK 02 ###

# # ## Instuctions:
# # # right mouse = generate stars 
# # # left mouse = toggle blink
# # # space = freeze/unfreeze
# # # Escape = exit
# # # up arrow = increase speed
# # # down arrow = decrease speed


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

 
Amazing_box = 50  
stars = []   
is_frozen = False
speed = 0.2   
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1)]

 
class STAR_CLASS:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.choice([-1, 1]) * speed
        self.dy = random.choice([-1, 1]) * speed
        self.color = random.choice(colors)
        self.visible = True  # blinking vari
        # Each point has unique blink interval (between 300 to 1000 ms)x
        # what I'm terying to do here is make them blink randomly so that it seems like a sky 
        # the left mouse button will toggle between blink and not blink however because of the random interval
        # it's hard to notice ; if you increase the interval from 250 to 900 you might see it. 
        self.blink_interval = random.randint(250, 1000)

    def update_position(self):
        if not is_frozen:
            self.x += self.dx
            self.y += self.dy

            # when it bounces off of a wall it will reversee
            if self.x > Amazing_box or self.x < -Amazing_box:
                self.dx = -self.dx
            if self.y > Amazing_box or self.y < -Amazing_box:
                self.dy = -self.dy

    def blink(self):
        # Toggles visibility when blinking
        self.visible = not self.visible

 
def display():
    glClear(GL_COLOR_BUFFER_BIT)

   
    glColor3f(0, 1, 1)  
    glBegin(GL_LINE_LOOP)
    glVertex2f(-Amazing_box, -Amazing_box)
    glVertex2f(Amazing_box, -Amazing_box)
    glVertex2f(Amazing_box, Amazing_box)
    glVertex2f(-Amazing_box, Amazing_box)
    glEnd()

 
    glPointSize(5.0)  

    
    for point in stars:
        if point.visible:
            glColor3f(*point.color)
            glBegin(GL_POINTS)
            glVertex2f(point.x, point.y)
            glEnd()

    glutSwapBuffers()

 
def updated_star(value):
    if not is_frozen:
        for point in stars:
            point.update_position()
    glutPostRedisplay()
    glutTimerFunc(16, updated_star, 0)  # 60 FPS

 
def blink_timer(value):
    if not is_frozen:
        for point in stars:
            # Use each point's unique blink interval
            if random.randint(0, point.blink_interval) < 50:   
                point.blink()
    glutTimerFunc(100, blink_timer, 0)   

 
def mouse(button, state, x, y):
    if state == GLUT_DOWN:
        window_width = glutGet(GLUT_WINDOW_WIDTH)
        window_height = glutGet(GLUT_WINDOW_HEIGHT)
 
        px = (x - window_width / 2) / (window_width / Amazing_box)
        py = -(y - window_height / 2) / (window_height / Amazing_box)

        if button == GLUT_RIGHT_BUTTON:  # Right-click to spawn a new point
            stars.append(STAR_CLASS(px, py))
            print(f"New star in the sky")
        elif button == GLUT_LEFT_BUTTON:  # Left-click to toggle blink
            blink_timer(0)
            print(f"You made the star blink")
            

 
def keyboard(key, x, y):
    global is_frozen, speed
    if key == b' ':
        is_frozen = not is_frozen  # Toggle freeze/unfreeze
        print(f"You've the power to freeze the sky")
        
    elif key == b'\x1b':  # Escape key to exit
        glutLeaveMainLoop()
        print(f"You're done playing with stars")
        

 
def special_input(key, x, y):
    global speed
    if not is_frozen:
        if key == GLUT_KEY_UP:
            speed += 0.05
            print(f"You're making the stars go faster")
              
        elif key == GLUT_KEY_DOWN:
            speed = max(0.05, speed - 0.05) 
            print(f"You're making the stars go slower")
            
            # Min=> speed of 0.05 to prevent stopping
            
        for point in stars:
            point.dx = (point.dx / abs(point.dx)) * speed
            point.dy = (point.dy / abs(point.dy)) * speed
 
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 500)
    glutCreateWindow(b"Raven's Amazing Box with Randomly Blinking Points")
    gluOrtho2D(-Amazing_box, Amazing_box, -Amazing_box, Amazing_box)

 
    glutDisplayFunc(display)
    glutTimerFunc(0, updated_star, 0)
    glutMouseFunc(mouse)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_input)
 
    blink_timer(0)
    glutMainLoop()

if __name__ == "__main__":
    main()
