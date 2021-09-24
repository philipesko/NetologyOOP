class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached and (0 <= grade <= 10):
            if course in lecturer.result_grade:
                lecturer.result_grade[course] += [grade]
            else:
                lecturer.result_grade[course] = [grade]
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
        self.result_grade = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, grade, course):
        if isinstance(student, Student) and course in self.courses_attached and course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка, курсы не совпадают"


first_student = Student('Ruoy', 'Eman', 'man')
first_student.finished_courses += ['Pascal']


strong_reviwer = Reviewer('Dragon', 'Fire')
strong_reviwer.courses_attached += ['Pascal']
strong_reviwer.rate_hw(first_student, 10, 'Pascal')


last_lecturer = Lecturer('Loren', 'Avgsh')
last_lecturer.courses_attached += ['Pascal']

first_student.rate_lecturer(last_lecturer, 'Pascal', 4)



print(first_student.grades)
print(last_lecturer.result_grade)    


""" 
best_student = Student('Ruoy', 'Eman', 'man')
best_student.finished_courses += ['Python']
 
cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

best_student.rate_hw(cool_mentor, 'Python', 2) """


 
# print(best_student.grades)

