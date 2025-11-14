#
# tests for takehome.inventory
#
import pytest

from takehome.inventory import Inventory, Product


def test_add_product():
    inv = Inventory()
    p = Product(id=1, name="Laptop", price=999.99, quantity=5)
    inv.add_product(p)
    assert len(inv.products) == 1


def test_add_duplicate_product():
    inv = Inventory()
    p = Product(id=1, name="Laptop", price=999.99, quantity=5)
    inv.add_product(p)
    with pytest.raises(ValueError):
        inv.add_product(p)
    assert len(inv.products) == 1


def test_remove_product():
    inv = Inventory()
    p = Product(id=1, name="Laptop", price=999.99, quantity=5)
    inv.add_product(p)
    inv.remove_product(1)
    assert len(inv.products) == 0
    with pytest.raises(ValueError):
        inv.get_product(1)


def test_get_product():
    inv = Inventory()
    p = Product(id=1, name="Laptop", price=999.99, quantity=5)
    inv.add_product(p)
    assert len(inv.products) == 1
    assert inv.get_product(1)


def test_update_quantity():
    inv = Inventory()
    p = Product(id=1, name="Laptop", price=999.99, quantity=5)
    inv.add_product(p)
    inv.update_quantity(1, 3)
    assert inv.products[0].quantity == 3


def test_update_quantity_negative():
    inv = Inventory()
    p = Product(id=1, name="Laptop", price=999.99, quantity=5)
    inv.add_product(p)
    inv.update_quantity(1, 3)
    with pytest.raises(ValueError):
        inv.update_quantity(1, -1)
    assert inv.products[0].quantity == 3


def test_update_quantity_missing():
    inv = Inventory()
    with pytest.raises(ValueError):
        inv.update_quantity(1, 1)


def test_total_value():
    inv = Inventory()
    inv.add_product(Product(id=1, name="Laptop", price=1000, quantity=2))
    inv.add_product(Product(id=2, name="Mouse", price=50, quantity=4))
    assert inv.total_value() == 2 * 1000 + 4 * 50


def test_remove_nonexistent_product():
    inv = Inventory()
    with pytest.raises(ValueError):
        inv.remove_product(999)
