#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Vector():
    def __init__(self,vector):
        self.vector=vector
        self.dim=len(vector)
        self.norm=sum([x**2 for x in self.vector])**(0.5)
    
    def __add__(self,other):
        return Vector([self.vector[i]+other.vector[i] for i in range(min(self.dim,other.dim))])
    
    def __sub__(self,other):
        return Vector([self.vector[i]-other.vector[i] for i in range(min(self.dim,other.dim))])
    
    def __mul__(self,other):
        return Vector([self.vector[i]*other for i in range(self.dim)])
    
    def __truediv__(self,other):
        return Vector([self.vector[i]/other for i in range(self.dim)])
    
    def __getitem__(self,key):
        return self.vector[key]
    
    def __setitem__(self,key,new_number):
        output=self.vector
        output[key]=new_number
        return Vector(output)
    
    def copy(self):
        return Vector(self.vector.copy())


def nelder_mead_optimize(f,x0,init_step=0.025,step_coeff=1.025,
                         x_err=1e-5,y_err=1e-5,max_iter=5000,
                         alpha=1,gamma=2,rho=0.5,sigma=0.5):
    
    # f: function to be optimized, it must return a scalar
    # x0: initial guess
    # init_step & step_coeff: can be changed if necessary, 
    #   but init_step has to be >0 and step_coeff has to be >1
    # x_err: when the error of result point <= x_err, iteration stops and returns result
    # f_err: when the error of function value <= f_err, iteration stops and returns result
    # max_iter: the maximum number of times of iteration is to be excuted
    # alpha, gamma, rho, sigma are some default prameters, please change them carefully if necessary,
    #   you can get detailed information about these parameters at "https://en.wikipedia.org/wiki/Nelder–Mead_method"

    #initialization
    iter_num=0
    x_init=Vector(x0)
    dim=x_init.dim
    y_init=f(x_init.vector)
    iter_num+=1
    pond=[(x_init,y_init)]

    for i in range(dim):
        x_temp=x_init.copy()
        if x_temp[i]==0:
            x_temp[i]=init_step
        else:
            x_temp[i]*=step_coeff
        y_temp=f(x_temp.vector)
        iter_num+=1
        pond.append((x_temp,y_temp))

    x_error,y_error=10*x_err,10*y_err
    while iter_num<=max_iter and x_error>x_err and y_error>y_err:
        #order
        pond.sort(key=lambda x: x[1])

        #average point, noted as x_m or x_o
        x_m=Vector([0]*dim)
        for i in range(dim):
            x_m+=pond[i][0]
        x_m/=dim

        #reflection point, noted as x_r
        #pond[-1][0] is the worst point
        x_r=x_m+(x_m-pond[-1][0])*alpha
        y_r=f(x_r.vector)

        if pond[0][-1]<=y_r and y_r<pond[-2][-1]:
            pond[-1]=(x_r,y_r)
            continue
        elif y_r<pond[0][-1]:
            #expanded point, noted as x_e or x_s
            x_s=x_m+(x_m-pond[-1][0])*gamma*alpha
            y_s=f(x_s.vector)
            iter_num+=1
            if y_s<y_r:
                pond[-1]=(x_s,y_s)
            else:
                pond[-1]=(x_r,y_r)
            continue
        elif pond[-2][-1]<=y_r and y_r<pond[-1][-1]:
            #contraction point
            x_c1=x_m+(x_r-x_m)*rho
            y_c1=f(x_c1.vector)
            iter_num+=1
            if y_c1<y_r:
                pond[-1]=(x_c1,y_c1)
                continue
            else:
                #shrink
                for i in range(1,dim+1):
                    x_temp=pond[0][0]+(pond[i][0]-pond[0][0])*sigma
                    y_temp=f(x_temp.vector)
                    iter_num+=1
                    pond[i]=(x_temp,y_temp)
        elif pond[-1][-1]<=y_r:
            x_c2=x_m+(pond[-1][0]-x_m)*sigma
            y_c2=f(x_c2.vector)
            iter_num+=1
            if y_c2<pond[-1][-1]:
                pond[-1]=(x_c2,y_c2)
            else:
                #shrink
                for i in range(1,dim+1):
                    x_temp=pond[0][0]+(pond[i][0]-pond[0][0])*sigma
                    y_temp=f(x_temp.vector)
                    iter_num+=1
                    pond[i]=(x_temp,y_temp)
        
        x_error=(pond[0][0]-pond[-1][0]).norm
        y_error=abs(pond[0][-1]-pond[-1][-1])
    
    optimized_result=(pond[0][0].vector,pond[0][1])
    return optimized_result


    



