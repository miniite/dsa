I'll update the Bubble Sort article by replacing the variable `i` with `passno` and `j` with `i` in the Python code, and add another example to demonstrate the algorithm. Since this is an update to the previous artifact, I'll use the same `artifact_id` and include the full modified content with the requested changes, keeping all unchanged parts intact.


# Bubble Sort in Python

Bubble Sort is a simple sorting algorithm that repeatedly steps through a list, compares adjacent elements, and swaps them if they are in the wrong order. The process continues until no more swaps are needed, indicating the list is sorted. It’s named "Bubble Sort" because smaller elements "bubble" to the top of the list with each iteration.

## How Bubble Sort Works
1. Start at the beginning of the list.
2. Compare each pair of adjacent elements.
3. If the elements are out of order (e.g., the first is greater than the second), swap them.
4. Move to the next pair and repeat until the end of the list.
5. After each pass, the largest unsorted element is placed at the end.
6. Repeat the process for the remaining unsorted portion until no swaps are needed.

## Time and Space Complexity
- **Time Complexity**: 
  - Worst and Average case: O(n²), where n is the number of elements.
  - Best case: O(n) when the list is already sorted.
- **Space Complexity**: O(1), as it sorts in-place with no additional data structures.

## Python Implementation
Below is a Python implementation of the Bubble Sort algorithm:

```python
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for passno in range(n):
        # Flag to optimize for already sorted arrays
        swapped = False
        # Last passno elements are already in place
        for i in range(0, n - passno - 1):
            # Compare adjacent elements
            if arr[i] > arr[i + 1]:
                # Swap if they are in wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    return arr
```
```python
# Example usage
if __name__ == "__main__":
    # Example 1: Unsorted array
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Example 1 - Original array:", arr1)
    sorted_arr1 = bubble_sort(arr1)
    print("Example 1 - Sorted array:", sorted_arr1)
    
    # Example 2: Nearly sorted array
    arr2 = [1, 2, 4, 3, 5, 6]
    print("\nExample 2 - Original array:", arr2)
    sorted_arr2 = bubble_sort(arr2)
    print("Example 2 - Sorted array:", sorted_arr2)
```

### Explanation of the Code
- The function `bubble_sort` takes a list `arr` as input.
- The outer loop `for passno in range(n)` iterates through the list, reducing the range of comparison each time since the largest elements are already sorted at the end.
- The inner loop `for i in range(0, n - passno - 1)` compares adjacent elements.
- If `arr[i] > arr[i + 1]`, the elements are swapped.
- The `swapped` flag optimizes the algorithm by breaking early if the list is already sorted.
- The sorted array is returned.

### Example Output
For the input arrays:
```
Example 1 - Original array: [64, 34, 25, 12, 22, 11, 90]
Example 1 - Sorted array: [11, 12, 22, 25, 34, 64, 90]

Example 2 - Original array: [1, 2, 4, 3, 5, 6]
Example 2 - Sorted array: [1, 2, 3, 4, 5, 6]
```

## Advantages
- Simple to understand and implement.
- Works well for small datasets or nearly sorted lists.
- In-place sorting (minimal memory usage).

## Disadvantages
- Inefficient for large datasets due to O(n²) time complexity.
- Outperformed by more advanced algorithms like Quick Sort or Merge Sort for larger lists.

## When to Use Bubble Sort
Bubble Sort is rarely used in practice for large datasets due to its inefficiency. However, it’s useful for:
- Educational purposes to understand sorting concepts.
- Small datasets where simplicity is preferred.
- Cases where the list is already mostly sorted, leveraging the early termination optimization.

## Conclusion
Bubble Sort is a foundational algorithm in computer science, offering a straightforward way to sort lists. 

While not practical for large-scale applications, its simplicity makes it a great learning tool for beginners. 

For better performance, consider using Python’s built-in `sorted()` function or Timsort algorithm for real-world applications.
