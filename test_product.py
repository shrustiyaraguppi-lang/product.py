from product import format_product


def test_format_product():
    result = format_product(
        product_id=101,
        name="Wireless Mouse",
        quantity=5,
        price=24.5,
    )

    assert result == (
        "Product ID: 101\n"
        "Name: Wireless Mouse\n"
        "Quantity: 5\n"
        "Price: $24.50"
    )
