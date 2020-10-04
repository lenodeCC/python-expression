from expression.src.handler import EqualsHandler
from expression.src.condition import Condition
from expression.tests.base_test_case import BaseTestCase


class HandlerTest(BaseTestCase):

    def test_equals_handler(self):

        handler = EqualsHandler({'a': 1})
        result = handler.handle(Condition('a', '=', 1))
        self.assertTrue(result)

        handler = EqualsHandler()
        result = handler.handle(Condition('a', '=', 1))
        self.assertFalse(result)

        handler = EqualsHandler()
        result = handler.handle(Condition('a', '>', 1))
        self.assertIsNone(result)

        handler = EqualsHandler({
            'a': 2
        })
        result = handler.handle(Condition('a', '=', 1))
        self.assertFalse(result)