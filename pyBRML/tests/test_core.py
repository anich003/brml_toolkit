from pyBRML import Array, utils
import pyBRML as brml
import numpy as np

class TestPyBRMLCore:
    def test_multiply_potentials(self):
        knife_index = [0,2,1]
        knife_table = np.zeros((2,2,2))
        knife_table[1,0,0] = 0.0
        knife_table[1,1,0] = 0.04
        knife_table[1,0,1] = 0.64
        knife_table[1,1,1] = 0.0
        knife_table[0,:,:] = 1 - knife_table[1,:,:]
        knife = Array(knife_index, knife_table)
        butler = Array([2],[0.4,0.6])
        maid = Array([1],[0.2,0.8])
        potentials = [knife,butler,maid]

        joint = brml.multiply_potentials(potentials).table

        correct_prob = 0.9897
        num = joint[1,:,1].sum()
        den = joint[1,:,:].sum()
        prob = num / den
        print(prob)
        assert np.isclose(correct_prob, prob)
