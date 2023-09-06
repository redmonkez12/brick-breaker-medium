class Settings:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.fps = 60
        self.bg_color = "#38B6FF"

        self.paddle_speed = 5
        self.paddle_width = 100
        self.paddle_height = 10

        self.ball_speed = 5
        self.ball_radius = 10

        self.brick_colors = [(255, 128, 159), (255, 184, 194)]
        self.cols = 10
        self.rows = 3
        self.brick_height = 20
        self.brick_width = self.width // self.cols - 2

        self.lives = 3
