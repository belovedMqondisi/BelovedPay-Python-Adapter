
# BelovedPay - Automated Unit Tests
# Adapter Design Pattern Project

import unittest
from decimal import Decimal

from payment_details import PaymentDetails
from payment_adapter import PaymentAdapter


class TestPaymentAdapter(unittest.TestCase):

    def setUp(self):
        self.adapter = PaymentAdapter()

    def test_successful_payment(self):
        payment = PaymentDetails(
            Decimal("100.00"), "PLN", "DEMO-TOKEN-001"
        )
        self.assertTrue(
            self.adapter.process_payment(payment)
        )

    def test_negative_amount(self):
        payment = PaymentDetails(
            Decimal("-50.00"), "PLN", "DEMO-TOKEN-002"
        )
        self.assertFalse(
            self.adapter.process_payment(payment)
        )

    def test_zero_amount(self):
        payment = PaymentDetails(
            Decimal("0.00"), "PLN", "DEMO-TOKEN-003"
        )
        self.assertFalse(
            self.adapter.process_payment(payment)
        )

    def test_unsupported_currency(self):
        payment = PaymentDetails(
            Decimal("75.00"), "USD", "DEMO-TOKEN-004"
        )
        self.assertFalse(
            self.adapter.process_payment(payment)
        )

    def test_invalid_token(self):
        payment = PaymentDetails(
            Decimal("100.00"), "PLN", "INVALID-TOKEN"
        )
        self.assertFalse(
            self.adapter.process_payment(payment)
        )

    def test_payment_conversion(self):
        payment = PaymentDetails(
            Decimal("100.00"), "PLN", "DEMO-TOKEN-005"
        )
        converted = self.adapter.convert_payment_request(
            payment
        )
        self.assertEqual(
            converted["amount_in_grosz"], 10000
        )


if __name__ == "__main__":
    unittest.main()
