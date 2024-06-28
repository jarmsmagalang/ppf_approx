# Pade-Partial Fraction Approximation

This package is an implementation of the Pade-partial fraction approximation for the inversion of the Laplace transform as proposed in [Computation of the Distribution of the Absorption Time of the Drifted Diffusion with Stochastic Resetting and Mixed Boundary Conditions](https://arxiv.org/abs/2311.03939) by Turin, Magalang, Aguilar, Colombani, Sanchez-Taltavull, and Gatto[^1]

# Installation

Install the package from PyPI:
```
pip install ppf_approx
```
# Usage
The main function of this package is the `ppf` function, with the following syntax:
```
ppf(m_ord, n_ord, v, D, x0, r, tval, correction = True)
```
Here is a description of each argument:
- `m_ord` : Integer. Numerator order of the Pade approximation.
- `n_ord` : Integer. Denominator order of the Pade approximation.
- `v` : Float. Drift constant.
- `D` : Float. Diffusion constant. Must be positive.
- `x0` : Float. Initial position. Must be from $0 \leq x_0 < 1$
- `r` : Float. Resetting constant. Must be non-negative.
- `tval` : Array. Range of time values at which the PPF will be performed. Single values are accepted.
- `correction` : Boolean, optional. Determines whether the PPF will perform the correction steps or not. The default is True.

The function can be used to generate whole distributions $t \in [0, \infty]$, segments $t \in [t_1, t_2]$, or single values of time $t$. The outputs will always be in arrays. This is an example of the usage of the `ppf` function:

```
import numpy as np
import ppf_approx

v = -0.01
D = 0.0001
x0 = 0.8
r = (1/3)*(1/365)
tvals = np.linspace(0,200, 10)

app_fptvals = ppf(2, 3, v, D, x0, r, tvals)
```
Sample output:
```
>>> app_fptvals
array([0., 0., 0.01115898, 0.01866108, 0.01345554, 0.00637309, 0.00200653, 0.00027748, 0., 0.])
```

## Auxiliary Functions

This package also contains auxiliary functions which are expressions for the bounded and biased Brownian motion with stochastic resetting that were derived in the reference[^1]:
1. `lt_fptd` computes for the Laplace-transformed FPT distribution.
2. `mfpt` computes for the analytical mean FPT from the Laplace-transformed FPT distribution.

[^1]: Turin, R., Magalang, J., Aguilar, J., Colombani, L., Sanchez-Taltavull, D., & Gatto, R. (2024).  _Computation of the distribution of the absorption time of the drifted diffusion with stochastic resetting and mixed boundary conditions_  (arXiv:2311.03939). arXiv. https://doi.org/10.48550/arXiv.2311.03939
> Written with [StackEdit](https://stackedit.io/).
