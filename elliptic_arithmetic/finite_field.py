#Galois filed is a set with...
#Two operations: + x
#Properties:
#Closure: a + b in set, a x b in set
#Addditive identity: a + 0 = a
#Multiplicative identify: a x 1 = a
#Additive inverse: a + (-a) = 0
#Multiplicative inverse: a x a^(-1)  = 1
#Field size for elliptic curves has to be prime!

from dataclasses import dataclass

@dataclass
class PrimeGaloisField:
	prime: int

	def __contains__(self, element: "FieldElement") -> bool:
		return 0 <= element.value < self.prime

@dataclass
class FieldElement:
	value: int
	field: PrimeGaloisField

	def __post_init__(self):
		if self not in self.field:
			raise ValueError

	def __repr__(self):
		return f"{self.value}".zfill(64)

	@property
	def prime(self):
		return self.field.prime

	def __add__(self, other: "FieldElement") -> "FieldElement":
		 return FieldElement(
			value = (self.value + other.value) % self.prime,
			field=self.field
			)

	def __sub__(self, other: "FieldElement") -> "FieldElement":
		return FieldElement(
			value=(self.value - other.value) % self.prime,
			field=self.field
		)

	def __rmul__(self, scalar: int) -> "FieldElement":
		return FieldElement(
			value=(self.value * scalar) % self.prime,
			field=self.field
		)

	def __mul__(self, other: "FieldElement") -> "FieldElement":
		return FieldElement(
			value=(self.value * other.value) % self.prime,
			field=self.field
		)
		
	def __pow__(self, exponent: int) -> "FieldElement":
		return FieldElement(
			value=pow(self.value, exponent, self.prime),
			field=self.field
		)

	def __truediv__(self, other: "FieldElement") -> "FieldElement":
	# self / other
		other_inv = other ** -1
		return self * other_inv
		
