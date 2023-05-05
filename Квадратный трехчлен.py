from typing import Optional


class QuadraticPolynomial:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self) -> Optional[int]:
        if self.b ** 2 - 4 * self.a * self.c < 0:
            return None
        return (-self.b - (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)

    @property
    def x2(self) -> Optional[int]:
        if self.b ** 2 - 4 * self.a * self.c < 0:
            return None
        return (-self.b + (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)

    @property
    def view(self) -> str:
        if self.b >= 0 and self.c >= 0:
            return f"{self.a}x^2 + {self.b}x + {self.c}"
        if self.b <= 0 <= self.c:
            return f"{self.a}x^2 - {abs(self.b)}x + {self.c}"
        if self.b >= 0 >= self.c:
            return f"{self.a}x^2 + {self.b}x - {abs(self.c)}"
        return f"{self.a}x^2 - {abs(self.b)}x - {abs(self.c)}"

    @property
    def coefficients(self) -> tuple:
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, coef: tuple) -> None:
        self.a, self.b, self.c = coef
