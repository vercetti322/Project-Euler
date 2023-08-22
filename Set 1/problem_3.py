# What is the largest prime factor of 600851475143?
   
def max_prime(threshould):
    '''
    input : the number
    output : list of all prime numbers which upto that number in sorted order
    Algorithm : sieve of erastothenes
    '''
    prime_list = {}
    for i in range(2, threshould + 1):
        prime_list[i] = True
    
    k = 2
    while k * k <= threshould:
        if prime_list[k] == True:
            for composite in range(k * k, threshould + 1, k):
                prime_list[composite] = False
        k += 1
        
    largest_prime_factor = 2
    for i in range(threshould, 2, -1):
        if prime_list[i] and threshould % i == 0:
            largest_prime_factor = i
            break
            
    return largest_prime_factor

input = 600851475143
print(max_prime(input))