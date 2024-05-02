class Demo:
    def add(self, *args):
        total = 0
        for i in args:
            total += i
        return total

d = Demo()
print(d.add(2, 3))  # Output: 5
print(d.add(10, 20, 30))  # Output: 60
