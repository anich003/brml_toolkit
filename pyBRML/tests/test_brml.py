import pytest
import pyBRML as brml

class TestPyBRML:
    def test_create_array_with_list(self):
        arr = brml.Array(['knife','butler'],[[1,2,3],[4,5,6]])
        assert arr.variables[0] == 'knife'
        assert arr.variables[1] == 'butler'
    
    def test_create_Array_with_ndarray(self):
        import numpy as np
        brml.Array(['knife','butler'], np.random.rand(2,2))
