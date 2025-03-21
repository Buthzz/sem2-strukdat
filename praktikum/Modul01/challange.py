def is_prima(x):
    # 0 and 1 are not prime numbers
    if x < 2:
        return False

    # Check divisibility only up to square root of x
    import math
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def cari_bilangan_prima(awal, akhir):
    list_bilangan_prima = []

    for x in range(awal, akhir + 1):
        if is_prima(x):
            list_bilangan_prima.append(x)

    return list_bilangan_prima


def palindrome(nomer):
    # Convert to string for palindrome check
    nomer_str = str(nomer)
    reverse = nomer_str[::-1]

    return nomer_str == reverse


# Get all prime numbers between 2 and 1000
prime_numbers = cari_bilangan_prima(2, 1000)
print("Prime numbers:", prime_numbers)

# Find prime palindromes
prime_palindromes = [num for num in prime_numbers if palindrome(num)]
print("Prime palindromes:", prime_palindromes)
