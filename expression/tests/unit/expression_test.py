from expression.src.expression import Expression
from expression.tests.base_test_case import BaseTestCase


class ExpressionTest(BaseTestCase):

    def test_expression_resolves_condition(self):

        expression = Expression('(a = 1)')
        conditions = expression.to_conditions()

        self.assertEqual('a', conditions.conditions[0].key)
        self.assertEqual('=', conditions.conditions[0].operator)
        self.assertEqual('1', conditions.conditions[0].value)

    def test_expression_resolves_compound_condition(self):

        expression = Expression('(a = 1 and b = 2)')
        conditions = expression.to_conditions()

        self.assertEqual('and', conditions.conditions[1].value)

        self.assertEqual('b', conditions.conditions[2].key)
        self.assertEqual('=', conditions.conditions[2].operator)
        self.assertEqual('2', conditions.conditions[2].value)

    def test_expression_resolves_nested_compound_condition(self):

        expression = Expression('(a = 1 or (b = 2 and c = 3))')
        conditions = expression.to_conditions()

        self.assertEqual('or', conditions.conditions[1].value)

        self.assertEqual('c', conditions.conditions[2][2].key)
        self.assertEqual('=', conditions.conditions[2][2].operator)
        self.assertEqual('3', conditions.conditions[2][2].value)
