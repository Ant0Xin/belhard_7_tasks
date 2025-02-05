"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: float

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __gt__(self, other):
        return self.average_score > other.average_score

    def __le__(self, other):
        return self.average_score <= other.average_score

    def __ge__(self, other):
        return self.average_score >= other.average_score

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __ne__(self, other):
        return self.average_score != other.average_score

    def __repr__(self):
        return f"Name = {self.name}, Surname = {self.surname}, "\
               f"Group = {self.group}, Average_score = {self.average_score}."


students_list = [
    Student('Anton', 'Dovnar', 33, 9.6),
    Student('Vova', 'Zaicev', 27, 3.2),
    Student('Eva', 'Petrova', 31, 7.3),
    Student('Slava', 'Dubok', 33, 2.9),
    Student('Klava', 'Xodich', 25, 4.5)
]

print(sorted(students_list))
print(sorted(students_list, reverse=True))
best_list = [student for student in students_list if student.average_score > 5]
print(best_list)
