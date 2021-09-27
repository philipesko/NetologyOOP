class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grades(self):
        counter = 0
        rating = 0
        for key in self.grades.keys():
            for rate in self.grades[key]:
                counter += 1
                rating = rating + rate
        avg_rate = rating / counter
        return round(avg_rate, 1)

    def __str__(self):
        finished_courses = ''
        grades_name = []
        for key in self.grades.keys():
            grades_name.append(key)
        response = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grades()}\
            \nКурсы в процессе изучения: {", ".join(grades_name)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return response

    def compare(self, compare_student):
        name_winner = ""
        win_grade = "No body"
        if isinstance(compare_student, Student):
            if self.avg_grades() > compare_student.avg_grades():
                name_winner = self.name
                win_grade = self.avg_grades()
            elif self.avg_grades() == compare_student.avg_grades():
                name_winner = "No body"
            else:
                name_winner = compare_student.name
                win_grade = compare_student.avg_grades()
        else: 
            print("I don't compare this objects")
        return f"Is winner: {name_winner} with grade: {win_grade}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.grades = {}

    def avg_grades(self):
        counter = 0
        rating = 0
        if len(self.grades):
            for key in self.grades.keys():
                for rate in self.grades[key]:
                    counter += 1
                    rating = rating + rate
            avg_rate = rating / counter
        else:
            avg_rate = 0
        return round(avg_rate, 1)

    def __str__(self):
        response = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grades()}'
        return response

    def compare(self, comp_lecturer):
        name_winner = ""
        win_grade = "No body"
        if isinstance(comp_lecturer, Lecturer):
            if self.avg_grades() > comp_lecturer.avg_grades():
                name_winner = self.name
                win_grade = self.avg_grades()
            elif self.avg_grades() == comp_lecturer.avg_grades():
                name_winner = "No body"
            else:
                name_winner = comp_lecturer.name
                win_grade = comp_lecturer.avg_grades()
        else: 
            print("I don't compare this objects")
        return f"Is winner: {name_winner} with grade: {win_grade}"

 
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        response = f'Имя: {self.name}\nФимилия: {self.surname}'
        return response
        
    def raiting(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка, курсы не совпадают"


first_student = Student('Ruoy', 'Eman', 'man')
first_student.courses_in_progress += ['Pascal']
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['Программирование для начинающих']
first_student.finished_courses += ['Программирование в стиле ООП']

next_student = Student('German', 'Petrovich', 'man')
next_student.courses_in_progress += ['Git']
next_student.courses_in_progress += ['Python']
next_student.finished_courses += ['Программирование для начинающих']
next_student.finished_courses += ['Гитолевел']


strong_reviwer = Reviewer('Dragon', 'Fire')
strong_reviwer.courses_attached += ['Pascal']
strong_reviwer.courses_attached += ['Python']
print(strong_reviwer.raiting(first_student, 'Pascal', 10))
print(strong_reviwer.raiting(first_student, 'Python', 3))
print(strong_reviwer.raiting(first_student, 'Pascal', 10))

light_reviwer = Reviewer('Big', 'Smaillovich')
light_reviwer.courses_attached += ['Git']
light_reviwer.courses_attached += ['Python']
print(light_reviwer.raiting(first_student, 'Git', 10))
print(light_reviwer.raiting(first_student, 'Python', 3))
print(light_reviwer.raiting(first_student, 'Git', 10))
print(light_reviwer.raiting(next_student, 'Git', 10))


last_lecturer = Lecturer('Loren', 'Avgsh')
last_lecturer.courses_attached += ['Pascal']
last_lecturer.courses_attached += ['Python']
last_lecturer.courses_attached += ['Git']

first_lecturer = Lecturer('Djedy', 'Avgers')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']



first_student.rate_hw(last_lecturer, 'Pascal', 4)
first_student.rate_hw(last_lecturer, 'Python', 8)

next_student.rate_hw(last_lecturer, 'Git', 4)
next_student.rate_hw(last_lecturer, 'Python', 8)


print(last_lecturer.grades)  
print(first_student.grades)
  
print(last_lecturer.avg_grades())
print(first_lecturer.avg_grades())

print('___avg students___')
print(first_student.__str__())
print(next_student.__str__())
print('___avg lecturers___')
print(first_lecturer.__str__())
print(last_lecturer.__str__())


print(first_lecturer.compare(last_lecturer))
print(first_student.compare(next_student))


