import pygame
import random
import sys
from typing import List, Tuple


class SandClock:
    def __init__(self, width: int, height: int, cell_size: int):
        self.cell_size = cell_size
        self.grid_width = width // cell_size
        self.grid_height = height // cell_size
        self.grid = [[0 for _ in range(self.grid_width)] for _ in range(self.grid_height)]

        # Цвета
        self.colors = {
            'background': (0, 0, 0),
            'border': (80, 80, 80),
            'sand': [
                (194, 178, 128),
                (210, 190, 140),
                (180, 160, 110),
                (200, 185, 135)
            ]
        }

        self.init_hourglass()
        self.fill_upper_chamber()

    def init_hourglass(self):
        neck_width = 3
        center_y = self.grid_height // 2
        max_width = self.grid_width // 2 - 2  # Максимальная ширина у основания

        for y in range(self.grid_height):
            if y < center_y:
                # Инвертируем прогресс для верхней части (1 - progress)
                progress = y / center_y
                width = int(max_width * (1 - progress) ** 0.5)  # Сужаемся к центру
            else:
                # Оставляем как было для нижней части
                progress = (y - center_y) / (self.grid_height - center_y)
                width = int(max_width * progress ** 0.5)  # Расширяемся от центра

            # Гарантируем минимальную ширину горловины
            width = max(neck_width, width)
            left = (self.grid_width - width) // 2
            right = left + width - 1

            # Формируем узкую горловину в центре
            if center_y - 2 <= y <= center_y + 2:
                width = neck_width
                left = (self.grid_width - width) // 2
                right = left + width - 1

            # Заполняем границы
            for x in range(self.grid_width):
                self.grid[y][x] = 2 if x < left or x > right else 0

    def fill_upper_chamber(self):
        center_y = self.grid_height // 2
        fill_height = center_y - 8

        for y in range(fill_height):
            progress = y / fill_height
            width = int((self.grid_width // 2 - 2) * (1 - progress ** 0.3))
            left = (self.grid_width - width) // 2
            right = left + width - 1

            for x in range(left, right + 1):
                if self.grid[y][x] == 0:
                    self.grid[y][x] = 1

    def update(self):
        new_grid = [row.copy() for row in self.grid]

        for y in range(self.grid_height - 2, -1, -1):
            for x in random.choice([range(self.grid_width), reversed(range(self.grid_width))]):
                if self.grid[y][x] == 1:
                    if new_grid[y + 1][x] == 0:
                        new_grid[y][x] = 0
                        new_grid[y + 1][x] = 1
                    else:
                        directions = [-1, 1] if random.random() < 0.5 else [1, -1]
                        for dx in directions:
                            if 0 <= x + dx < self.grid_width:
                                if new_grid[y + 1][x + dx] == 0 and self.grid[y][x + dx] != 2:
                                    new_grid[y][x] = 0
                                    new_grid[y + 1][x + dx] = 1
                                    break
                        if y < self.grid_height - 2:
                            for dx in [-1, 1]:
                                if 0 <= x + dx < self.grid_width:
                                    if new_grid[y + 2][x + dx] == 0 and self.grid[y + 1][x + dx] != 2:
                                        new_grid[y][x] = 0
                                        new_grid[y + 2][x + dx] = 1
                                        break

        self.grid = new_grid

    def reset(self):
        self.grid = [[0 for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        self.init_hourglass()
        self.fill_upper_chamber()


class Renderer:
    def __init__(self, width: int, height: int):
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.SysFont('Arial', 18)
        self.help_text = [
            "SPACE - пауза/продолжить",
            "R - перезапуск",
            "H - скрыть подсказки"
        ]

    def draw(self, sand_clock: SandClock, show_help: bool):
        self.screen.fill(sand_clock.colors['background'])

        # Рисуем песок
        for y in range(sand_clock.grid_height):
            for x in range(sand_clock.grid_width):
                if sand_clock.grid[y][x] == 1:
                    color = random.choice(sand_clock.colors['sand'])
                    offset = sand_clock.cell_size // 4
                    rect = (
                        x * sand_clock.cell_size + random.randint(0, offset),
                        y * sand_clock.cell_size + random.randint(0, offset),
                        sand_clock.cell_size - random.randint(0, offset),
                        sand_clock.cell_size - random.randint(0, offset)
                    )
                    pygame.draw.rect(self.screen, color, rect)

        # Рисуем границы
        for y in range(sand_clock.grid_height):
            for x in range(sand_clock.grid_width):
                if sand_clock.grid[y][x] == 2:
                    pygame.draw.rect(self.screen, sand_clock.colors['border'],
                                     (x * sand_clock.cell_size, y * sand_clock.cell_size,
                                      sand_clock.cell_size, sand_clock.cell_size))

        # Отображаем подсказки
        if show_help:
            for i, text in enumerate(self.help_text):
                text_surf = self.font.render(text, True, (255, 255, 255))
                self.screen.blit(text_surf, (10, 10 + i * 22))

        pygame.display.flip()


class App:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 800
        self.cell_size = 5
        self.clock = pygame.time.Clock()

        self.sand_clock = SandClock(self.width, self.height, self.cell_size)
        self.renderer = Renderer(self.width, self.height)

        self.running = True
        self.paused = False
        self.show_help = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r:
                    self.sand_clock.reset()
                elif event.key == pygame.K_h:
                    self.show_help = not self.show_help

    def run(self):
        while self.running:
            self.handle_events()

            if not self.paused:
                self.sand_clock.update()

            self.renderer.draw(self.sand_clock, self.show_help)
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    app = App()
    app.run()