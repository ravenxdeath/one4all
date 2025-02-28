from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

# Window size
frame_w = 500
frame_h = 650

# Spaceship position and speed
spaceship_x = 0
spaceship_speed = 5

# Lists to store bullets and obstacles (asteroids)
bullets = []
obstacles = []

# Asteroid speed, score, lives, and game state
asteroid_speed = .51
score = 0
lives = 3
game_state = {
    'left_pressed': False,
    'right_pressed': False
}

# Function to draw spaceship point
def points_draw_spaceship(x, y):
    glPointSize(2.7)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

# Function to draw asteroid point
def points_draw_asteroid(x, y, size):
    draw_circle(x, y, size)

# Function to draw a line using the Midpoint Algorithm
def draw_line(x1, y1, x2, y2):
    zone = determine_zone(x1, y1, x2, y2)
    x1, y1, x2, y2 = adjust_for_zone(zone, x1, y1, x2, y2)
    points = my_midpoint_algo(x1, y1, x2, y2)
    apply_zone_transform(zone, points)

# Midpoint algorithm for line drawing
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

# Determine which zone the line is in
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

# Adjust coordinates based on line's zone
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

# Apply transformations based on zone
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

# Draw the spaceship
def draw_spaceship(x, y, scale=0.3):
    draw_line(x, y + 50 * scale, x - 20 * scale, y + 20 * scale)
    draw_line(x, y + 50 * scale, x + 20 * scale, y + 20 * scale)
    draw_line(x - 20 * scale, y + 20 * scale, x + 20 * scale, y + 20 * scale)
    
    draw_line(x - 20 * scale, y + 20 * scale, x - 30 * scale, y - 20 * scale)
    draw_line(x + 20 * scale, y + 20 * scale, x + 30 * scale, y - 20 * scale)
    draw_line(x - 30 * scale, y - 20 * scale, x + 30 * scale, y - 20 * scale)

    draw_line(x - 30 * scale, y - 20 * scale, x - 50 * scale, y - 50 * scale)
    draw_line(x + 30 * scale, y - 20 * scale, x + 50 * scale, y - 50 * scale)

    draw_circle(x, y, 10 * scale)
    
    draw_line(x - 20 * scale, y - 20 * scale, x - 10 * scale, y - 50 * scale)
    draw_line(x - 22 * scale, y - 22 * scale, x - 12 * scale, y - 52 * scale)
    
    draw_line(x + 20 * scale, y - 20 * scale, x + 10 * scale, y - 50 * scale)
    draw_line(x + 22 * scale, y - 22 * scale, x + 12 * scale, y - 52 * scale)
    
    draw_line(x, y - 20 * scale, x, y - 50 * scale)
    draw_line(x + 2 * scale, y - 22 * scale, x, y - 52 * scale)

# Draw a circle at the given position and radius
def draw_circle(x, y, radius):
    for i in range(360):
        angle = math.radians(i)
        dx = radius * math.cos(angle)
        dy = radius * math.sin(angle)
        points_draw_spaceship(x + dx, y + dy)

# Draw a bullet at the given position
def draw_bullet(x, y):
    glPointSize(15)
    points_draw_spaceship(x, y)

# Add a new obstacle (asteroid)
def add_obstacle():
    x = random.randint(-200, 200)
    y = random.randint(50, 300)
    size = random.randint(7, 15)
    obstacles.append([x, y, size])

# Draw all obstacles (asteroids)
def draw_obstacles():
    for obs_x, obs_y, size in obstacles:
        points_draw_asteroid(obs_x, obs_y, size)

# Check for collisions between bullets, obstacles, and spaceship
def check_collision():
    global score, lives
    for bullet in bullets[:]:
        bullet_x, bullet_y = bullet
        for obs in obstacles[:]:
            obs_x, obs_y, obs_size = obs
            if abs(bullet_x - obs_x) < obs_size and abs(bullet_y - obs_y) < obs_size:
                bullets.remove(bullet)
                obstacles.remove(obs)
                score += 1

    for obs in obstacles[:]:
        obs_x, obs_y, obs_size = obs
        if abs(spaceship_x - obs_x) < obs_size and abs(-230 - obs_y) < obs_size:
            lives -= 1
            obstacles.remove(obs)
            if lives == 0:
                game_over()

# Update game state: spaceship movement, bullet and obstacle positions
def update_game_state():
    global spaceship_x, game_state, bullets, obstacles, asteroid_speed
    
    if game_state['left_pressed'] and spaceship_x > -200:
        spaceship_x -= spaceship_speed
    if game_state['right_pressed'] and spaceship_x < 200:
        spaceship_x += spaceship_speed
    
    for bullet in bullets[:]:
        bullet[1] += 10
        if bullet[1] > 300:
            bullets.remove(bullet)
    
    for obs in obstacles[:]:
        obs[1] -= asteroid_speed
        if obs[1] < -300:
            obstacles.remove(obs)

    if random.randint(1, 100) == 1:
        add_obstacle()

    check_collision()

# Display the game screen (draw spaceship, bullets, obstacles, score, and lives)
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Draw spaceship, bullets, and obstacles
    draw_spaceship(spaceship_x, -230)
    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])
    draw_obstacles()
    
    # Draw score and lives
    glColor3f(1, 1, 1)
    render_text(-230, 250, "Score: " + str(score))
    render_text(-230, 230, "Lives: " + str(lives))
    
    # Update the screen
    glutSwapBuffers()

# Function to render text on the screen
def render_text(x, y, text):
    glRasterPos2f(x, y)
    for c in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c))

# Reset the game state
def reset_game():
    global spaceship_x, bullets, obstacles, score, lives
    spaceship_x = 0
    bullets = []
    obstacles = []
    score = 0
    lives = 3

# Handle keyboard input (move spaceship or shoot bullet)
def keyboard(key, x, y):
    global game_state
    if key == b'a':
        game_state['left_pressed'] = True
    elif key == b'd':
        game_state['right_pressed'] = True
    elif key == b' ':
        bullets.append([spaceship_x, -230])
        
# Handle key release
def keyboard_up(key, x, y):
    global game_state
    if key == b'a':
        game_state['left_pressed'] = False
    elif key == b'd':
        game_state['right_pressed'] = False

# Main game loop (called by GLUT)
def idle():
    update_game_state()
    glutPostRedisplay()

# Game over function
def game_over():
    print("Game Over! Final Score:", score)
    reset_game()

# Initialize OpenGL settings
def init():
    glClearColor(0, 0, 0, 1)  # Black background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250, 250, -300, 300, -1, 1)  # 2D orthographic projection
    glMatrixMode(GL_MODELVIEW)

# Start the game
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(frame_w, frame_h)
    glutCreateWindow(b"Spaceship Game")
    init()
    
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    glutKeyboardFunc(keyboard)
    glutKeyboardUpFunc(keyboard_up)
    
    glutMainLoop()

if __name__ == "__main__":
    main()
