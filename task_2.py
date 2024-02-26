class Number:
    def __init__(self, num: int):
        self.num = num

    def eight(self):
        return oct(self.num)

    def sixteen(self):
        return hex(self.num)

    def double(self):
        return bin(self.num)


num = Number(16)
print(num.eight())
print(num.sixteen())
print(num.double())