# To Find First and Last Indices of a Target Element in a Sorted List with Duplicates using Binary Search



## **Why Handle Duplicates in Binary Search?**

In a sorted list with duplicates, the standard binary search stops when it finds any match for the target element, which might not be the first or last occurrence. 

For example, in the list `[1, 2, 2, 2, 3]`, searching for `2` could return index `1`, `2`, or `3`, depending on where the algorithm lands. However, certain applications require:

- **First occurrence**: Useful for finding the starting point of a range of duplicates (e.g., in range queries or when inserting into a sorted list).
- **Last occurrence**: Useful for finding the end of a range or the last valid position of the target.
- **Count of occurrences**: Determined by finding both the first and last occurrences and calculating the difference.

Handling duplicates requires modifying the standard binary search to continue searching after finding a match, narrowing down to the desired occurrence.

---

## **Standard Binary Search Recap**

The original implementation stops at the first match it finds:

```python
def binary_search(coll, ele):
    start = 0
    end = len(coll) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if coll[mid] == ele:
            return mid
        elif coll[mid] > ele:
            end = mid - 1
        else:
            start = mid + 1
    return -1
```

For a list like `[1, 2, 2, 2, 3]` with `ele = 2`, this could return `1`, `2`, or `3`, depending on how the midpoints are chosen during the search. Let’s extend this to handle duplicates explicitly.

---

## **Finding the First Occurrence**

To find the **first occurrence** of the target element, modify the algorithm to continue searching in the left half of the list even after finding a match, until you’re sure you’ve found the leftmost occurrence.

### **Logic**
- When `coll[mid] == ele`, don’t return immediately. Instead, check if this is the first occurrence by verifying:
  - The current index is `0` (the start of the list), or
  - The element to the left (`coll[mid - 1]`) is less than the target.
- If neither condition is met, there might be an earlier occurrence, so set `end = mid - 1` to search the left half.
- Otherwise, proceed as in standard binary search.

### **Implementation**

```python
from typing import List

def binary_search_first(coll: List[int], ele: int) -> int:
    """
    Finds the index of the first occurrence of an element in a sorted list.
    
    Args:
        coll: A sorted list of integers (ascending order).
        ele: The element to search for.
    
    Returns:
        The index of the first occurrence of the element, or -1 if not found.
    """
    if not coll:
        return -1
    
    start = 0
    end = len(coll) - 1
    result = -1
    
    while start <= end:
        mid = start + (end - start) // 2
        if coll[mid] == ele:
            result = mid  # Store potential result but keep searching left
            end = mid - 1
        elif coll[mid] > ele:
            end = mid - 1
        else:
            start = mid + 1
    
    return result
```

### **How It Works**
- **Key Difference**: Instead of returning `mid` immediately when `coll[mid] == ele`, store `mid` in `result` and continue searching the left half (`end = mid - 1`) to find an earlier occurrence.
- **Termination**: The loop ends when `start > end`, and `result` holds the index of the first occurrence (or -1 if the element wasn’t found).
- **Example**:
  - List: `[1, 2, 2, 2, 3]`, `ele = 2`
  - First iteration: `mid = 2`, `coll[2] = 2` (match), store `result = 2`, search left (`end = 1`).
  - Second iteration: `mid = 0`, `coll[0] = 1`, search right (`start = 1`).
  - Third iteration: `mid = 1`, `coll[1] = 2`, store `result = 1`, search left (`end = 0`).
  - Loop ends, return `result = 1` (first occurrence at index `1`).

---

## **Finding the Last Occurrence**

To find the **last occurrence**, modify the algorithm to continue searching in the right half after finding a match, until you’re sure you’ve found the rightmost occurrence.

### **Logic**
- When `coll[mid] == ele`, don’t return immediately. Check if this is the last occurrence by verifying:
  - The current index is `len(coll) - 1` (the end of the list), or
  - The element to the right (`coll[mid + 1]`) is greater than the target.
- If neither condition is met, set `start = mid + 1` to search the right half.
- Otherwise, proceed as in standard binary search.

### **Implementation**

```python
from typing import List

def binary_search_last(coll: List[int], ele: int) -> int:
    """
    Finds the index of the last occurrence of an element in a sorted list.
    
    Args:
        coll: A sorted list of integers (ascending order).
        ele: The element to search for.
    
    Returns:
        The index of the last occurrence of the element, or -1 if not found.
    """
    if not coll:
        return -1
    
    start = 0
    end = len(coll) - 1
    result = -1
    
    while start <= end:
        mid = start + (end - start) // 2
        if coll[mid] == ele:
            result = mid  # Store potential result but keep searching right
            start = mid + 1
        elif coll[mid] > ele:
            end = mid - 1
        else:
            start = mid + 1
    
    return result
```

### **How It Works**
- **Key Difference**: When `coll[mid] == ele`, store `mid` in `result` and continue searching the right half (`start = mid + 1`) to find a later occurrence.
- **Termination**: The loop ends when `start > end`, and `result` holds the index of the last occurrence (or -1 if not found).
- **Example**:
  - List: `[1, 2, 2, 2, 3]`, `ele = 2`
  - First iteration: `mid = 2`, `coll[2] = 2`, store `result = 2`, search right (`start = 3`).
  - Second iteration: `mid = 3`, `coll[3] = 2`, store `result = 3`, search right (`start = 4`).
  - Loop ends, return `result = 3` (last occurrence at index `3`).

---

<br>

<table >
<tr>
<th>Search First Occurance in the List </th>
<th>Search Last Occurance in the List</th>
</tr>
<tr>
<td>

