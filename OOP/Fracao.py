class Fracao:

    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __repr__(self):
        if self.den != 1:
            return '%d/%d' % (self.num, self.den)
        else:
            return '%d' % (self.num)

    def get(self):
        return self.num, self.den

    def put(self, n=0, d=1):
        self.num, self.den = n, d

    def mdc(self, a=4, b=7):

        if self.num % a == 0 and self.den % b == 0:

            self.num /= a
            self.den /= b

            return '%d/%d' % (self.num, self.den)

        else:

            return '%d/%d' % (self.num, self.den)

    def __add__(self, sum):

        sum = self.num + self.den

        return '%d+%d' % (self.num, self.den), sum

    def __sub__(self, sub):

        sub = self.num - self.den

        return '%d-%d' % (self.num, self.den), sub

    def __mult__(self, mult):

        mult = self.num * self.den

        return '%d*%d' % (self.num, self.den), mult

    def __div__(self, div):

        div = self.num / self.den

        return '%d/%d' % (self.num, self.den), div


f1 = Fracao(4, 1)
f2 = Fracao(12, 20)
# print(f1+f2)
print(f2.mdc())
print(f1.__add__(0))
print(f1.__sub__(0))
print(f2.__mult__(0))
print(f2.__div__(2))
