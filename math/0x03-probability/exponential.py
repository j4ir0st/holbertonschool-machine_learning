#!/usr/bin/env python3
"""
Creating Exponential class
"""


def fact(f):
    """ Factorial function """
    fact = 1
    for times in range(2, f + 1):
        fact = fact * times
    return fact


class Exponential:
    """ Represents a exponential distribution """
    def __init__(self, data=None, lambtha=1.):
        self.e = 2.7182818285
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            acum = 0
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            for elem in data:
                acum += elem
            self.lambtha = float(len(data) / acum)

    def pmf(self, k):
        """ Calculates the value of PMF for a given number of “successes” """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        p = (self.e**(-self.lambtha) * (self.lambtha ** k)) / Poisson.fact(k)
        return p

    def cdf(self, k):
        """ Calculates the value of CDF for a given number of “successes” """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        cdf = 0
        for a in range(k + 1):
            cdf += (self.e ** (-self.lambtha) * (self.lambtha ** a)) / fact(a)
        return cdf
