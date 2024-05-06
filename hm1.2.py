class String(str):
    def __add__(self, other):
        return String(super().__add__(str(other)))

    def __radd__(self, other):
        return String(str(other) + self)

    def __sub__(self, other):
        if isinstance(other, str):
            return String(self.replace(other, '', 1))
        else:
            return self


s1 = String("hello")
s2 = String("world")
print(s1 + s2)

s3 = String("I have ")
num = 5
print(s3 + num)

s4 = String("hello world")
print(s4 - "hello")
print(s4 - "goodbye")
