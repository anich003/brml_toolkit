import pytest
from pyBRML import Array

class TestArray:
    def test_create_array_with_list(self):
        arr = Array([1,2],[[1,2,3],[4,5,6]])

    def test_create_Array_with_ndarray(self):
        import numpy as np
        Array([1,2], np.random.rand(2,2))

    def test_raises_an_exception_if_variable_idxs_not_list(self):
        with pytest.raises(ValueError):
            Array(1,[0.2, 0.8])

    def test_variable_len_does_not_match_table_dim_raises_exception(self):
        with pytest.raises(ValueError):
            Array([0], [[1,2],[3,4]])

    def test_variable_len_does_not_match_table_dim_raises_exception_2(self):
        with pytest.raises(ValueError):
            Array([0,1],[3,5])

    @pytest.mark.skip(reason='not implemented yet')
    def test_raise_exception_if_table_not_numeric(self):
        raise NotImplementedError


