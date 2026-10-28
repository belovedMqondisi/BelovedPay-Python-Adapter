
# BelovedPay - Payment Integration System
# Design Pattern: Adapter
# Main Application

from decimal import Decimal

from payment_details import PaymentDetails
from payment_adapter import PaymentAdapter


def main():
    print("=" * 45)
    print("       BELOVEDPAY PAYMENT SYSTEM")
    print("       Adapter Design Pattern")
    print("=" * 45)

    # Create the adapter
    payment_adapter = PaymentAdapter()

    # Scenario 1: Successful payment
    print("\nTEST 1: VALID PAYMENT")

    payment1 = PaymentDetails(
        amount=Decimal("100.00"),
        currency="PLN",
        payment_token="DEMO-TOKEN-001"
    )

    result1 = payment_adapter.process_payment(payment1)

    if result1:
        print("RESULT: Payment successfully processed!")
    else:
        print("RESULT: Payment processing failed.")

    # Scenario 2: Invalid payment amount
    print("\nTEST 2: INVALID PAYMENT AMOUNT")

    payment2 = PaymentDetails(
        amount=Decimal("-50.00"),
        currency="PLN",
        payment_token="DEMO-TOKEN-002"
    )

    result2 = payment_adapter.process_payment(payment2)

    if result2:
        print("RESULT: Payment successfully processed!")
    else:
        print("RESULT: Payment processing failed.")

    # Scenario 3: Unsupported currency
    print("\nTEST 3: UNSUPPORTED CURRENCY")

    payment3 = PaymentDetails(
        amount=Decimal("75.00"),
        currency="USD",
        payment_token="DEMO-TOKEN-003"
    )

    result3 = payment_adapter.process_payment(payment3)

    if result3:
        print("RESULT: Payment successfully processed!")
    else:
        print("RESULT: Payment processing failed.")

    print("\n" + "=" * 45)
    print("       END OF BELOVEDPAY DEMO")
    print("=" * 45)


if __name__ == "__main__":
    main()
