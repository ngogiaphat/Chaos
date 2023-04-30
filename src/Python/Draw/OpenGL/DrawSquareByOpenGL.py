from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def drawSquare():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.5, -0.5)
    glEnd()
    
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glLoadIdentity()
    glOrtho2d(-1.0, 1.0, -1.0, 1.0, -1, 1)
    drawSquare()
    glFlush()
    
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(250, 250)
glutInitWindowPosition(100, 100)
glutCreateWindow("OpenGL Window")
glutDisplayFunc(display)
glutMainLoop()