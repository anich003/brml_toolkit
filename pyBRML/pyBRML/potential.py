"""
Adapted from David Barber BRML Toolkit

Author: Aaron Nichols
Date: 04/12/2018
"""
import abc

class Potential:
    """
    Base class inherited by pybrml.array and pybrml.const
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self,variables,table):
        self.variables = variables
        self.table = table
