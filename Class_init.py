class Person:
  name = ""
  age = 1
  def __init__(self, name=None, age=None):
    self.name = name
    self.age = age

p2 = Person()
p2.name = "josh"
p2.age = 35
print(p2.name)
print(p2.age)

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
