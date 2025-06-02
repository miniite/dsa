# Brute Force Method For Prime Number Checking

## Overview
The brute force method is a simple, straightforward approach to determine whether a given number `n` is a prime number. A prime number is a natural number greater than 1 that is divisible only by 1 and itself (e.g., 2, 3, 5, 7, 11). <u>This method systematically checks for divisibility to identify whether the number is prime or composite.</u>

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Example usage
number = 17
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
```

## How the Brute Force Method Works
1. **Input Validation**: 
   - If the input number `n` is less than or equal to 1, it is not prime, so the method returns `False`.
2. **Divisibility Check**: 
   - The method tests if `n` is divisible by any integer `i` from 2 to `n-1`. If `n % i == 0` for any `i`, then `n` is divisible by a number other than 1 and itself, meaning it is not prime.
3. **Result**: 
   - If no divisors are found in the range, `n` is prime, and the method returns `True`.



## Characteristics
- **Time Complexity**: O(n), as it checks all integers from 2 to `n-1`. This makes it inefficient for large numbers.
- **Space Complexity**: O(1), as it uses only a constant amount of extra space.
- **Advantages**: 
  - Simple to understand and implement.
  - Suitable for small numbers or educational purposes.
- **Limitations**: 
  - Inefficient for large numbers due to the linear number of iterations.
  - Can be optimized by checking only up to the square root of `n` or skipping even numbers after checking 2.

## Use Case in Computer Science
This method is often used in introductory programming exercises to teach loops and conditionals. While not practical for large-scale applications like cryptography (where advanced algorithms like Miller-Rabin are preferred), it serves as a foundational concept for understanding primality testing.

## Example Output
For `number = 17`:
- The function checks if 17 is divisible by any integer from 2 to 16.
- Since no such divisor exists, it outputs: `17 is a prime number`.

For `number = 15`:
- The function finds that 15 is divisible by 3, so it outputs: `15 is not a prime number`.

## Optimization Note
To improve efficiency, consider modifying the loop to check only up to `int(n ** 0.5)` and skip even numbers after 2, as shown in the trial division method. This reduces the time complexity to O(√n), making it more practical for larger inputs.


