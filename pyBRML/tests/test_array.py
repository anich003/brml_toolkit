import pytest
import pyBRML as brml

class TestArray:
    def test_create_array_with_list(self):
        arr = brml.Array(['knife','butler'],[[1,2,3],[4,5,6]])
        assert arr.variables[0] == 'knife'
        assert arr.variables[1] == 'butler'
    
    def test_create_Array_with_ndarray(self):
        import numpy as np
        brml.Array(['knife','butler'], np.random.rand(2,2))

    def test_variable_len_does_not_match_table_dim_raises_exception(self):
        with pytest.raises(ValueError):
            brml.Array(['knife'], [[1,2],[3,4]])

    def test_variable_len_does_not_match_table_dim_raises_exception_2(self):
        with pytest.raises(ValueError):
            brml.Array(['knife','butler'],[3,5])

    def test_raise_exception_if_table_not_numeric(self):
        raise NotImplementedError
    
    