import pygame
import math

from settings import Settings
from paddle import Paddle
from ball import Ball
from brick import Brick


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.paddle = Paddle(self, "#77dd77")
        self.ball = Ball(self, self.settings.width / 2, self.paddle.y - self.settings.ball_radius, "#a96148")
        self.bricks = self.generate_bricks(self.settings.rows, self.settings.cols)

        self.window = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption("Brick Breaker")

        self.font_lives = pygame.font.SysFont("ubuntu", 40)  # new
        self.lives = self.settings.lives

    def display_text(self, text):  # new
        text_render = self.font_lives.render(text, 1, "red")
        self.window.blit(text_render, (
            self.settings.width / 2 - text_render.get_width() / 2,
            self.settings.height / 2 - text_render.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(3000)

    def generate_bricks(self, rows, cols):
        gap = 2
        bricks = []

        for row in range(rows):
            for col in range(cols):
                brick = Brick(self, col * self.settings.brick_width + gap * col,
                              row * self.settings.brick_height + gap * row, 2)
                bricks.append(brick)

        return bricks

    def ball_paddle_collision(self):
        if not (self.paddle.x + self.paddle.width >= self.ball.x >= self.paddle.x):
            return
        if not (self.ball.y + self.ball.radius >= self.paddle.y):
            return

        paddle_center = self.paddle.x + self.paddle.width / 2
        distance_to_center = self.ball.x - paddle_center

        percent_width = distance_to_center / self.paddle.width
        angle = percent_width * 90
        angle_radians = math.radians(angle)

        x_vel = math.sin(angle_radians) * self.settings.ball_speed
        y_vel = math.cos(angle_radians) * self.settings.ball_speed * -1

        self.ball.set_vel(x_vel, y_vel)

    def reset(self, lives=None):  # new
        self.paddle.reset()
        self.ball.reset()
        self.lives = self.lives if lives is None else lives

    def draw(self):
        self.window.fill(self.settings.bg_color)
        self.paddle.draw()
        self.ball.draw()

        for brick in self.bricks:
            brick.draw()

        lives_text = self.font_lives.render(f"Lives: {self.lives}", 1, "black")  # new
        self.window.blit(lives_text, (10, self.settings.height - lives_text.get_height() - 10))  # new

        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()
        is_running = True

        while is_running:
            clock.tick(self.settings.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    break

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.paddle.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.paddle.moving_left = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.paddle.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.paddle.moving_left = False

            self.paddle.move()
            self.ball.move()
            self.ball.collision()
            self.ball_paddle_collision()

            for brick in self.bricks[:]:
                brick.collide(self.ball)

                if brick.health <= 0:
                    self.bricks.remove(brick)

            if self.ball.y + self.ball.radius >= self.settings.height:
                self.lives -= 1
                self.reset()
                self.ball.set_vel(0, self.settings.ball_speed * -1)

            if self.lives <= 0:
                self.bricks = self.generate_bricks(3, 10)
                self.reset(3)
                self.display_text("You Lost!")

            if len(self.bricks) == 0:
                self.bricks = self.generate_bricks(3, 10)
                self.reset(3)
                self.display_text("You Won!")

            self.draw()

        pygame.quit()
        quit()


if __name__ == "__main__":
    game = Game()
    game.run()
