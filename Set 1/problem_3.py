# What is the largest prime factor of 600851475143?

def max_prime(threshould, divisor=2):
    if threshould == 1:
        return []
    
    while threshould % divisor != 0:
        divisor += 1
    
    return [divisor] + max_prime(threshould // divisor, divisor)
    
    
input = 600851475143
print(max(max_prime(input)))