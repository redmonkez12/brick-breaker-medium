import pygame


class Paddle:
    def __init__(self, game, color):
        self.settings = game.settings
        self.game = game

        self.width = self.settings.paddle_width
        self.height = self.settings.paddle_height
        self.color = color
        self.moving_left = False
        self.moving_right = False

        self.x = 0
        self.y = 0

        self.reset()

    def draw(self):
        pygame.draw.rect(
            self.game.window,
            self.color,
            (self.x, self.y, self.width, self.height),
        )

    def move(self):
        if self.moving_left and self.x - self.settings.paddle_speed >= 0:
            self.x -= self.settings.paddle_speed

        if self.moving_right and self.x + self.width + self.settings.paddle_speed <= self.settings.width:
            self.x += self.settings.paddle_speed

    def reset(self):
        self.x = self.settings.width / 2 - self.width / 2
        self.y = self.settings.height - self.height - 5
