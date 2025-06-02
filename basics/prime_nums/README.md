# Introduction to Prime Numbers for Computer Science Students

- A **prime number** is a natural number greater than 1 that has no positive divisors other than 1 and itself. 

- In simpler terms, a prime number is divisible only by 1 and the number itself. 

        For p%n where p is a prime and n is any whole number
         
        Where n = 0 or 1,    p%1 = 0 and p%p = 0
        For all other n,     p%n != 0
         
- For example, 2, 3, 5, 7, 11, and 13 are prime numbers, while 4 (divisible by 2), 6 (divisible by 2 and 3), or 9 (divisible by 3) are not.

## Why Prime Numbers Matter in CS

- In computer science, prime numbers play a significant role in various algorithms and applications due to their unique mathematical properties. 

- They are fundamental in areas like **cryptography** (e.g., RSA encryption relies on large prime numbers for security), **hashing** (primes are used in hash functions to minimize collisions), and **number theory-based algorithms**. 

- Understanding prime numbers is essential for tackling problems involving divisibility, modular arithmetic, and optimization.


- For instance, the number 2 is the only even prime number, and all other primes are odd. 
- A number that is not prime (and greater than 1) is called a **composite number**. 
- Identifying whether a number is prime—through methods like **trial division**, the **Sieve of Eratosthenes**, or advanced primality tests like **Miller-Rabin**—is a common computational task in computer science.

This foundational concept connects to real-world applications and algorithmic challenges, making it a critical topic for computer science students to revisit and master.

## Methods to Check a Number is Prime or Not


| Method                | Time Complexity | Space Complexity | Key Characteristics | Relevant Thoughts |
|-----------------------|-----------------|------------------|---------------------|-------------------|
| [**Brute Force**](bruteforce.md)       | O(n)            | O(1)             | Checks all integers from 2 to n-1. | Simplest but highly inefficient. Best for small numbers or learning. |
| [**Trial Division**](trialdivision.md)    | O(√n)           | O(1)             | Checks divisors up to √n, skips even numbers. | Suitable for small to medium numbers (up to ~10^6). Deterministic but slow for large numbers. |
| [**6k±1 Optimization**](6k_1opt.md) | O(√n)           | O(1)             | Tests 2, 3, and 6k±1 numbers up to √n. | Reduces checks by ~2/3 vs. trial division. Simple, deterministic, good for numbers up to ~10^9. |
| [**Fermat Primality**](fermat.md)  | O(k log² n)     | O(1)             | Probabilistic test using Fermat’s Little Theorem with k bases. | Faster than 6k±1, simpler than Miller-Rabin. Susceptible to Carmichael numbers, less reliable. Good for learning probabilistic methods. |
| [**Miller-Rabin**](miller-rabin.md)      | O(k log³ n)     | O(1)             | Probabilistic test with strong witness checks. | Fastest and most reliable for large numbers. Used in cryptography. More complex but robust. |


## Methods to find N Primes and Nth Prime

Read about [`find_prime`](find_prime.md) method to understand how we generate the prime number or prime number list after checking each number


| Method                | Time Complexity (Both)           | Space Complexity (nth Prime) | Space Complexity (All n Primes)        | Key Difference                                    |
|-----------------------|-------------------------------|-----------------------------|---------------------------------------|--------------------------------------------------|
| Brute Force           | O(n² ln(n))                  | O(1)                        | O(n)                                  | Only space increases for list storage; no runtime difference. |
| Trial Division        | O(n<sup>(1.5)</sup> ln<sup>(1.5)</sup>(n))         | O(1)                        | O(n)                                  | Same as brute force—only space increases for list. |
| 6k±1 Optimization     | O(n<sup>(1.5)</sup> ln<sup>(1.5)</sup>(n))       | O(1)                        | O(n)                                  | Same as trial division—only space increases for list. |
| Sieve of Eratosthenes | O(n log(n) log log(n))       | O(n log(n))                 | O(n log(n)) + O(n) ≈ O(n log(n))      | Negligible space increase; no runtime difference. |
