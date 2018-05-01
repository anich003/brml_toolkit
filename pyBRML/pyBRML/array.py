"""
Adapted from David Barber BRML Toolkit

Author: Aaron Nichols
Date: 04/12/2018
"""
import numpy as np
from .potential import Potential

# class Array(Potential):
class Array:
    """ Python implementation of BRML Array class using numpy
    """
    def __init__(self, variables, table):
        """
        Args:
            variables: A list of variable identifies, usually (int) or (string)
            table: a numpy ndarray of values, where dim=1 is equal to the number of variables
        
        Returns:
            A data structure housing the array of potentials and name information
        
        Raises:
            ValueError: if len(variables) does not equal np.shape(table)[0]
        """
        if not isinstance(variables, list):
            raise ValueError("variables must by of type list")
        self.variables = variables

        # TODO check validity of table
        # Cast to numpy 
        self.table = np.asarray(table)
