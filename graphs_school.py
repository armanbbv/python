import numpy as np
import matplotlib.pyplot as plt


students = ['Иван', 'Мария', 'Петр', 'Ольга', 'Анна']
groups = [1, 1, 2, 2, 1]
steps = np.arange(1, 6)
scores = np.random.randint(50, 100, size=(len(students), len(steps)))

def plot_student_progress(students, scores):
    plt.figure()
    for i, student in enumerate(students):
        plt.plot(steps, scores[i], label=student)
    plt.title("Динамика успеваемости")
    plt.xlabel("Ходы")
    plt.ylabel("Баллы")
    plt.legend()
    plt.show()

    plt.figure()
    for i, student in enumerate(students):
        plt.bar(steps, scores[i], alpha=0.5, label=student)
    plt.title("Гистограммы успеваемости студентов")
    plt.xlabel("Ходы")
    plt.ylabel("Баллы")
    plt.legend()
    plt.show()

def plot_group_average(groups, scores):
    plt.figure()
    unique_groups = np.unique(groups)
    for g in unique_groups:
        group_scores = scores[np.array(groups) == g]
        avg_scores = np.mean(group_scores, axis=0)
        plt.bar(steps + 0.1*g, avg_scores, width=0.2, label=f'Группа {g}')
    plt.title("Средняя успеваемость групп")
    plt.xlabel("Ходы")
    plt.ylabel("Средний балл")
    plt.legend()
    plt.show()

def plot_single_student(student_index, scores):
    plt.figure()
    plt.plot(steps, scores[student_index], marker='o')
    plt.title(f"Изменение показателей {students[student_index]}")
    plt.xlabel("Ходы")
    plt.ylabel("Баллы")
    plt.show()

def plot_pie_chart(groups, scores, threshold=70):
    good_students = [groups[i] for i in range(len(students)) if np.mean(scores[i]) > threshold]
    unique_groups, counts = np.unique(good_students, return_counts=True)
    plt.figure()
    plt.pie(counts, labels=[f'Группа {g}' for g in unique_groups], autopct='%1.1f%%')
    plt.title(f"Доля студентов с успеваемостью выше {threshold}")
    plt.show()

if __name__ == "__main__":
    plot_student_progress(students, scores)
    plot_group_average(groups, scores)
    plot_single_student(1, scores)
    plot_pie_chart(groups, scores, threshold=70)