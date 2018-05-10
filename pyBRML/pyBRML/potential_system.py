from pyBRML import Variable

class PotentialSystem:
    def __init__(self):
        self.variables = []
        self.potentials = []

    def add_variable(self, name, domain):
        new_var = Variable(name, domain)
        self.variables.append(new_var)

    def add_potential(self,potential):
        """potentials should be of the form:
        {
            variables: [3,1,2]
                table: [[[1,2],[3,4]],
                        [[5,6],[7,8]]]
        }
        where
            table is an numpy ndarray and
            variables is a list of ints
        """
        self.potentials.append(potential)
