def format_product(product_id, name, quantity, price):
    """Return product details as a formatted string."""
    return (
        f"Product ID: {product_id}\n"
        f"Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: ${price:.2f}"
    )


