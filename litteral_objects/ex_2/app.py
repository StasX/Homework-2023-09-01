
clothes = [
    {"type": "T-shirt", "size": "M", "price": 100, "color": "Black"},
    {"type": "Jacket", "size": "L", "price": 300, "color": "Red"},
    {"type": "Jeans", "size": "S", "price": 200, "color": "Blue"},
    {"type": "Coat", "size": "M", "price": 380, "color": "Green"},
    {"type": "Sweater", "size": "XL", "price": 250, "color": "White"}
]

#  Run over all literal objects in list
for item in clothes:

    # Print features
    for key, value in item.items():
        print(key, ":", value)

# Calculate total price
total = 0
for item in clothes:
    total += item["price"]

# Calculate and display average price
avg = total / len(clothes)
print("Average price is:", avg)

# Create dictionary of sizes
sizes = {"no_size": 0, "XXS": 1, "XS": 2,
         "S": 3, "M": 4, "L": 5, "XL": 6, "XXL": 7}  # Now all sizes have weight

# Calculate and display largest size
max_size = "no_size"
for item in clothes:
    item_size = item["size"]
    if sizes[item_size] > sizes[max_size]:
        max_size = item_size
print("Max clothes size is", max_size)
