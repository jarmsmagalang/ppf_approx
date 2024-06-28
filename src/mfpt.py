import mpmath as mp
from .lt_fptd import lt_fptd   

def mfpt(v, D, x0, r):
    """
    Computes for the analytical mean FPT from the Laplace-transformed FPT distribution

    Parameters
    ----------
    v : Float
        Drift constant.
    D : Float
        Diffusion constant.
    x0 : Float
        Initial position. Must be from 0 <= x0 < 1.
    r : Float
        Resetting rate.

    Returns
    -------
    Float
        Analytical mean first passage time.

    """
    lt_fpt = lambda s: lt_fptd(v, D, s, x0, r)
    mfpt = float(-mp.diff(lt_fpt, 0))
    return mfpt