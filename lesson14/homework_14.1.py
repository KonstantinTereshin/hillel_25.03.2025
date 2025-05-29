#ДЗ 14.1. Виняток користувача
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
        return isinstance(other, Student) and self.record_book == other.record_book

    def __hash__(self):
        return hash(self.record_book)


class GroupFullError(Exception):
    """Raised when trying to add more than 10 students to a group."""
    pass


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Can only add Student instances")
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupFullError(
                f"Cannot add {student.first_name} {student.last_name}: group '{self.number}' is full (max {self.MAX_STUDENTS} students)."
            )
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
        students_list = sorted(self.group, key=lambda s: s.last_name)
        all_students = "\n".join(str(s) for s in students_list)
        return f"Group {self.number}:\n{all_students}"


if __name__ == "__main__":
    gr = Group('PD1')
    # Пробуем добавить 11 студентів — на одинадцятому спрацює виняток
    try:
        for i in range(1, 12):  # 1..11
            st = Student('Male', 20 + i, f'Name{i}', f'Last{i}', f'RB{i:03}')
            gr.add_student(st)
            print(f"Added: {st}")
    except GroupFullError as e:
        print(f"Error: {e}")

    print("\nCurrent group members:")
    print(gr)
