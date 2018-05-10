from pyBRML import utils
import pytest
import numpy as np

class TestUtilityFunctions:
    def test_reorder_array_returns_correctly_reordered(self):
        test = np.arange(8).reshape((2,2,2))
        swapped = test.swapaxes(2,1)
        reordered = utils.reorder_table([0,2,1],swapped)
        assert np.all(np.isclose(test,reordered))

    def test_reorder_array_returns_correctly_reordered_2(self):
        test = np.arange(81).reshape((3,3,3,3))
        swaps = [(0,1),(3,0),(1,2)]
        order = [3,2,0,1]
        swapped = test.copy()
        for swap in swaps:
           swapped = swapped.swapaxes(swap[0],swap[1])
        reordered = utils.reorder_table([3,2,0,1],swapped)
        assert np.all(np.isclose(test,reordered))

    def test_reshape_table_returns_copy_of_original(self):
        table = np.array([[1,2],[3,4]])
        new_table = utils.reshape_table([],table)
        assert table is not new_table

    def test_reshape_table_returns_correct_dimensions_all_dims_present(self):
        variable_idxs  = [3,2,0,1] # order of table
        num_states     = (4,2,2,3) # shape of table
        correct_states = (2,3,2,4)
        table          = np.random.rand(*num_states)
        new_table      = utils.reshape_table(variable_idxs, table)

        assert correct_states  == new_table.shape, 'Returned table is not correct shape'

    def test_reshape_table_returns_correct_dimensions_all_dims_present_2(self):
        variable_idxs  = [0,2,1] # order of table
        num_states     = (5,2,3) # shape of table
        correct_states = (5,3,2)
        table          = np.random.rand(*num_states)
        new_table      = utils.reshape_table(variable_idxs, table)

        assert correct_states  == new_table.shape, 'Returned table is not correct shape'

    def test_reshape_table_returns_correct_dimensions_single_dim_present(self):
        variable_idxs  = [2]
        num_states     = (3,)
        correct_states = (1,1,3)
        table          = np.random.rand(*num_states)
        new_table      = utils.reshape_table(variable_idxs, table)

        assert correct_states == new_table.shape, 'Returned table is not correct shape'
