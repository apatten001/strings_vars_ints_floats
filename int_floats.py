# you can use integers just like you would in a calculator

print(1+3)
print(1-3)
print(1*3)
print(1/3)
print(1//3) # floor division leaves out the number after the decimal
print(1**3) # exponents

print("The answer to 1/3 = " + str(1/3) + " is considered a float because it shows thee numbers after the decimal")

# to add a string and a float
print(1 + (1.4))

# to add int to int of the float
print(1 + int(1.7))

# this rounds the int anf the float
print(round(1+ 1.7))

# this turns the integer into a float
print(float(1) + 1)

# order of operations do matter in Python PEMDAS

print(1+3-2 * 6)

print((1+3-2) * 6)