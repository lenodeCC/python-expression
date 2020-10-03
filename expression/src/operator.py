from expression.src.exceptions import ParameterNotFound


class Schema():
    NAME = 'name'
    IS_ARRAY = 'is_array'


class Operator():

    def __init__(self, name, is_array = False):
        self.name = name
        self.is_array = is_array


class OperatorBuilder():

    def __init__(self, parameters):
        self.parameters = self._resolve_parameters(parameters)

    def _resolve_parameters(self, parameters):
        if Schema.NAME not in parameters:
            raise ParameterNotFound

        if Schema.IS_ARRAY not in parameters:
            parameters[Schema.IS_ARRAY] = False

        return parameters

    def to_operator(self):
        return Operator(
            self.parameters[Schema.NAME],
            self.parameters[Schema.IS_ARRAY]
        )


class Operators():

    def __init__(self, operators):
        self.operators = operators

    def get_operator(self, name):
        if name in self.operators:
            return self.operators[name]

        return None

    def get_operator_names(self):
        return list(self.operators.keys())


class OperatorsBuilder():

    def __init__(self, operators):
        self.operators = operators

    def to_operators(self):
        operators = {}
        for operator in self.operators:
            operator = OperatorBuilder(operator).to_operator()
            operators[operator.name] = operator
        
        return Operators(operators)
