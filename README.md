## BelovedPay — Python Adapter Design Pattern

**Project:** External Payment System Integration  
**Author:** Beloved Mqondisi Banda  
**Programming Language:** Python 3  
**Design Pattern:** Adapter (Structural Design Pattern)

## 1. Project Overview

BelovedPay is a Python application developed to demonstrate the Adapter Design Pattern through integration with a simulated external payment gateway.

The application processes payment requests using a standard interface, while the external gateway expects a different method name, payment amount format, and response structure.

The PaymentAdapter class resolves these incompatibilities.

## 2. Project Objectives

- Implement the Adapter Design Pattern.
- Validate payment information.
- Convert payment amounts from PLN to grosz.
- Communicate with a simulated external payment gateway.
- Convert gateway responses into Boolean results.
- Demonstrate successful and unsuccessful payment scenarios.
- Verify functionality through automated unit testing.

## 3. System Architecture

The system consists of four main Python modules:

- **payment_details.py:** Stores and validates payment information.
- **external_gateway.py:** Simulates a third-party payment provider.
- **payment_adapter.py:** Implements the payment interface and converts requests and responses.
- **main.py:** Runs the application and demonstrates payment scenarios.

The `tests/test_payment_adapter.py` file contains automated unit tests.

## 4. How the Adapter Works

1. The application creates a PaymentDetails object.
2. The PaymentAdapter validates the payment information.
3. The adapter converts the amount from PLN into grosz.
4. The external gateway processes the simulated transaction.
5. The gateway returns an approval or decline response.
6. The adapter converts that response into True or False.

**Example:**

Input: 100.00 PLN  
Converted amount: 10000 grosz  
Gateway response: APPROVED  
Application response: True

## 5. Running the Application

Open a terminal in the project directory and execute:

`python main.py`

## 6. Running Automated Tests

Execute:

`python -m unittest discover -s tests -v`

Six automated tests verify:

- Successful payments
- Negative payment amounts
- Zero payment amounts
- Unsupported currencies
- Invalid payment tokens
- Correct payment amount conversion

**Test result:** 6 tests passed.

## 7. Technologies Used

- Python 3
- Python unittest
- Python dataclasses
- Python decimal
- Git and GitHub
- Cursor IDE

## 8. Limitations

BelovedPay uses a simulated payment gateway for educational purposes. It does not process real financial transactions or communicate with a live payment provider API.

The current implementation supports PLN transactions only. Production integration would require secure authentication, provider-specific API handling, error management, and additional security controls.

## 9. Conclusion

BelovedPay demonstrates how the Adapter Design Pattern enables communication between applications and external systems with incompatible interfaces.

The project successfully implements request conversion, simulated gateway communication, response transformation, and automated testing.
