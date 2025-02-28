from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

 
window_width, window_height = 800, 600
spaceship_x, spaceship_y = 0.0, -0.8
bullet_speed = 0.05
bullets = []
 
def draw_spaceship():
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(spaceship_x, spaceship_y)
    glVertex2f(spaceship_x - 0.05, spaceship_y - 0.1)
    glVertex2f(spaceship_x + 0.05, spaceship_y - 0.1)
    glEnd()

 
def draw_bullets():
    glColor3f(1.0, 0.0, 0.0)
    for bullet in bullets:
        glBegin(GL_QUADS)
        glVertex2f(bullet[0] - 0.01, bullet[1])
        glVertex2f(bullet[0] + 0.01, bullet[1])
        glVertex2f(bullet[0] + 0.01, bullet[1] + 0.05)
        glVertex2f(bullet[0] - 0.01, bullet[1] + 0.05)
        glEnd()
 
def update_bullets():
    global bullets
    for i in range(len(bullets)):
        bullets[i][1] += bullet_speed
    bullets = [bullet for bullet in bullets if bullet[1] <= 1.0]
 
def render_scene():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_spaceship()
    draw_bullets()
    glutSwapBuffers()
 
def keyboard(key, x, y):
    global spaceship_x, bullets
    if key == b'a':  # Move left
        spaceship_x -= 0.05
    elif key == b'd':  # Move right
        spaceship_x += 0.05
    elif key == b' ':  # Shoot
        bullets.append([spaceship_x, spaceship_y + 0.1])
 
def update(value):
    update_bullets()
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # Approx 60 FPS

 
def initialize():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
 
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"Spaceship Shooter")
    initialize()
    glutDisplayFunc(render_scene)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(16, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
