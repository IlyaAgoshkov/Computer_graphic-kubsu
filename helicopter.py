from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from math import pi, sin, cos
from australia_flag import draw_circle
from australia_flag import draw_triangle
from australia_flag import getX
from australia_flag import getY

def rotate(key, x, y):
    if key == GLUT_KEY_RIGHT:
        glRotate(-5, 0, 1, 0)
    elif key == GLUT_KEY_LEFT:
        glRotate(5, 0, 1, 0)
    elif key == GLUT_KEY_UP:
        glRotate(5, 1, 0, 0)
    elif key == GLUT_KEY_DOWN:
        glRotate(-5, 1, 0, 0)
def show():
    white = (1.0, 1.0, 1.0)
    green = (0.0, 0.25, 0.1)
    red = (1.0, 0.0, 0.0)
    blue = (0.0, 0.0, 1.0)
    glClearColor(*blue, 1.0)
    glClear(GL_COLOR_BUFFER_BIT or GL_DEPTH_BUFFER_BIT)
    glColor3f(*green)
    move_list = [0, 0, 0]

    glMatrixMode(GL_PROJECTION)
    '''Рисуем корпус'''

    draw_circle(0.0, 0.0, 0.5)
    glColor3f(0.0, 0.0, 0.0)  # Установить цвет рисования в черный
    draw_circle(0.3, -0.5, 0.1)
    draw_circle(-0.3, -0.5, 0.1)
    glLineWidth(10.0)  # Установить толщину линии

    # Центральная линия
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.6)  # Координата начала линии
    glVertex2f(0.0, 0.5)  # Координата конца линии
    glEnd()
    # Правая лопасть
    glBegin(GL_LINES)
    glVertex2f(0.8, 0.5)  # Координата начала линии
    glVertex2f(0.0, 0.6)  # Координата конца линии
    glEnd()
    # Левая лопасть
    glBegin(GL_LINES)
    glVertex2f(-0.8, 0.5)  # Координата начала линии
    glVertex2f(0.0, 0.6)  # Координата конца линии
    glEnd()
    '''ХВОСТ'''
    glBegin(GL_LINES)
    glVertex2f(0.5, 0.0)  # Координата начала линии
    glVertex2f(0.7, 0.0)  # Координата конца линии
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0.7, 0.0)  # Координата начала линии
    glVertex2f(0.9, 0.8)  # Координата конца линии
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0.9, 0.8)  # Координата начала линии
    glVertex2f(0.78, 0.8)  # Координата конца линии
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0.9, 0.8)  # Координата начала линии
    glVertex2f(1.0, 0.7)  # Координата конца линии
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0.9, 0.8)  # Координата начала линии
    glVertex2f(1.0, 0.7)  # Координата конца линии
    glEnd()
    '''Фара вертолёта'''
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.27, 0.0)
    glVertex2f(-0.4, -0.1)
    glVertex2f(-0.3, -0.1)
    glVertex2f(-0.4, 0.1)
    glVertex2f(-0.3, 0.1)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.27, 0.0)
    glVertex2f(-0.2, -0.1)
    glVertex2f(-0.3, -0.1)
    glVertex2f(-0.2, 0.1)
    glVertex2f(-0.3, 0.1)
    glEnd()

    '''Дверь вертолёта'''
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(-0.15, -0.3)
    glVertex2f(0.0, -0.3)
    glVertex2f(0.0, 0.3)
    glVertex2f(-0.15, 0.3)
    glEnd()
    '''Окно вертолёта'''
    glBegin(GL_QUADS)
    glColor3f(0.25, 0.66, 1.0)
    glVertex2f(0.2, -0.1)
    glVertex2f(0.48, -0.1)
    glVertex2f(0.48, 0.1)
    glVertex2f(0.2, 0.1)
    glEnd()

    rb = 0.06
    r = 0.025
    rb1 = 0.1
    r1 = 0.04



    # Пятигранная звезда
    centre = (0.6, 0.25)
    for deg in range(55, 415, 72):
        tr_vertexes = [centre, (getX(centre[0], r, deg), getY(centre[1], r, deg)),
                       (getX(centre[0], rb, deg + 36), getY(centre[1], rb, deg + 36))]
        draw_triangle(tr_vertexes)
        tr_vertexes = [centre, (getX(centre[0], r, deg + 72), getY(centre[1], r, deg + 72)),
                       (getX(centre[0], rb, deg + 36), getY(centre[1], rb, deg + 36))]
        draw_triangle(tr_vertexes)


    # Звезда сверху
    centre = (0.4, 0.8)
    for deg in range(55, 415, 360 // 7):
        tr_vertexes = [centre, (getX(centre[0], r1, deg), getY(centre[1], r1, deg)),
                       (getX(centre[0], rb1, deg + 36), getY(centre[1], rb1, deg + 36))]
        draw_triangle(tr_vertexes)
        tr_vertexes = [centre, (getX(centre[0], r1, deg + 72), getY(centre[1], r1, deg + 72)),
                       (getX(centre[0], rb1, deg + 36), getY(centre[1], rb1, deg + 36))]
        draw_triangle(tr_vertexes)

    # Звезда снизу
    centre = (0.5, -0.6)
    for deg in range(55, 415, 360 // 7):
        tr_vertexes = [centre, (getX(centre[0], r1, deg), getY(centre[1], r1, deg)),
                       (getX(centre[0], rb1, deg + 36), getY(centre[1], rb1, deg + 36))]
        draw_triangle(tr_vertexes)
        tr_vertexes = [centre, (getX(centre[0], r1, deg + 72), getY(centre[1], r1, deg + 72)),
                       (getX(centre[0], rb1, deg + 36), getY(centre[1], rb1, deg + 36))]
        draw_triangle(tr_vertexes)


    glFlush()  # Очистить все очереди команд и выполнить все оставшиеся команды
    glFlush()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1600, 700)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("helicopter")
    glutDisplayFunc(show)
    glutIdleFunc(show)
    glutSpecialFunc(rotate)
    glutMainLoop()


if __name__ == '__main__':
    main()