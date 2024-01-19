from dataclasses import dataclass, field, InitVar


@dataclass
class Fruit:
    name: str
    grams: float
    cost_per_kg: float
    is_rare: InitVar[bool] = False

    # total_value: float = self.grams / 1000 * self.cost_per_kg
    # Need to create a placeholder -- CALCULATE LATER!
    total_value: float = field(init=False)

    def __post_init__(self, is_rare: bool) -> None:
        self.total_value = self.grams / 1000 * self.cost_per_kg

        if is_rare:
            self.total_value * 2


def main() -> None:
    apple: Fruit
    apple = Fruit("Apple", 2500, 3)
    banana = Fruit("Banana", 1500, 10, is_rare=True)

    print(apple)
    print(apple.grams)
    print(apple.total_value)
    print(banana)
    print(banana.total_value)


if __name__ == "__main__":
    main()
    #
