from expression.src.condition import Condition, Conjunction
from expression.src.expression import Expression


class Evaluate():

    def __init__(self, data = {}):
        self._data = data
        self._condition_handlers = []

    def add_condition_handler(self, condition_handler):
        self._condition_handlers.append(condition_handler)

    def from_expression(self, expression):
        conditions = Expression(expression).to_conditions()

        return self.from_conditions(conditions.conditions)

    def from_conditions(self, conditions):
        return eval(self._resolve_conditions(conditions))

    def _resolve_conditions(self, conditions):
        store = ''
        for condition in conditions:

            if isinstance(condition, list):
                store += '({})'.format(self._resolve_conditions(condition))
            elif isinstance(condition, Condition):
                store += '{}'.format(self._resolve_condition(condition))
            elif isinstance(condition, Conjunction):
                store += ' {} '.format(condition.value)

        return store

    def _resolve_condition(self, condition):

        for handler in self._condition_handlers:
            result = handler(self._data).handle(condition)

            if result is None:
                continue
            else:
                return result

        return False
