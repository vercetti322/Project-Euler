# What is the smallest positive number that is evenly divisible by
# all the numbers from 1 to 20
import math


def check_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# print(check_prime(23))


def prime_list(num):
    ans = []
    for number in range(num):
        if check_prime(number):
            ans.append(number)
    return ans


# print(prime_list(20))


def highest_powers(num, list_prime):
    """
    :param num: it is the number till we want a list of highest powers
    :param list_prime : all list of prime which make up the numbers till num
    :return: returns a list of the numbers <= num which are the highest powers
    """
    highest_ans = []
    for i in list_prime:
        i_power = 1
        while i_power <= num:
            i_power *= i
        highest_ans.append(i_power // i)

    return highest_ans


# print(highest_powers(20, prime_list(20)))


def main():
    ans = highest_powers(20, prime_list(20))
    final_ans = 1
    for num in ans:
        final_ans *= num

    print(final_ans)


if __name__ == '__main__':
    main()
