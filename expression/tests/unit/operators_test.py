from expression.src.operators import OperatorsBuilder, Schema
from expression.tests.base_test_case import BaseTestCase
from expression.src.exceptions import ParameterNotFound


class OperatorsTest(BaseTestCase):

    def test_operators_can_be_built_from_list(self):

        operators = [
            {
                Schema.NAME: "eq"
            },
            {
                Schema.NAME: "lt"
            },
            {
                Schema.NAME: "in",
                Schema.IS_ARRAY: True
            }
        ]

        subject = OperatorsBuilder(operators).to_operators()
        self.assertEqual(subject.get_operator('eq').name, 'eq')
        self.assertEqual(subject.get_operator('lt').name, 'lt')
        self.assertEqual(subject.get_operator('foo'), None)
        self.assertEqual(subject.get_operator('in').is_array, True)
        self.assertEqual(['eq', 'lt', 'in'], subject.get_operator_names())

def test_exception_thrown_when_operator_name_not_supplied(self):

        operators = [
            {
                Schema.IS_ARRAY: True
            }
        ]

        with self.assertRaises(ParameterNotFound):
            subject = OperatorsBuilder(operators).to_operators()
