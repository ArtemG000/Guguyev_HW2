#Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі додавання до групи більше 10-ти студентів, було порушено виняток користувача.
# Таким чином потрібно створити ще й виняток користувача для цієї ситуації.
# І обробити його поза межами класу. Тобто. потрібно перехопити цей виняток, при спробі додавання 11-го студента
#Artem Guguyev

class FullGroupError(Exception):
    pass

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.age} years old'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.record_book}'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise FullGroupError('The Group is full')

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

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'


st3 = Student('Male', 30, 'Steve', 'Job', 'AN142')
st4 = Student('Female', 25, 'Liza', 'Taylok', 'AN145')
st5 = Student('Male', 30, 'Steve', 'Jobyu', 'AN142')
st6 = Student('Female', 25, 'Liza', 'Taybor', 'AN145')
st7 = Student('Male', 30, 'Steve', 'Kobs', 'AN142')
st8 = Student('Female', 25, 'Liza', 'Tiolor', 'AN145')
st9 = Student('Male', 30, 'Steve', 'Jonnmies', 'AN142')
st10 = Student('Female', 25, 'Liza', 'Tor', 'AN145')
st11 = Student('Male', 31, 'Stye', 'Blok', 'AN146')

for i in (st3, st4, st5, st6, st7, st8, st9, st10):
    gr.add_student(i)
print(str(gr))

try:
    gr.add_student(st11)
except FullGroupError as error:
    print(f'ERROR! Its not possible to add a new student, because "{error}"')