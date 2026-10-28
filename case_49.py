products = [
    ("P101", 250, 10),
    ("P102", 500, 3),
    ("P103", 150, 0),
    ("P104", 0, 5),
    ("P105", 800, 2)
]
total_value = 0
reorder_level = 4

for product_id, price, stock in products:
    print("\nProduct:", product_id)
    if price <= 0 or stock < 0:
        print("Invalid product record")
        continue

    value = price * stock
    total_value += value
    print("Price:", price, "Stock:", stock, "Inventory value:", value)
    if stock < reorder_level:
        print("Reorder required")

print("Total inventory value:", total_value)
