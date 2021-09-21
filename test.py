#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nelder_mead import nelder_mead_optimize

def rosenbrock(x):
    return (1-x[0])**2+100*(x[1]-x[0]**2)**2

print(nelder_mead_optimize(rosenbrock,[0,0]))

#result:
#([1.0009458592568854, 1.0018107252417174], 1.5652129072985298e-06)