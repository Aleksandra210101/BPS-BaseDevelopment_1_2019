
"""
Creator: Aleksandra Krylova
"""
from math import gcd


class Rational:
    "Fractions calculator"
    def __init__(self, a_number=0, b_number=1):
        self.a_number = a_number
        self.b_number = b_number
        if self.b_number == 0:
            self.b_number = 1
            self.a_number = 0


    def add(self, trans_object):
        "The function to add a_number and b_number"
        a_number = self.a_number*trans_object.b_number+trans_object.a_number*self.b_number
        b_number = round(self.b_number*trans_object.b_number)
        return Rational(a_number, b_number)


    def sub(self, trans_object):
        "The function to subtract a_number and b_number"
        a_number = self.a_number*trans_object.b_number-trans_object.a_number*self.b_number
        b_number = round(self.b_number*trans_object.b_number)
        return Rational(a_number, b_number)


    def mult(self, trans_object):
        "The function to multiplication a_number and b_number"
        a_number = self.a_number*trans_object.a_number
        b_number = round(self.b_number*trans_object.b_number)
        return Rational(a_number, b_number)


    def div(self, trans_object):
        "The function to divide a_number and b_number"
        a_number = self.a_number*trans_object.b_number
        b_number = round(self.b_number*trans_object.a_number)
        return Rational(a_number, b_number)


    def get(self):
        "The function to get answer"
        print(round(self.a_number/ gcd(self.a_number, self.b_number)), '/', \
        + round(self.b_number / gcd(self.a_number, self.b_number)), sep="")
