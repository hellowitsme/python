# クラス
# ---------------------------------------
class Capsule():
    def __init__(self, public, private):
        self.public_name = public
        self.privale_age = private

    def change(self, public):
        self.public_name = public

    def _change(self, private):
        self.privale_age = private
r = Capsule("太郎", 25)
print(r.public_name)
print(r.privale_age)


# 継承
# ---------------------------------------
class Creature():
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

class Human(Creature):
    def greet(self):
        return "私は、{}です。年齢は{}歳です。".format(self.name, self.age)

class Dog(Creature):
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


person = Human("太郎", "man", 25)
dog = Dog("Stanly", "Golden", person)

print(person.greet())
print(dog.owner.name)
