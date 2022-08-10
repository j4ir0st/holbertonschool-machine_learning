#!/usr/bin/env python3
"""
Creating Poisson class
"""


class Poisson:
    """ Represents a poisson distribution """
    def __init__(self, data=None, lambtha=1.):
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
            self.lambtha = float(acum / len(data))


    def pmf(self, k):
        """ Calculates the value of PMF for a given number of “successes” """
        if type(k) is not int:
            k = int(k)
            if k < 0:
                return 0
            fact = 1
            for times in range(2, k + 1):
                fact = fact * times
            pmf = (self.e**(-self.lambtha) * (self.lambtha ** k)) / fact
            return pmf
