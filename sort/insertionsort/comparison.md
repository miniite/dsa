# Comparison between the Different Implementation of Insertion Sort

## Comparison b/w Single For Loop with While Loop & Double For Loop

| Feature | Single For Loop with While Loop | Double For Loop |
|---------|--------------------------------|-----------------|
| **Core Structure** | Uses one for loop for iteration and a while loop for shifting | Uses two for loops: one for iteration, one for shifting |
| **Loop Mechanism** | For loop iterates through array; while loop shifts elements | Outer for loop iterates; inner for loop handles shifting and insertion |
| **Control Flow** | While loop continues until correct position is found or start of array is reached | Inner for loop iterates backward, with explicit break condition |
| **Code Readability** | Slightly less intuitive due to while loop condition | More structured due to for loop, but requires explicit break |
| **Time Complexity** | O(n²) worst/average, O(n) best | O(n²) worst/average, O(n) best |
| **Space Complexity** | O(1) | O(1) |
| **Key Assignment** | Key assigned once per outer loop; placed after while loop | Key assigned once per outer loop; placed in inner loop with break |
| **Shift Logic** | Shifts elements while condition is true | Shifts elements until condition fails or break is triggered |
| **Performance** | Identical in practice; while loop may be slightly optimized in some cases | Identical in practice; for loop may be clearer but requires break |
| **Use Case** | Preferred in traditional implementations; more concise | Useful when for loop structure is preferred for consistency or readability |



Both implementations achieve the same result, with the primary difference being the use of a while loop versus a second for loop for shifting elements. The choice between them often depends on coding style preference or specific project requirements.



## Code Comparisons

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
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1     # Index of the last element in the sorted portion
        
        # Shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place key in its correct position
        arr[j + 1] = key
    
    return arr
```
</td>
<td>

```python
def insertion_sort(arr):
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        # Iterate backwards through the sorted portion
        for j in range(i, -1, -1):
            # Check if previous element is greater than key
            if j > 0 and arr[j-1] > key:
                # Shift larger element to the right
                arr[j] = arr[j-1]
            else:
                # Place key in its correct position
                arr[j] = key
                break
    return arr
```
</td>
</tr>
</table>






## Line By Line Comparisons

| Aspect | Single For Loop with While Loop | Double For Loop |
|--------|--------------------------------|-----------------|
| **Total Logic Lines** | 6 lines of functional code | 7 lines of functional code |
| **Outer Loop** | **1 line**: `for i in range(1, len(arr)):`<br>Iterates through the array starting from the second element (index 1) to the end, selecting each element to be inserted into the sorted portion. | **1 line**: `for i in range(1, len(arr)):`<br>Performs the same iteration as the while loop version, processing each element from index 1 to the end of the array for insertion. |
| **Key Assignment** | **1 line**: `key = arr[i]`<br>Stores the current element at index `i` as the `key`, which will be inserted into the correct position in the sorted portion of the array. | **1 line**: `key = arr[i]`<br>Identical to the while loop version, captures the current element at index `i` as the `key` for insertion into the sorted portion. |
| **Inner Loop/Shift Control** | **2 lines**: <br>1. `j = i - 1`<br>Initializes `j` as the index of the last element in the sorted portion.<br>2. `while j >= 0 and arr[j] > key:`<br>Continues looping as long as `j` is valid (non-negative) and the element at `j` is greater than the `key`, indicating a need to shift elements right. | **2 lines**: <br>1. `for j in range(i, -1, -1):`<br>Sets up a backward iteration from index `i` to 0 (inclusive), handling the shifting process.<br>2. `if j > 0 and arr[j-1] > key:`<br>Checks if the previous element (at `j-1`) is greater than the `key` and ensures `j` is valid to avoid accessing invalid indices. |
| **Shift Operation** | **1 line**: `arr[j + 1] = arr[j]`<br>Shifts the element at index `j` one position to the right (to `j + 1`), making space for the `key` as the while loop moves backward. | **1 line**: `arr[j] = arr[j-1]`<br>Shifts the element at index `j-1` to position `j`, effectively moving larger elements right to make space for the `key`. |
| **Key Placement** | **1 line**: `arr[j + 1] = key`<br>Places the `key` at index `j + 1`, which is the correct position after shifting all larger elements right, determined when the while loop terminates. | **1 line**: `arr[j] = key`<br>Inserts the `key` at index `j`, the correct position after shifting, triggered when the `if` condition fails (i.e., no more shifting needed). |
| **Loop Termination** | **0 lines**: Implicit termination<br>The while loop stops when either `j < 0` (reached the start of the array) or `arr[j] <= key` (found the correct position), requiring no explicit termination statement. | **1 line**: `break`<br>Explicitly exits the inner for loop when the `if` condition fails (i.e., `j == 0` or `arr[j-1] <= key`), ensuring the key is placed and no further iteration occurs. |
| **Descriptive Difference** | The while loop version combines index initialization and condition checking in a concise structure. It relies on the while loop's condition to naturally terminate when the correct position is found or the array start is reached. This makes it slightly more compact but may be less intuitive for those unfamiliar with while loops. The shifting and placement logic uses `j + 1` due to the index being decremented in the loop. | The double for loop version uses a structured for loop to iterate backward, requiring an explicit `break` to exit once the key is placed. The `if` condition ensures safe index access and comparison, making the logic more explicit but adding an extra line for termination. The shifting and placement use `j` and `j-1` due to the loop's range-based iteration. |
| **Line Count Impact** | Fewer lines (6) due to implicit loop termination, making it more concise. The while loop's condition handles both boundary and comparison checks efficiently. | More lines (7) due to the explicit `break` statement, which adds clarity by clearly marking the end of the inner loop but increases the line count slightly. |
| **Performance** | Identical performance: O(n²) worst/average case, O(n) best case. The while loop may be marginally optimized in some interpreters due to fewer explicit statements. | Identical performance: O(n²) worst/average case, O(n) best case. The for loop's explicit structure may be clearer but has no significant performance difference. |
| **Readability** | Concise but may be less intuitive for beginners due to the while loop and manual index management (`j = i - 1`, `j -= 1`). | More structured with for loop iteration, potentially easier to follow for those familiar with for loops, but requires understanding the `break` condition. |

