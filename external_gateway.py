
# BelovedPay - External Payment Gateway
# Simulates an external payment provider


class ExternalPaymentGateway:

    def send_transaction(self, amount_in_grosz, token):
        print("\n--- External Payment Gateway ---")
        print(f"Amount received: {amount_in_grosz} grosz")

        if amount_in_grosz <= 0:
            return {
                "status": "DECLINED",
                "message": "Invalid payment amount"
            }

        if not token.startswith("DEMO-TOKEN-"):
            return {
                "status": "DECLINED",
                "message": "Invalid payment token"
            }

        return {
            "status": "APPROVED",
            "message": "Transaction approved"
        }
