import numpy as np
import copy
#from pyBRML import Array

def mysize(ndarray):
    """Returns the number of dimensions of a numpy ndarray"""

    # 1-D vectors are either [1 n] or [n 1]
    dims = ndarray.shape
    if len(dims) == 2 and (dims[0]==1 or dims[1]==1):
       return 1
    else:
        return len(dims)

def reorder_table(variable_idxs, table):
    """
    Returns a copy of table that is re-ordered by sorting variable_idxs

    For example:
        >>> pot = pyBRML.Array([3,2,0,1], [...data...])
        >>> ordered_table = reorder_table(pot.variable_idxs, pot.table)

    This method utilizes numpy's transpose functionality. A good example of when
    this is useful is when dealing with image data that is provided in a different
    order. For example, some OpenCV io utilities return images whose dimensions
    correspond to (B,G,R). One could simply call np.transpose(2,1,0) to reorder
    the same data as (R,G,B).
    """
    old = variable_idxs
    new = sorted(variable_idxs)
    # Determine where in the old order the now sorted index is
    transpose_order = [old.index(n) for n in new]
    new_table = table.copy().transpose(*transpose_order)
    return new_table

def reshape_table(variable_idxs, table):
    """
    Returns a copy of table, projected into the dimensions specified in variable
    """
    new_table = reorder_table(variable_idxs,copy.deepcopy(table))
    return new_table
