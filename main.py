class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def info(self):
        avg = self.average_grade()
        print(f"Talaba: {self.name}")
        print(f"Baholar: {self.grades}")
        print(f"O'rtacha: {avg:.1f}")
        print("-" * 30)


if __name__ == "__main__":
    t1 = Student("Hasan")
    for b in [85, 90, 95, 78]:
        t1.add_grade(b)
    t1.info()

    t2 = Student("Malika")
    for b in [92, 88, 76, 95]:
        t2.add_grade(b)
    t2.info()
