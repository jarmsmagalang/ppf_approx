import numpy as np
import mpmath as mp

def lt_fptd(v,D,s,x0,r):
    """
    Computes for the Laplace-transformed FPT distribution

    Parameters
    ----------
    v : Float
        Drift constant.
    D : Float
        Diffusion constant.
    s : Float
        Argument of the Laplace transform.
    x0 : Float
        Initial position. Must be from 0 <= x0 < 1.
    r : Float
        Resetting rate.

    Returns
    -------
    Float
        Laplace-transformed FPT distribution at s.

    """
    def lt_fptd0(v,D,s,x0):
        #Equation 2.22
        
        rho = v/(2*D)
        omega = np.sqrt(v**2 + (4*D*s))
        theta = omega/(2*D)
        
        num1 = mp.exp(-rho*x0)
        num2a = omega*mp.cosh(theta*(x0-1))
        num2b = v*mp.sinh(theta*(x0-1))
        
        den1 = omega*mp.cosh(theta)
        den2 = v*mp.sinh(theta)
        
        return num1*((num2a+num2b)/(den1-den2))
        
    def lt_fptdr(v,D,s,x0,r):
        #Equation 3.1
        num = (s+r)*lt_fptd0(v,D,s+r,x0)
        den = s + r*lt_fptd0(v,D,s+r,x0)
        
        return num/den
    
    if r>0:
        return lt_fptdr(v,D,s,x0,r)
    else:
        return lt_fptd0(v,D,s,x0)