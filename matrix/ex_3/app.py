colored_items = [
    ["Red Apple", "Red Rose", "Fire Truck"],
    ["Lemon", "Sunflower", "Banana", "Rubber Duck"],
    ["Grass", "Cucumber"]
]

print(colored_items)

shortest = [colored_items[0][0]]

for items in colored_items:
    for item in items:
        if len(item) < len(shortest[0]):
            shortest = [item]
        elif len(item) == len(shortest[0]):
            shortest.append(item)

print(f"First shortest string in matrix is \"{shortest[0]}\"")

longest = [colored_items[0][0]]

for items in colored_items:
    for item in items:
        if len(item) > len(longest[0]):
            longest = [item]
        elif len(item) == len(longest[0]):
            longest.append(item)

shortest = ", ".join(shortest)
print(f"First shortest string in matrix is \"{shortest}\"")
longest = ", ".join(longest)
print(f"First longest string in matrix is \"{longest}\"")
