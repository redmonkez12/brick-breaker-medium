import pygame


class Brick:
    def __init__(self, game, x, y, health):
        self.x = x
        self.y = y

        self.settings = game.settings
        self.game = game

        self.width = self.settings.brick_width
        self.height = self.settings.brick_height
        self.health = health
        self.max_health = health
        self.color = self.settings.brick_colors[0]

    @staticmethod
    def interpolate(color_a, color_b, t):
        return tuple(int(a + (b - a) * t) for a, b in zip(color_a, color_b))

    def draw(self):
        pygame.draw.rect(
            self.game.window, self.color, (self.x, self.y, self.width, self.height))

    def collide(self, ball):
        if not (self.x + self.width >= ball.x >= self.x):
            return False
        if not (ball.y - ball.radius <= self.y + self.height):
            return False

        self.hit()
        ball.set_vel(ball.x_vel, ball.y_vel * -1)
        return True

    def hit(self):
        self.health -= 1
        self.color = self.interpolate(*self.settings.brick_colors, self.health / self.max_health)
