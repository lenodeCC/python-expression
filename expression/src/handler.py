class Handler():

    def __init__(self, data = {}):
        self._data = data

    def handle(self, condition):
        pass


class EqualsHandler(Handler):

    def handle(self, condition):

        key = self._data.get(condition.key)
        key = key if key else condition.key

        if condition.operator in ['eq', '==', '=']:
            return key == condition.value

        return None
