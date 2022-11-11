class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def mid_grade(self):
        for course, grade in self.grades.items():
            res = sum(grade) / len(grade)
            return res

    def __str__(self):
        res1 = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {round(Lecturer.mid_grade(self), 1)}"
        return res1
    #
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a Lecturer")
            return
        return round(Lecturer.mid_grade(self), 1) < round(other.mid_grade(), 1)


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Error"

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_courses(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Error"

    def mid_grade(self):
        for course, grade in self.grades.items():
            res = sum(grade) / len(grade)
            return res

    def __str__(self):
        for course, grade in self.grades.items():
            res = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
                  f"Cредняя оценка за домашние задания {round(Student.mid_grade(self), 1)}\n" \
                  f"Курсы в процессе изучения:{self.courses_in_progress}\n" \
                  f"Завершенные курсы: {self.finished_courses}"
            return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student")
            return
        return round((Student.mid_grade(self)), 1) < round((other.mid_grade()), 1)


def mid_grade_students_courses(course, *args):
    grades_all_students = []
    for Student in args:
        if course in student1.courses_in_progress:
            grades_all_students.append(round(Student.mid_grade(), 1))
            res = sum(grades_all_students) / len(grades_all_students)
        return f'Средняя оценка студентов за курс "{course}" {round(res, 1)}'

def mid_grade_lecturers_courses(course, *args):
    grades_all_lecturers = []
    for Lecturer in args:
        if course in Lecturer.courses_attached:
            grades_all_lecturers.append(round(Lecturer.mid_grade(), 1))
            res1 = sum(grades_all_lecturers) / len(grades_all_lecturers)
    return f'Средняя оценка всех лекторов за курс "{course}"  {round(res1, 1)}'

#Студенты
student1 = Student("Vasia", "Pupkin", "male")
student1.courses_in_progress += ["Python"]
student1.finished_courses += ["JS"]

student2 = Student("Tora", "Apples", "female")
student2.courses_in_progress += ["Python", "Lolcode"]
student2.finished_courses += ["YoptaScript", "C++"]

# Проверяющие
reviewer1 = Reviewer("Jon", "Smit")
reviewer1.courses_attached += ["Python"]

reviewer2 = Reviewer("Ted", "Braflovsky")
reviewer2.courses_attached += ["Python", "C++"]

# Лекторы
lecturer_1 = Lecturer("Sam", "Smith")
lecturer_1.courses_attached += ["Python", "C++"]

lecturer_2 = Lecturer("Nancy", "Anderson")
lecturer_2.courses_attached += ["Python", "JS"]

# Оценки студ
reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student1, "Python", 8)
reviewer1.rate_hw(student1, "Python", 4)

reviewer2.rate_hw(student2, "Python", 9)
reviewer2.rate_hw(student2, "Python", 7)
reviewer2.rate_hw(student2, "Python", 10)

# Оценки лекторам
student1.rate_courses(lecturer_1, "Python", 10)
student1.rate_courses(lecturer_1, "Python", 10)
student1.rate_courses(lecturer_1, "Python", 10)

student2.rate_courses(lecturer_2, "Python", 10)
student2.rate_courses(lecturer_2, "Python", 7)
student2.rate_courses(lecturer_2, "Python", 9)

print('Проверяющие:')
print(reviewer1)
print(reviewer2)
print('')
print('Информация по Лекторам:')
print(lecturer_1)
print(lecturer_2)
print('')
print('Информация по Студентам:')
print(student1)
print(student2)
print('')
print(mid_grade_students_courses('Python', student1, student2))
print(mid_grade_lecturers_courses('Python', lecturer_2, lecturer_1))
