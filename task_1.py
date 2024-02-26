

class Numbers:
    def __init__(self, lst: list[int]):
        self.lst=lst

    def summ(self):
        return sum(self.lst)

    def middle(self):
        return sum(self.lst)/len(self.lst)

    def maximum(self):
        return max(self.lst)

    def minimum(self):
        return min(self.lst)


