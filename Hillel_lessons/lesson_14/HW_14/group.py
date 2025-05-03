class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        if self.find_student(last_name) in self.group:
            self.group.remove(self.find_student(last_name))

    def find_student(self, last_name):
        for st in self.group:
            if st.last_name == last_name:
                return st
        return None

    def __str__(self):
        all_students = list(map(str, self.group))
        ...
        return f'Numbers:{self.number}\n{'\n'.join(all_students)} '
