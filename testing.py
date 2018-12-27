operationToRuletable=["and",1,"xor",6,"or",7,"nor",8,"nand",14]

def binary(n):
	return bin(n)[2:]

def operationBit(a,b,rule):
	newRule = binary(rule)
	if len(binary(rule)) < 4:
		newRule = ('0'*(4-len(binary(rule)))) + binary(rule)
	return int(newRule[2*a+b])

def operationNumber(a,b,rule):
	ba = binary(a)
	bb = binary(b)

	# Make len(aa) = len(bb) without changing the binary value of it. (For iterating through it later)
	if len(ba) > len(bb):
		bb = ('0'*(len(ba)-len(bb))) + bb
	elif len(ba) < len(bb):
		ba = ('0'*(len(bb)-len(ba))) + ba

	out=0
	# Run bit operation on every bit in the numbers
	for i in range(len(ba)):
		b1 = int(ba[i])
		b2 = int(bb[i])
		out += (2**i)*operationBit(b1, b2, rule)

	return out

def stringIsNum(string):
	for char in string:
		if char not in "0123456789":
			return False
	return True

# Same as operationNumber(), except the rule can be a string like "and" or "xor", and they will map to their corresponding ruletables (0001 and 0110 for "and" and "xor")
# Maps stored in operationToRuletable list
def operationWithMap(a,b,rule):
	if type(rule) is str:
		return operationNumber(a,b,operationToRuletable.index(rule)+1)
	return operationNumber(a,b,rule)

print(str(operationBit(1,0,0b0110)))

print("o(255,0,xor) = " + str(operationWithMap(255,0,"xor")))
print("o(255,0,nand) = " + str(operationWithMap(255,0,"nand")))
print("o(255,0,or) = " + str(operationWithMap(255,0,"or")))
print("o(255,255,0b0110) = " + str(operationWithMap(255,255,0b0110)))
