class Fraction:
    '''A class to represent a fraction'''
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    def show(self):
        print(self.num, "/", self.den)
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        common = self.__gcd__(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    
    def __gcd__(self, m, n):
        while m % n != 0:
            m, n = n, m % n
        return n
    
    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num
# To make sure you understand how operators are implemented in Python classes, 
# and how to properly write methods, write some methods to implement *, /, and - . Also implement comparison operators > and <  
    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = self.__gcd__(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    def __div__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = self.__gcd__(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        common = self.__gcd__(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num > second_num
    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num < second_num

my_fraction = Fraction(3, 5)
fraction2 = Fraction(1, 2)
print(my_fraction)
print(fraction2)   
print(my_fraction + fraction2)