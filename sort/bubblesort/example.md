# Bubble Sort Examples Explained

### Bubble Sort Algorithm Recap
Bubble Sort compares adjacent elements in a list and swaps them if they are in the wrong order (i.e., if the first element is greater than the second). Each pass through the list places the largest unsorted element at the end. The process repeats until no swaps are needed. The code includes an optimization (`swapped` flag) to exit early if the list is already sorted.

## Example 1: Sorting `[64, 34, 25, 12, 22, 11, 90]`
**Input Array**: `[64, 34, 25, 12, 22, 11, 90]`  
**Length (n)**: 7

#### Pass 1 (`passno = 0`)
- **Inner Loop** (`i` from 0 to `n - passno - 1` = 6):
  - `i = 0`: 
    - Compare `arr[0]` (64) and `arr[1]` (34). 
    - Since 64 > 34, **swap**. 
    - Array: `[34, 64, 25, 12, 22, 11, 90]`, `swapped = True`.
  - `i = 1`: 
    - Compare `arr[1]` (64) and `arr[2]` (25). 
    - Since 64 > 25, **swap**. 
    - Array: `[34, 25, 64, 12, 22, 11, 90]`, `swapped = True`.
  - `i = 2`: 
    - Compare `arr[2]` (64) and `arr[3]` (12). 
    - Since 64 > 12, **swap**. 
    - Array: `[34, 25, 12, 64, 22, 11, 90]`, `swapped = True`.
  - `i = 3`: 
    - Compare `arr[3]` (64) and `arr[4]` (22). 
    - Since 64 > 22, **swap**. 
    - Array: `[34, 25, 12, 22, 64, 11, 90]`, `swapped = True`.
  - `i = 4`: 
    - Compare `arr[4]` (64) and `arr[5]` (11). 
    - Since 64 > 11, **swap**. 
    - Array: `[34, 25, 12, 22, 11, 64, 90]`, `swapped = True`.
  - `i = 5`: 
    - Compare `arr[5]` (64) and `arr[6]` (90). 
    - Since 64 < 90, no swap.
- **End of Pass 1**: Largest element (90) is already at the end. Array: `[34, 25, 12, 22, 11, 64, 90]`.

#### Pass 2 (`passno = 1`)
- **Inner Loop** (`i` from 0 to 5):
  - `i = 0`: 
    - Compare `arr[0]` (34) and `arr[1]` (25). 
    - Since 34 > 25, **swap**. 
    - Array: `[25, 34, 12, 22, 11, 64, 90]`, `swapped = True`.
  - `i = 1`: 
    - Compare `arr[1]` (34) and `arr[2]` (12). 
    - Since 34 > 12, **swap**. 
    - Array: `[25, 12, 34, 22, 11, 64, 90]`, `swapped = True`.
  - `i = 2`: 
    - Compare `arr[2]` (34) and `arr[3]` (22). 
    - Since 34 > 22, **swap**. 
    - Array: `[25, 12, 22, 34, 11, 64, 90]`, `swapped = True`.
  - `i = 3`: 
    - Compare `arr[3]` (34) and `arr[4]` (11). 
    - Since 34 > 11, **swap**. 
    - Array: `[25, 12, 22, 11, 34, 64, 90]`, `swapped = True`.
  - `i = 4`: 
    - Compare `arr[4]` (34) and `arr[5]` (64). 
    - Since 34 < 64, no swap.
- **End of Pass 2**: Second largest element (64) is in place. Array: `[25, 12, 22, 11, 34, 64, 90]`.

#### Pass 3 (`passno = 2`)
- **Inner Loop** (`i` from 0 to 4):
  - `i = 0`: Compare `arr[0]` (25) and `arr[1]` (12). Since 25 > 12, **swap**. Array: `[12, 25, 22, 11, 34, 64, 90]`, `swapped = True`.
  - `i = 1`: Compare `arr[1]` (25) and `arr[2]` (22). Since 25 > 22, **swap**. Array: `[12, 22, 25, 11, 34, 64, 90]`, `swapped = True`.
  - `i = 2`: Compare `arr[2]` (25) and `arr[3]` (11). Since 25 > 11, **swap**. Array: `[12, 22, 11, 25, 34, 64, 90]`, `swapped = True`.
  - `i = 3`: Compare `arr[3]` (25) and `arr[4]` (34). Since 25 < 34, no swap.
- **End of Pass 3**: Array: `[12, 22, 11, 25, 34, 64, 90]`.

