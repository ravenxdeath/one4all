import sys
import random
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_width = 500
window_height = 650
shooter_x = window_width // 2
shooter_y = 50
shooter_speed = 10
projectiles = []
falling_circles = []
falling_speed = 2
score = 0
lives = 5
game_over = False
paused = False

def set_color(r, g, b):
    glColor3f(r, g, b)

def draw_spaceship(x, y, scale=0.3):
    glBegin(GL_LINES)
    glVertex2f(x, y + 50 * scale)
    glVertex2f(x - 20 * scale, y + 20 * scale)
    glVertex2f(x, y + 50 * scale)
    glVertex2f(x + 20 * scale, y + 20 * scale)
    glVertex2f(x - 20 * scale, y + 20 * scale)
    glVertex2f(x + 20 * scale, y + 20 * scale)
    glVertex2f(x - 20 * scale, y + 20 * scale)
    glVertex2f(x - 30 * scale, y - 20 * scale)
    glVertex2f(x + 20 * scale, y + 20 * scale)
    glVertex2f(x + 30 * scale, y - 20 * scale)
    glVertex2f(x - 30 * scale, y - 20 * scale)
    glVertex2f(x + 30 * scale, y - 20 * scale)
    glVertex2f(x - 30 * scale, y - 20 * scale)
    glVertex2f(x - 50 * scale, y - 50 * scale)
    glVertex2f(x + 30 * scale, y - 20 * scale)
    glVertex2f(x + 50 * scale, y - 50 * scale)
    glVertex2f(x - 20 * scale, y - 20 * scale)
    glVertex2f(x - 10 * scale, y - 50 * scale)
    glVertex2f(x - 22 * scale, y - 22 * scale)
    glVertex2f(x - 12 * scale, y - 52 * scale)
    glVertex2f(x + 20 * scale, y - 20 * scale)
    glVertex2f(x + 10 * scale, y - 50 * scale)
    glVertex2f(x + 22 * scale, y - 22 * scale)
    glVertex2f(x + 12 * scale, y - 52 * scale)
    glVertex2f(x, y - 20 * scale)
    glVertex2f(x, y - 50 * scale)
    glEnd()

def draw_circle(x, y, radius):
    glBegin(GL_POINTS)
    x0 = 0
    y0 = radius
    d = 1 - radius
    while x0 <= y0:
        for dx, dy in [(x0, y0), (y0, x0), (-x0, y0), (-y0, x0),
                       (-x0, -y0), (-y0, -x0), (x0, -y0), (y0, -x0)]:
            glVertex2f(x + dx, y + dy)
        if d < 0:
            d += 2 * x0 + 3
        else:
            d += 2 * (x0 - y0) + 5
            y0 -= 1
        x0 += 1
    glEnd()

def draw_cross(x, y, size):
    glBegin(GL_LINES)
    glVertex2f(x - size, y - size)
    glVertex2f(x + size, y + size)
    glVertex2f(x - size, y + size)
    glVertex2f(x + size, y - size)
    glEnd()

def draw_play_pause(x, y, size, paused):
    glBegin(GL_TRIANGLES if not paused else GL_QUADS)
    if not paused:
        glVertex2f(x - size, y - size)
        glVertex2f(x + size, y)
        glVertex2f(x - size, y + size)
    else:
        glVertex2f(x - size, y - size)
        glVertex2f(x - size + size / 3, y - size)
        glVertex2f(x - size + size / 3, y + size)
        glVertex2f(x - size, y + size)
        glVertex2f(x + size - size / 3, y - size)
        glVertex2f(x + size, y - size)
        glVertex2f(x + size, y + size)
        glVertex2f(x + size - size / 3, y + size)
    glEnd()

def draw_controls():
    set_color(1, 1, 0)
    draw_circle(25, window_height - 25, 20)
    set_color(1, 0.5, 0)
    draw_play_pause(75, window_height - 25, 15, paused)
    set_color(1, 0, 0)
    draw_cross(window_width - 25, window_height - 25, 15)

def key_pressed(key, x, y):
    global shooter_x, paused, game_over
    if paused or game_over:
        return

    if key == b'a' and shooter_x - 15 > 0:
        shooter_x -= shooter_speed
    elif key == b'd' and shooter_x + 15 < window_width:
        shooter_x += shooter_speed
    elif key == b' ':
        projectiles.append([shooter_x, shooter_y + 20])

def mouse_click(button, state, x, y):
    global game_over, score, falling_circles, projectiles, lives, paused
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        gl_x = x
        gl_y = window_height - y

        if (gl_x - 25)**2 + (gl_y - (window_height - 25))**2 <= 400:
            score = 0
            falling_circles = []
            projectiles = []
            lives = 3
            game_over = False
            print("Starting Over")
        elif 60 <= gl_x <= 90 and window_height - 40 <= gl_y <= window_height - 10:
            paused = not paused
        elif window_width - 40 <= gl_x <= window_width - 10 and window_height - 40 <= gl_y <= window_height - 10:
            print(f"Goodbye. Final Score: {score}")
            sys.exit()

def check_collision(obj1, obj2):
    return math.sqrt((obj1[0] - obj2[0])**2 + (obj1[1] - obj2[1])**2) <= obj2[2]

def update(value):
    global falling_circles, projectiles, score, lives, game_over
    if paused or game_over:
        return

    for circle in falling_circles:
        circle[1] -= falling_speed

    missed_circles = [circle for circle in falling_circles if circle[1] <= 0]
    for circle in missed_circles:
        falling_circles.remove(circle)
        lives -= 1
        print(f"Missed a circle! Lives remaining: {lives}")

    for proj in projectiles:
        proj[1] += 5

    projectiles = [proj for proj in projectiles if proj[1] < window_height]

    for proj in projectiles[:]:
        for circle in falling_circles[:]:
            if check_collision(proj, circle):
                projectiles.remove(proj)
                falling_circles.remove(circle)
                score += 1
                print(f"Score: {score}")
                break

    for circle in falling_circles[:]:
        if check_collision([shooter_x, shooter_y], circle):
            falling_circles.remove(circle)
            lives -= 1
            print(f"Collision! Lives remaining: {lives}")

    if lives <= 0:
        game_over = True
        print(f"Game Over. Final Score: {score}")

    if random.random() < 0.02:
        falling_circles.append([random.randint(20, window_width - 20), window_height - 20, random.randint(10, 20)])

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def display():
    global game_over
    glClear(GL_COLOR_BUFFER_BIT)
    draw_controls()
    if not game_over:
        set_color(0, 1, 0)
        draw_spaceship(shooter_x, shooter_y)
    set_color(1, 0, 0)
    for proj in projectiles:
        draw_circle(proj[0], proj[1], 3)
    set_color(0, 0, 1)
    for circle in falling_circles:
        draw_circle(circle[0], circle[1], circle[2])
    glutSwapBuffers()

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(0, window_width, 0, window_height)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"Shoot The Circles!")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(key_pressed)
    glutMouseFunc(mouse_click)
    glutTimerFunc(16, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
