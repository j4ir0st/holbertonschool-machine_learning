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

pi = 3.1415926536

def erf(x):
    """Error function"""
    fact = x - (x ** 3) / 3 + (x ** 5) / 10 - (x ** 7) / 42 + (x ** 9) / 216
    errf = (2 / (pi ** (0.5))) * fact
    return errf

class Normal:
    """ Represents a normal distribution """
    def __init__(self, data=None, mean=0., stddev=1.):
        self.e = 2.7182818285
        self.pi = 3.1415926536
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

    def z_score(self, x):
        """ Calculates the z-score of a given x-value """
        z = (x - self.mean) / self.stddev
        return z

    def x_value(self, z):
        """ Calculates the x-value of a given z-score """
        x = (z * self.stddev) + self.mean
        return x

    def pdf(self, x):
        """ Calculates the value of PDF for a given number of “successes” """
        dev = (((2 * self.pi) ** 0.5) * self.stddev) ** (-1)
        exp = (-(x - self.mean) ** 2) / (2 * (self.stddev ** 2))
        p = dev * (self.e ** exp)
        return p

    def cdf(self, x):
        """ Calculates the value of CDF for a given number of “successes” """
        cdf = 0.5 * (1 + erf((x - self.mean) / (self.stddev * (2 ** 0.5))))
        return cdf
