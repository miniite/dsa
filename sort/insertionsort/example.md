# Examples with Insertion Sort

**Example Walkthrough**:
Input array: `[5, 2, 8, 1, 9]`

<table>

<tr>
<th>

### Single For Loop with While Loop
</th>
<th>

### Double For Loop
</th>
</tr>

<tr>
<td>

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```
</td>
<td>

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        for j in range(i, -1, -1):
            if j > 0 and arr[j-1] > key:
                arr[j] = arr[j-1]
            else:
                arr[j] = key
                break
    return arr
```
</td>
</tr>


<tr>
<td>

- **Pass 1 (i = 1)**:
  - `key = arr[1] = 2`
  - `j = i - 1 = 0` (points to `arr[0] = 5`)
  - While loop: `j >= 0` (true) and `arr[j] = 5 > key = 2` (true)
    - Shift: `arr[j + 1] = arr[0]`, so `arr[1] = 5`
    - `j = j - 1 = -1`
  - While loop ends (`j < 0`)
  - Place key: `arr[j + 1] = arr[0] = 2`
  - Array: `[2, 5, 8, 1, 9]`
</td>
<td>

- **Pass 1 (i = 1)**:
  - `key = arr[1] = 2`
  - Inner loop: `j` from 1 to 0
    - `j = 1`: `j > 0` (true) and `arr[j-1] = arr[0] = 5 > key = 2` (true)
      - Shift: `arr[1] = arr[0] = 5`
    - `j = 0`: `j > 0` (false)
      - Place key: `arr[0] = 2`
      - Break
  - Array: `[2, 5, 8, 1, 9]`
</td>
</tr>

<tr>
<td>

- **Pass 2 (i = 2)**:
  - `key = arr[2] = 8`
  - `j = i - 1 = 1` (points to `arr[1] = 5`)
  - While loop: `j >= 0` (true) and `arr[j] = 5 > key = 8` (false)
  - While loop ends (no shifting needed)
  - Place key: `arr[j + 1] = arr[2] = 8` (no change)
  - Array: `[2, 5, 8, 1, 9]`
</td>
<td>

- **Pass 2 (i = 2)**:
  - `key = arr[2] = 8`
  - Inner loop: `j` from 2 to 0
    - `j = 2`: `j > 0` (true) and `arr[j-1] = arr[1] = 5 > key = 8` (false)
      - Place key: `arr[2] = 8` (no change)
      - Break
  - Array: `[2, 5, 8, 1, 9]`
</td>
</tr>

<tr>
<td>

- **Pass 3 (i = 3)**:
  - `key = arr[3] = 1`
  - `j = i - 1 = 2` (points to `arr[2] = 8`)
  - While loop: `j >= 0` (true) and `arr[j] = 8 > key = 1` (true)
    - Shift: `arr[3] = arr[2]`, so `arr[3] = 8`
    - `j = j - 1 = 1`
  - While loop: `j >= 0` (true) and `arr[j] = 5 > key = 1` (true)
    - Shift: `arr[2] = arr[1]`, so `arr[2] = 5`
    - `j = j - 1 = 0`
  - While loop: `j >= 0` (true) and `arr[j] = 2 > key = 1` (true)
    - Shift: `arr[1] = arr[0]`, so `arr[1] = 2`
    - `j = j - 1 = -1`
  - While loop ends (`j < 0`)
  - Place key: `arr[j + 1] = arr[0] = 1`
  - Array: `[1, 2, 5, 8, 9]`
</td>
<td>

- **Pass 3 (i = 3)**:
  - `key = arr[3] = 1`
  - Inner loop: `j` from 3 to 0
    - `j = 3`: `j > 0` (true) and `arr[j-1] = arr[2] = 8 > key = 1` (true)
      - Shift: `arr[3] = arr[2] = 8`
    - `j = 2`: `j > 0` (true) and `arr[j-1] = arr[1] = 5 > key = 1` (true)
      - Shift: `arr[2] = arr[1] = 5`
    - `j = 1`: `j > 0` (true) and `arr[j-1] = arr[0] = 2 > key = 1` (true)
      - Shift: `arr[1] = arr[0] = 2`
    - `j = 0`: `j > 0` (false)
      - Place key: `arr[0] = 1`
      - Break
  - Array: `[1, 2, 5, 8, 9]`
</td>
</tr>

<tr>
<td>

- **Pass 4 (i = 4)**:
  - `key = arr[4] = 9`
  - `j = i - 1 = 3` (points to `arr[3] = 8`)
  - While loop: `j >= 0` (true) and `arr[j] = 8 > key = 9` (false)
  - While loop ends (no shifting needed)
  - Place key: `arr[j + 1] = arr[4] = 9` (no change)
  - Array: `[1, 2, 5, 8, 9]`
</td>
<td>

- **Pass 4 (i = 4)**:
  - `key = arr[4] = 9`
  - Inner loop: `j` from 4 to 0
    - `j = 4`: `j > 0` (true) and `arr[j-1] = arr[3] = 8 > key = 9` (false)
      - Place key: `arr[4] = 9` (no change)
      - Break
  - Array: `[1, 2, 5, 8, 9]`

</td>
</tr>

</table>













**Final Output**: `[1, 2, 5, 8, 9]`












### Comparison of Examples
- **Process Similarity**: Both implementations produce the same array transformations at each step, as they follow the same Insertion Sort logic: selecting a key, shifting larger elements right, and placing the key in the correct position.
- **Key Differences**:
  - **While Loop Version**: Uses `j` to track the sorted portion's last index, decrementing it manually (`j -= 1`) and checking conditions (`j >= 0 and arr[j] > key`). Shifts occur at `j + 1`, and the key is placed at `j + 1` after the loop ends. The loop terminates implicitly when conditions fail.
  - **Double For Loop Version**: Uses a for loop with `range(i, -1, -1)` to iterate backward, checking `j > 0 and arr[j-1] > key`. Shifts occur at `j`, and the key is placed at `j` when the condition fails, followed by an explicit `break`. The loop structure is more rigid but requires the break to avoid unnecessary iterations.
- **Step Count**: Both require the same number of comparisons and shifts for this example. For instance, in Pass 3 (sorting `1`), both perform three shifts (moving `8`, `5`, `2`) and place `1` at index 0.
- **Clarity in Execution**:
  - While loop: The shifting and placement logic is split (shifting in the loop, placement after). The index `j + 1` reflects the position opened by shifting.
  - Double for loop: Shifting and placement are within the same loop, with `j` directly indicating the insertion point. The explicit `break` clarifies when insertion is complete.

Both implementations correctly sort the array `[5, 2, 8, 1, 9]` into `[1, 2, 5, 8, 9]`, with the same sequence of operations, differing only in how the inner loop is controlled and terminated.