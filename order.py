menu = [
    {"name": "burger", "price": 5.99},
    {"name": "espresso", "price": 1.99},
    {"name": "fries", "price": 2.49},
    {"name": "cake", "price": 2.79},
    {"name": "salad", "price": 3.99},
    {"name": "sandwich", "price": 4.99},
]

TAX_RATE = 0.0725


def calculate_subtotal(order):
    return sum(item["price"] for item in order)


def calculate_tax(subtotal):
    return subtotal * TAX_RATE


def summarize_order(order):
    names = [f"{item['name']} - ${item['price']:.2f}" for item in order]
    subtotal = calculate_subtotal(order)
    total = subtotal + calculate_tax(subtotal)
    return names, round(total, 2)


# Example usage
if __name__ == "__main__":
    customer_order = [menu[0], menu[1], menu[3]]  # burger, espresso, cake
    items, total = summarize_order(customer_order)
    print("Order summary:")
    for item in items:
        print(f"  {item}")
    print(f"Total (incl. tax): ${total:.2f}")
