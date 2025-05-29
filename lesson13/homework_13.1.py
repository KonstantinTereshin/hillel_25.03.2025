#ДЗ 13.1. Група студентів
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        base = super().__str__()
        return f"{base}, Record Book: {self.record_book}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.record_book == other.record_book

    def __hash__(self):
        return hash(self.record_book)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Can only add Student instances")
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        if not self.group:
            return f"Group {self.number} is empty"
        # Sort by last name for consistent ordering
        students_list = sorted(self.group, key=lambda s: s.last_name)
        all_students = "\n".join(str(s) for s in students_list)
        return f"Group {self.number}:\n{all_students}"


if __name__ == "__main__":
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr = Group('PD1')

    gr.add_student(st1)
    gr.add_student(st2)
    print(gr)
    # Проверка поиска
    assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
    assert gr.find_student('Jobs2') is None, 'Test2'
    assert isinstance(gr.find_student('Jobs'), Student), 'Метод поиска должен возвращать экземпляр'

    # Удаление студента
    gr.delete_student('Taylor')
    print("\nAfter deleting Taylor:")
    print(gr)  # Должен остаться только st1

    # Повторное удаление не вызывает ошибок
    gr.delete_student('Taylor')
    print("\nAfter trying to delete Taylor again:")
    print(gr)
