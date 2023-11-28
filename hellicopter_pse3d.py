from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

angleX = 0
angleY = 0

def display():
global angleX, angleY
glClearColor(253, 244, 230, 250)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glLoadIdentity()
glTranslatef(0.0, 0.0, -5.0)

glRotatef(angleX, 1.0, 0.0, 0.0)
glRotatef(angleY, 0.0, 1.0, 0.0)
glBegin(GL_QUADS) # кабина пилота
glColor3f(0.68, 0.93, 0.93)
glVertex3f(-0.55, -0.65, 0.5)
glVertex3f(-0.55, -0.65, -0.25)
glVertex3f(-0.85, -0.65, -0.25)
glVertex3f(-0.85, -0.65, 0.5)

glColor3f(0.68, 0.93, 0.93)

glVertex3f(-0.55, 0.35, 0.5)
glVertex3f(-0.55, 0.35, -0.25)
glVertex3f(-0.85, 0.35, -0.25)
glVertex3f(-0.85, 0.35, 0.5)

glColor3f(0.68, 0.93, 0.93)

glVertex3f(-0.85, -0.65, -0.25)
glVertex3f(-0.85, 0.35, -0.25)
glVertex3f(-0.55, 0.35, -0.25)
glVertex3f(-0.55, -0.65, -0.25)

glColor3f(0.68, 0.93, 0.93)

glVertex3f(-0.85, -0.65, 0.5)
glVertex3f(-0.85, 0.35, 0.5)
glVertex3f(-0.55, 0.35, 0.5)
glVertex3f(-0.55, -0.65, 0.5)

glColor3f(0.68, 0.93, 0.93)

glVertex3f(-0.85, -0.65, 0.5)
glVertex3f(-0.85, -0.65, -0.25)
glVertex3f(-0.85, 0.35, -0.25)
glVertex3f(-0.85, 0.35, 0.5)

glColor3f(0.68, 0.93, 0.93)

glVertex3f(-0.55, -0.65, 0.5)
glVertex3f(-0.55, -0.65, -0.25)
glVertex3f(-0.55, 0.35, -0.25)
glVertex3f(-0.55, 0.35, 0.5)

glEnd()

glBegin(GL_TRIANGLES) # треугольник
glColor3f(0.68, 0.93, 0.93)

glVertex3f(-0.85, 0.35, -0.25)
glVertex3f(-0.85, 0.35, 0.5)
glVertex3f(-1.25, 0.0, 0.15)

glColor3f(0.68, 0.93, 0.93)

glVertex3f(-0.85, -0.65, -0.25)
glVertex3f(-0.85, -0.65, 0.5)
glVertex3f(-1.25, 0.0, 0.15)

glColor3f(0.68, 0.93, 0.93)

glVertex3f(-0.85, -0.65, 0.5)
glVertex3f(-0.85, 0.35, 0.5)
glVertex3f(-1.25, 0.0, 0.15)

glColor3f(0.68, 0.93, 0.93)

glVertex3f(-0.65, -0.65, -0.25)
glVertex3f(-0.65, 0.35, -0.25)
glVertex3f(-1.25, 0.0, 0.15)

glEnd()

glBegin(GL_QUADS) # нижний пол
glColor3f(0.2, 0.4, 0.2)
glVertex3f(-0.55, -0.65, 0.5)
glVertex3f(-0.55, -0.65, -0.25)
glVertex3f(0.7, -0.65, -0.25)
glVertex3f(0.7, -0.65, 0.5)

glColor3f(0.2, 0.4, 0.2)
glVertex3f(-0.55, -0.6, 0.5)
glVertex3f(-0.55, -0.6, -0.25)
glVertex3f(0.7, -0.6, -0.25)
glVertex3f(0.7, -0.6, 0.5)

glColor3f(0.2, 0.4, 0.2)
glVertex3f(-0.55, -0.65, 0.5)
glVertex3f(-0.55, -0.6,0.5)
glVertex3f(0.7, -0.6, 0.5)
glVertex3f(0.7, -0.65, 0.5)

glColor3f(0.2, 0.4, 0.2)
glVertex3f(-0.55, -0.65, -0.25)
glVertex3f(-0.55, -0.6, -0.25)
glVertex3f(0.7, -0.6, -0.25)
glVertex3f(0.7, -0.65, -0.25)

