from collections.abc import Sequence
from dataclasses import dataclass
from typing import Optional, Callable, NamedTuple


class Customer(NamedTuple):
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: float

    def total(self) -> float:
        return self.price * self.quantity


@dataclass(frozen=True)
class Order:  # the Context
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], float]] = None

    def total(self) -> float:
        totals = (item.total() for item in self.cart)
        return sum(totals)

    def due(self) -> float:
        discount = self.promotion(self) if self.promotion else 0
        return self.total() - discount

    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'


"""
Decorator-Enhanced Strategy Pattern
- Registration Decorators
"""


Promotion = Callable[[Order], float]

promos: list[Promotion] = []


def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo


def best_promo(order: Order) -> float:
    return max(promo(order) for promo in promos)


@promotion
def fidelity(order: Order) -> float:
    """5% discount for customers with 1000 or more fidelity points"""
    if order.customer.fidelity >= 1000:
        return order.total() * 0.05
    return 0


@promotion
def bulk_item(order: Order) -> float:
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


@promotion
def large_order(order: Order) -> float:
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


if __name__ == '__main__':
    # jason = Customer('Jason', 100)
    # cart = [
    #     LineItem('banana', 4, 0.5),
    #     LineItem('apple', 10, 1.5),
    #     LineItem('watermelon', 5, 5)
    # ]
    # print(Order(jason, cart))
    print(promos)
