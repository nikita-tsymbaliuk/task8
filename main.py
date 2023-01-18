import pgzrun
import pygame

from Paddle import Paddle
from Ball import Ball

WIDTH = 700
HEIGHT = 400
window = pygame.display.set_mode((WIDTH,HEIGHT))
paddle = Paddle(window)
ball = Ball(window)
windowRect = window.get_rect()

def on_mouse_move(pos): # функция управления платформой с помощью курсора
    x, y = pos
    paddle.rect.x = x
    if (paddle.rect.right >= window.get_rect().right):
        paddle.rect.right = window.get_rect().right
    if (paddle.rect.left <= window.get_rect().left):
        paddle.rect.left = window.get_rect().left


pgzrun.go()
