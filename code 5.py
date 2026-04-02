# Setup variables (required for the code to run)
a = 132
n = 30
fmt0 = '{:<10}'
fmt1 = '0b{:08b} 0x{:02x} {:3}'

print("bitwise left shift:")
print(fmt0.format('a'), fmt1.format(a, a, a))
print('-' * n)

# The result of shifting 'a' left by 2 positions
print(fmt0.format('a << 2'), fmt1.format((a << 2) & 0xFF, (a << 2) & 0xFF, (a << 2) & 0xFF))
