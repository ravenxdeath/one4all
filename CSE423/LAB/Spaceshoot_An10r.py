from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

#window information
window_width=600
window_height=900
#shooter information
x_center=window_width//2
y_center=20
shooterspeed=15
radius=15
#fireball information
shooter_fireposition_x=x_center
shooter_fireposition_y=y_center+radius+4
fire_speed=15
fire_details=[] #to keep track of the fireballs co-ord's
#color information
yellow = (1.0, 1.0, 0.0)
uniball_color=yellow #universal color for shooter, asteroid, fireballs
#general inndormations
score=0
lives=3 #to keep track how many how many asteroid were missed
pause_count=0
count=0 #to keep track how many fires misfired
#status flags
pause_flag = False
gameover_flag = False
restarted_flag = False 
fire_flag=False
#asteroid information
falling_asteroid=[] #to keep track of the falling circle's co-ord's
asteroid_speed=2.75


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)
    left_arrow()
    cross()
    draw_shooter()
    if not gameover_flag:
        drawfire()
        for asteroid in falling_asteroid:
            glColor3fv(uniball_color) 
            midpointCircle(asteroid['x'], asteroid['y'], asteroid['radius'])
    if (pause_flag==True):
        pause()
    if (pause_flag==False):
        play()
    glutSwapBuffers()

