import numpy as np

def mysize(ndarray):
    """Returns the number of dimensions of a numpy ndarray"""
    
    # 1-D vectors are either [1 n] or [n 1]
    dims = ndarray.shape
    if len(dims) == 2 and (dims[0]==1 or dims[1]==1):
       return 1
    else:
        return len(dims) 