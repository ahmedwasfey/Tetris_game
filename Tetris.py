from controllingFunc import *


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, hight)
    glutCreateWindow(b'Tetris')
    init()
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutKeyboardFunc(keyboard)
    glutKeyboardUpFunc(keyboardup)
    glutSpecialFunc(keyboards)
    glutMainLoop()


main()