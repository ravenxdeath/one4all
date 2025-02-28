from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

frame_w = 500
frame_h = 650

# Spaceship and game state
spaceship_x = 0
spaceship_speed = 5
bullets = []
obstacles = []  # List to store obstacles (asteroids)
asteroid_speed = .51  # Set initial asteroid speed to a low value
score = 0  # Variable to track the score
game_state = {
    'left_pressed': False,
    'right_pressed': False
}

def points_draw_spaceship(x, y):
    glPointSize(2.7)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def points_draw_asteroid(x, y, size):
    # Use hollow circle for asteroid
    draw_circle(x, y, size)

def draw_line(x1, y1, x2, y2):
    zone = determine_zone(x1, y1, x2, y2)
    x1, y1, x2, y2 = adjust_for_zone(zone, x1, y1, x2, y2)
    points = my_midpoint_algo(x1, y1, x2, y2)
    apply_zone_transform(zone, points)

def my_midpoint_algo(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    del_d = 2 * dy - dx
    North_E = 2 * (dy - dx)
    E = 2 * dy
    
    x = x1
    y = y1
    points.append([x, y])

    while x < x2:
        if del_d <= 0:
            del_d += E
        else:
            del_d += North_E
            y += 1
        x += 1
        points.append([x, y])
    return points

def determine_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx > 0 and dy >= 0:
        if abs(dx) > abs(dy):
            return 0
        else:
            return 1
    elif dx <= 0 <= dy:
        if abs(dx) > abs(dy):
            return 3
        else:
            return 2
    elif dx < 0 and dy < 0:
        if abs(dx) > abs(dy):
            return 4
        else:
            return 5
    elif dx >= 0 > dy:
        if abs(dx) > abs(dy):
            return 7
        else:
            return 6

def adjust_for_zone(zone, x1, y1, x2, y2):
    if zone == 1:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    elif zone == 2:
        x1, y1 = y1, -x1
        x2, y2 = y2, -x2
    elif zone == 3:
        x1, y1 = -x1, y1
        x2, y2 = -x2, y2
    elif zone == 4:
        x1, y1 = -x1, -y1
        x2, y2 = -x2, -y2
    elif zone == 5:
        x1, y1 = -y1, -x1
        x2, y2 = -y2, -x2
    elif zone == 6:
        x1, y1 = -y1, x1
        x2, y2 = -y2, x2
    elif zone == 7:
        x1, y1 = x1, -y1
        x2, y2 = x2, -y2
    return x1, y1, x2, y2

def apply_zone_transform(zone, points):
    if zone == 0:
        for x, y in points:
            points_draw_spaceship(x, y)
    elif zone == 1:
        for x, y in points:
            points_draw_spaceship(y, x)
    elif zone == 2:
        for x, y in points:
            points_draw_spaceship(-y, x)
    elif zone == 3:
        for x, y in points:
            points_draw_spaceship(-x, y)
    elif zone == 4:
        for x, y in points:
            points_draw_spaceship(-x, -y)
    elif zone == 5:
        for x, y in points:
            points_draw_spaceship(-y, -x)
    elif zone == 6:
        for x, y in points:
            points_draw_spaceship(y, -x)
    elif zone == 7:
        for x, y in points:
            points_draw_spaceship(x, -y)

def draw_spaceship(x, y, scale=0.3):
    # Top pointy triangle (nose of spaceship)
    draw_line(x, y + 50 * scale, x - 20 * scale, y + 20 * scale)  # left side of triangle
    draw_line(x, y + 50 * scale, x + 20 * scale, y + 20 * scale)  # right side of triangle
    draw_line(x - 20 * scale, y + 20 * scale, x + 20 * scale, y + 20 * scale)  # bottom of triangle
    
    # Body of spaceship (rectangle)
    draw_line(x - 20 * scale, y + 20 * scale, x - 30 * scale, y - 20 * scale)  # left side of body
    draw_line(x + 20 * scale, y + 20 * scale, x + 30 * scale, y - 20 * scale)  # right side of body
    draw_line(x - 30 * scale, y - 20 * scale, x + 30 * scale, y - 20 * scale)  # bottom of body

    # Wings (diagonal lines on both sides)
    draw_line(x - 30 * scale, y - 20 * scale, x - 50 * scale, y - 50 * scale)  # left wing
    draw_line(x + 30 * scale, y - 20 * scale, x + 50 * scale, y - 50 * scale)  # right wing

    # Circular window on the spaceship body
    draw_circle(x, y, 10 * scale)  # window position at (x, y) with scaled radius
    
    # Fire at the bottom (3 lines)
    draw_line(x - 20 * scale, y - 20 * scale, x - 10 * scale, y - 50 * scale)  # left fire
    draw_line(x - 22 * scale, y - 22 * scale, x - 12 * scale, y - 52 * scale)  # left fire
    
    draw_line(x + 20 * scale, y - 20 * scale, x + 10 * scale, y - 50 * scale)  # right fire
    draw_line(x + 22 * scale, y - 22 * scale, x + 12 * scale, y - 52 * scale)  # right fire
    
    draw_line(x, y - 20 * scale, x, y - 50 * scale)  # middle fire
    draw_line(x + 2 * scale, y - 22 * scale, x, y - 52 * scale)  # middle fire

def draw_circle(x, y, radius):
    # Draw a hollow circle using points
    for i in range(360):
        angle = math.radians(i)
        dx = radius * math.cos(angle)
        dy = radius * math.sin(angle)
        points_draw_spaceship(x + dx, y + dy)

def draw_bullet(x, y):
    glPointSize(15)  # Increased bullet size
    points_draw_spaceship(x, y)

def add_obstacle():
    # Add a new obstacle at a random position above the screen
    x = random.randint(-200, 200)
    y = random.randint(50, 300)
    size = random.randint(7, 15)  # Random size from 7 to 15
    obstacles.append([x, y, size])  # Store size along with position

def draw_obstacles():
    # Draw all obstacles (asteroids)
    for obs_x, obs_y, size in obstacles:
        points_draw_asteroid(obs_x, obs_y, size)

def check_collision():
    global score
    for bullet in bullets[:]:
        bullet_x, bullet_y = bullet
        for obs in obstacles[:]:
            obs_x, obs_y, obs_size = obs
            # Check if the bullet hits the asteroid
            if abs(bullet_x - obs_x) < obs_size and abs(bullet_y - obs_y) < obs_size:
                # Collision detected, remove bullet and asteroid
                bullets.remove(bullet)
                obstacles.remove(obs)
                score += 1  # Increase score

def update_game_state():
    global spaceship_x, game_state, bullets, obstacles, asteroid_speed
    
    # Spaceship movement
    if game_state['left_pressed'] and spaceship_x > -200:
        spaceship_x -= spaceship_speed
    if game_state['right_pressed'] and spaceship_x < 200:
        spaceship_x += spaceship_speed
    
    # Update bullets
    for bullet in bullets[:]:
        bullet[1] += 10  # Move bullet upwards
        if bullet[1] > 300:
            bullets.remove(bullet)
    
    # Update obstacles (move asteroids slower using asteroid_speed)
    for obs in obstacles[:]:
        obs[1] -= asteroid_speed  # Move obstacles downward slower
        if obs[1] < -300:
            obstacles.remove(obs)

    # Add new obstacle every 100 frames (or adjust as needed)
    if random.randint(1, 100) == 1:
        add_obstacle()

    # Check for collisions between bullets and asteroids
    check_collision()

def keyboard(key, x, y):
    global spaceship_x, game_state, bullets
    
    # Convert key to byte for Python 3 compatibility
    if isinstance(key, bytes):
        key = key.decode('utf-8')
    
    if key == 'a':  # Move Left
        game_state['left_pressed'] = True
    elif key == 'd':  # Move Right
        game_state['right_pressed'] = True
    elif key == ' ':  # Shoot
        bullets.append([spaceship_x, -200])  # Shoot from spaceship position

def keyboard_up(key, x, y):
    global game_state
    
    # Convert key to byte for Python 3 compatibility
    if isinstance(key, bytes):
        key = key.decode('utf-8')
    
    if key == 'a':
        game_state['left_pressed'] = False
    elif key == 'd':
        game_state['right_pressed'] = False

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    
    # Update game logic
    update_game_state()
    
    # Draw spaceship slightly higher (changed from -250 to -230)
    draw_spaceship(spaceship_x, -230, scale=0.35)
    
    # Draw bullets
    for bullet_x, bullet_y in bullets:
        draw_bullet(bullet_x, bullet_y)

    # Draw obstacles (asteroids)
    draw_obstacles()
 

    glutSwapBuffers()

def idle():
    glutPostRedisplay()

def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(103, 1, 1, 1000.0)

# Initialize GLUT and create window
glutInit()
glutInitWindowSize(frame_w, frame_h)
glutInitWindowPosition(500, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
frame = glutCreateWindow(b"Spaceship Game")

# Register callbacks
init()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutKeyboardUpFunc(keyboard_up)
glutIdleFunc(idle)

# Start game loop
glutMainLoop()