glColor3f(0.2, 0.4, 0.2)
glVertex3f(0.7, -0.65, 0.5)
glVertex3f(0.7, -0.65, -0.25)
glVertex3f(0.7, -0.6, -0.25)
glVertex3f(0.7, -0.6, 0.5)

glEnd()

glBegin(GL_QUADS) # крыша
glColor3f(0.2, 0.4, 0.2)
glVertex3f(-0.55, 0.35, 0.5)
glVertex3f(-0.55, 0.35, -0.25)
glVertex3f(0.7, 0.35, -0.25)
glVertex3f(0.7, 0.35, 0.5)

glColor3f(0.2, 0.4, 0.2)
glVertex3f(-0.55, 0.3, 0.5)
glVertex3f(-0.55, 0.3, -0.25)
glVertex3f(0.7, 0.3, -0.25)
glVertex3f(0.7, 0.3, 0.5)

glColor3f(0.2, 0.4, 0.2)
glVertex3f(-0.55, 0.35, 0.5)
glVertex3f(-0.55, 0.3, 0.5)
glVertex3f(0.7, 0.3, 0.5)
glVertex3f(0.7, 0.35, 0.5)

glColor3f(0.2, 0.4, 0.2)
glVertex3f(-0.55, 0.35, -0.25)
glVertex3f(-0.55, 0.3, -0.25)
glVertex3f(0.7, 0.3, -0.25)
glVertex3f(0.7, 0.35, -0.25)

glColor3f(0.2, 0.4, 0.2)
glVertex3f(0.7, 0.35, 0.5)
glVertex3f(0.7, 0.35, -0.25)
glVertex3f(0.7, 0.3, -0.25)
glVertex3f(0.7, 0.3, 0.5)

glEnd()

glBegin(GL_QUADS) # задняя стенка
glColor3f(0.2, 0.4, 0.2)
glVertex3f(0.7, -0.65, 0.5)
glVertex3f(0.7, -0.65, -0.25)
glVertex3f(0.8, -0.65, -0.25)
glVertex3f(0.8, -0.65, 0.5)

glColor3f(0.2, 0.4, 0.2)
glVertex3f(0.7, 0.35, 0.5)
glVertex3f(0.7, 0.35, -0.25)
glVertex3f(0.8, 0.35, -0.25)
glVertex3f(0.8, 0.35, 0.5)

glColor3f(0.2, 0.4, 0.2)
glVertex3f(0.7, -0.65, 0.5)
glVertex3f(0.7, -0.65, -0.25)
glVertex3f(0.7, 0.35, -0.25)
glVertex3f(0.7, 0.35, 0.5)

glColor3f(0.2, 0.4, 0.2)
glVertex3f(0.8, -0.65, 0.5)
glVertex3f(0.8, -0.65, -0.25)
glVertex3f(0.8, 0.35, -0.25)
glVertex3f(0.8, 0.35, 0.5)

glColor3f(0.2, 0.4, 0.2)
glVertex3f(0.7, -0.65, 0.5)
glVertex3f(0.8, -0.65, 0.5)
glVertex3f(0.8, 0.35, 0.5)
glVertex3f(0.7, 0.35, 0.5)

glColor3f(0.2, 0.4, 0.2)
glVertex3f(0.7, -0.65, -0.25)
glVertex3f(0.8, -0.65, -0.25)
glVertex3f(0.8, 0.35, -0.25)
glVertex3f(0.7, 0.35, -0.25)

glEnd()

glBegin(GL_QUADS) # крепление
glColor3f(0, 0.0, 0.0)
glVertex3f(0.12, 0.35, 0.13)
glVertex3f(0.12, 0.35, 0.17)
glVertex3f(0.12, 0.45, 0.17)
glVertex3f(0.12, 0.45, 0.13)

glColor3f(0, 0.0, 0.0)
glVertex3f(0.16, 0.35, 0.13)
glVertex3f(0.16, 0.35, 0.17)
glVertex3f(0.16, 0.45, 0.17)
glVertex3f(0.16, 0.45, 0.13)

glColor3f(0, 0.0, 0.0)
glVertex3f(0.16, 0.35, 0.13)
glVertex3f(0.12, 0.35, 0.13)
glVertex3f(0.12, 0.45, 0.13)
glVertex3f(0.16, 0.45, 0.13)

