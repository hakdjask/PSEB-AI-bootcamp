def add(x, items = []):
    items.append(x)
    return items

print(add(1))  # Output: [1]
print(add(2))  # Output: [1, 2] - This is because the default list is mutable and retains its state across function calls.