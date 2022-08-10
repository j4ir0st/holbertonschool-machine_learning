#!/usr/bin/env python3
"""
Creating Normal class
"""


def fact(f):
    """ Factorial function """
    fact = 1
    for times in range(2, f + 1):
        fact = fact * times
    return fact


class Normal:
    """ Represents a normal distribution """
    def __init__(self, data=None, mean=0., stddev=1.):
        self.e = 2.7182818285
        if data is None:
            if stddev <= 0:
                raise ValueError('stddev must be a positive value')
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.mean = float(sum(data) / len(data))
            dif_2 = [(elem - self.mean) ** 2 for elem in data]
            sum_dif2 = 0
            for elem in dif_2:
                sum_dif2 += elem
            self.stddev = (sum_dif2 / len(data)) ** 0.5

    def pdf(self, x):
        """ Calculates the value of PDF for a given number of “successes” """
        if x < 0:
            return 0
        p = (self.e**(-self.lambtha * x) * (self.lambtha))
        return p

    def cdf(self, x):
        """ Calculates the value of CDF for a given number of “successes” """
        if x < 0:
            return 0
        cdf = 1 - (self.e ** (-self.lambtha * x))
        return cdf
