class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        total_minutes %= 60
        return Time(total_hours, total_minutes)

    def displayTime(self):
        print(f"{self.hours} hour(s) and {self.minutes} minute(s)")

    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes}")

time1 = Time(1, 2)
time2 = Time(2, 50)

print("Time 1:")
time1.displayTime()
time1.displayMinute()

print("\nTime 2:")
time2.displayTime()
time2.displayMinute()

result = time1.addTime(time2)
print("\nAfter adding:")
result.displayTime()
result.displayMinute()
