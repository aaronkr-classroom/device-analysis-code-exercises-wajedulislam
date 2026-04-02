a = 132
b = 45

fmt0 = '{:<10}'
fmt1 = 'Ob{:08b} Ox{:02x} {:3}'
n = 30
print("bitwise or:")
print(fmt0.format('a'), fmt1.format(a, a, a))
print(fmt0.format('b'), fmt1.format(b, b, b))
print('_'*n)
print(fmt0.format('a & b'),fmt1.format(a&b,a&b,a&b))
