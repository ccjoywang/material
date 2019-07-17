import datetime
from person import Person


class Student(Person):
    def __init__(self, name, birthday, courses):
        Person.__init__(self, name, birthday)
        self.courses = courses

    def get_courses(self):
        return self.courses

    def speak(self):
        print("I'm so tired!")


# usage
peter = Student('Peter', datetime.date(2000, 1, 1), ['Math', 'English'])
peter.speak()
peter.walk()
peter.cry()
print(peter.get_name())
print(peter.get_age())
print(peter.get_courses())