```diff
from typing import List

def binary_search_first(coll: List[int], ele: int) -> int:
    if not coll:
        return -1
    
    start = 0
    end = len(coll) - 1
+++ result = -1
    
    while start <= end:
        mid = start + (end - start) // 2
        if coll[mid] == ele:
+++            result = mid  # Store potential result but keep searching left
+            end = mid - 1
        elif coll[mid] > ele:
            end = mid - 1
        else:
            start = mid + 1
    
+++   return result
```

</td>
<td>

```diff
from typing import List

def binary_search_last(coll: List[int], ele: int) -> int:
    if not coll:
        return -1
    
    start = 0
    end = len(coll) - 1
+++  result = -1
    
    while start <= end:
        mid = start + (end - start) // 2
        if coll[mid] == ele:
+++           result = mid      # Store potential result but keep searching right
+            start = mid + 1
        elif coll[mid] > ele:
            end = mid - 1
        else:
            start = mid + 1
    
+++   return result
```
</td>
</tr>
</table>

><small>Here the suggestion block is used for highlighting code lines different from the basic binary search.
<br>
> Here:
<br>
> - "+" defines most important line or core change that is added
<br>
> - "+++" defines code line that have slight changes </small>

<br>

## **Counting Occurrences**

To count the number of occurrences of the target element, use both the first and last occurrence functions:

```python
def count_occurrences(coll: List[int], ele: int) -> int:
    """
    Counts the number of occurrences of an element in a sorted list.
    
    Args:
        coll: A sorted list of integers (ascending order).
        ele: The element to count.
    
    Returns:
        The number of occurrences of the element.
    """
    first = binary_search_first(coll, ele)
    if first == -1:
        return 0
    last = binary_search_last(coll, ele)
    return last - first + 1
```

### **Example**
- List: `[1, 2, 2, 2, 3]`, `ele = 2`
- `binary_search_first` returns `1` (index of first `2`).
- `binary_search_last` returns `3` (index of last `2`).
- Count: `3 - 1 + 1 = 3` (three occurrences of `2`).

---

## **Why These Modifications Work**

- **Preserving O(log n) Time Complexity**: Both modified algorithms maintain the O(log n) time complexity of binary search because they still halve the search space in each iteration. The only difference is continuing the search after finding a match to locate the boundary occurrence.
- **Correctness**: By checking the left or right side systematically, the algorithms guarantee finding the first or last occurrence without scanning the entire list.
- **Edge Cases**:
  - Empty list: Returns -1.
  - No duplicates: First and last occurrence are the same.
  - Element not present: Returns -1.
  - Single element: Handled correctly if it matches or doesn’t match.

---

## **Testing with Duplicates**

Test the implementations with various cases:
- **List with duplicates**: `[1, 2, 2, 2, 3]`, `ele = 2`
  - First occurrence: `1`
  - Last occurrence: `3`
  - Count: `3`
- **No duplicates**: `[1, 2, 3, 4]`, `ele = 3`
  - First occurrence: `2`
  - Last occurrence: `2`
  - Count: `1`
- **Element not present**: `[1, 2, 3]`, `ele = 4`
  - First occurrence: `-1`
  - Last occurrence: `-1`
  - Count: `0`
- **Single element**: `[2]`, `ele = 2`
  - First occurrence: `0`
  - Last occurrence: `0`
  - Count: `1`
- **All elements same**: `[2, 2, 2, 2]`, `ele = 2`
  - First occurrence: `0`
  - Last occurrence: `3`
  - Count: `4`

---

## **Complete Example**

Here’s a combined implementation with all three functions:

```python
from typing import List

def binary_search_first(coll: List[int], ele: int) -> int:
    if not coll:
        return -1
    start = 0
    end = len(coll) - 1
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        if coll[mid] == ele:
            result = mid
            end = mid - 1
        elif coll[mid] > ele:
            end = mid - 1
        else:
            start = mid + 1
    return result

def binary_search_last(coll: List[int], ele: int) -> int:
    if not coll:
        return -1
    start = 0
    end = len(coll) - 1
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        if coll[mid] == ele:
            result = mid
            start = mid + 1
        elif coll[mid] > ele:
            end = mid - 1
        else:
            start = mid + 1
    return result

def count_occurrences(coll: List[int], ele: int) -> int:
    first = binary_search_first(coll, ele)
    if first == -1:
        return 0
    last = binary_search_last(coll, ele)
    return last - first + 1

# Example usage
coll = [1, 2, 2, 2, 3]
ele = 2
print(f"First occurrence of {ele}: {binary_search_first(coll, ele)}")  # Output: 1
print(f"Last occurrence of {ele}: {binary_search_last(coll, ele)}")   # Output: 3
print(f"Count of {ele}: {count_occurrences(coll, ele)}")             # Output: 3
```

---

## **Applications of Handling Duplicates**

- **Range Queries**: Finding the range of indices where a value appears (e.g., in databases or search systems).
- **Insertion Point**: Determining where to insert a new element in a sorted list while maintaining order.
- **Frequency Analysis**: Counting occurrences for statistical or data processing tasks.
- **Algorithm Design**: Many problems (e.g., finding boundaries in rotated sorted arrays) rely on finding the first or last occurrence.

---

## **Summary**

Handling duplicates in binary search involves modifying the standard algorithm to find the **first** or **last** occurrence of a target element. By continuing the search after finding a match (to the left for first, to the right for last), you can pinpoint the desired index while maintaining O(log n) time complexity. The provided implementations include input validation, type hints, and the safe midpoint formula (`mid = start + (end - start) // 2`), making them robust and portable. Testing with various edge cases ensures correctness, and combining first and last occurrence functions allows counting duplicates efficiently.




