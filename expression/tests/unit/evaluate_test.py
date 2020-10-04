from expression.src.handler import EqualsHandler, InHandler, DateBetweenHandler
from expression.src.evaluate import Evaluate, NoHandlerFound
from expression.tests.base_test_case import BaseTestCase
from datetime import datetime


class EvaluateTest(BaseTestCase):

    def test_can_evaluate_date_between_example(self):

        evaluate = Evaluate({
            "date": datetime.strptime("2020-09-27", '%Y-%M-%d')
        })
        evaluate.add_condition_handlers({
            'date_between': DateBetweenHandler
        })
        result = evaluate.from_expression('date date_between 2020-09-26,2020-09-28')
        self.assertTrue(result)

    def test_can_evaluate_compound_condition(self):

        evaluate = Evaluate({
            "a": 1,
            "b": 2
        })
        evaluate.add_condition_handlers({
            '==': EqualsHandler
        })

        result = evaluate.from_expression('(a == 1 and b == 2)')
        self.assertTrue(result)

    def test_can_evaluate_nested_compound_condition(self):

        evaluate = Evaluate({
            "a": 1,
            "b": 2,
            "c": 3
        })
        evaluate.add_condition_handlers({
            '==': EqualsHandler
        })

        result = evaluate.from_expression('(a == 1 and (b == 2 or c == 3))')
        self.assertTrue(result)

    def test_can_evaluate_in(self):

        evaluate = Evaluate({
            "a": 1,
            "b": 2
        })
        evaluate.add_condition_handlers({
            'in': InHandler
        })

        result = evaluate.from_expression('a in 1,8')
        self.assertTrue(result)

    def test_exception_thrown_when_there_is_no_handler(self):

        evaluate = Evaluate()
        with self.assertRaises(NoHandlerFound):
            evaluate.from_expression('a foo b')
