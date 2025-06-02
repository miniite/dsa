# Miller-Rabin Primality Test

## Overview
The **Miller-Rabin Primality Test** is a probabilistic algorithm for determining whether a number `n` is prime, offering high efficiency and accuracy. 

It is based on properties of modular arithmetic and Fermat’s Little Theorem, enhanced with strong witness checks to reduce false positives (e.g., Carmichael numbers). 

It is more complex than trial division or the Fermat test but far more efficient for large numbers, making it a standard in cryptographic applications like RSA.

```python
def mod_pow(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def miller_rabin_test(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as d * 2^s
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Test with k=5 random bases
    k = 5
    import random
    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = mod_pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

# Example usage
number = 17
if miller_rabin_test(number):
    print(f"{number} is likely a prime number")
else:
    print(f"{number} is not a prime number")
```

## How the Miller-Rabin Primality Test Works
1. **Input Validation**:
   - If `n ≤ 1`, return `False` (not prime).
   - If `n = 2` or `n = 3`, return `True` (prime).
   - If `n` is even and not 2, return `False`.
2. **Rewrite n-1**:
   - Express `n-1` as `d * 2^s`, where `d` is odd and `s` is the number of times 2 divides `n-1`.
3. **Witness Loop**:
   - For `k` random bases `a` (where `2 ≤ a < n-2`):
     - Compute `x = a^d mod n` using modular exponentiation.
     - If `x = 1` or `x = n-1`, `n` passes for this `a`.
     - For `r` from 0 to `s-1`, compute `x = x^2 mod n`. If `x = n-1`, `n` passes; if `x = 1` and not previously `n-1`, `n` is composite.
     - If any `a` fails, `n` is composite.
4. **Result**:
   - If `n` passes all `k` tests, it is likely prime (error probability < `4^(-k)`).




## Characteristics
- **Time Complexity**: O(k log³ n), where `k` is the number of iterations (e.g., 5) and modular exponentiation contributes O(log³ n).
- **Space Complexity**: O(1), excluding the random number generator.
- **Advantages**:
  - Extremely efficient for large numbers, making it ideal for cryptographic applications.
  - Highly accurate, with an error probability of less than `4^(-k)` (e.g., <1/1000 for k=5).
  - Handles Carmichael numbers better than the Fermat test.
- **Limitations**:
  - Probabilistic, so there’s a small chance of false positives (though much lower than Fermat).
  - More complex than trial division or Fermat, requiring understanding of modular exponentiation and strong witness checks.
  - Implementation requires careful handling of edge cases and modular arithmetic.

## Use Case in Computer Science
The Miller-Rabin test is widely used in cryptography (e.g., generating large primes for RSA) and algorithms requiring fast primality testing. It’s a practical choice for large numbers (>10^9) and serves as an advanced topic for students learning about probabilistic algorithms and number theory.

## Example Output
For `number = 17`:
- The function tests 17 with 5 random bases, passes all checks, and outputs: `17 is likely a prime number`.

For `number = 15`:
- The function detects 15 as composite (e.g., fails for some `a`), outputting: `15 is not a prime number`.

## Comparison with Trial Division
- **Efficiency**: Miller-Rabin is significantly faster than trial division (O(k log³ n) vs. O(√n)) for large numbers, as it avoids iterative division and uses modular exponentiation.
- **Reliability**: Trial division is deterministic and always correct, while Miller-Rabin is probabilistic but highly accurate, with a negligible error rate for small `k`.
- **Complexity**: Miller-Rabin is more complex, requiring knowledge of modular arithmetic and the concept of strong witnesses, but its speed makes it superior for large-scale applications.