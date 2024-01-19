##   ##

# from dataclasses import dataclass  # , field, InitVar
from dataclasses import dataclass


# Non DataClass way
class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    # def __eq__(self, other):
    #     return self.__dict__ == other.__dict__


banana = Fruit("banana", 10)
apple = Fruit("apple", 20)
print(" --  Normal Class")
print(banana)
print(apple.name)
print(banana.calories)
banana2 = Fruit("banana", 10)
print(banana == banana2)
print(banana is banana2)


# @dataclass
# @dataclass(frozen=True)
# @dataclass(slots=True)
@dataclass(kw_only=True)
class Fruit:
    # __slots__: list[str] = ["name", "calories"]
    name: str
    calories: float
    # calories: float = 10

    def __str__(self) -> str:
        return f"{self.name}: {self.calories} calories"


# banana = Fruit("banana", 10)
# apple = Fruit("apple", 20)
# print(" --  Dataclass")
# print(banana)
# banana2 = Fruit("banana", 10)
# print(banana == banana2)
# print(banana is banana2)

# print(" --  banana.calories")
# print(banana.calories)
# banana.calories = 60  # This becoses an issue if dataclass is frozen!
# print(banana.calories)
# print(banana)
banana3 = Fruit(name="Banana", calories=30)
