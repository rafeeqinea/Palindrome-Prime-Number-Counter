# Palindrome Prime Number Counter

An algorithm to efficiently find and count palindromic prime numbers within a given range. The implementation combines a **palindrome number generator** with the **Miller-Rabin probabilistic primality test** to handle arbitrarily large ranges without brute-force iteration.

## How It Works

The algorithm avoids testing every integer in the range for both palindromicity and primality. Instead, it takes a generate-then-filter approach:

1. **Palindrome Generation** -- A generator function produces palindrome numbers in ascending order by constructing them from their left halves. For a given digit length, it generates both odd-length palindromes (e.g., 12321) and even-length palindromes (e.g., 1221) by mirroring digit strings. This yields all palindromes without checking every integer.

2. **Primality Testing** -- Each generated palindrome is tested using the Miller-Rabin probabilistic primality test rather than trial division. Miller-Rabin runs in O(k log^2 n) time per test (where k is the number of witness rounds), making it significantly faster than trial division O(sqrt(n)) for large numbers. The implementation uses k=3 rounds with random witnesses.

3. **Range Filtering** -- The generator is advanced to the start of the requested range, then palindromes are collected and tested until the upper bound is reached.

## Algorithm Details

### Palindrome Generator

The generator works by digit length batches. For each batch with lower bound `l` and upper bound `l*10`:
- **Odd-length palindromes**: Takes each number `i` in [l, l\*10), converts to string `s`, and produces `s + reverse(s[:-1])`. For example, `123` becomes `12321`.
- **Even-length palindromes**: Takes each number `i` in [l, l\*10), converts to string `s`, and produces `s + reverse(s)`. For example, `123` becomes `123321`.

This ensures palindromes are generated in sorted order without gaps.

### Miller-Rabin Primality Test

The test decomposes `n-1` as `2^r * d` (where d is odd), then for k random witnesses `a`:
1. Compute `x = a^d mod n`
2. If `x = 1` or `x = n-1`, the witness does not indicate compositeness
3. Otherwise, square x up to `r-1` times, checking for `n-1`
4. If no squaring yields `n-1`, n is composite

With k=3 rounds, the probability of a false positive (composite reported as prime) is at most 4^(-3) = 1/64 per candidate.

## Usage

```bash
python primepalindrome.py
```

The program prompts for the lower bound `m` and upper bound `n`, then outputs:
- The count of palindromic primes in the range [m, n)
- The first three and last three palindromic primes found
- The execution time

### Example

```
m: 1
n: 1000000
Range: (1, 1000000)
113: [2, 3, 5, 98689, 98899, 99929]
Time taken: 0.0045 seconds
```

## Requirements

- Python 3.6+
- No external dependencies (uses only `math`, `timeit`, `random` from the standard library)
