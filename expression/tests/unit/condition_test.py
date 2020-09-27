from expression.src.condition import Condition, ConditionSerializer
from expression.src.operators import OperatorsBuilder
from expression.tests.base_test_case import BaseTestCase


class ConditionTest(BaseTestCase):

    def test_serializer_deserializes_basic_condition(self):

        subject = ConditionSerializer().deserialize('a = b')

        self.assertEqual('a', subject.key)
        self.assertEqual('=', subject.operator)
        self.assertEqual('b', subject.value)

    def test_serializer_deserializes_without_operator_value(self):

        subject = ConditionSerializer().deserialize('a')

        self.assertEqual('a', subject.key)
        self.assertEqual(None, subject.operator)
        self.assertEqual(None, subject.value)

    def test_serializer_deserializes_and_keeps_value_intact(self):

        subject = ConditionSerializer().deserialize('a = b,c,d,e')

        self.assertEqual('a', subject.key)
        self.assertEqual('=', subject.operator)
        self.assertEqual('b,c,d,e', subject.value)

        subject = ConditionSerializer().deserialize('a = b, c, d, e')

        self.assertEqual('a', subject.key)
        self.assertEqual('=', subject.operator)
        self.assertEqual('b, c, d, e', subject.value)

    def test_serializer_serializes_and_keeps_value_intact(self):

        condition = Condition('a')
        subject = ConditionSerializer().serialize(condition)

        self.assertEqual('a', subject)

        condition = Condition('a', '=', 'b')
        subject = ConditionSerializer().serialize(condition)

        self.assertEqual('a = b', subject)