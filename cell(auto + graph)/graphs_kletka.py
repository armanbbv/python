import numpy as np
import matplotlib.pyplot as plt

field_size = 100
radius = 20
initial_mass = 500
threshold_mass = 250

field = np.zeros((field_size, field_size))
center = field_size // 2
for i in range(field_size):
    for j in range(field_size):
        if (i - center) ** 2 + (j - center) ** 2 <= radius ** 2:
            field[i, j] = initial_mass

def update_field(field):
    new_field = field.copy()
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            mass = field[i, j]
            if mass > threshold_mass:
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < field.shape[0] and 0 <= nj < field.shape[1]:
                        neighbor_mass = field[ni, nj]
                        if neighbor_mass <= threshold_mass:
                            delta = 0.0001 * (250 - neighbor_mass)
                            new_field[ni, nj] += delta
                            new_field[i, j] -= delta
                if new_field[i, j] < threshold_mass:
                    new_field[i, j] = max(new_field[i, j], 0)
            else:
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < field.shape[0] and 0 <= nj < field.shape[1]:
                        neighbor_mass = field[ni, nj]
                        if neighbor_mass < mass:
                            delta = 0.001 * (mass - neighbor_mass)
                            new_field[ni, nj] += delta
                            new_field[i, j] -= delta
    return new_field

time_steps = []
release_amounts = []
max_steps = 1000
for step in range(max_steps):
    time_steps.append(step)
    # Сумма вещества в жидких клетках
    release = np.sum(field[field <= threshold_mass])
    release_amounts.append(release)
    if np.all(field <= threshold_mass):
        print(f"Растворение завершено на шаге {step}")
        break
    field = update_field(field)

filename = 'release_data_real.csv'
np.savetxt(filename, np.column_stack((time_steps, release_amounts)), delimiter=',', header='Time,Release', comments='')
print(f"Данные сохранены в {filename}")

data = np.loadtxt(filename, delimiter=',', skiprows=1)
time = data[:, 0]
release = data[:, 1]

plt.plot(time, release, marker='o')
plt.title("График высвобождения вещества из таблетки")
plt.xlabel("Время")
plt.ylabel("Количество вещества в жидкости")
plt.grid(True)
plt.show()