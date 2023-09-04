def is_palindrome(num):
    # Check if a number is a palindrome
    num_str = str(num)
    return num_str == num_str[::-1]


def largest_palindrome():
    max_palindrome = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if product > max_palindrome and is_palindrome(product):
                max_palindrome = product

    return max_palindrome


result = largest_palindrome()
print(result)
