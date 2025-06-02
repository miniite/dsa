# Finding the nth Prime Number Using Brute Force

## Overview
To find the **nth prime number** using a brute-force approach, we iterate through numbers starting from 2, check each for primality using a simple primality test, and count primes until we reach the nth one. For primality testing, we’ll use the basic brute-force method (checking divisibility from 2 to n-1), as it aligns with the brute-force theme. This approach is straightforward but inefficient for large `n` due to its high computational cost.

```python
def is_prime_brute_force(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def nth_prime_brute_force(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    count = 0
    number = 2
    while True:
        if is_prime_brute_force(number):
            count += 1
            if count == n:
                return number
        number += 1

# Example usage
n = 5
result = nth_prime_brute_force(n)
print(f"The {n}th prime number is {result}")
```

## How the Brute Force Method Works
1. **Initialize**:
   - Start with a counter for primes found (initially 0) and a number to check (starting at 2).
2. **Primality Check**:
   - For each number `i`, test if it’s prime by checking divisibility by all integers from 2 to `i-1`.
   - If no divisors are found, increment the prime counter.
3. **Stop Condition**:
   - When the prime counter reaches `n`, return the current number as the nth prime.
4. **Edge Cases**:
   - If `n ≤ 0`, return an error or handle as invalid input.



## Characteristics
- **Time Complexity**: 
  - Primality check: O(n) for each number.
  - Finding the nth prime: Approximately O(n * p_n), where `p_n` is the nth prime (roughly `p_n ≈ n ln(n)` by the Prime Number Theorem). Thus, overall complexity is O(n * p_n) = O(n² ln(n)).
- **Space Complexity**: O(1), as only a few variables are used.
- **Advantages**:
  - Simple to understand and implement, ideal for learning.
  - Works well for small `n` (e.g., n < 100).
- **Limitations**:
  - Extremely inefficient for large `n` due to checking every number up to `p_n` and testing divisibility up to each number.
  - Slow for `n > 1000` due to the quadratic growth in complexity.

## Example Output
For `n = 5`:
- The function checks numbers: 2 (1st prime), 3 (2nd), 5 (3rd), 7 (4th), 11 (5th).
- Outputs: `The 5th prime number is 11`.

For `n = 10`:
- Finds the 10th prime (29), outputting: `The 10th prime number is 29`.

## Use Case in Computer Science
This brute-force approach is primarily educational, helping students understand prime numbers and loops. It’s impractical for large `n` due to its inefficiency, but it lays the groundwork for learning optimized methods like the Sieve of Eratosthenes for finding the nth prime.

## Note for Optimization
For larger `n`, this method becomes prohibitively slow. More efficient approaches, like the Sieve of Eratosthenes or trial division with optimizations (e.g., checking up to √n or using 6k±1), can significantly reduce computation time. These can be explored next for better performance.