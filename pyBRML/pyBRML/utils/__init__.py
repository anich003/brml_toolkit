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

def format_table(variable_idxs, table, var_set=None):
    """
    Returns a copy of table that is re-ordered by sorting variable_idxs and projecting
    the table into the appropriate dimension as defined by var_set or variable_idxs.

    For example:
        >>> pot = pyBRML.Array([3,2,0,1], [...data...])
        >>> ordered_table = format_table(pot.variable_idxs, pot.table)

    This method utilizes numpy's transpose functionality, to achieve the reordering
    of table indices. A good example of when this is useful is when dealing with
    image data that is provided in a different  order. For example, some OpenCV io
    utilities return images whose dimensions correspond to (B,G,R). One could simply
    call np.transpose(2,1,0) to reorder the same data as (R,G,B). In the context of pyBRML,
    this allows the user of the library to specify conditional probability tables in
    arbitrary order and ensures that the data corresponding to specific variables are
    aligned during arithmetic operations like multiplication.
    """
    # 1. Sort existing table
    old = variable_idxs
    sorted_idx = sorted(variable_idxs)
    #   Determine where in the old order the now sorted index is
    transpose_order = [old.index(n) for n in sorted_idx]
    new_table = table.copy().transpose(*transpose_order)

    # 2. Generate complete variable list
    max_var = max(var_set) if var_set else max(variable_idxs)
    new_idxs = np.arange(max_var+1, dtype=np.int)

    # 3. Expand table to match complete variable list
    for idx in new_idxs:
        if idx not in old:
            new_table = np.expand_dims(new_table,idx)

    return new_table
