
We use the following OpenGL modules:
- `OpenGL.GL` for OpenGL commands
- `OpenGL.GLUT` for window creation and handling user inputs
- `OpenGL.GLU` for setting up the camera view

### 2. **Initializing a Window with OpenGL and GLUT**

The `GLUT` library helps create a window for OpenGL and handles things like mouse and keyboard inputs. Here's how to set up a basic window:

```python
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen with a color
    glFlush()  # Force the execution of OpenGL commands

def main():
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Set display mode (single buffer and RGB color)
    glutInitWindowSize(500, 500)  # Set window size
    glutInitWindowPosition(100, 100)  # Set window position on screen
    glutCreateWindow(b"OpenGL Basics")  # Create window with title
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color (black)
    glutDisplayFunc(display)  # Register display callback
    gluOrtho2D(-50, 50, -50, 50)  # Set 2D orthographic projection
    glutMainLoop()  # Enter the main loop to process events
```

This code initializes a simple window with a black background and a coordinate system from `(-50, -50)` to `(50, 50)`.

### 3. **Drawing Points, Lines, and Shapes**

#### Drawing a Point

To draw a point, we use the `GL_POINTS` primitive, which represents individual points in OpenGL.

```python
def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear screen
    glPointSize(5.0)  # Set point size
    glColor3f(1.0, 0.0, 0.0)  # Set point color to red
    glBegin(GL_POINTS)  # Start drawing points
    glVertex2f(0.0, 0.0)  # Draw a point at the origin
    glEnd()  # End drawing
    glFlush()  # Force execution of OpenGL commands
```

#### Drawing a Line

Lines are drawn using the `GL_LINES` primitive. We can set up two vertices to define a line.

```python
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)  # Set line color to green
    glBegin(GL_LINES)
    glVertex2f(-25.0, -25.0)  # Start point of line
    glVertex2f(25.0, 25.0)    # End point of line
    glEnd()
    glFlush()
```

#### Drawing a Rectangle

A rectangle can be drawn by using four vertices. Here, we use the `GL_QUADS` primitive.

```python
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)  # Set color to blue
    glBegin(GL_QUADS)
    glVertex2f(-20.0, -10.0)  # Bottom left
    glVertex2f(20.0, -10.0)   # Bottom right
    glVertex2f(20.0, 10.0)    # Top right
    glVertex2f(-20.0, 10.0)   # Top left
    glEnd()
    glFlush()
```

### 4. **Animating Points**

Now, let’s create a simple animation by moving a point across the screen. We need a timer to update the point’s position continuously.

```python
point_x = -50.0  # Starting x position

def display():
    global point_x
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(10.0)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POINTS)
    glVertex2f(point_x, 0.0)  # Move point horizontally
    glEnd()
    glFlush()

def update(value):
    global point_x
    point_x += 1.0  # Move the point to the right
    if point_x > 50:  # Reset position if it goes out of bounds
        point_x = -50
    glutPostRedisplay()  # Request display update
    glutTimerFunc(100, update, 0)  # Call update again after 100 ms

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Animating a Point")
    gluOrtho2D(-50, 50, -50, 50)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)  # Start the timer for animation
    glutMainLoop()
```

### 5. **Handling Keyboard Input**

Let's add keyboard controls to change the color of a point when specific keys are pressed. Here, we check if the 'r', 'g', or 'b' keys are pressed to change the color to red, green, or blue.

```python
color = (1.0, 0.0, 0.0)  # Start with red

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(10.0)
    glColor3f(*color)  # Use the current color
    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.0)  # Draw point at origin
    glEnd()
    glFlush()

def keyboard(key, x, y):
    global color
    if key == b'r':
        color = (1.0, 0.0, 0.0)  # Red
    elif key == b'g':
        color = (0.0, 1.0, 0.0)  # Green
    elif key == b'b':
        color = (0.0, 0.0, 1.0)  # Blue
    glutPostRedisplay()  # Request a display update

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Keyboard Input Example")
    gluOrtho2D(-50, 50, -50, 50)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)  # Register keyboard function
    glutMainLoop()
```

### 6. **Adding Mouse Input**

Here, we’ll make the point move to wherever the user clicks. When you click in the window, the point jumps to the cursor's location.

```python
point_x, point_y = 0.0, 0.0

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(10.0)
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_POINTS)
    glVertex2f(point_x, point_y)  # Draw point at the mouse click position
    glEnd()
    glFlush()

def mouse(button, state, x, y):
    global point_x, point_y
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        window_width = glutGet(GLUT_WINDOW_WIDTH)
        window_height = glutGet(GLUT_WINDOW_HEIGHT)
        point_x = (x - window_width / 2) / (window_width / 50)  # Convert x
        point_y = -(y - window_height / 2) / (window_height / 50)  # Convert y
        glutPostRedisplay()  # Request display update

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Mouse Input Example")
    gluOrtho2D(-50, 50, -50, 50)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutMouseFunc(mouse)  # Register mouse function
    glutMainLoop()
```

---

This covers the basics of working with points, lines, shapes, animations, and input handling in OpenGL. You can build on this foundation to create more complex behaviors, such as