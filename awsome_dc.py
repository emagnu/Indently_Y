from dataclasses import dataclass, field, InitVar


@dataclass
class Fruit:
    name: str
    grams: float
    cost_per_kg: float
    is_rare: InitVar[bool] = False
    similar_fruits: list[str] = field(default_factory=list)

    # total_value: float = self.grams / 1000 * self.cost_per_kg
    # Need to create a placeholder -- CALCULATE LATER!
    total_value: float = field(init=False)

    def __post_init__(self, is_rare: bool) -> None:
        self.total_value = self.grams / 1000 * self.cost_per_kg

        if is_rare:
            self.total_value *= 2
            self.cost_per_kg *= 2


def main() -> None:
    apple: Fruit
    apple = Fruit("Apple", 2500, 3)
    banana = Fruit("Banana", 1500, 10, is_rare=True)
    print(f" --  Banana: {banana}")
    banana = Fruit("Banana", 1500, 10, is_rare=False)
    print(f" --  Banana: {banana}")
    orange: Fruit = Fruit("Orange", 500, 1, similar_fruits=["apple", "lemon"])
    print(f" --  Orange: {orange}")

    print(apple)
    print(apple.grams)
    print(apple.total_value)
    print(banana)
    print(banana.total_value)
    print(orange.total_value)


if __name__ == "__main__":
    main()
