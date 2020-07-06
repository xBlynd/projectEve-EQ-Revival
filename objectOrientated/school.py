
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade   # 0 - 100

    #gets grades
    def get_grade(self):
        return self.grade
#creats a course class
class Course:
    #initiate the class
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False

    #adds student to list
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    # averages the grades
    def get_average_grade(self):
        value = 0
        #pulls student data
        for student in self.students:
            #calculates average in students
            value += student.get_grade()

        return value / len(self.students)

# Students.  can move somewhere later.  Database.
s1 = Student('tim', 19, 95)
s2 = Student('bill', 19, 75)
s3 = Student('Liz', 19, 75)



course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_average_grade())