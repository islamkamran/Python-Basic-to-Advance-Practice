counter = 0
print(counter)
counter += 1
print(counter)

numbers = [1, 2, 3]
print(numbers)
numbers += [4, 5]
print(numbers)
permissions = 0b0001  # Read permission
print(permissions)
write = 0b0010  # Write permission
permissions |= write
print(bin(permissions))