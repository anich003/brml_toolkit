import pytest
import pyBRML as brml

class Test_Variable:
    def test_instantiate_variable(self):
        butler = brml.Variable('butler',['not_murderer','murderer'])

    def test_instantiate_variable_2(self):
        butler = brml.Variable('butler',[0,1])

    def test_instantiate_variable_without_domain(self):
        knife = brml.Variable('knife')

    def test_access_attribues_on_variable(self):
        butler = brml.Variable('butler',['not_murderer','murderer'])
        assert butler.not_murderer    == 0
        assert butler['not_murderer'] == 0
        assert butler.murderer  == 1
        assert butler['murderer'] == 1

    def test_default_binary_state_if_no_domain(self):
        binary = brml.Variable('binary')
        assert binary.true  == 1
        assert binary.false == 0

    def test_raises_error_if_state_does_not_exist(self):
        butler = brml.Variable('butler',['murderer','not_murderer'])
        with pytest.raises(AttributeError):
            butler['is_handsome']

    def test_instantiate_with_probabilities(self):
        butler = brml.Variable('butler',['not_murderer','murderer'], [0.2, 0.8])
