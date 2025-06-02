# 6k±1 Optimization for Prime Number Checking

## Overview
The **6k±1 optimization** is a simpler and more efficient deterministic method than basic trial division for testing whether a number `n` is prime. 

It builds on the observation that all prime numbers greater than 3 can be expressed in the form `6k+1` or `6k-1` (e.g., 5 = 6×1-1, 7 = 6×1+1, 11 = 6×2-1). 

This method is easier to implement than probabilistic algorithms like Miller-Rabin and more efficient than basic trial division, though still slower than Miller-Rabin for very large numbers. It’s ideal for computer science students seeking a balance between simplicity and performance.

```python
def is_prime_6k(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
number = 17
if is_prime_6k(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
```

## How the 6k±1 Optimization Works
1. **Input Validation**:
   - If `n ≤ 1`, return `False` (not prime).
   - If `n = 2` or `n = 3`, return `True` (prime).
   - If `n` is divisible by 2 or 3, return `False`.
2. **Divisibility Check**:
   - Check divisibility by numbers of the form `6k-1` and `6k+1` (e.g., 5, 7, 11, 13, …) up to `√n`.
   - This works because all primes greater than 3 are of the form `6k±1`, and checking these reduces the number of divisions compared to testing all numbers up to `√n`.
3. **Result**:
   - If no divisors are found, `n` is prime, and the method returns `True`.




## Characteristics
- **Time Complexity**: O(√n), similar to trial division, but with fewer iterations since it skips numbers not of the form `6k±1`.
- **Space Complexity**: O(1), as it uses constant extra space.
- **Advantages**:
  - Simpler than Miller-Rabin, requiring no modular exponentiation or probabilistic concepts.
  - More efficient than basic trial division by reducing the number of divisors checked (roughly one-third as many).
  - Deterministic, ensuring 100% accuracy.
- **Limitations**:
  - Still slower than Miller-Rabin for very large numbers (e.g., >10^9).
  - Less efficient than advanced algorithms for cryptographic applications.

## Use Case in Computer Science
The 6k±1 optimization is ideal for educational settings and small to medium-sized numbers (up to ~10^9). It teaches students about number theory optimizations while remaining accessible. It’s less complex than Miller-Rabin, making it a good stepping stone before diving into probabilistic methods.

## Example Output
For `number = 17`:
- The function checks divisibility by 2, 3, 5, and 7 (since `√17 ≈ 4.12`, only 5 and 7 are tested after 2 and 3).
- No divisors are found, so it outputs: `17 is a prime number`.
For `number = 15`:
- The function finds 15 is divisible by 3, so it outputs: `15 is not a prime number`.

## Comparison with Trial Division
Compared to trial division (O(√n)), the 6k±1 method is more efficient because:
- It skips checking divisors that are multiples of 2 or 3.
- It only tests numbers of the form `6k-1` and `6k+1` (e.g., 5, 7, 11, 13), reducing the number of iterations by about two-thirds.
This makes it a practical choice for students and applications where simplicity and moderate efficiency are prioritized over the speed of probabilistic methods like Miller-Rabin.