#### Pass 4 (`passno = 3`)
- **Inner Loop** (`i` from 0 to 3):
  - `i = 0`: Compare `arr[0]` (12) and `arr[1]` (22). Since 12 < 22, no swap.
  - `i = 1`: Compare `arr[1]` (22) and `arr[2]` (11). Since 22 > 11, **swap**. Array: `[12, 11, 22, 25, 34, 64, 90]`, `swapped = True`.
  - `i = 2`: Compare `arr[2]` (22) and `arr[3]` (25). Since 22 < 25, no swap.
- **End of Pass 4**: Array: `[12, 11, 22, 25, 34, 64, 90]`.

#### Pass 5 (`passno = 4`)
- **Inner Loop** (`i` from 0 to 2):
  - `i = 0`: Compare `arr[0]` (12) and `arr[1]` (11). Since 12 > 11, **swap**. Array: `[11, 12, 22, 25, 34, 64, 90]`, `swapped = True`.
  - `i = 1`: Compare `arr[1]` (12) and `arr[2]` (22). 
  - Since 12 < 22, no swap.
- **End of Pass 5**: Array: `[11, 12, 22, 25, 34, 64, 90]`.

#### Pass 6 (`passno = 5`)
- **Inner Loop** (`i` from 0 to 1):
  - `i = 0`: 
    - Compare `arr[0]` (11) and `arr[1]` (12). 
    - Since 11 < 12, no swap.
- **End of Pass 6**: No swaps occurred (`swapped = False`), so the algorithm terminates early.
- **Final Output**: `[11, 12, 22, 25, 34, 64, 90]`.

## Example 2: Sorting `[1, 2, 4, 3, 5, 6]`
**Input Array**: `[1, 2, 4, 3, 5, 6]`  
**Length (n)**: 6

#### Pass 1 (`passno = 0`)
- **Inner Loop** (`i` from 0 to 5):
  - `i = 0`: 
    - Compare `arr[0]` (1) and `arr[1]` (2). 
    - Since 1 < 2, no swap.
  - `i = 1`: 
    - Compare `arr[1]` (2) and `arr[2]` (4). 
    - Since 2 < 4, no swap.
  - `i = 2`: 
    - Compare `arr[2]` (4) and `arr[3]` (3). 
    - Since 4 > 3, **swap**. 
    - Array: `[1, 2, 3, 4, 5, 6]`, `swapped = True`.
  - `i = 3`: 
    - Compare `arr[3]` (4) and `arr[4]` (5). 
    - Since 4 < 5, no swap.
  - `i = 4`: 
    - Compare `arr[4]` (5) and `arr[5]` (6). 
    - Since 5 < 6, no swap.
- **End of Pass 1**: Array: `[1, 2, 3, 4, 5, 6]`.

#### Pass 2 (`passno = 1`)
- **Inner Loop** (`i` from 0 to 4):
  - `i = 0`: 
    - Compare `arr[0]` (1) and `arr[1]` (2). 
    - Since 1 < 2, no swap.
  - `i = 1`: 
    - Compare `arr[1]` (2) and `arr[2]` (3). 
    - Since 2 < 3, no swap.
  - `i = 2`: 
    - Compare `arr[2]` (3) and `arr[3]` (4). 
    - Since 3 < 4, no swap.
  - `i = 3`: 
    - Compare `arr[3]` (4) and `arr[4]` (5). 
    - Since 4 < 5, no swap.
- **End of Pass 2**: No swaps occurred (`swapped = False`), so the algorithm terminates early.
- **Final Output**: `[1, 2, 3, 4, 5, 6]`.

## Key Observations
- **Example 1**: 
  - The array required multiple passes because it was highly unsorted. 
  - The algorithm performed swaps in each pass until the list was sorted, but the `swapped` flag allowed it to terminate after Pass 6 when no further swaps were needed.

- **Example 2**: 
  - The array was nearly sorted, requiring only one swap in the first pass. 
  - The second pass confirmed the array was sorted, triggering the early termination (`swapped = False`). 
  - This demonstrates the optimization for nearly sorted lists.
- Each pass reduces the inner loop range by `passno`, as the largest elements are correctly placed at the end.
- The `swapped` flag prevents unnecessary passes when the array is sorted early, improving efficiency in the best case (O(n)).

>For more detailed explanation on `passno` and `swapped`, click [here](best_practice.md)

This step-by-step breakdown shows how Bubble Sort systematically orders the elements, with Example 2 highlighting its efficiency for nearly sorted data.