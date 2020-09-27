class EmptyCondition(Exception):
    pass


class Condition():

    def __init__(self, key, operator = None, value = None):
        self.key = key
        self.operator = operator
        self.value = value


class ConditionSerializer():

    def serialize(self, condition):
        if condition.operator is None or condition.value is None:
            return '{}'.format(
                condition.key
            )

        return '{} {} {}'.format(
            condition.key, 
            condition.operator, 
            condition.value
        )

    def deserialize(self, condition):
        condition = condition.strip()

        if not condition:
            raise EmptyCondition

        parts = condition.split(' ')
            
        if len(parts) < 3: 
            return Condition(parts[0])

        return Condition(parts[0], parts[1], ' '.join(parts[2:]))
