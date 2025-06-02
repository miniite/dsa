

## Generalized `find_prime` Code for All Primality Methods

<table >
<tr>
<th>Nth Prime </th>
<th>List of N Primes</th>
</tr>
<tr>
<td>

```python

def nth_prime(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    count = 0
    number = 2
    while True:
        if is_prime(number):
            count += 1
            if count == n:
                return number
        number += 1

```
</td>
<td>

```python

def all_n_primes_(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    primes = []
    number = 2
    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1
    return primes


```
</td>
</tr>
</table>

```python
def find_primes(n, return_all=False):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    primes = []
    count = 0
    number = 2
    while len(primes) < n:
        if is_prime(number):
            count += 1
            primes.append(number)
            if not return_all and count == n:
                return number
        number += 1
    return primes
```