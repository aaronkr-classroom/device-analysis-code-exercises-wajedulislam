a = 132
n = 30
fmt0 = '{:<10}'
fmt1 = '0b{:08b} 0x{:02x} {:3}'

# Now your existing code will work:
print("bitwise NOT:")
print(fmt0.format('a'), fmt1.format(a, a, a))
print('-' * n)
print(fmt0.format('~ a'), fmt1.format(~a & 0xFF, ~a & 0xFF, ~a & 0xFF))