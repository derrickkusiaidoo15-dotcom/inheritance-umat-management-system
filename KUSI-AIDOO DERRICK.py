class Person:
    def __init__(self):
        self.name =input('Enter your name: ')
        self.age =input('Enter your age: ')

    def display(self):
        print('My name is ', self.name)
        print(f'I am {self.age} years old')
kojo = Person()
kojo.display()

print('\n==Student Details===')
class Student(Person):
    def __init__(self):
        super().__init__()
class Student(Person):
    def __init__(self):
        super().__init__()
        self.student_id = input('Enter your student id: ')
        self.enroll_ourse = input('Enter your enrolled course: ')
    def sam(self):
        print('Student id: ', self.student_id)
        print('Enroll ourse: ', self.enroll_ourse)
joseph = Student()
joseph.display()
joseph.sam()

print('\n==Lecturer Details===')
class Lecturer(Person):
class Lecturer(Person):
    def __init__(self):
        super().__init__()
        self.employee_id = input('Enter your employee_id: ')
        self.teach_course = input('Enter your teach_course: ')
    def kojo(self):
        print('Lecturer id: ', self.employee_id)
        print('Teacher course: ', self.teach_course)
lecturer = Lecturer()
lecturer.display()
lecturer.kojo()



