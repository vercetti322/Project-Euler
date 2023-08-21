# Find sum of even fibonacchi numbers less than 4000000.

def fibonachi(fib_dict, n):
    if n in fib_dict:
        return fib_dict[n]
    else:
        ans = fibonachi(fib_dict, (n - 1)) + fibonachi(fib_dict, (n - 2))
        fib_dict[n] = ans
        return ans
    
def calculate_sum(fib_dict, upper=4000000):
    sum = 0
    i = 2
    while fibonachi(fib_dict, i) < upper:
        if fibonachi(fib_dict, i) % 2 == 0:
            sum += fibonachi(fib_dict, i)
        i += 1
    return sum
    
fib_dict = {1:1, 2:2}
print(calculate_sum(fib_dict))
