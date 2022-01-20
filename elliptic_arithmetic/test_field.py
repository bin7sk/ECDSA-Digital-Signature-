#module to test Galois Field
#always random values

from finite_field import PrimeGaloisField, FieldElement
import random

prime = random.randint(5, 10**4)
field = PrimeGaloisField(prime)

class FieldError(Exception):
#Field class doesn't work properly
	pass

#test if class throws exception when value more then prime
try:
	r = random.randint(1, prime - 1)
	e = FieldElement(prime + r, field) # should raise exception here
	raise FieldError

except ValueError:
	print("OK: class throws ValueError when value more then prime")

except FieldError:
	print("Field class doesn't work properly")
	print("It doesn't throw exception when value more then prime")


a = FieldElement(random.randrange(prime), field)
b = FieldElement(random.randrange(prime), field)
print('prime = ', prime)
print('a = ', a)
print('b = ', b)

result = a + b
print(f'a + b = {result}')
assert result.value == (a.value + b.value) % prime

result = a - b
print(f'a - b = {result}')
assert result.value == (a.value - b.value) % prime

integer = random.randrange(100)
result = integer * b
print(f'{integer} * b = {result}')
assert result.value == (integer * b.value) % prime

result = a * b
print(f'a * b = {result}')
assert result.value == (a.value * b.value) % prime

power = random.randrange(100)
result = a ** power
print(f'a ** {power} = {result}')
assert result.value == pow(a.value, power, prime)

result = a / b
print(f'a / b = {result}')
assert result.value == (a.value * pow(b.value, -1, prime)) % prime