#
# Problem:
# Some of our Inventory methods are incomplete and not all tests are passing.
#
# TODO: implement add_product() and remove_product()
#
from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    id: int
    name: str
    price: float
    quantity: int


class Inventory:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        # TODO: Prevent adding duplicate IDs
        self.products.append(product)

    def remove_product(self, product_id: int) -> None:
        # TODO: remove product by Product.id
        raise ValueError(f"Product with id {product_id} not found.")

    def update_quantity(self, product_id: int, new_quantity: int) -> None:
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        for p in self.products:
            if p.id == product_id:
                p.quantity = new_quantity
                return
        raise ValueError(f"Product with id {product_id} not found.")

    def total_value(self) -> float:
        return sum(p.price * p.quantity for p in self.products)

    def get_product(self, product_id: int) -> Product:
        for p in self.products:
            if p.id == product_id:
                return p
        raise ValueError(f"Product with id {product_id} not found.")
