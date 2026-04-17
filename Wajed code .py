# SayDays.py

class SayDays:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    def is_leap(self) -> bool:
        y = self.year
        return (
            (y % 4 == 0 and y % 100 != 0) or
            (y % 400 == 0)
        )

    def days(self) -> int:
        # On Jan 1, how many days until now?
        days_in_month = [
            31, 29 if self.is_leap() else 28, 31, 30,
            31, 30, 31, 31,
            30, 31, 30, 31
        ]

        total = 0
        m = 0  # 0th month = January

        # Calculates all days in all previous months
        while m < self.month - 1:
            total += days_in_month[m]
            m += 1

        # Add the days in this month until today
        total += self.day
        return total

    def days_left(self):
        # Until Dec 31, how many days left?
        total_days = 366 if self.is_leap() else 365
        return total_days - self.days()

    def weekday(self):
        # Use Zeller's formula
        y = self.year
        m = self.month
        d = self.day

        if m < 3:
            m += 12
            y -= 1

        k = y % 100
        J = y // 100

        h = (d + (13 * (m + 1)) // 5 + k + k // 4 + J // 4 + 5 * J) % 7
        return h

    def weekday_name(self):
        names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return names[self.weekday()]


# RUN IT!
while True:
    year = int(input("What year is it? "))
    month = int(input("What month is it? "))
    day = int(input("What day is it? "))

    date = SayDays(year, month, day)

    print("Days after Jan 1:", date.days())
    print("Days until Dec 31:", date.days_left())
    print("English day of the week:", date.weekday_name())