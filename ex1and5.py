class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []  #список оценок
    
    def add_grade(self, grade):
        #Проверка что оценка от 0 до 10
        if 0 <= grade <= 10:
            self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:  #если нет оценок
            return 0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        print(f"Студент: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.get_average():.2f}")
    
    #Методы
    def __str__(self):
        return f"Студент {self.name} (ID: {self.student_id})"
    
    def __eq__(self, other):
        #Сравнение по ID студента
        return self.student_id == other.student_id
    
    def __len__(self):
        #Количество оценок
        return len(self.grades)

#Тестирование
student1 = Student("Иван Иванов", "001")
student1.add_grade(8)
student1.add_grade(9)
student1.add_grade(7)
student1.display_info()

student2 = Student("Петр Сидоров", "002")
print(f"\nСравнение студентов: {student1 == student2}")
print(f"Количество оценок: {len(student1)}")
