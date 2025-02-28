from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

frame_w = 500
frame_h = 650

# Enhanced game state
game_state = {
    'left_pressed': False,
    'right_pressed': False,
    'is_paused': False,
    'game_over': False,
    'missed_circles': 0,
    'missed_shots': 0
}

# Spaceship and game parameters
spaceship_x = 0
spaceship_speed = 5
bullets = []
obstacles = []  # List to store obstacles (falling circles)
asteroid_speed = 0.51  # Initial falling circle speed
score = 0
lives = 3

# Button state tracking
buttons = {
    'restart': {'x': -200, 'y': 300, 'width': 50, 'height': 50},
    'play_pause': {'x': 0, 'y': 300, 'width': 50, 'height': 50},
    'exit': {'x': 200, 'y': 300, 'width': 50, 'height': 50}
}

def points_draw_spaceship(x, y):
    glPointSize(2.7)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def points_draw_asteroid(x, y, size):
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

def draw_buttons():
    # Restart Button (Triangle) - Green
    glColor3f(0, 1, 0)  # Green color for restart
    glBegin(GL_POLYGON)
    glVertex2f(-220, 310)
    glVertex2f(-180, 350)
    glVertex2f(-200, 290)
    glVertex2f(-240, 290)
    glEnd()

    # Play/Pause Button (Amber) - Yellow color
    glColor3f(1, 0.75, 0)  # Yellow color for play/pause
    if game_state['is_paused']:
        # Draw Play Triangle (for paused state)
        glBegin(GL_POLYGON)
        glVertex2f(0, 280)
        glVertex2f(0, 320)
        glVertex2f(30, 300)
        glEnd()
    else:
        # Draw Pause Bars (for playing state)
        glBegin(GL_POLYGON)
        glVertex2f(-15, 280)
        glVertex2f(-15, 320)
        glVertex2f(15, 320)
        glVertex2f(15, 280)
        glEnd()

    # Exit Button (Cross) - Red
    glColor3f(1, 0, 0)  # Red color for exit
    glBegin(GL_LINES)
    glVertex2f(180, 280)
    glVertex2f(220, 320)
    glVertex2f(180, 320)
    glVertex2f(220, 280)
    glEnd()

def add_obstacle():
    x = random.randint(-200, 200)
    y = random.randint(50, 300)
    size = random.randint(7, 15)
    obstacles.append([x, y, size])

def draw_obstacles():
    # Draw all obstacles (falling circles)
    for obs_x, obs_y, size in obstacles:
        points_draw_asteroid(obs_x, obs_y, size)

def check_collision():
    global score, lives, game_state
    
    # Check bullet-circle collisions
    for bullet in bullets[:]:
        bullet_x, bullet_y = bullet
        for obs in obstacles[:]:
            obs_x, obs_y, obs_size = obs
            if abs(bullet_x - obs_x) < obs_size and abs(bullet_y - obs_y) < obs_size:
                bullets.remove(bullet)
                obstacles.remove(obs)
                score += 1
                game_state['missed_shots'] = 0  # Reset missed shots on successful hit
                break
        else:
            # If no collision occurred
            game_state['missed_shots'] += 1
    
    # Check missed shots game over condition
    if game_state['missed_shots'] >= 3:
        game_over("Too many missed shots!")

    # Check spaceship-circle collision
    for obs in obstacles[:]:
        obs_x, obs_y, obs_size = obs
        if abs(spaceship_x - obs_x) < obs_size and abs(-230 - obs_y) < obs_size:
            game_over("Asteroid hit spaceship!")
    
    # Check missed circles game over condition
    for obs in obstacles[:]:
        if obs[1] < -300:
            obstacles.remove(obs)
            game_state['missed_circles'] += 1
            
            if game_state['missed_circles'] >= 3:
                game_over("Too many missed circles!")

def game_over(reason):
    if not game_state['game_over']:
        game_state['game_over'] = True
        print(f"Game Over! {reason}")
        print(f"Final Score: {score}")

def reset_game():
    global spaceship_x, bullets, obstacles, lives, score, game_state
    spaceship_x = 0
    bullets.clear()
    obstacles.clear()
    lives = 3
    score = 0
    game_state['missed_circles'] = 0
    game_state['missed_shots'] = 0
    game_state['game_over'] = False
    game_state['is_paused'] = False
    print("Starting Over")

def keyboard(key, x, y):
    global game_state, bullets
    
    # Convert key to byte for Python 3 compatibility
    if isinstance(key, bytes):
        key = key.decode('utf-8')
    
    if game_state['game_over'] or game_state['is_paused']:
        return
    
    if key == 'a':
        game_state['left_pressed'] = True
    elif key == 'd':
        game_state['right_pressed'] = True
    elif key == ' ':
        bullets.append([spaceship_x, -200])

def keyboard_up(key, x, y):
    global game_state
    
    if isinstance(key, bytes):
        key = key.decode('utf-8')
    
    if key == 'a':
        game_state['left_pressed'] = False
    elif key == 'd':
        game_state['right_pressed'] = False

def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        # Convert GLUT window coordinates to OpenGL coordinates
        mouse_x = (x - frame_w/2) * (400 / frame_w)
        mouse_y = (frame_h/2 - y) * (650 / frame_h)
        
        # Check restart button
        if (-220 < mouse_x < -180 and 280 < mouse_y < 320):
            reset_game()
        
        # Check play/pause button
        elif (-25 < mouse_x < 25 and 280 < mouse_y < 320):
            game_state['is_paused'] = not game_state['is_paused']
        
        # Check exit button
        elif (180 < mouse_x < 220 and 280 < mouse_y < 320):
            print("Goodbye")
            print(f"Final Score: {score}")
            glutDestroyWindow(frame)
            exit()

def update_game_state():
    global spaceship_x, game_state, bullets, obstacles, asteroid_speed
    
    if game_state['game_over'] or game_state['is_paused']:
        return
    
    # Spaceship movement
    if game_state['left_pressed'] and spaceship_x > -200:
        spaceship_x -= spaceship_speed
    if game_state['right_pressed'] and spaceship_x < 200:
        spaceship_x += spaceship_speed
    
    # Update bullets
    for bullet in bullets[:]:
        bullet[1] += 10
        if bullet[1] > 300:
            bullets.remove(bullet)
    
    # Update obstacles (move falling circles)
    for obs in obstacles[:]:
        obs[1] -= asteroid_speed
        if obs[1] < -300:
            obstacles.remove(obs)
            game_state['missed_circles'] += 1

    # Add new obstacle periodically
    if random.randint(1, 100) == 1:
        add_obstacle()

    # Check for collisions
    check_collision()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200,0, 0, 0, 0, 1, 0)
    
    # Update game logic
    update_game_state()
    
    # Draw spaceship
    if not game_state['game_over']:
        draw_spaceship(spaceship_x, -230, scale=0.35)
    
    # Draw bullets
    for bullet_x, bullet_y in bullets:
        draw_bullet(bullet_x, bullet_y)

    # Draw obstacles (falling circles)
    draw_obstacles()

    # Draw buttons
    draw_buttons()

    # Print game status
    print(f"Score: {score} | Missed Circles: {game_state['missed_circles']}")
    
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

# Register callbacksa
init()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutKeyboardUpFunc(keyboard_up)
glutMouseFunc(mouse_click)
glutIdleFunc(idle)

# Start game loop
glutMainLoop()