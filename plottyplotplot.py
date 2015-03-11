# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:37:11 2015

@author: Manash
"""

import pylab

principal = 10000
interestRate = 0.05
years = 20

values = []

for i in range(years + 1):
    values.append(principal)
    principal += principal * interestRate

pylab.title('5% Growth, Compounded Annually')
pylab.xlabel('Years of compunding')
pylab.ylabel('Value of Principal ($)')

pylab.plot(range(years + 1), values)
pylab.show()
