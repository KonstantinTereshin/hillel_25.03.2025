from student import Student

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
                f"Cannot add {student.first_name} {student.last_name}: "
                f"group '{self.number}' is full (max {self.MAX_STUDENTS} students)."
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
