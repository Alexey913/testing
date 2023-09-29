import unittest

from order_service import OrderService
from payment_service import PaymentService


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.order_service = OrderService(PaymentService())

    def test_user(self):
        self.assertEqual(self.order_service.get_payment(25.50), 'Оплата на сумму 25.5')

if __name__ == '__main__':
    unittest.main()