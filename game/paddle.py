import pygame

class Paddle:
    def __init__(self, x, y, width, height):
        # position
        self.pos_x = x
        self.pos_y = y
        # dimensions
        self.paddle_w = width
        self.paddle_h = height
        # movement speed (pixels per update)
        self.move_speed = 7

    def move(self, dy, screen_height):
        self.pos_y += dy
        # clamp inside screen bounds
        self.pos_y = max(0, min(self.pos_y, screen_height - self.paddle_h))

    def rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self.paddle_w, self.paddle_h)

    def auto_track(self, ball, screen_height):
        # simple AI: move up/down to follow the ball's vertical position
        if ball.pos_y < self.pos_y:
            self.move(-self.move_speed, screen_height)
        elif ball.pos_y > self.pos_y + self.paddle_h:
            self.move(self.move_speed, screen_height)