glColor3f(0, 0.0, 0.0)
glVertex3f(0.16, 0.35, 0.17)
glVertex3f(0.12, 0.35, 0.17)
glVertex3f(0.12, 0.45, 0.17)
glVertex3f(0.16, 0.45, 0.17)

glColor3f(0, 0.0, 0.0)
glVertex3f(0.16, 0.45, 0.17)
glVertex3f(0.12, 0.45, 0.17)
glVertex3f(0.12, 0.45, 0.13)
glVertex3f(0.16, 0.45, 0.13)

glEnd()

glBegin(GL_QUADS) # винты
glColor3f(0, 0.0, 0.0)
glVertex3f(0.16, 0.45, -0.8)
glVertex3f(0.12, 0.45, -0.8)
glVertex3f(0.12, 0.45, 0.9)
glVertex3f(0.16, 0.45, 0.9)

glColor3f(0, 0.0, 0.0)
glVertex3f(0.16, 0.49, -0.8)
glVertex3f(0.12, 0.49, -0.8)
glVertex3f(0.12, 0.49, 0.9)
glVertex3f(0.16, 0.49, 0.9)

glColor3f(0, 0.0, 0.0)
glVertex3f(0.16, 0.45, -0.8)
glVertex3f(0.16, 0.45, 0.9)
glVertex3f(0.16, 0.49, 0.9)
glVertex3f(0.16, 0.49, -0.8)

glColor3f(0, 0.0, 0.0)
glVertex3f(0.12, 0.45, -0.8)
glVertex3f(0.12, 0.45, 0.9)
glVertex3f(0.12, 0.49, 0.9)
glVertex3f(0.12, 0.49, -0.8)

glColor3f(0, 0.0, 0.0)
glVertex3f(0.12, 0.45, 0.9)
glVertex3f(0.16, 0.45, 0.9)
glVertex3f(0.16, 0.49, 0.9)
glVertex3f(0.12, 0.49, 0.9)

glColor3f(0, 0.0, 0.0)
glVertex3f(0.12, 0.45, -0.8)
glVertex3f(0.16, 0.45, -0.8)
glVertex3f(0.16, 0.49, -0.8)
glVertex3f(0.12, 0.49, -0.8)

glEnd()

glBegin(GL_QUADS) # винты

glColor3f(0, 0.0, 0.0)
glVertex3f(-0.75, 0.45, 0.17)
glVertex3f(-0.75, 0.45, 0.13)
glVertex3f(0.8, 0.45, 0.13)
glVertex3f(0.8, 0.45, 0.17)

glColor3f(0, 0.0, 0.0)
glVertex3f(-0.75, 0.49, 0.17)
glVertex3f(-0.75, 0.49, 0.13)
glVertex3f(0.8, 0.49, 0.13)
glVertex3f(0.8, 0.49, 0.17)

glColor3f(0, 0.0, 0.0)
glVertex3f(-0.75, 0.45, 0.17)
glVertex3f(0.8, 0.45, 0.17)
glVertex3f(0.8, 0.49, 0.17)
glVertex3f(-0.75, 0.49, 0.17)

glColor3f(0, 0.0, 0.0)
glVertex3f(-0.75, 0.45, 0.13)
glVertex3f(0.8, 0.45, 0.13)
glVertex3f(0.8, 0.49, 0.13)
glVertex3f(-0.75, 0.49, 0.13)

glColor3f(0, 0.0, 0.0)
glVertex3f(-0.75, 0.45, 0.13)
glVertex3f(-0.75, 0.45, 0.17)
glVertex3f(-0.75, 0.49, 0.17)
glVertex3f(-0.75, 0.49, 0.13)

glColor3f(0, 0.0, 0.0)
glVertex3f(0.8, 0.45, 0.13)
glVertex3f(0.8, 0.45, 0.17)
glVertex3f(0.8, 0.49, 0.17)
glVertex3f(0.8, 0.49, 0.13)

glEnd()

glBegin(GL_QUADS) # задняя стенка
glColor3f(0, 0.0, 0.0)
glVertex3f(1.5, 0.15, 0.13)
glVertex3f(1.5, 0.18, 0.13)
glVertex3f(1.5, 0.18, 0.17)
glVertex3f(1.5, 0.15, 0.17)

