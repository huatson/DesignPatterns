from dataclasses import dataclass, field

#
# OBJECTS
#


class PersonObj(object):
    def __init__(self, name: str, job: str, age: int) -> None:
        self._name = name
        self._job = job
        self._age = age


# create object instance
personobj = PersonObj("Geralt", "Witcher", 30)
print(personobj)
# <__main__.PersonObj object at 0x000001FBA8427730>

#
# DATA CLASSES
#


@dataclass
class Person:
    # dataclass types
    # init not required
    _name: str
    _job: str
    _age: int


# create dataclass instance
person1 = Person("Geralt", "Witcher", 30)
person2 = Person("Yennefer", "Sorcerer", 25)
person3 = Person("Yennefer", "Sorcerer", 25)

print(person1)
# Person(_name='Geralt', _job='Witcher', _age=30)
print(hex(id(person1)))
print(hex(id(person2)))
print(hex(id(person3)))

# both have the same data
print(person2 == person3)

#
# COMPARE DATA
#


@dataclass(order=True, frozen=True)
class PersonOrdered:
    # ORDER: data is sorted
    # FROZEN: data can not be changed after creation

    # sort index: used for compare values
    # Create fields:
    #   we dont want use it as a required argument for the class
    #   and we dont want it to show it when we print the object
    sort_idx: int = field(init=False, repr=False)
    # dataclass types
    # init not required
    name: str
    job: str
    age: int
    strength: int = 100

    # called after init: sort by age|strength
    def __post_init__(self):
        # since dataclass is FROZEN, we can not assign directly with
        # self.sort_idx = self.strength
        object.__setattr__(self, "sort_idx", self.strength)

    def __str__(self) -> str:
        return f"Name: {self.name}, Job: {self.job}, Age: {self.age}, Strenght: {self.strength}"


# create dataclass instance
person1o = PersonOrdered("Geralt", "Witcher", 30)
person2o = PersonOrdered("Yennefer", "Sorcerer", 25, 50)
person3o = PersonOrdered("Yennefer", "Sorcerer", 25, 50)

print(person1o)
print(person2o)
# ordered by age|strength, compare geralt with yennefer
print(person1o > person2o)

# since dataclass is frozen, we can not change attributes
try:
    person1o.age = 50
except Exception as error:
    print(error)
    pass
