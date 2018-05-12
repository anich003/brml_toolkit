import copy
from pyBRML import utils
from pyBRML import Array

def multiply_potentials(list_of_potentials):
    """
    Returns the product of each potential in list_of_potentials, useful for
    calculating joint probabilities.

    For example, if the joint probability of a system is defined as

        p(A,B,C) = p(C|A,B) p(A) p(B)

    then, list_of_potentials should contain 3 potentials corresponding to each factor.

    Since, potentials can be defined in an arbitrary order, each potential will be
    reshaped and cast using numpy ndarray functions before being multiplied, taking
    advantage of numpy's broadcasting functionality.
    """

    # Collect the set of variables from each pot. Used to reshape each potential.table
    variable_set = set(var for potential in list_of_potentials for var in potential.variables)
    variable_set = list(variable_set)

    # Copy potentials to avoid mutating original objects
    potentials = copy.deepcopy(list_of_potentials)

    # Reshape each potential prior to taking their product
    for pot in potentials:
        pot = utils.format_table(pot.variables, pot.table, variable_set)

    # Multiply potentials and return
    new_potential = potentials[0]
    for pot in potentials[1:]:
        new_potential.table = new_potential.table * pot.table

    return new_potential
