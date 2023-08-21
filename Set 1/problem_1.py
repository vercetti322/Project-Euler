# If we list all the natural numbers below 10 that are multiples of 3 or 5 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all multiples of 3 or 5 below 1000.

def sum(multiple, num=1000):
    a = multiple
    num -= 1
    while num % multiple != 0:
        num -= 1
    f = num
    n = (f - a) / multiple + 1
    sum = ((f + a) * n) / 2
    return int(sum)
    
def final_sum():
    ans = sum(3) + sum(5) - sum(15)
    return ans


print(final_sum())