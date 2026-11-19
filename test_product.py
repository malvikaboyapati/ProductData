from product import product_details

def test_product_details():
    result = product_details(101, "Phone", 5, 600)

    expected_product = (
        "Product ID:101\n"
        "Name: Phone\n"
        "Quantity:5\n"
        "Price: 600\n"
    )

    assert result == expected_product