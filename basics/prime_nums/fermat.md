# Understanding the Fermat Primality Test

The **Fermat Primality Test** is a probabilistic method to determine whether a number `n` is prime, based on Fermat's Little Theorem:

> if `n` is prime and `1 ≤ a < n`, then `a^(n-1) ≡ 1 (mod n)` 

It is faster than deterministic methods like trial division or 6k±1 optimization and simpler than the Miller-Rabin test, making it a good intermediate approach for computer science students. 

However, it is less reliable due to false positives for Carmichael numbers (e.g., 561).

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

def fermat_primality_test(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Test with k=5 random bases
    k = 5
    import random
    for _ in range(k):
        a = random.randrange(2, n - 1)
        if mod_pow(a, n - 1, n) != 1:
            return False
    return True

# Example usage
number = 17
if fermat_primality_test(number):
    print(f"{number} is likely a prime number")
else:
    print(f"{number} is not a prime number")
```

## How the Fermat Primality Test Works
1. **Input Validation**:
   - If `n ≤ 1`, return `False` (not prime).
   - If `n = 2` or `n = 3`, return `True` (prime).
   - If `n` is even and not 2, return `False`.
2. **Fermat’s Theorem Check**:
   - Select `k` random bases `a` (where `1 < a < n-1`) and compute `a^(n-1) mod n` using modular exponentiation.
   - If `a^(n-1) ≠ 1 (mod n)` for any `a`, then `n` is composite.
3. **Result**:
   - If `a^(n-1) ≡ 1 (mod n)` for all `k` bases, `n` is likely prime (error probability ~`2^(-k)`).




## Characteristics
- **Time Complexity**: O(k log² n), where `k` is the number of iterations (e.g., 5) and modular exponentiation takes O(log² n).
- **Space Complexity**: O(1), excluding the random number generator.
- **Advantages**:
  - Faster than trial division (O(√n)) for large numbers due to logarithmic complexity.
  - Simpler than Miller-Rabin, requiring only Fermat’s Little Theorem and modular exponentiation.
  - Suitable for educational purposes to introduce probabilistic primality testing.
- **Limitations**:
  - Probabilistic, with a risk of false positives for Carmichael numbers (e.g., 561, 1105), which pass the test despite being composite.
  - Less reliable than Miller-Rabin, which uses stronger checks to reduce errors.
  - Not suitable for cryptographic applications due to its vulnerability to certain composite numbers.

## Use Case in Computer Science
The Fermat Primality Test is ideal for teaching students about probabilistic algorithms and modular arithmetic. It’s faster than trial division and 6k±1 for large numbers (up to ~10^12) and serves as a stepping stone to understanding more robust methods like Miller-Rabin. It’s best for non-critical applications where simplicity and speed are prioritized over absolute accuracy.

## Example Output
For `number = 17`:
- The function tests 17 with 5 random bases, finds `a^16 ≡ 1 (mod 17)` for each, and outputs: `17 is likely a prime number`.
For `number = 15`:
- The function detects 15 as composite (e.g., fails for some `a`), outputting: `15 is not a prime number`.

## Comparison with Trial Division
- **Efficiency**: Fermat is much faster than trial division (O(k log² n) vs. O(√n)) for large numbers, as it avoids iterative division and uses modular exponentiation.
- **Reliability**: Trial division is deterministic and always correct, while Fermat is probabilistic and may misidentify Carmichael numbers as prime.
- **Complexity**: Fermat requires understanding modular exponentiation, slightly more complex than trial division’s simple divisibility checks, but still accessible for students.