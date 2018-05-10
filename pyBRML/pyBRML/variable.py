
class Variable:
    def __init__(self, name, domain=None, probs=None):
        self.name = name
        if domain and isinstance(domain,list):
            for i,state in enumerate(domain):
                self.__setattr__(str(state),i)
        else:
            # If no domain provided, assumes Variable is binary
            self.false = 0
            self.true  = 1
        if probs:
            # Normalize so that sum(probs) = 1
            total = sum(probs)
            norm_probs = [p / total for p in probs]
            self.probs = norm_probs

    def __getitem__(self,arg):
        return self.__getattribute__(arg)

    def __str__(self):
        return f'{self.name} = {self.domain}'
