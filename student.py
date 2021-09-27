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
        for key in self.grades.keys():
            for rate in self.grades[key]:
                counter += 1
                rating = rating + rate
        avg_rate = rating / counter
        return avg_rate

    def __str__(self):
        response = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grades}'
        return response
 
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

strong_reviwer = Reviewer('Dragon', 'Fire')
strong_reviwer.courses_attached += ['Pascal']
print(strong_reviwer.raiting(first_student, 'Pascal', 10))


last_lecturer = Lecturer('Loren', 'Avgsh')
last_lecturer.courses_attached += ['Pascal']
last_lecturer.courses_attached += ['Python']

first_student.rate_hw(last_lecturer, 'Pascal', 4)
first_student.rate_hw(last_lecturer, 'Python', 8)


print(last_lecturer.grades)  
print(first_student.grades)
  
print(last_lecturer.avg_grades())




