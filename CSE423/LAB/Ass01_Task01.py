## TASK 01 ###

# INSTRUCTIONS :-

# keep pressing 'D'= Day or 'N'= Night to change the skin 
# keep pressing up or down arrow keys to change rain density
# keep pressing left or right arrowkeys to change rain direction 
# Esc key to exit


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random


rain_direction_angle = 0.0
bg_color = 0.5  # Mid-gray start for dusk
raindrops = []
rain_density = 250  
is_daytime = True  # keeping tyack day/night for rain color

 
def init_raindrops():
    global raindrops
    raindrops = [(random.uniform(-50, 50), random.uniform(-50, 50)) for i in range(rain_density)]

def display():
    global bg_color
    glClearColor(bg_color, bg_color, bg_color, 1.0)  # Background color changes for day/night
    glClear(GL_COLOR_BUFFER_BIT)

    # roof
    glColor3f(0.75, 0.58, 0.89)  
    glBegin(GL_TRIANGLES)
    glVertex2f(-10, -10)   
    glVertex2f(0, 10)     
    glVertex2f(10, -10)
    glEnd()
    
    glColor3f(0.1, 0.7, 1.0)  # custom lavender of my choice
    glBegin(GL_LINES)
    glVertex2f(-10, -10)  # Left  roof
    glVertex2f(0,10)
    glVertex2f(10, -10)  # Left  root
    glVertex2f(0,10)
    
    glVertex2f(10, -10)
    glVertex2f(-10, -10)   
    glEnd()

    # house walls
    glColor3f(0.1, 0.7, 1.0)     
    glLineWidth(3)            
      
    glBegin(GL_LINES)
    
    glVertex2f(-10, -30)  # Left  
    glVertex2f(-10, -10)
    glVertex2f(10, -30)   # Right 
    glVertex2f(10, -10)
    
    glVertex2f(-10, -30)  # Bottom 
    glVertex2f(10, -30)
    glEnd()

    # # door knob
    glColor3f(0.1, 0.0, 1.0)   
    glPointSize(3.5)            
    glBegin(GL_POINTS)
    
    glVertex2f(1, -26)         
    glEnd()

    # door
    glColor3f(0.5, 0.35, 0.2)  
    glBegin(GL_LINES)
    glVertex2f(-2, -30)  # Left  
    glVertex2f(-2, -20)
    
    glVertex2f(2, -30)   # Right 
    glVertex2f(2, -20)
    glVertex2f(-2, -20)  # Top 
    glVertex2f(2, -20)
    glEnd()
    
    # window
    glColor3f(0.5, 1.0, 0.2)  
    glBegin(GL_LINES)
    glVertex2f(4, -15)   
    glVertex2f(7, -15)
    glVertex2f(4, -18)   
    glVertex2f(7, -18)
    glVertex2f(4, -15)   
    glVertex2f(4, -18)   

    glVertex2f(7, -15)
    glVertex2f(7, -18)  
    
    
    glVertex2f(4, -15)
    glVertex2f(7, -18)   
    
    glVertex2f(7, -15)
    glVertex2f(4, -18)
    
    
       
    
      
    glEnd()
    

 
 

    # Rain color changes based on day/night
    if is_daytime:
        glColor3f(0.0, 0.0, 0.0)  # Dark blue for daytime  
    else:
        glColor3f(1.0, 1.0, 0.0)  # Yellow for nighttime  

    glPointSize(1.5)

    glBegin(GL_POINTS)
    for drop in raindrops:
        glVertex2f(drop[0], drop[1])
    glEnd()

    glutSwapBuffers()

 
def rain_ani(value):
    global raindrops, rain_direction_angle
    new_drops = []
    for (x, y) in raindrops:
       
        x += math.sin(rain_direction_angle) * 0.5   
        y -= 0.7   

        
        if y < -50:
            y = 50
            x = random.uniform(-50, 50)  

        new_drops.append((x, y))

    raindrops = new_drops
    glutPostRedisplay()
    glutTimerFunc(16, rain_ani, 0)  # 60 FPS

 

def keyboard(key, x, y):
    global rain_direction_angle, bg_color, is_daytime

    if key == b'\x1b':  # Escape key to exit
        print("ESC pressed: Exiting program.")
        glutLeaveMainLoop()

    elif key == b'd':  # Daytime mode
        bg_color = min(1.0, bg_color + 0.01)
        is_daytime = True
        print("Switching to daytime mode.")

    elif key == b'n':  # Nighttime mode
        bg_color = max(0.0, bg_color - 0.01)
        is_daytime = False
        print("Switching to nighttime mode.")


def special_input(key, x, y):
    global rain_direction_angle, raindrops, rain_density

    if key == GLUT_KEY_LEFT:  # left
        rain_direction_angle -= 0.05
        print("Rotating rain to the left.")

    elif key == GLUT_KEY_RIGHT:  # right
        rain_direction_angle += 0.05
        print("Rotating rain to the right.")

    elif key == GLUT_KEY_UP:   
        if rain_density < 300:
            rain_density += 10
            init_raindrops()
            print(f"Increasing rain density to {rain_density}.")
        else:
            print("Rain density is already at maximum.")

    elif key == GLUT_KEY_DOWN:  
        if rain_density > 10:
            rain_density -= 10
            init_raindrops()
            print(f"Decreasing rain density to {rain_density}.")
        else:
            print("Rain density is already at minimum.")


 
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Raven's house on a rainy day")
    gluOrtho2D(-50, 50, -50, 50)

    init_raindrops()
    glutDisplayFunc(display)
    glutTimerFunc(0, rain_ani, 0)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_input)
    glutMainLoop()

if __name__ == "__main__":
    main()