
# BelovedPay - Adapter Design Pattern
# Module: Payment Adapter
# Connects BelovedPay to an external payment gateway

from abc import ABC, abstractmethod
from decimal import Decimal

from payment_details import PaymentDetails
from external_gateway import ExternalPaymentGateway


# Interface expected by the BelovedPay application
class IPaymentAdapter(ABC):

    @abstractmethod
    def process_payment(self, payment: PaymentDetails) -> bool:
        pass


# Adapter implementation
class PaymentAdapter(IPaymentAdapter):

    def __init__(self):
        self.gateway = ExternalPaymentGateway()

    def convert_payment_request(self, payment):
        """
        Convert PLN into grosz.
        Example: 100.00 PLN becomes 10000 grosz.
        """
        amount_in_grosz = int(
            payment.amount * Decimal("100")
        )

        return {
            "amount_in_grosz": amount_in_grosz,
            "token": payment.payment_token
        }

    def process_payment(self, payment: PaymentDetails) -> bool:

        print("\nBelovedPay: Starting payment process...")

        # Step 1: Validate the payment request
        if not payment.is_valid():
            print("Adapter: Invalid payment details.")
            return False

        # This demo gateway supports PLN only
        if payment.currency != "PLN":
            print("Adapter: Unsupported currency.")
            return False

        # Step 2: Check the monetary precision
        if payment.amount != payment.amount.quantize(
            Decimal("0.01")
        ):
            print("Adapter: Amount has too many decimals.")
            return False

        # Step 3: Convert the payment request
        converted = self.convert_payment_request(payment)

        print("Adapter: Payment request converted.")

        # Step 4: Communicate with the gateway
        response = self.gateway.send_transaction(
            converted["amount_in_grosz"],
            converted["token"]
        )

        # Step 5: Transform the gateway response
        if response.get("status") == "APPROVED":
            print("Adapter: Payment approved.")
            return True

        print("Adapter: Payment declined.")
        return False
