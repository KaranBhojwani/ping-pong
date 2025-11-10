import pygame
import random

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        # initial position (to reset to)
        self.start_x = x
        self.start_y = y
        # current position
        self.pos_x = x
        self.pos_y = y
        # dimensions
        self.ball_w = width
        self.ball_h = height
        # screen bounds
        self.screen_w = screen_width
        self.screen_h = screen_height
        # velocities
        self.vel_x = random.choice([-5, 5])
        self.vel_y = random.choice([-3, 3])

    def move(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

        # bounce off top/bottom
        if self.pos_y <= 0 or self.pos_y + self.ball_h >= self.screen_h:
            self.vel_y *= -1

    def check_collision(self, player, ai):
        if self.rect().colliderect(player.rect()) or self.rect().colliderect(ai.rect()):
            self.vel_x *= -1

    def reset(self):
        self.pos_x = self.start_x
        self.pos_y = self.start_y
        self.vel_x *= -1
        self.vel_y = random.choice([-3, 3])

    def rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.ball_w, self.ball_h)
