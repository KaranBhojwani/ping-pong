import pygame
from .paddle import Paddle
from .ball import Ball

# Game Engine

WHITE = (255, 255, 255)


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.paddle_width = 10
        self.paddle_height = 100

        # paddles and ball
        self.player_paddle = Paddle(10, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ai_paddle = Paddle(width - 20, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ball_obj = Ball(width // 2, height // 2, 7, 7, width, height)

        # scores and fonts
        self.player_points = 0
        self.ai_points = 0
        self.score_font = pygame.font.SysFont("Arial", 30)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_paddle.move(-10, self.height)
        if keys[pygame.K_s]:
            self.player_paddle.move(10, self.height)

    def update(self):
        self.ball_obj.move()
        self.ball_obj.check_collision(self.player_paddle, self.ai_paddle)

        if self.ball_obj.pos_x <= 0:
            self.ai_points += 1
            self.ball_obj.reset()
        elif self.ball_obj.pos_x >= self.width:
            self.player_points += 1
            self.ball_obj.reset()

        self.ai_paddle.auto_track(self.ball_obj, self.height)

    def render(self, screen):
        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, self.player_paddle.rect())
        pygame.draw.rect(screen, WHITE, self.ai_paddle.rect())
        pygame.draw.ellipse(screen, WHITE, self.ball_obj.rect())
        pygame.draw.aaline(screen, WHITE, (self.width // 2, 0), (self.width // 2, self.height))

        # Draw score
        player_text = self.score_font.render(str(self.player_points), True, WHITE)
        ai_text = self.score_font.render(str(self.ai_points), True, WHITE)
        screen.blit(player_text, (self.width // 4, 20))
        screen.blit(ai_text, (self.width * 3 // 4, 20))
