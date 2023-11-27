from OpenGL.GLUT import *
from OpenGL.GL import *
from math import cos, sin, pi
def getX(centre, r, angle):
    return centre + r * cos(angle * pi / 180)


def getY(centre, r, angle):
    return centre + r * sin(angle * pi / 180)


def draw_circle(x, y, r):
    v = 100000  # чем больше число, тем выше точность прорисовки круга
    glBegin(GL_TRIANGLE_FAN)
    glVertex2d(x, y)
    for i in range(v):
        a = i / v * pi * 2
        glVertex2d(x + r * cos(a), y + r * sin(a))
    glEnd()


def draw_triangle(vertexes):
    glBegin(GL_TRIANGLES)
    for vertex in vertexes:
        glVertex2d(*vertex)
    glEnd()
def show():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Рисуем прямоугольник
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.3)
    glVertex2f(-1.0, -1)
    glVertex2f(1.0, -1)
    glVertex2f(1.0, 1)
    glVertex2f(-1.0, 1)
    glEnd()
    white = (1.0, 1.0, 1.0)
    glColor3f(*white)
    rb = 0.06
    r = 0.025
    rb1 = 0.1
    r1 = 0.04

    #Пятигранная звезда
    centre = (0.6, 0.25)
    for deg in range(55, 415, 72):
        tr_vertexes = [centre, (getX(centre[0], r, deg), getY(centre[1], r, deg)),
                       (getX(centre[0], rb, deg + 36), getY(centre[1], rb, deg + 36))]
        draw_triangle(tr_vertexes)
        tr_vertexes = [centre, (getX(centre[0], r, deg + 72), getY(centre[1], r, deg + 72)),
                       (getX(centre[0], rb, deg + 36), getY(centre[1], rb, deg + 36))]
        draw_triangle(tr_vertexes)
    #Звезда справа

    centre = (0.7, 0.5)
    for deg in range(55, 415, 360//7):
        tr_vertexes = [centre, (getX(centre[0], r1, deg), getY(centre[1], r1, deg)),
                       (getX(centre[0], rb1, deg + 36), getY(centre[1], rb1, deg + 36))]
        draw_triangle(tr_vertexes)
        tr_vertexes = [centre, (getX(centre[0], r1, deg + 72), getY(centre[1], r1, deg + 72)),
                       (getX(centre[0], rb1, deg + 36), getY(centre[1], rb1, deg + 36))]
        draw_triangle(tr_vertexes)

    #Левая звезда
    centre = (0.1, 0.35)
    for deg in range(55, 415, 360 // 7):
        tr_vertexes = [centre, (getX(centre[0], r1, deg), getY(centre[1], r1, deg)),
                       (getX(centre[0], rb1, deg + 36), getY(centre[1], rb1, deg + 36))]
        draw_triangle(tr_vertexes)
        tr_vertexes = [centre, (getX(centre[0], r1, deg + 72), getY(centre[1], r1, deg + 72)),
                       (getX(centre[0], rb1, deg + 36), getY(centre[1], rb1, deg + 36))]
        draw_triangle(tr_vertexes)

    #Звезда сверху
    centre = (0.4, 0.8)
    for deg in range(55, 415, 360 // 7):
        tr_vertexes = [centre, (getX(centre[0], r1, deg), getY(centre[1], r1, deg)),
                       (getX(centre[0], rb1, deg + 36), getY(centre[1], rb1, deg + 36))]
        draw_triangle(tr_vertexes)
        tr_vertexes = [centre, (getX(centre[0], r1, deg + 72), getY(centre[1], r1, deg + 72)),
                       (getX(centre[0], rb1, deg + 36), getY(centre[1], rb1, deg + 36))]
        draw_triangle(tr_vertexes)

    #Звезда снизу
    centre = (0.5, -0.6)
    for deg in range(55, 415, 360 // 7):
        tr_vertexes = [centre, (getX(centre[0], r1, deg), getY(centre[1], r1, deg)),
                       (getX(centre[0], rb1, deg + 36), getY(centre[1], rb1, deg + 36))]
        draw_triangle(tr_vertexes)
        tr_vertexes = [centre, (getX(centre[0], r1, deg + 72), getY(centre[1], r1, deg + 72)),
                       (getX(centre[0], rb1, deg + 36), getY(centre[1], rb1, deg + 36))]
        draw_triangle(tr_vertexes)

    #Большая звезда
    rb3 = 0.2
    r3 = 0.08
    centre = (-0.5, -0.7)
    for deg in range(55, 415, 360 // 7):
        tr_vertexes = [centre, (getX(centre[0], r3, deg), getY(centre[1], r3, deg)),
                       (getX(centre[0], rb3, deg + 36), getY(centre[1], rb3, deg + 36))]
        draw_triangle(tr_vertexes)
        tr_vertexes = [centre, (getX(centre[0], r3, deg + 72), getY(centre[1], r3, deg + 72)),
                       (getX(centre[0], rb3, deg + 36), getY(centre[1], rb3, deg + 36))]
        draw_triangle(tr_vertexes)
    glBegin(GL_QUADS)
    glVertex2f(-1.0, 1.0)
    glVertex2f(-0.85, 1.0)
    glVertex2f(-0.2, 0.3)
    glVertex2f(-0.35, 0.3)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(-1.0, 0.3)
    glVertex2f(-0.85, 0.3)
    glVertex2f(-0.2, 1.0)
    glVertex2f(-0.35, 1.0)
    glEnd()

    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_QUADS)
    glVertex2f(-0.65, 1.0)
    glVertex2f(-0.55, 1.0)
    glVertex2f(-0.55, 0.3)
    glVertex2f(-0.65, 0.3)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(-1.0, 0.75)
    glVertex2f(-0.2, 0.75)
    glVertex2f(-0.2, 0.55)
    glVertex2f(-1.0, 0.55)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(-0.93, 1.0)
    glVertex2f(-0.87, 1.0)
    glVertex2f(-0.27, 0.3)
    glVertex2f(-0.32, 0.3)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(-0.93, 0.3)
    glVertex2f(-0.87, 0.3)
    glVertex2f(-0.27, 1.0)
    glVertex2f(-0.32, 1.0)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_QUADS)
    glVertex2f(-0.7, 1.0)
    glVertex2f(-0.5, 1.0)
    glVertex2f(-0.5, 0.3)
    glVertex2f(-0.7, 0.3)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(-1.0, 0.8)
    glVertex2f(-0.2, 0.8)
    glVertex2f(-0.2, 0.5)
    glVertex2f(-1.0, 0.5)
    glEnd()
    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_QUADS)
    glVertex2f(-0.65, 1.0)
    glVertex2f(-0.55, 1.0)
    glVertex2f(-0.55, 0.3)
    glVertex2f(-0.65, 0.3)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(-1.0, 0.75)
    glVertex2f(-0.2, 0.75)
    glVertex2f(-0.2, 0.55)
    glVertex2f(-1.0, 0.55)
    glEnd()

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(50, 50)
    window = glutCreateWindow("Australia flag")
    glutDisplayFunc(show)
    glutIdleFunc(show)
    glutMainLoop()


if __name__ == '__main__':
    main()







