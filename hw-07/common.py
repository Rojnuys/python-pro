from decimal import Decimal
from colorama import Fore, Style


class frange:
    def __init__(self, first: int | float | Decimal, second: int | float | Decimal | None = None,
                 step: int | float | Decimal = 1):
        if second is None:
            self.first = 0
            self.second = first
        else:
            self.first = first
            self.second = second

        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.first >= self.second and self.step > 0) or (self.first <= self.second and self.step < 0):
            raise StopIteration
        result = self.first
        self.first += self.step
        return result


class colorizer:
    def __init__(self, color: str):
        self.color = color

    def __enter__(self):
        print(getattr(Fore, self.color.upper()), end="")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(Style.RESET_ALL, end="")
