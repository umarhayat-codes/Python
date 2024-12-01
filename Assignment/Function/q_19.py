def power(base, exponent):    
    if exponent == 0:
        return 1
    
    result = 1
    abs_exponent = abs(exponent)
    for _ in range(abs_exponent):
        result *= base
    
    if exponent < 0:
        return 1 / result
    return result

base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(f"The result of {base} raised to the power of {exponent} is: {power(base, exponent)}")
