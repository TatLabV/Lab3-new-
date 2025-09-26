class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # наследуем от Person
        self.subject = subject
        self.students = []  # список студентов
    
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
    
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
    
    def list_students(self):
        print(f"Студенты преподавателя {self.name}:")
        for student in self.students:
            print(f"- {student.name}")

# Тестирование
teacher = Teacher("Мария Петровна", 45, "Математика")
student1 = Student("Иван Иванов", "001")
student2 = Student("Петр Сидоров", "002")

teacher.add_student(student1)
teacher.add_student(student2)
teacher.list_students()