glColor3f(0, 0.0, 0.0)
glVertex3f(1.5, 0.15, 0.13)
glVertex3f(1.5, 0.18, 0.13)
glVertex3f(0.8, 0.18, 0.13)
glVertex3f(0.8, 0.15, 0.13)

glColor3f(0, 0.0, 0.0)
glVertex3f(1.5, 0.15, 0.17)
glVertex3f(1.5, 0.18, 0.17)
glVertex3f(0.8, 0.18, 0.17)
glVertex3f(0.8, 0.15, 0.17)

glColor3f(0, 0.0, 0.0)
glVertex3f(1.5, 0.18, 0.13)
glVertex3f(1.5, 0.18, 0.17)
glVertex3f(0.8, 0.18, 0.17)
glVertex3f(0.8, 0.18, 0.13)

glColor3f(0, 0.0, 0.0)
glVertex3f(1.5, 0.15, 0.13)
glVertex3f(1.5, 0.15, 0.17)
glVertex3f(0.8, 0.15, 0.17)
glVertex3f(0.8, 0.15, 0.13)

glEnd()

glBegin(GL_QUADS) # задняя лопасть
glColor3f(0, 0.0, 0.0)
glVertex3f(1.5, 0.05, 0.17)
glVertex3f(1.5, 0.25, 0.17)
glVertex3f(1.45, 0.25, 0.17)
glVertex3f(1.45, 0.05, 0.17)

glColor3f(0, 0.0, 0.0)
glVertex3f(1.5, 0.05, 0.2)
glVertex3f(1.5, 0.25, 0.2)
glVertex3f(1.45, 0.25, 0.2)
glVertex3f(1.45, 0.05, 0.2)

glColor3f(0, 0.0, 0.0)
glVertex3f(1.5, 0.05, 0.17)
glVertex3f(1.5, 0.25, 0.17)
glVertex3f(1.5, 0.25, 0.2)
glVertex3f(1.5, 0.05, 0.2)

glColor3f(0, 0.0, 0.0)
glVertex3f(1.45, 0.05, 0.17)
glVertex3f(1.45,
0.25, 0.17)
glVertex3f(1.45, 0.25, 0.2)
glVertex3f(1.45, 0.05, 0.2)

glColor3f(0, 0.0, 0.0)
glVertex3f(1.45, 0.25, 0.17)
glVertex3f(1.45, 0.25, 0.2)
glVertex3f(1.5, 0.25, 0.2)
glVertex3f(1.5, 0.25, 0.17)

glColor3f(0, 0.0, 0.0)
glVertex3f(1.45, 0.05, 0.17)
glVertex3f(1.45, 0.05, 0.2)
glVertex3f(1.5, 0.05, 0.2)
glVertex3f(1.5, 0.05, 0.17)

glEnd()

glBegin(GL_QUADS) # место под окно спереди
glColor3f(0, 0.0, 0.0)
glVertex3f(-0.55, -0.6, 0.5)
glVertex3f(-0.55, 0.0, 0.5)
glVertex3f(0.7, 0.0, 0.5)
glVertex3f(0.7, -0.6, 0.5)

glEnd()

glBegin(GL_QUADS) # место под окно сзади
glColor3f(0, 0.0, 0.0)
glVertex3f(-0.55, -0.6, -0.25)
glVertex3f(-0.55, 0.0, -0.25)
glVertex3f(0.7, 0.0, -0.25)
glVertex3f(0.7, -0.6, -0.25)

glEnd()

glBegin(GL_QUADS) # окно
glColor3f(0, 0.0, 1.0)
glVertex3f(-0.55, 0.0, -0.25)
glVertex3f(-0.55, 0.0, -0.25)
glVertex3f(0.7, 0.0, -0.25)
glVertex3f(0.7, -0.6, -0.25)

glEnd()

glutSwapBuffers()

def reshape(w, h):
glViewport(0, 0, w, h)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45.0, w / h, 1.0, 100.0)
glMatrixMode(GL_MODELVIEW)

def idle():
global angleX, angleY
angleX += 0.2
angleY += 0.2
glutPostRedisplay()

def main():
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow("Hellicopter")
glEnable(GL_DEPTH_TEST)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutIdleFunc(idle)
glutMainLoop()

main()
