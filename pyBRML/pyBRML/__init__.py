import copy
from .array import Array
from .variable import Variable

def multiply_potentials(list_of_potentials):
    """
    Returns the product of each potential in list_of_potentials, useful for
    calculating joint probabilities. For example, if the joint probability of a system
    is defined as
        p(A,B,C) = p(C|A,B) p(A) p(B)
    then, list_of_potentials should contain 3 potentials corresponding to each factor.
    Since, potentials can be defined in an arbitrary order, each potential will be
    reshaped and cast using numpy ndarray functions before being multiplied, taking
    advantage of numpy's broadcasting functionality.
    """

    # Collect the set of variables from each pot. Used to reshape each potential.table
    variables = set(var for potential in list_of_potentials for var in potential.variables)

    # Copy potentials to avoid mutating original objects
    pots = copy.deepcopy(list_of_potentials)

    # Reshape each potential prior to taking their product
