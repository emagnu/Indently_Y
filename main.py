##   ##

from dataclasses import dataclass


@dataclass(slots=True)  # , kw_only=True)
class Person:
    name: str
    age: str
    job: str = None
    friends: list[str] = None

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old and worls at {self.job}. His freinds are {self.friends}"


json: dict = {
    "name": "Bob",
    "age": "21",
    "job": "Salesman",
    "friends": ["Mario", "Luigi"],
}


print(json["name"])
bob = Person(json["name"], json["age"], json["job"], json["friends"])

print(bob.job)
print(bob)
