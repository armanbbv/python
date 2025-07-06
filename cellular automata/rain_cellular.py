import pygame
import random as r


class Field:
    def __init__(self):
        self.arena = [[' '] * 200 for _ in range(200)]


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def act(self, arena):
        new_y = self.y + 1
        if new_y < 200 and arena[new_y][self.x] == ' ':
            self.y = new_y
        else:
            can_move_left = (self.x - 1 >= 0) and (arena[self.y][self.x - 1] == ' ')
            can_move_right = (self.x + 1 < 200) and (arena[self.y][self.x + 1] == ' ')

            if can_move_left and can_move_right:
                self.x += r.choice([-1, 1])
            elif can_move_left:
                self.x -= 1
            elif can_move_right:
                self.x += 1


def render_pygame(scr, arena):
    scale = 4 # Увеличено для уменьшения относительной толщины рамки
    border_color = (60, 60, 60)  # Менее контрастный цвет

    scr.fill((135, 206, 250))

    # Сначала рисуем все клетки
    for y in range(200):
        for x in range(200):
            rect = pygame.Rect(x * scale, y * scale, scale, scale)

            if arena[y][x] == 'X':
                color = (139, 69, 19) if y < 130 else (245, 222, 179)
            elif arena[y][x] == 'W':
                color = (255, 255, 180)  # Более светлый желтый
            elif arena[y][x] == 'o':
                color = (30, 144, 255)
            else:
                continue

            pygame.draw.rect(scr, color, rect)

    # Затем рисуем сетку поверх всех клеток
    for y in range(200):
        for x in range(200):
            rect = pygame.Rect(x * scale, y * scale, scale, scale)
            # Тонкие линии только между клетками
            if x < 199:
                pygame.draw.line(scr, border_color,
                                 (rect.right, rect.top),
                                 (rect.right, rect.bottom), 1)
            if y < 199:
                pygame.draw.line(scr, border_color,
                                 (rect.left, rect.bottom),
                                 (rect.right, rect.bottom), 1)


def create_house(arena):
    # Стены
    wall_height = 50
    wall_y = 130
    for y in range(wall_y, wall_y + wall_height):
        for x in range(60, 140):
            arena[y][x] = 'X'

    # Окно
    window_size = 24
    for y in range(wall_y + 10, wall_y + 30):
        for x in range(100 - window_size // 2, 100 + window_size // 2):
            arena[y][x] = 'W'

    # Крыша
    roof_base_y = wall_y - 30
    roof_height = 30
    for dy in range(roof_height):
        width = 40 + dy * 3
        start_x = 100 - width // 2
        y = roof_base_y + dy
        for dx in range(width):
            x = start_x + dx
            arena[y][x] = 'X'


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Rain")
    clock = pygame.time.Clock()

    arena = Field()
    water_list = []

    create_house(arena.arena)

    running = True
    pause = False
    spawn_timer = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause

        if not pause:
            # Генерация воды
            spawn_timer += 1
            if spawn_timer % 1 == 0:
                for _ in range(5):
                    x = r.randint(0, 199)
                    y = r.randint(0, 3)
                    if arena.arena[y][x] == ' ':
                        water = Cell(x, y)
                        water_list.append(water)
                        arena.arena[y][x] = 'o'

            # Обновление позиций
            for y in range(200):
                for x in range(200):
                    if arena.arena[y][x] == 'o':
                        arena.arena[y][x] = ' '

            for wat in water_list[:]:
                wat.act(arena.arena)
                if 0 <= wat.y < 190:
                    if arena.arena[wat.y][wat.x] == ' ':
                        arena.arena[wat.y][wat.x] = 'o'
                else:
                    water_list.remove(wat)

        render_pygame(screen, arena.arena)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()