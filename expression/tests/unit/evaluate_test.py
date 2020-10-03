from expression.src.evaluate import Evaluate
from expression.tests.base_test_case import BaseTestCase
from expression.src.exceptions import ParameterNotFound
from datetime import datetime


class DummyConditionHandler():

    def __init__(self, data):
        self._data = data

    def handle(self, condition):

        key = self._data.get(condition.key)
        values = condition.value.split(',')
        operator = condition.operator

        if condition.operator == 'in':
            key = str(key)
            return key in values

        return '{} {} {}'.format(key, operator, values[0])


class DummyDateBetweenHandler():

    def __init__(self, data):
        self._data = data

    def handle(self, condition):

        key = self._data.get(condition.key)
        values = condition.value.split(',')
        operator = condition.operator

        if condition.operator == 'date_between':
            date1 = datetime.strptime(values[0], '%Y-%M-%d')
            date2 = datetime.strptime(values[1], '%Y-%M-%d')

            if date1 <= key <= date2:
                return True

        return False


class EvaluateTest(BaseTestCase):

    def test_can_evaluate_date_between_example(self):

        evaluate = Evaluate(DummyDateBetweenHandler({
            "date": datetime.strptime("2020-09-27", '%Y-%M-%d')
        }))

        result = evaluate.from_expression('date date_between 2020-09-26,2020-09-28')
        self.assertTrue(result)

    def test_can_evaluate_compound_condition(self):

        evaluate = Evaluate(DummyConditionHandler({
            "a": 1,
            "b": 2
        }))
    
        result = evaluate.from_expression('(a == 1 and b == 2)')
        self.assertTrue(result)


    def test_can_evaluate_in(self):

        evaluate = Evaluate(DummyConditionHandler({
            "a": 1,
            "b": 2
        }))
    
        result = evaluate.from_expression('a in 1,8')
        self.assertTrue(result)