def drawPixel(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
def drawCirclePoints(xc, yc, x, y):
    drawPixel(xc+x, yc+y)
    drawPixel(xc-x, yc+y)
    drawPixel(xc+x, yc-y)
    drawPixel(xc-x, yc-y)
    drawPixel(xc+y, yc+x)
    drawPixel(xc-y, yc+x)
    drawPixel(xc+y, yc-x)
    drawPixel(xc-y, yc-x)

def draw_shooter():
    global x_center,y_center,ball_color,radius
    glColor3fv(uniball_color)
    midpointCircle(x_center,y_center,radius)

def midpointCircle(x_center, y_center, radius):
    x = 0
    y = radius
    p = 1 - radius
    drawCirclePoints(x_center, y_center, x, y)
    while x < y:
        x += 1
        if p < 0:
            p = p + 2*x + 1
        else:
            y -= 1
            p = p + 2*x - 2*y + 1
        
        drawCirclePoints(x_center, y_center, x, y)

def find_zone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    zone = -1
    if abs(dx) > abs(dy):
        if dx > 0:
            if dy > 0:
                zone = 0
            else:
                zone = 7
        else:
            if dy > 0:
                zone = 3
            else:
                zone = 4
    else:
        if dy > 0:
            if dx > 0:
                zone = 1
            else:
                zone = 2
        else:
            if dx > 0:
                zone = 6
            else:
                zone = 5
    return zone


def convert(original_zone,x,y):
    if (original_zone == 0):
        return x,y
    elif (original_zone == 1):
        return y,x
    elif (original_zone == 2):
        return -y,x
    elif (original_zone == 3):
        return -x,y
    elif (original_zone == 4):
        return -x,-y
    elif (original_zone == 5):
        return -y,-x
    elif (original_zone == 6):
        return -y,x
    elif (original_zone == 7):
        return x,-y

def convert_original(original_zone,x,y):
    if (original_zone == 0):
        return x,y
    elif (original_zone == 1):
        return y,x
    elif (original_zone == 2):
        return -y,-x
    elif (original_zone == 3):
        return -x,y
    elif (original_zone == 4):
        return -x,-y
    elif (original_zone == 5):
        return -y,-x
    elif (original_zone == 6):
        return y,-x
    elif (original_zone == 7):
        return x,-y

def midpointline(zone,x0,y0, x1,y1):
    dx = x1-x0
    dy = y1-y0
    d = (2*dy) - dx
    forE = 2*dy
    forNE = 2*(dy-dx)
    x = x0
    y = y0
    while (x < x1):
        org_x, org_y = convert_original(zone,x,y)
        drawPixel(org_x,org_y)
        if (d<=0):
            x += 1
            d += forE
        else:
            x += 1
            y += 1
            d += forNE

def eight_way_symmetry(x0,y0,x1,y1):
    zone = find_zone(x0,y0,x1,y1)
    conv_x0, conv_y0 = convert(zone,x0,y0)
    conv_x1, conv_y1 = convert(zone,x1,y1)
    midpointline(zone,conv_x0,conv_y0,conv_x1,conv_y1)  


def mouseListener(button,state,x,y):
    global pause_flag,restarted_flag,gameover_flag,pause_count
    new_y=window_height-y
    if (button==GLUT_LEFT_BUTTON) and (state==GLUT_DOWN):
        #restart
        if (20<=x<=100) and (845<=new_y<=855):
            restarted_flag=True
            print("Starting over")
        #pause
        if(297<=x<=310) and (820<=new_y<=870):
            if not gameover_flag:
                pause_count+=1
                if(pause_count%2 !=0):
                    pause_flag = True
                    print(f"Pause Score: {score}")
                elif(pause_count%2 ==0):
                    pause_flag = False
                    print('Game Resumed')
        #terminate
        if (500<=x<=575) and (840<=new_y<=880):
            print(f"Goodbye! Score: {score}")
            glutLeaveMainLoop()

def keylistener(key,x,y):
    global x_center,radius,fire_flag,shooter_fireposition_x,shooter_fireposition_y,gameover_flag
    if not gameover_flag:
        xl=x_center-radius
        xr=x_center+radius
        if (pause_flag==False):
            if key == b'a':
                if (xl>0):
                    x_center-=shooterspeed
            if key == b'd':
                if (xr<600):
                    x_center+=shooterspeed
            if key == b' ':
                fire_flag=True
                shooter_fireposition_x = x_center
                shooter_fireposition_y = y_center + radius+4
                fire_details.append({'x': shooter_fireposition_x, 'y': shooter_fireposition_y})
    glutPostRedisplay()
    
def cross():
    glColor3f(1.0,0.0,0.0)
    eight_way_symmetry(500,840,575,880)
    eight_way_symmetry(500,880,575,840)

def play():
    glColor3f(1.0,1.0,0.0)
    eight_way_symmetry(297,870,297,820)
    eight_way_symmetry(310,870,310,820)
    
def pause():
    glColor3f(1.0,1.0,0.0)
    eight_way_symmetry(297,870,297,820)
    eight_way_symmetry(297,870,310,845)
    eight_way_symmetry(297,820,310,845)

def iterate():
    glViewport(0,0,600,900)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0,600,0.0,900,0.0,1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def left_arrow():
    glColor3f(0.0,1.0,1.0)
    eight_way_symmetry(20,850,100,850)
    eight_way_symmetry(40,855,20,850)
    eight_way_symmetry(40,845,20,850)    
    
def drawfire():
    #to draw the fire particle
    global fire_details
    for fireball in fire_details:
        midpointCircle(fireball['x'], fireball['y'],4)

def create_falling_circles(): 
    global falling_asteroid
    while len(falling_asteroid) < 5:
        overlapping = False
        x_pos = random.randint(25, 575)
        y_pos = 692 
        r = random.randint(15, 25)
        # Checking overlapping or not
        for asteroid in falling_asteroid:
            dx = asteroid['x'] - x_pos
            dy = asteroid['y'] - y_pos
            distance = (dx**2 + dy**2)**0.5
            if distance < asteroid['radius'] + r:
                overlapping = True
                break
        # If not overlapping
        if not overlapping:
            falling_asteroid.append({'x': x_pos, 'y': y_pos, 'radius': r})
   
def update(value):
    global score,lives,pause_count,count,pause_flag, gameover_flag,restarted_flag, fire_flag, x_center,y_center,radius,shooter_fireposition_y, shooter_fireposition_x,uniball_color,falling_asteroid,fire_details
    if restarted_flag==True:
        score=0
        lives=3
        pause_count=0
        count=0
        x_center=window_width//2
        y_center=20
        shooter_fireposition_x=x_center
        shooter_fireposition_y=y_center+radius+4
        fire_flag=False
        uniball_color=yellow
        pause_flag=False
        gameover_flag=False
        fire_details.clear()
        falling_asteroid.clear()
        create_falling_circles()
        restarted_flag=False
        
    #checking if game paused or game over based on that stopping movement of every particle
    if pause_flag or gameover_flag:
        glutPostRedisplay()
        glutTimerFunc(10, update, 0)
        return
    #if game is not over yet
    if not gameover_flag:
        move_fireballs() #fireball going upwards and checking if it missfires three times
        move_asteroids() #asteroid falling down and checking if it misses three asteroids
        check_collisions() #collision checking between fireball and asteroids and checking if asteroid falls right over the shooter
        maintain_falling_asteroids() #to maintian 5 asteroids all the time
    glutPostRedisplay()
    glutTimerFunc(33, update, 0)
    
def move_fireballs():
    global fire_details,count,gameover_flag,pause_flag,fire_speed
    for fireball in fire_details:
        fireball['y'] += fire_speed #updating the fireball position
        if fireball['y'] > 817:
            count+=1
            fire_details.remove(fireball)
            print(f"You misfired {count} times")
            if count>=3:
                gameover_flag = True
                pause_flag = True
                print("You misfired three times and failed to hit any falling circle three times")
                print("Game Over! Final Score:", score)
                break

def move_asteroids():
    global lives,asteroid_speed,gameover_flag,pause_flag
    for asteroid in falling_asteroid:
        asteroid['y'] -= asteroid_speed  #updating the asteroids position
        if asteroid['y'] < 0:
            falling_asteroid.remove(asteroid)
  
            lives-=1
            print(f"Current avilable life: {lives}")
            if lives <= 0:
                gameover_flag = True
                pause_flag = True
                print("You lost as three circles crossed the bottom boundary")
                print("Game Over! Final Score:", score)
                break 
            
def check_collisions():
    global score,falling_asteroid,fire_details,x_center,y_center,radius,gameover_flag,pause_flag
    #checking if asteroid falls right over the shooter
    for asteroid in falling_asteroid:
        if ((x_center - asteroid['x']) ** 2 + (y_center - asteroid['y']) ** 2) ** 0.5 < (radius + asteroid['radius']):
            gameover_flag = True
            pause_flag = True
            falling_asteroid.clear()  
            print("You failed because a falling circle directly collided with the circle shooter.")
            print("Game Over! Final Score:", score)
            return
    #collision checking between fireball and asteroids
    for fireball in fire_details[:]:
        for asteroid in falling_asteroid[:]:
            distance = ((fireball['x'] - asteroid['x']) ** 2 + (fireball['y'] - asteroid['y']) ** 2) ** 0.5
            if distance < asteroid['radius']:
                fire_details.remove(fireball)
                falling_asteroid.remove(asteroid)
                score += 1
                print(f"Score: {score}")
                break 

def maintain_falling_asteroids():
    if len(falling_asteroid) < 5:  # Add new asteroids if fewer than 5 are present
        create_falling_circles()

print("Each  falling circle that crosses the window boundary will cost you one life.") 
print(f"Lives : {lives}")      
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(window_width,window_height)
glutInitWindowPosition(1100,0)
glutCreateWindow(b"Shoot the circles!")
glutDisplayFunc(showScreen)
glutMouseFunc(mouseListener)
glutKeyboardFunc(keylistener)
glutTimerFunc(10, update, 0)
glutMainLoop()