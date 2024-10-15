import math
import timeit
import random

def is_prime(num, k=3):  # Miller-Rabin test, K= number of tests done
    beginning_primes = [2, 3, 5, 7]  # List of initial prime numbers used for quick checks
    if num in beginning_primes:  # If the number is in the list of initial prime numbers, return True
        return True

    # If the number is less than or equal to 1, or divisible by any of the initial primes, return False
    if num <= 1 or any(num % p == 0 for p in beginning_primes):
        return False

    r, d = 0, num - 1  # Initialize variables r and d for later use
    while d % 2 == 0:  # While d is even
        r += 1  # Increment r
        d //= 2  # Divide d by 2

        # Witness Loop taken from:
        # https://github.com/davidb2/projecteuler/blob/a9297f8ec32040db99f4d258ece97a11d6fd97c7/python/pe118.py    
        for _ in range(k):  # Perform the following test k times
        a = random.randint(2, num - 1)  # Choose a random integer a in the range [2, num - 1]
        x = pow(a, d, num)  # Compute x = a^d mod num
        if x == 1 or x == num - 1:  # If x is 1 or num - 1, continue to the next iteration
            continue
        for _ in range(r - 1):  # Repeat r - 1 times
            x = pow(x, 2, num)  # Compute x = x^2 mod num
            if x == num - 1:  # If x is num - 1, break the loop
                break
        else:  # If the loop completes without finding x == num - 1, return False (indicating num is composite)
            return False
    return True  # If all tests pass, return True (indicating num is likely prime)

def palindrome_number_generator():
    yield 0  # The first palindrome number is 0.
    lower = 1  # Initialize the lower limit for the batch of numbers.
    while True:  # Starts an infinite loop.
        higher = lower*10  # Sets the upper limit for the batch of numbers.
        for i in range(lower, higher):  # For each number in the current batch,
            s = str(i)  # Converts the number to a string.
            yield int(s+s[-2::-1])  # Generates a palindrome by appending the reverse of the string (excluding the last digit) to the original string.
        for i in range(lower, higher):  # For each number in the current batch,
            s = str(i)  # Converts the number to a string.
            yield int(s+s[::-1])  # Generates a palindrome by appending the reverse of the string (including the last digit) to the original string.
        lower = higher  # Moves to the next batch by multiplying the lower limit by 10.

# This function generates prime palindromes within a given range.
def prime_palindromes(m, n):
    all_palindrome_numbers = palindrome_number_generator()  # Generate all palindrome numbers.
    for p in all_palindrome_numbers:  # For each palindrome number,
        if p >= m:  # If the palindrome number is greater than or equal to the lower limit of the range,
            break  # Stop the loop.
    prime_palindrome_list = [p] if is_prime(p) else []  # If the palindrome number is prime, add it to the list of prime palindromes.
    for p in all_palindrome_numbers:  # For each palindrome number,
        if p >= n:  # If the palindrome number is greater than or equal to the upper limit of the range,
            break  # Stop the loop.
        if is_prime(p):  # If the palindrome number is prime,
            prime_palindrome_list.append(p)  # Add it to the list of prime palindromes.
    return prime_palindrome_list  # Return the list of prime palindromes.

m = int(input("m: ")) 
n = int(input("n: "))  

start_time = timeit.default_timer()  # Starts the timer.
prime_palindrome_list = prime_palindromes(m, n)  # Generates the list of prime palindromes within the given range.
combined = prime_palindrome_list[:3] + prime_palindrome_list[-3:]  # Combines the first three and last three prime palindromes in the list.
combined_values = ", ".join(map(str, combined))  # Converts the combined list of prime palindromes to a string.
print(f"Range: ({m}, {n})")  # Prints the range.
print(f"{len(prime_palindrome_list)}: {combined}")  # Prints the number of prime palindromes and the combined list of prime palindromes.
end_time = timeit.default_timer()  # Stops the timer.
print("Time taken: ", end_time - start_time,' seconds\n')  # Prints the time taken to generate the list of prime palindromes.
