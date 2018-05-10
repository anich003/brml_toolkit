"""
Adapted from David Barber BRML Toolkit

Author: Aaron Nichols
Date: 04/12/2018
"""

import numpy as np
from pyBRML import utils

# class Array(Potential):
class Array:
    """ Python implementation of BRML Array class using numpy"""

    def __init__(self, variable_idxs, table, description=None):
        """
        Args:
            variable_idxs: list of integers, indicating the variable each value
                corresponds to
            table: a numpy ndarray of values, where table.ndim is equal to the
                number of variables encoded by the table
            description: a short string describing what this potential encodes.
                For example:
                   p(C|B,A)
                   p(knife|butler,maid)
                   p(radio|earthquake)

        Returns:
            A data structure containing the array of potentials, variable
            indexes and a description of the potential

        Raises:
            ValueError: if len(variables) does not equal np.shape(table)[0]
        """
        if not isinstance(variable_idxs, list):
            raise ValueError("variable_idxs must by of type list")
        np_table = np.asarray(table)
        if len(variable_idxs) != utils.mysize(np_table):
            raise ValueError("number of declared variables does not match size of table")

        self.variables = variable_idxs
        self.table = np_table
        self.description = description
