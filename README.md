# nelder-mead-optimization
A simple python implementation of nelder mead algorithm without any packages.

## A simple introduction to nelder-mead
Nelder-mead is a commonly used optimization algorithm in many areas. It's used to search for the loacal minimum of the multivariate function.
It has many advantages, such that it's simple, it doesn't need gradient information, its principle is not difficult to be understood, etc... .
But one of its biggest disadvantages is the slow convergence speed under some circumstances.

You can get the basic procedure of nelder mead at https://en.wikipedia.org/wiki/Nelder–Mead_method

## Installation
It's okay to just copy "nelder_mead.py" file to your computer.

## Usage
The basic function is "nelder_mead_optimize".

Here is a demonstration.
```python
from nelder_mead import nelder_mead_optimize

def rosenbrock(x):
    return (1-x[0])**2+100*(x[1]-x[0]**2)**2

print(nelder_mead_optimize(rosenbrock,[0,0]))
```
Output:
```
([1.0009458592568854, 1.0018107252417174], 1.5652129072985298e-06)
```

In this simple case, just two parameters are needed, the first is the function to be optimized, the second is the initial guess.
Function to be optimized must accept a list, and return a scalar. Initial guess should be a list.

The optimization result are shown in the form of (min_value_point,min_value).

## More details about nelder_mead_optimize function
There are many parameters that nelder_mead_optimize function needs, but most of them are set default.
Here is the complete input of nelder_mead_optimize
```python
nelder_mead_optimize(f,x0,init_step=0.025,step_coeff=1.025,
                         x_err=1e-5,y_err=1e-5,max_iter=5000,
                         alpha=1,gamma=2,rho=0.5,sigma=0.5)
```

Let's see what these stand for.

- f: function to be optimized
- x0: initial guess
- init_step: can be changed if necessary, when x0[i]=0, the predicted point x_p[i]=init_step
- step_coeff: can be changed if necessary, when x0[i]!=0, the predicted point x_p[i]=x0[i]*step_coeff
- x_err: when the error of result point <= x_err, iteration stops and returns result
- f_err: when the error of function value <= f_err, iteration stops and returns result
- max_iter: the maximum number of times of iteration is to be excuted
- alpha, gamma, rho, sigma are some default prameters, please change them carefully if necessary, you can get detailed information about these parameters at   https://en.wikipedia.org/wiki/Nelder–Mead_method

Here are some advices
- If you think the best point is far from the initial guess, you can set init_step and step_coeff to a larger number.
- Although max_iter can be set at your will, it's recommended to set max_iter to 200*len(x0)
