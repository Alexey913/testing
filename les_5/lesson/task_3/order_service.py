from payment_service import PaymentService


class OrderService:
    def __init__(self, payment_service: PaymentService):
        self._payment_service = payment_service

    def get_payment(self, cost: float) -> str:
        return self._payment_service.pay_for_order(cost)
