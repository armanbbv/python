import numpy as np
import pygame
import random

field_size = 100
radius = 20
initial_mass = 500
threshold_mass = 250
cell_size = 5
frame_rate = 10


frame_fraction = 0.1

field = np.zeros((field_size, field_size))
state = np.zeros((field_size, field_size), dtype=int)  # 0 – раствор, 1 – твердая, 2 – каркас

center = field_size // 2
for i in range(field_size):
    for j in range(field_size):
        if (i - center) ** 2 + (j - center) ** 2 <= radius ** 2:
            if random.random() < frame_fraction:
                state[i, j] = 2
                field[i, j] = 0
            else:
                state[i, j] = 1
                field[i, j] = initial_mass

def update_field(field, state):
    new_field = field.copy()
    new_state = state.copy()
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if state[i, j] == 2:
                continue
            mass = field[i, j]
            if state[i, j] == 1:
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < field.shape[0] and 0 <= nj < field.shape[1]:
                        if state[ni, nj] == 0:
                            delta = 0.0001 * (250 - field[ni, nj])
                            new_field[ni, nj] += delta
                            new_field[i, j] -= delta
                if new_field[i, j] < threshold_mass:
                    new_state[i, j] = 0
            elif state[i, j] == 0:
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < field.shape[0] and 0 <= nj < field.shape[1]:
                        if state[ni, nj] == 0 and field[ni, nj] < mass:
                            delta = 0.001 * (mass - field[ni, nj])
                            new_field[ni, nj] += delta
                            new_field[i, j] -= delta
    return new_field, new_state

pygame.init()
screen = pygame.display.set_mode((field_size * cell_size, field_size * cell_size))
pygame.display.set_caption("Клеточный автомат с каркасом")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    field, state = update_field(field, state)

    screen.fill((0, 0, 0))
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if state[i, j] == 2:
                color = (128, 128, 128)
            elif state[i, j] == 1:
                color = (255, 0, 0)
            else:
                blue_intensity = int(255 * field[i, j] / threshold_mass)
                blue_intensity = max(0, min(255, blue_intensity))
                color = (255 - blue_intensity, 255 - blue_intensity, 255)
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

    pygame.display.flip()
    clock.tick(frame_rate)

pygame.quit()