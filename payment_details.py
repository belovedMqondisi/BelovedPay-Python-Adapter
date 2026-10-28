
# BelovedPay - Adapter Design Pattern Project
# Module: Payment Details
# Purpose: Store payment information used by the application.

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class PaymentDetails:
    """
    Represents a payment request in BelovedPay.
    """

    amount: Decimal
    currency: str
    payment_token: str

    def is_valid(self):
        """Check whether payment details are valid."""

        if self.amount <= 0:
            return False

        if self.currency not in ("PLN", "USD", "EUR"):
            return False

        if not self.payment_token.strip():
            return False

        return True
